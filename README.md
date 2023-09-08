# Cell Painting Gallery

This page provides a guide to the datasets that are available in the Cell Painting Gallery, hosted by the AWS Registry of Open Data (RODA): <https://registry.opendata.aws/cellpainting-gallery>

## Citation/license

All the data is released with CC0 1.0 Universal (CC0 1.0).
Still, professional ethics require that you cite the appropriate resources/publications, [listed below](#available-datasets), when using individual datasets.
For example,

> We used the dataset `cpg0000` ([Chandrasekaran et al., 2022](https://doi.org/10.1101/2022.01.05.475090)), available from the Cell Painting Gallery on the Registry of Open Data on AWS (<https://registry.opendata.aws/cellpainting-gallery/>).

## Available datasets

All datasets are generated using the Cell Painting assay unless indicated otherwise. Several updates to that protocol exist ([Cell Painting wiki](https://github.com/carpenterlab/2022_Cimini_NatureProtocols/wiki)).

The datasets are stored with the prefix indicated by the dataset name.
E.g. the first dataset is located at `s3://cellpainting-gallery/cpg0000-jump-pilot` and can be listed using `aws s3 ls --no-sign-request s3://cellpainting-gallery/cpg0000-jump-pilot/` (note the `/` at the end).

The datasets' accession numbers are the first seven characters of the dataset name.
E.g. the accession number of the first dataset is `cpg0000`.

| Dataset name | Description | Publication to cite | Associated repositories | Total size | Images size | Numerical data size | Cell Painting protocol | IDR accession number |
|---|---|---|---|:---:|:---:|:---:|:---:|:---:|
| cpg0000-jump-pilot | 300+ compounds and 160+ genes (CRISPR knockout and overexpression) profiled in A549 and U2OS cells, at two timepoints | 3 | [data](https://github.com/jump-cellpainting/2023_Chandrasekaran_submitted) | 12.3 TB |  |  | v2.5 |  |
| cpg0001-cellpainting-protocol | 300+ compounds profiled in U2OS cells using several different modifications of the Cell Painting protocol | 6 | [data](https://github.com/carpenter-singh-lab/2023_Cimini_NatureProtocols) | 40.3 TB | 18.7 TB | 21.6 TB | v3 and experiments |  |
| cpg0002-jump-scope | 300+ compounds profiled in U2OS using different microscopes and settings | 7 | [data](https://github.com/jump-cellpainting/jump-scope), [analysis](https://github.com/jump-cellpainting/jump-scope-analysis) | 16.7 TB | 12.5 TB | 4.2 TB | v2.5 |  |
| cpg0003-rosetta | 28,000+ genes and compounds profiled in Cell Painting and [L1000](https://doi.org/10.1016%2Fj.cell.2017.10.049) gene expression | 5 | [data](https://github.com/carpenter-singh-lab/2022_Haghighi_NatureMethods) | 8.5 GB |  |  |  |  |
| cpg0004-lincs | 1,571 compounds across 6 doses in A549 cells | 4 | [data](https://github.com/broadinstitute/lincs-cell-painting) | 65.7 TB | 61.9 TB | 3.8 TB | v2 | idr0125 |
| cpg0011-lipocyteprofiler | Variety of lipocytes in different metabolic states and with genetic and drug perturbations | 14 | [analysis](https://github.com/ClaussnitzerLab/Lipocyte-Profiler) | 1.2 TB |  |  | lipocyte |  |
| cpg0012-wawer-bioactivecompoundprofiling | 30,000 compound dataset in U2OS cells | 1,2 |  | 10.7 TB | 3.1 TB | 7.6 TB | v1 | idr0016 |
| cpg0015-heterogeneity | 2,200+ compounds and 200+ genes profiles in U2OS cells | 8 | [data](https://github.com/carpenterlab/2018_Rohban_NatComm) | 204 GB |  |  |  | idr0016, idr0036, idr0033 |
| cpg0016-jump | 116,000+ compounds and 16+ genes (CRISPR knockout and overexpression) profiled in U2OS cells. Over 8 million images (>126 TB), over 1.5 billion cells of numerical data (>126TB), for over 250 TB data in total. | 9 | [resource](https://github.com/jump-cellpainting/datasets) | 358.4 TB |  |  | v3 |  |
| cpg0017-rohban-pathways | 323 genes overexpressed in U2OS cells. Original images re-profiled in 2023 | 11 | [re-profiled data](https://github.com/broadinstitute/cpg0017-rohban-pathways), [original data](https://github.com/carpenterlab/2017_Rohban_eLife) | 321 GB |  |  | v1 |  |
| cpg0018-sing-seedseq | U2OS cells treated with each of 315 unique shRNA sequences |  |  | 247.1 GB | 247.1 GB | 0 |  |  |
| cpg0019-moshkov-deepprofiler | 8.3 million single cells from 232 plates, across 488 treatments from 5 public datasets, used for learning representations | 10 | [data](https://github.com/broadinstitute/DeepProfilerExperiments), [software](https://github.com/cytomining/DeepProfiler) | 522 GB |  |  | dataset dependent |  |
| cpg0021-periscope | 30 million cells with 20,000 single-gene knockouts in pooled format. A549 cells and HeLa cells in two growth media | 12,15 | [analysis](https://github.com/broadinstitute/2022_PERISCOPE), [data](https://github.com/broadinstitute/CP186-A549-WG), [data](https://github.com/broadinstitute/CP257-HeLa-WG) | 56.0 TB | 45.0 TB | 11.0 TB | pooled |  |
| cpg0022-cmqtl | 297 iPSC lines | 13 | [data](https://github.com/broadinstitute/cmQTL) | 10.6 TB |  |  | v2.5 |  |
| cpg0028-kelley-resistance | Bortezomib resistant HCT116 clones | 16 | [data](https://github.com/broadinstitute/profiling-resistance-mechanisms) |  |  |  |  |  |

## Downloading from Cell Painting Gallery

See [Folder Structure](folder_structure.md) for a complete description of data organization in Cell Painting gallery.
Note that for each dataset you can download just images, just extracted features and metadata, or both.
Note also that many datasets contain separate batches and you may want a subset of available batches.

If you'd like to just browse the data, it's a lot easier [to do so using a storage browser](https://stackoverflow.com/a/72143198/1094109).

## Publications using datasets in Cell Painting Gallery

|    | First Author   | <div style="width:350px">Title</div>                                                                                                 | Year | <div style="width:150px">Publication URL</div> | Dataset Name in Gallery                  |
|----|----------------|--------------------------------------------------------------------------------------------------------------------------------------|------|------------------------------------------------|------------------------------------------|
| 1  | Wawer          | Toward performance-diverse small-molecule libraries for cell-based phenotypic screening using multiplexed high-dimensional profiling | 2014 | [Publication](https://doi.org/10.1073/pnas.1410933111)      | cpg0012-wawer-bioactivecompoundprofiling |
| 2  | Bray           | A dataset of images and morphological profiles of 30 000 small-molecule treatments using the Cell Painting assay                     | 2017 | [Publication](https://doi.org/10.1093/gigascience/giw014)   | cpg0012-wawer-bioactivecompoundprofiling |
| 3  | Chandrasekaran | Three million images and morphological profiles of cells treated with matched chemical and genetic perturbations                     | 2022 | [Preprint](https://doi.org/10.1101/2022.01.05.475090)    | cpg0000-jump-pilot                       |
| 4  | Way            | Morphology and gene expression profiling provide complementary information for mapping cell state                                    | 2022 | [Publication](https://doi.org/10.1016/j.cels.2022.10.001), [Preprint](https://doi.org/10.1101/2021.10.21.465335) | cpg0004-lincs                            |
| 5  | Haghighi       | High-Dimensional Gene Expression and Morphology Profiles of Cells across 28,000 Genetic and Chemical Perturbations                   | 2022 | [Publication](https://doi.org/10.1038/s41592-022-01667-0), [Preprint](https://doi.org/10.1101/2021.09.08.459417) | cpg0003-rosetta                          |
| 6  | Cimini         | Optimizing the Cell Painting assay for image-based profiling                                                                         | 2022 | [Publication](https://doi.org/10.1038/nprot.2016.105), [Preprint](https://doi.org/10.1101/2022.07.13.499171) | cpg0001-cellpainting-protocol            |
| 7  | Tromans-Coia and Jamali | Assessing the performance of the Cell Painting assay across different imaging systems                                       | 2023 | [Preprint](https://doi.org/10.1101/2023.02.15.528711)    | cpg0002-jump-scope                       |
| 8  | Rohban         | Capturing single-cell heterogeneity via data fusion improves image-based profiling                                                   | 2019 | [Publication](https://doi.org/10.1038/s41467-019-10154-8)   | cpg0015-heterogeneity                    |
| 9  | Chandrasekaran | JUMP Cell Painting dataset: morphological impact of 136,000 chemical and genetic perturbations                                       | 2023 | [Preprint](https://doi.org/10.1101/2023.03.23.534023)    | cpg0016-jump                             |
| 10 | Moshkov        | Learning representations for image-based profiling of perturbations                                                                  | 2022 | [Preprint](https://doi.org/10.1101/2022.08.12.503783)    | cpg0019-moshkov-deepprofiler             |
| 11 | Rohban         | Systematic morphological profiling of human gene and allele function via Cell Painting                                               | 2017 | [Publication](https://doi.org/10.7554/eLife.24060), [Preprint](https://doi.org/10.1101/092403) | cpg0017-rohban-pathways                  |
| 12 | Ramezani, Bauman, Singh, and Weisbart | A genome-wide atlas of human cell morphology | 2023 | [Preprint](https://doi.org/10.1101/2023.08.06.552164)          | cpg0021-periscope                  |
| 13 | Tegtmeyer | High-dimensional pheotyping to define the genetic basis of cellular morphology | 2023 | [Preprint](https://doi.org/10.1101/2023.01.09.522731)          | cpg0022-cmqtl                 |
| 14 | Laber and Strobel | Discovering cellular programs of intrinsic and extrinsic drivers of metabolic traits using LipocyteProfiler | 2023 | [Publication](https://doi.org/10.1016/j.xgen.2023.100346), [Preprint](https://www.biorxiv.org/content/10.1101/2021.07.17.452050v1) | cpg0011-lipocyteprofiler                |
| 15 | Haghighi | Pseudo-labeling enhanced by privileged information and its application to in situ sequencing images | 2023 | [Publication](https://www.ijcai.org/proceedings/2023/0531.pdf), [Preprint](https://arxiv.org/abs/2306.15898)| cpg0021-periscope  |
| 16 | Kelley | High-content microscopy reveals a morphological signature of bortezomib resistance | 2023 | [Preprint](https://doi.org/10.1101/2023.05.02.539137) | cpg0028-kelley-resistance  |

## Cell Painting protocol versions
More information about protocol changes and development is available [here](https://github.com/carpenter-singh-lab/2023_Cimini_NatureProtocols/wiki#updates-to-the-cell-painting-protocol).

| Protocol | Year | Publication |
| -------- | ---- | ----------- |
| v1 | 2013 | Gustafsdottir, SM., et al. [Multiplex cytological profiling assay to measure diverse cellular states](https://doi.org/10.1371/journal.pone.0080999). PLoS ONE 8(12): e80999. |
| v2 | 2016 | Bray, MA., et al. [Cell Painting, a high-content image-based assay for morphological profiling using multiplexed fluorescent dyes](https://doi.org/10.1038/nprot.2016.105). Nat Protoc 11, 1757–1774 |
| v2.5 | 2021 | 3 |
| v3 | 2023 | 6 |
| pooled | 2023 | 12 |
| lipocyte | 2023 | 14 |

## Contributing to Cell Painting Gallery

See [Folder Structure](folder_structure.md) for the required folder structure of your data.
See [Upload](upload.md) for a complete description of how to upload to the Cell Painting gallery bucket.

Any data contributions to Cell Painting Gallery must be accompanied by a pull request to this repository with updates to this README to add your dataset to [Available datasets](#available-datasets) and [Publications](#publications-using-datasets-in-cell-painting-gallery).

## Complementary Datasets

For other sources of publicly available Cell Painting datasets we encourage you to explore:

- [Recursion](https://www.rxrx.ai)
- [Broad Bioimage Benchmark Collection (BBBC)](https://bbbc.broadinstitute.org)
- [Image Data Resource](https://idr.openmicroscopy.org)
