# Organizational Philosophy of the Cell Painting Gallery

This document explains the design philosophy behind the Cell Painting Gallery's folder structure, its evolution, and how it addresses the practical challenges of organizing large-scale scientific data.

## Core Philosophy: Hierarchical Workflow Preservation

The Cell Painting Gallery follows a philosophy of strict standardization that mirrors the experimental and computational workflow:

```
images → analysis → backend → profiles
(raw data) → (segmentation) → (aggregation) → (normalized features)
```

### Key Principles

1. **Rigid Standardization**: Every project must follow the exact same hierarchy, even requiring "redundant" nesting (e.g., institution folders even for single-source projects).

2. **Workflow Preservation**: The structure preserves key stages of the analysis pipeline - from raw microscope output through segmentation to final profiles.

3. **Temporal-Spatial Organization**: 
   - Time: Batches by date (YYYY_MM_DD)
   - Space: Institution → Plate → Well → Site
   - Purpose: Raw → Processed → Analyzed

4. **Separation by Computational Paradigm**: Clear boundaries between traditional analysis (`workspace/`) and deep learning approaches (`workspace_dl/`).

## The Evolution Challenge: One-to-Many Analysis

The original structure assumed a linear pipeline where each dataset has one canonical analysis. In practice, scientific exploration requires multiple valid interpretations of the same data:

```
                  ┌→ CellProfiler v3 → profiles_v1
images ─────────→ ├→ CellProfiler v4 → profiles_v2
                  ├→ Cellpose → different segmentations → profiles_v3
                  └→ DeepProfiler → embeddings → profiles_dl
```

This created a fundamental constraint: where do alternative analyses go without breaking existing tools or overwriting data?

## The Adaptive Solution

The Cell Painting Gallery evolved a two-tier architecture while maintaining backward compatibility:

### Tier 1: Primary Processing (Rigid)
- Follows the original standardized structure
- One canonical path for each data type
- Located in standard folders: `profiles/`, `analysis/`, etc.

### Tier 2: Assembled/Derived Products (Flexible)
- Allows versioning and multiple processing variants
- Uses parameterized paths within the existing structure
- Example: `profiles_assembled/{subset_name}/{version}/{variant}.parquet`

This pattern embeds flexibility exactly where needed:
```
Rigid part:                         Flexible part:
/workspace/profiles_assembled/  →   /subset/version/processing_variant.parquet
(where assembled profiles live)     (which subset, how processed)
```

## Implementation Strategies

### 1. Method Encoding in Paths
The `workspace_dl` structure pioneered encoding processing identity in paths:
```
workspace_dl/embeddings/efficientnet_v2_imagenet1k_s_feature_vector_2_ec756ff/
```

### 2. Versioned Subdirectories
For assembled profiles, versions and variants are explicit (introduced in the [JUMP Hub manifest guide](https://github.com/broadinstitute/jump_hub/blob/213f90a6e1cdcf7ee665eb56ecf5d16c886dd7eb/howto/2_create_project_manifest.md)):
```
profiles_assembled/compound_no_source7/v1.0/profiles_var_mad_int_featselect.parquet
```

### 3. Manifest-Based Indexing
External manifest files track:
- What data was processed (`profile_url`)
- How it was processed (`recipe_permalink`)
- With what parameters (`config_permalink`)
- Result verification (`etag`)

This separates storage (simple folder structure) from organization (rich metadata).

## Consistency Through Evolution

Despite these adaptations, the core structure remains consistent:
- Primary data paths never changed
- New patterns extend rather than replace existing ones
- Tools expecting the original structure continue to work
- The Gallery remains the single source of truth for both raw and processed data

## Practical Benefits

This evolved philosophy provides:
1. **Reproducibility**: Standardized paths and manifest tracking enable recreation of analyses
2. **Scalability**: Consistent structure across thousands of datasets
3. **Flexibility**: Multiple analysis approaches without disrupting core data
4. **Automation**: Tools can reliably navigate the standardized structure
5. **Discovery**: Researchers can explore different processing approaches

## Summary

The Cell Painting Gallery's organizational philosophy has successfully evolved from a rigid, single-pipeline structure to a flexible system that accommodates multiple analysis approaches while maintaining backward compatibility. The key insight is that standardization and flexibility are not opposing forces - by establishing rigid conventions at the storage level and flexible patterns at the analysis level, the Gallery serves both automated processing and exploratory science.