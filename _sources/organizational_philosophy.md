# Data Organization in the Cell Painting Gallery

This document explains the reasoning behind the Cell Painting Gallery's folder structure and how it has evolved.
For the technical specification of the folder structure itself, see [data_structure.md](data_structure.md).

The Cell Painting Gallery has evolved from supporting single analyses to multiple processing variants while maintaining backwards compatibility.
Fixed storage conventions combined with parameterized analysis paths support both automated pipelines and exploratory research.

## Core Principle: Mirror the Cell Painting Workflow

The Cell Painting Gallery structure was built around the standard Cell Painting analysis workflow:

```
images → analysis → backend → profiles
(raw data) → (image and object measurements) → (collation of single cell measurements) → (aggregation and processing of features)
```

It was built around the principles of:

1. **Uniform Structure**: Every project uses identical folder hierarchy, including seemingly redundant levels (e.g., institution folders even for single-source projects).

2. **Workflow Mapping**: Folders correspond to analysis stages - from raw images through analysis measurements to normalized profiles.

3. **Time and Location Hierarchy**:
   - Time: Batches by date (YYYY_MM_DD)
   - Space: Institution → Plate → Well → Site
   - Purpose: Raw → Processed → Analyzed

4. **Method Separation**: Traditional CellProfiler analysis in `workspace/`, deep learning approaches in `workspace_dl/`.

## The Evolution Challenge: One-to-Many Analysis

The original structure assumed a linear pipeline where each dataset has one canonical analysis.
In practice, scientific exploration requires multiple valid interpretations of the same data.
For example, the same images may be processed multiple times with similar but distinct tools:

```
                  ┌→ CellProfiler v3 → profiles_v1
images ─────────→ ├→ CellProfiler v4 → profiles_v2
                  ├→ Cellpose → different segmentations → profiles_v3
                  └→ DeepProfiler → embeddings → profiles_dl
```

This created a constraint: where to store alternative analyses without breaking existing tools or overwriting data?
As a solution, we adopted a two-tier system that maintains backward compatibility:

**Tier 1: Primary Data (Fixed Structure)**

- Original standardized paths
- Single canonical location per data type
- Standard folders: `profiles/`, `analysis/`, etc.

**Tier 2: Derived Products (Parameterized)**

- Multiple versions and processing variants
- Flexible, parameterized paths are embedded within existing rigid structure

Examples:

```
Fixed path (standardized location):   Parameterized path (specific analysis parameters):
/workspace/profiles_assembled/   →    /{subset}/{version}/{processing_variant}.parquet
/workspace/profiles_assembled/   →    /compound_no_source7/v1.0/profiles_var_mad_int_featselect.parquet

/workspace_dl/embeddings/      →      /{network_or_model_with_hash}/
/workspace_dl/embeddings/      →      /efficientnet_v2_imagenet1k_s_feature_vector_2_ec756ff/
```

For assembled profiles, we use versioned subdirectories combined with manifest files for provenance tracking ([introduced](https://github.com/broadinstitute/jump_hub/pull/101) in the [JUMP Hub manifest guide](https://github.com/broadinstitute/jump_hub/blob/213f90a6e1cdcf7ee665eb56ecf5d16c886dd7eb/howto/2_create_project_manifest.md)).
This approach decouples physical storage from logical organization - files can be moved or reorganized while maintaining complete history and provenance through the manifest.

**Metadata tracking** (manifest files) documents include:
- What data was processed (`profile_url`)
- How it was processed (`recipe_permalink`)
- With what parameters (`config_permalink`)
- Result verification (`etag`)

## Benefits

This approach enables:

1. **Reproducibility**: Standardized paths and manifests document analysis provenance
2. **Scalability**: Consistent structure across thousands of plates
3. **Multiple analyses**: Different processing pipelines without data conflicts
4. **Automation**: Predictable paths for computational tools
5. **Flexibility**: Researchers can iterate on processing methods
