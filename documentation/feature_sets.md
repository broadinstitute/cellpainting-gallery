# Feature Sets

## CellProfiler Features

An overview of CellProfiler features as typically measured in Cell Painting is available in the [Cell Painting Assay Wiki](https://github.com/carpenter-singh-lab/2023_Cimini_NatureProtocols/wiki/What-do-Cell-Painting-features-mean%3F).

Features measured can vary from dataset to dataset in the Cell Painting Gallery.
Common sources of variation for measured features include:

1) the version of the Cell Painting Assay analysis pipeline used
2) the version of CellProfiler used
3) the microscope used
4) the stain panel used

Note that feature selection is a component of the Cell Painting Assay data analysis workflow so usually not all features measured by CellProfiler are contained in the final profiles used for data analysis.

For the creation of the Cell Painting Gallery, we re-processed a number of historical datasets using the most up-to-date [Cell Painting Assay analysis pipeline](https://github.com/broadinstitute/imaging-platform-pipelines/blob/master/JUMP_production/JUMP_analysis_v3.cppipe).
Reprocessed datasets include:

- `cpg0012-wawer-bioactivecompoundprofiling`
- `cpg0017-rohban-pathways`
- `cpg0031-caicedo-cmvip`

For `cpg0031-caicedo-cmvip`, the new feature set contains 3616 features that are not in the original feature set.

- 230 features are additional features measured only from the Mitochondrial channel that quantify the mitochondrial structure (including skeleton and branching).
- 979 features are Image features - measurements taken on the whole image (instead of in segmented Nuclei, Cell or Cytoplasm compartments).
These features can be used as per-image QC measurements to enable filtering of low-quality images.
They can also be used for exploration of signal contained in images without requiring segmentation.
- 112 features are Granularity features.
We show an example of this category of features being used for specific biological discovery in [PERISCOPE](https://doi.org/10.1101/2023.08.06.552164).
- 3120 features are Texture features.
(The original dataset had 630 Texture features which do have correspondents in the new Texture features but do not have the exact same name because we added extra information to the feature name to indicate the number of gray levels at which the feature was measured).
Major [improvements to our CellProfiler software](https://doi.org/10.1186/s12859-021-04344-9) enabled this dramatic expansion of Texture features.
