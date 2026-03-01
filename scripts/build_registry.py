#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["pyyaml"]
# ///
"""
Build script for the Cell Painting Gallery dataset registry.

Reads registry.yml and generates:
  - documentation/complete_datasets.md with table + external contributions
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
COMPLETE_DATASETS_PATH = ROOT / "documentation" / "complete_datasets.md"
PREFIXES_PATH = ROOT / "documentation" / "prefixes.md"

NAME_PATTERN = re.compile(r"^cpg\d{4}(-[A-Za-z0-9_-]+)?$")

# Markers in documentation files
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

    if not isinstance(datasets, list):
        errors.append("'datasets' must be a list")
        return errors

    seen_names = set()

    for i, ds in enumerate(datasets):
        prefix = f"Dataset #{i + 1}"

        if not isinstance(ds, dict):
            errors.append(f"{prefix}: entry must be a mapping, got {type(ds).__name__}")
            continue

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

        if "complete" not in ds:
            errors.append(f"{prefix}: missing 'complete'")
        elif not isinstance(ds["complete"], bool):
            errors.append(
                f"{prefix}: 'complete' must be a boolean (true/false)"
            )

        if "description" not in ds:
            errors.append(f"{prefix}: missing 'description'")
        elif ds.get("complete") is True and not ds.get("description"):
            errors.append(f"{prefix}: 'description' required when complete is true")

        if "retired" in ds and not isinstance(ds["retired"], bool):
            errors.append(f"{prefix}: 'retired' must be a boolean (true/false)")
        elif ds.get("retired") is True and ds.get("complete") is True:
            errors.append(f"{prefix}: retired datasets cannot be marked complete")

        if "references" in ds and not isinstance(ds["references"], list):
            errors.append(f"{prefix}: 'references' must be a list")
            continue

    return errors


def format_reference_cell(references):
    """Format the reference column from a list of reference strings/dicts."""
    if not references:
        return ""

    parts = []
    for ref in references:
        if isinstance(ref, str):
            text = ref.strip()
            if text:
                parts.append(text)
            continue

        if not isinstance(ref, dict):
            continue

        authors = ref.get("authors", "")
        publication_url = ref.get("publication", "")
        preprint_url = ref.get("preprint", "")
        generic_url = ref.get("url", "")
        generic_label = ref.get("label", "Reference")
        text = ref.get("text") or ref.get("title") or ""
        note = ref.get("note", "")
        ref_prefix = ref.get("prefix", "")

        piece = ""
        if ref_prefix:
            piece += f"{ref_prefix} "
        if authors:
            piece += f"({authors})"

        if publication_url:
            piece += f" [Publication]({publication_url})"
            if preprint_url:
                piece += f", [Preprint]({preprint_url})"
        elif preprint_url:
            piece += f" [Preprint]({preprint_url})"
        elif generic_url:
            piece += f" [{generic_label}]({generic_url})"
        elif text:
            piece += f" {text}"

        if note:
            piece += f" {note}"
        piece = piece.strip()
        if piece:
            parts.append(piece)

    return escape_md(" ".join(parts))


def format_link_list(items):
    """Format a list of strings or {label, url} dicts as markdown links."""
    if not items:
        return ""

    parts = []
    for item in items:
        if isinstance(item, str):
            parts.append(item)
        else:
            label = item.get("label", "")
            url = item.get("url", "")
            if url:
                parts.append(f"[{label}]({url})")
            else:
                parts.append(label)

    return escape_md(", ".join(parts))


def build_md_table(headers, alignments, rows):
    """Build a markdown table from headers, column alignments, and row data."""
    sep_map = {"left": "---", "center": ":---:", "right": "---:"}
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(sep_map[a] for a in alignments) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def build_datasets_table(datasets):
    """Build the unified 9-column dataset table for all complete datasets."""
    complete = sorted(
        [d for d in datasets if d.get("complete") is True],
        key=lambda d: d["name"],
    )

    headers = [
        "Dataset name",
        "Description",
        "References",
        "Associated repositories",
        "Total size",
        "Images size",
        "Numerical data size",
        "Cell Painting protocol",
        "Other aliases",
    ]
    alignments = [
        "left", "left", "left", "left",
        "center", "center", "center", "center", "center",
    ]

    rows = []
    for ds in complete:
        name = ds["name"]
        if ds.get("external_contributions"):
            name += " `*`"
        size = ds.get("size") or {}
        rows.append([
            name,
            escape_md(ds.get("description", "")),
            format_reference_cell(ds.get("references", [])),
            format_link_list(ds.get("repositories", [])),
            escape_md(size.get("total", "")),
            escape_md(size.get("images", "")),
            escape_md(size.get("numerical", "")),
            escape_md(ds.get("protocol", "")),
            format_link_list(ds.get("aliases", [])),
        ])

    return build_md_table(headers, alignments, rows)


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

    headers = ["Dataset", "Contributor", "Description", "Link", "Date"]
    alignments = ["left", "left", "left", "left", "left"]

    rows = []
    for e in entries:
        link_cell = f"[Link]({escape_md(e['link'])})" if e["link"] else ""
        rows.append([
            escape_md(e["dataset"]),
            escape_md(e["contributor"]),
            escape_md(e["description"]),
            link_cell,
            escape_md(e["date"]),
        ])

    lines = [
        "## External Contributions",
        "",
        "The following external contributions have been added to existing datasets:",
        "",
        build_md_table(headers, alignments, rows),
    ]
    return "\n".join(lines)


def build_prefixes_table(datasets):
    """Build the single-column prefixes table from all datasets."""
    all_datasets = sorted(datasets, key=lambda d: d["name"])
    return build_md_table(
        ["Dataset name"], ["left"],
        [[ds["name"]] for ds in all_datasets],
    )


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


def generate_complete_datasets(datasets):
    """Generate documentation/complete_datasets.md."""
    lines = ["# Complete Datasets", ""]

    table = build_datasets_table(datasets)
    lines.append(table)
    lines.append("")

    has_contribs = any(ds.get("external_contributions") for ds in datasets)
    if has_contribs:
        lines.append(
    "`*` This dataset has external contributions (see below)."
        )
        lines.append("")

    contrib_section = build_external_contributions_section(datasets)
    if contrib_section:
        lines.append(contrib_section)
        lines.append("")

    in_progress = sorted(
        [d for d in datasets if d.get("complete") is not True and not d.get("retired")],
        key=lambda d: d["name"],
    )
    if in_progress:
        lines.append("## Datasets in progress")
        lines.append("")
        lines.append(
            "The following datasets are in progress and not yet fully documented:"
        )
        lines.append("")
        for ds in in_progress:
            lines.append(f"- {ds['name']}")
        lines.append("")

    retired = sorted(
        [d for d in datasets if d.get("retired")],
        key=lambda d: d["name"],
    )
    if retired:
        lines.append("## Retired prefixes")
        lines.append("")
        lines.append(
            "The following prefixes are reserved but not associated with any dataset:"
        )
        lines.append("")
        for ds in retired:
            lines.append(f"- {ds['name']}")
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
    if not isinstance(data, dict):
        print("Registry validation errors:", file=sys.stderr)
        print(
            f"  - Expected a YAML mapping at top level, got {type(data).__name__}",
            file=sys.stderr,
        )
        sys.exit(1)
    datasets = data.get("datasets", [])

    errors = validate(datasets)
    if errors:
        print("Registry validation errors:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        sys.exit(1)

    complete_count = sum(1 for d in datasets if d.get("complete") is True)
    incomplete_count = sum(1 for d in datasets if d.get("complete") is not True)
    print(
        f"Registry valid: {len(datasets)} datasets "
        f"({complete_count} complete, {incomplete_count} incomplete)"
    )

    if args.check:
        print("Check mode: no files written.")
        return

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
