#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["pyyaml"]
# ///
"""
Build script for the Cell Painting Gallery dataset registry.

Reads registry.yml and generates:
  - Published dataset table in README.md (between markers)
  - Unpublished dataset table in README.md (between markers)
  - documentation/complete_datasets.md with both tables + external contributions
  - documentation/prefixes.md prefix table (between markers)

Usage:
  uv run scripts/build_registry.py          # generate all outputs
  uv run scripts/build_registry.py --check  # validate only, no writes
"""

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PATH = ROOT / "registry.yml"
README_PATH = ROOT / "README.md"
COMPLETE_DATASETS_PATH = ROOT / "documentation" / "complete_datasets.md"
PREFIXES_PATH = ROOT / "documentation" / "prefixes.md"

NAME_PATTERN = re.compile(r"^cpg\d{4}(-[A-Za-z0-9_-]+)?$")
VALID_STATUSES = {"published", "unpublished"}

# Markers in README.md
PUB_START = "<!-- AUTO-GENERATED PUBLISHED TABLE START -->"
PUB_END = "<!-- AUTO-GENERATED PUBLISHED TABLE END -->"
UNPUB_START = "<!-- AUTO-GENERATED UNPUBLISHED TABLE START -->"
UNPUB_END = "<!-- AUTO-GENERATED UNPUBLISHED TABLE END -->"
PREFIX_START = "<!-- AUTO-GENERATED PREFIX TABLE START -->"
PREFIX_END = "<!-- AUTO-GENERATED PREFIX TABLE END -->"


def load_registry():
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data


def escape_md(text):
    """Escape markdown table-breaking characters."""
    if not text:
        return ""
    text = str(text).replace("|", "\\|")
    text = text.replace("\n", " ").replace("\r", "")
    return text.strip()


def validate(datasets):
    """Validate the registry schema. Returns list of error strings."""
    errors = []
    seen_names = set()

    for i, ds in enumerate(datasets):
        prefix = f"Dataset #{i + 1}"

        # Required fields
        name = ds.get("name")
        if not name:
            errors.append(f"{prefix}: missing 'name'")
            continue

        prefix = f"Dataset '{name}'"

        if not NAME_PATTERN.match(name):
            errors.append(
                f"{prefix}: name '{name}' does not match pattern cpgNNNN[-tag]"
            )

        if name in seen_names:
            errors.append(f"{prefix}: duplicate name")
        seen_names.add(name)

        status = ds.get("status")
        if not status:
            errors.append(f"{prefix}: missing 'status'")
        elif status not in VALID_STATUSES:
            errors.append(
                f"{prefix}: invalid status '{status}', must be one of {VALID_STATUSES}"
            )

        if "description" not in ds:
            errors.append(f"{prefix}: missing 'description'")

    return errors


def format_publication_cell(publications):
    """Format the publication column from a list of publication dicts."""
    if not publications:
        return ""

    parts = []
    for pub in publications:
        authors = pub.get("authors", "")
        publication_url = pub.get("publication", "")
        preprint_url = pub.get("preprint", "")
        note = pub.get("note", "")
        pub_prefix = pub.get("prefix", "")

        piece = ""
        if pub_prefix:
            piece += f"{pub_prefix} "

        piece += f"({authors})"

        if publication_url:
            piece += f" [Publication]({publication_url})"
            if preprint_url:
                piece += f", [Preprint]({preprint_url})"
        elif preprint_url:
            piece += f" [Preprint]({preprint_url})"

        if note:
            piece += f" {note}"

        parts.append(piece)

    # Join multiple publications
    cell = " ".join(parts)
    return escape_md(cell)


def format_repositories_cell(repositories):
    """Format the repositories column from a list of repo dicts."""
    if not repositories:
        return ""

    parts = []
    for repo in repositories:
        if isinstance(repo, str):
            parts.append(repo)
        else:
            label = repo.get("label", "")
            url = repo.get("url", "")
            if url:
                parts.append(f"[{label}]({url})")
            else:
                parts.append(label)

    return escape_md(", ".join(parts))


def format_aliases_cell(aliases):
    """Format the aliases column from a list of alias items."""
    if not aliases:
        return ""

    parts = []
    for alias in aliases:
        if isinstance(alias, str):
            parts.append(alias)
        else:
            label = alias.get("label", "")
            url = alias.get("url", "")
            if url:
                parts.append(f"[{label}]({url})")
            else:
                parts.append(label)

    return escape_md(", ".join(parts))


def build_published_table(datasets):
    """Build the 9-column published dataset table matching current README format."""
    published = sorted(
        [d for d in datasets if d.get("status") == "published"],
        key=lambda d: d["name"],
    )

    lines = []
    # Header
    headers = [
        "Dataset name",
        "Description",
        "Publication to cite",
        "Associated repositories",
        "Total size",
        "Images size",
        "Numerical data size",
        "Cell Painting protocol",
        "Other aliases",
    ]
    lines.append("| " + " | ".join(headers) + " |")
    seps = [
        "---",
        "---",
        "---",
        "---",
        ":---:",
        ":---:",
        ":---:",
        ":---:",
        ":---:",
    ]
    lines.append("| " + " | ".join(seps) + " |")

    for ds in published:
        name = ds["name"]
        desc = escape_md(ds.get("description", ""))
        pub_cell = format_publication_cell(ds.get("publications", []))
        repo_cell = format_repositories_cell(ds.get("repositories", []))

        size = ds.get("size", {})
        total = escape_md(size.get("total", ""))
        images = escape_md(size.get("images", ""))
        numerical = escape_md(size.get("numerical", ""))

        protocol = escape_md(ds.get("protocol", ""))
        aliases = format_aliases_cell(ds.get("aliases", []))

        row = (
            f"| {name:<40} "
            f"| {desc} "
            f"| {pub_cell} "
            f"| {repo_cell} "
            f"| {total:^10} "
            f"| {images:^11} "
            f"| {numerical:^19} "
            f"| {protocol:^22} "
            f"| {aliases:^160} |"
        )
        lines.append(row)

    return "\n".join(lines)


def build_unpublished_table(datasets):
    """Build the simplified unpublished dataset table."""
    unpublished = sorted(
        [d for d in datasets if d.get("status") == "unpublished"],
        key=lambda d: d["name"],
    )

    if not unpublished:
        return ""

    lines = []
    lines.append(
        "| Dataset name                             "
        "| Description "
        "| Citable reference "
        "| Total size "
        "| Cell Painting protocol |"
    )
    lines.append(
        "|------------------------------------------"
        "|-------------"
        "|-------------------"
        "|:----------:"
        "|:----------------------:|"
    )

    for ds in unpublished:
        name = ds["name"]
        desc = escape_md(ds.get("description", ""))
        zenodo = ds.get("zenodo_doi", "")
        if zenodo:
            citable = f"[Zenodo]({zenodo})"
        else:
            citable = ""

        size = ds.get("size", {})
        total = escape_md(size.get("total", "")) if size else ""
        protocol = escape_md(ds.get("protocol", "")) if ds.get("protocol") else ""

        row = (
            f"| {name:<40} "
            f"| {desc} "
            f"| {citable} "
            f"| {total:^10} "
            f"| {protocol:^22} |"
        )
        lines.append(row)

    return "\n".join(lines)


def build_external_contributions_section(datasets):
    """Build a markdown section listing external contributions."""
    entries = []
    for ds in sorted(datasets, key=lambda d: d["name"]):
        contribs = ds.get("external_contributions", [])
        if not contribs:
            continue
        for c in contribs:
            entries.append(
                {
                    "dataset": ds["name"],
                    "contributor": c.get("contributor", ""),
                    "description": c.get("description", ""),
                    "link": c.get("link", ""),
                    "date": c.get("date", ""),
                }
            )

    if not entries:
        return ""

    lines = ["## External Contributions", ""]
    lines.append(
        "The following external contributions have been added to existing datasets:"
    )
    lines.append("")
    lines.append(
        "| Dataset | Contributor | Description | Link | Date |"
    )
    lines.append(
        "|---------|-------------|-------------|------|------|"
    )

    for e in entries:
        dataset = escape_md(e["dataset"])
        contributor = escape_md(e["contributor"])
        description = escape_md(e["description"])
        date = escape_md(e["date"])
        link_cell = f"[Link]({escape_md(e['link'])})" if e["link"] else ""
        lines.append(
            f"| {dataset} "
            f"| {contributor} "
            f"| {description} "
            f"| {link_cell} "
            f"| {date} |"
        )

    return "\n".join(lines)


def build_prefixes_table(datasets):
    """Build the single-column prefixes table from all datasets."""
    all_datasets = sorted(datasets, key=lambda d: d["name"])

    lines = []
    lines.append("| Dataset name                             |")
    lines.append("|------------------------------------------|")

    for ds in all_datasets:
        lines.append(f"| {ds['name']:<40} |")

    return "\n".join(lines)


def splice_between_markers(content, start_marker, end_marker, replacement):
    """Replace content between start and end markers (exclusive of markers)."""
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

    if start_idx == -1:
        print(f"ERROR: Start marker not found: {start_marker}", file=sys.stderr)
        sys.exit(1)
    if end_idx == -1:
        print(f"ERROR: End marker not found: {end_marker}", file=sys.stderr)
        sys.exit(1)

    before = content[: start_idx + len(start_marker)]
    after = content[end_idx:]

    return before + "\n" + replacement + "\n" + after


def generate_readme(datasets, readme_content):
    """Splice generated tables into README.md content."""
    pub_table = build_published_table(datasets)
    unpub_table = build_unpublished_table(datasets)

    result = splice_between_markers(readme_content, PUB_START, PUB_END, pub_table)
    result = splice_between_markers(result, UNPUB_START, UNPUB_END, unpub_table)

    return result


def generate_complete_datasets(datasets):
    """Generate documentation/complete_datasets.md."""
    lines = ["# Complete Datasets", ""]

    pub_table = build_published_table(datasets)
    lines.append(pub_table)
    lines.append("")

    unpub_table = build_unpublished_table(datasets)
    if unpub_table:
        lines.append("## Datasets without publications")
        lines.append("")
        lines.append(
            "These datasets are available in the Cell Painting Gallery but do not have an associated publication."
        )
        lines.append(
            "If you use them, please cite the "
            "[Cell Painting Gallery paper](https://doi.org/10.1038/s41592-024-02399-z) "
            "and any reference listed below."
        )
        lines.append("")
        lines.append(unpub_table)
        lines.append("")

    contrib_section = build_external_contributions_section(datasets)
    if contrib_section:
        lines.append(contrib_section)
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Build Cell Painting Gallery registry outputs"
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate only, no file writes; exits non-zero on errors",
    )
    args = parser.parse_args()

    # Load and validate
    data = load_registry()
    datasets = data.get("datasets", [])

    errors = validate(datasets)
    if errors:
        print("Registry validation errors:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        sys.exit(1)

    published_count = sum(1 for d in datasets if d.get("status") == "published")
    unpublished_count = sum(1 for d in datasets if d.get("status") == "unpublished")
    print(
        f"Registry valid: {len(datasets)} datasets "
        f"({published_count} published, {unpublished_count} unpublished)"
    )

    if args.check:
        print("Check mode: no files written.")
        return

    # Generate README
    readme_content = README_PATH.read_text(encoding="utf-8")
    new_readme = generate_readme(datasets, readme_content)
    README_PATH.write_text(new_readme, encoding="utf-8")
    print(f"Updated {README_PATH}")

    # Generate complete_datasets.md
    complete = generate_complete_datasets(datasets)
    COMPLETE_DATASETS_PATH.write_text(complete, encoding="utf-8")
    print(f"Generated {COMPLETE_DATASETS_PATH}")

    # Generate prefixes.md
    prefixes_content = PREFIXES_PATH.read_text(encoding="utf-8")
    prefixes_table = build_prefixes_table(datasets)
    new_prefixes = splice_between_markers(
        prefixes_content, PREFIX_START, PREFIX_END, prefixes_table
    )
    PREFIXES_PATH.write_text(new_prefixes, encoding="utf-8")
    print(f"Updated {PREFIXES_PATH}")


if __name__ == "__main__":
    main()
