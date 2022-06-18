# Cell Painting Gallery

Documentation for https://registry.opendata.aws/cellpainting-gallery

## Citation

All the data will be released with CC0 1.0 Universal (CC0 1.0).
However, please cite the appropriate resources/publications, [listed below](#available-datasets), when citing individual datasets.

## Available datasets

| Name in Gallery                          | Description                                  | Publication to cite | IDR identifier |
| ---------------------------------------- | -------------------------------------------- | ------------------- | -------------- |
| jump-pilot/source_4                      |                                              |                     |                |
| cpg0003-rosetta                          |                                              | 10                  |                |
| cpg0004-lincs                            | 1,571 compounds across 6 doses in A549 cells | 9                   | idr0125        |
| cpg0012-wawer-bioactivecompoundprofiling | 30,000 compound dataset in U2-OS cells       | 2,4                 | idr0016        |

## Downloading from Cell Painting Gallery

See [Folder Structure](folder_structure.md) for a complete description of data organization in Cell Painting gallery.
Note that for each dataset you can download just images, just extracted features and metadata, or both.
Note also that many datasets contain separate batches and you may want a subset of available batches.

## Publications using datasets in Cell Painting Gallery

|     | First Author   | <div style="width:350px">Title</div>                                                                                                 | Year | <div style="width:150px">Publication URL</div> | Dataset Name in Gallery                  |
| --- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---- | ---------------------------------------------- | ---------------------------------------- |
| 1   | Gustafsdottir  | Multiplex Cytological Profiling Assay to Measure Diverse Cellular States                                                             | 2013 | https://doi.org/10.1371/journal.pone.0080999   |                                          |
| 2   | Wawer          | Toward performance-diverse small-molecule libraries for cell-based phenotypic screening using multiplexed high-dimensional profiling | 2014 | https://doi.org/10.1073/pnas.1410933111        | cpg0012-wawer-bioactivecompoundprofiling |
| 3   | Singh          | Morphological Profiles of RNAi-Induced Gene Knockdown Are Highly Reproducible but Dominated by Seed Effects                          | 2015 | https://doi.org/10.1371/journal.pone.0131370   |                                          |
| 4   | Bray           | A dataset of images and morphological profiles of 30 000 small-molecule treatments using the Cell Painting assay                     | 2017 | https://doi.org/10.1093/gigascience/giw014     | cpg0012-wawer-bioactivecompoundprofiling |
| 5   | Bray           | Cell Painting, a high-content image-based assay for morphological profiling using multiplexed fluorescent dyes                       | 2016 | https://doi.org/10.1038/nprot.2016.105         |                                          |
| 6   | Rohban         | Systematic morphological profiling of human gene and allele function via Cell Painting                                               | 2017 | https://doi.org/10.7554/eLife.24060            |                                          |
| 7   | Caicedo        | Cell Painting predicts impact of lung cancer variants                                                                                | 2022 | https://doi.org/10.1091/mbc.E21-11-0538        |                                          |
| 8   | Chandrasekaran | Three million images and morphological profiles of cells treated with matched chemical and genetic perturbations                     | 2022 | https://doi.org/10.1101/2022.01.05.475090      | jump-pilots/source_4                     |
| 9   | Way            | Morphology and gene expression profiling provide complementary information for mapping cell state                                    | 2022 | https://doi.org/10.1101/2021.10.21.465335      | cpg0004-lincs                            |
| 10  | Haghighi       | High-Dimensional Gene Expression and Morphology Profiles of Cells across 28,000 Genetic and Chemical Perturbations                   | 2022 | https://doi.org/10.1101/2021.09.08.459417      | cpg0003-rosetta                          |
| 11  | Cimini         | Optimizing the Cell Painting assay for image-based profiling                                                                         | 2022 | In Preparation                                 | jump-pilots/source_4                     |

## Contributing to Cell Painting Gallery

See [Folder Structure](folder_structure.md) for the required folder structure of your data.
See [Upload](upload.md) for a complete description of how to upload to the Cell Painting gallery bucket.

Any data contributions to Cell Painting Gallery must be accompanied by a pull request to this repository with updates to this README to add your dataset to [Available datasets](#available-datasets) and [Publications](#publications-using-datasets-in-cellpainting-gallery).

## Complementary Datasets

For other sources of publicly available Cell Painting datasets we encourage you to explore:
- [Recursion](https://www.rxrx.ai)
- [Broad Bioimage Benchmark Collection (BBBC)](https://bbbc.broadinstitute.org)
- [Image Data Resource](https://idr.openmicroscopy.org)
