# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the **Cell Painting Gallery documentation repository**. The Cell Painting Gallery is a public collection of Cell Painting microscopy datasets hosted on AWS S3 (Registry of Open Data). This repository contains:

- Documentation (Jupyter Book format) published to GitHub Pages
- Dataset registry and metadata (README.md table of datasets)
- Guidelines for data contributors

**Important**: This repository does **NOT** contain the actual imaging data. The datasets live on AWS S3 at `s3://cellpainting-gallery/`. This repo only documents how to access and contribute to that S3-hosted data.

## Data Structure Philosophy

The Cell Painting Gallery follows a **rigid hierarchical structure** designed to mirror the Cell Painting analysis workflow:

```
images → analysis → backend → profiles
(raw microscopy) → (CellProfiler output) → (SQLite databases) → (processed features)
```

### Key Structural Principles

1. **Fixed Storage Conventions**: Every dataset uses identical folder hierarchy
   - `<project>/<source>/images/` - raw microscopy images
   - `<project>/<source>/workspace/` - CellProfiler-based analysis
   - `<project>/<source>/workspace_dl/` - deep learning features

2. **Batch Organization**: Data grouped by acquisition date
   - Format: `YYYY_MM_DD_<batch-name>/`
   - Example: `2021_04_26_Batch1/`

3. **Two-Tier System**:
   - **Tier 1** (Fixed): Primary data with standardized paths (`profiles/`, `analysis/`)
   - **Tier 2** (Parameterized): Derived products with flexible paths embedded in rigid structure
     - Example: `workspace/profiles_assembled/{subset}/{version}/{processing_variant}.parquet`
     - Example: `workspace_dl/embeddings/{network_hash}/`

4. **Required Folders** under `workspace/`:
   - `analysis/` - CellProfiler CSV outputs
   - `backend/` - SQLite databases and aggregated profiles
   - `load_data_csv/` - CellProfiler LoadData files (with S3 URLs)
   - `metadata/` - Plate maps and barcode assignments
   - `profiles/` - Per-plate processed profiles

5. **Optional Folders**:
   - `profiles_assembled/` - Cross-batch/cross-source aggregated profiles
   - `segmentation/` - Alternative segmentation masks
   - `quality_control/` - QC heatmaps and reports
   - `pipelines/` - CellProfiler .cppipe files

See `documentation/data_structure.md` for complete specification and `documentation/organizational_philosophy.md` for design rationale.

## Dataset Naming Conventions

- **Project prefix**: `cpg####-<descriptive-tag>` (e.g., `cpg0016-jump`, `cpg0022-cmqtl`)
- **Accession number**: First 7 characters (e.g., `cpg0016`)
- **Source identifier**: Institution or anonymized (e.g., `broad/`, `source_4/`)
- **Plate names**: Must be unique identifiers, may be truncated from full microscope output

## Contributing Data

Data contributions follow a **staging-to-production workflow**:

1. Contributor contacts @erinweisbart or @shntnu to initiate discussion
2. Gallery maintainers assign a `cpg####` identifier and create a tracking GitHub Discussion
3. Data is uploaded to `s3://staging-cellpainting-gallery/` using AWS CLI
4. Contributor/champion verifies structure compliance
5. Maintainers approve and transfer to production `s3://cellpainting-gallery/`
6. Contributor submits PR to update `README.md` with new dataset entry

See `documentation/contributing_to_cpg.md` and `documentation/uploading_to_cpg.md` for complete workflow.

## Editing Documentation

### Adding a New Dataset

1. **Update README.md**: Add row to the main datasets table with all required columns
   - Dataset name (`cpg####-tag`)
   - Description
   - Publication links
   - Associated repositories
   - Size information
   - Protocol version
   - Other aliases

2. **Update publications.md** (if applicable): Add publication reference

3. The `add_README_to_docs.py` script automatically extracts the table to `complete_datasets.md` during build

### Modifying Structure Documentation

When documenting changes to the data structure:

- Update `documentation/data_structure.md` for technical specifications
- Update `documentation/organizational_philosophy.md` for design rationale
- Ensure examples use real dataset prefixes (e.g., `cpg0016-jump`)
- Include complete folder trees with proper indentation
- Use S3 URLs starting with `s3://cellpainting-gallery/`

## Key External Links

- Main AWS registry page: <https://registry.opendata.aws/cellpainting-gallery>
- Published documentation: <https://broadinstitute.github.io/cellpainting-gallery/>
- JUMP Hub (cpg0016 analysis): <https://broad.io/jump>
- Profiling recipe: <https://github.com/cytomining/profiling-recipe>
- JUMP profiling recipe: <https://github.com/broadinstitute/jump-profiling-recipe>
- Image-based Profiling Handbook: <https://cytomining.github.io/profiling-handbook/>
