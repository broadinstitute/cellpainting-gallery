# CellPainting Gallery

Documentation for https://registry.opendata.aws/cellpainting-gallery

## Citation

All the data will be released with CC0 1.0 Universal (CC0 1.0).
However, please cite the appropriate resources/publications, [listed below](#available-datasets), when citing individual datasets.

## Available datasets

| Name in Gallery                          | Description                                                               | Publication to cite | IDR identifier   |
| ---------------------------------------- | ------------------------------------------------------------------------- | ------------------- | ---------------- |
| cpg0003-rosetta                          |                                                                           |                     |                  |
| cpg0004-lincs                            |                                                                           |                     |                  |
| cpg0005-gerry-bioactivity                |                                                                           |                     |                  |
| cpg0006-miami                            |                                                                           |                     |                  |
| cpg0007-prism                            |                                                                           |                     |                  |
| cpg0009-molglue                          |                                                                           |                     |                  |
| cpg0012-wawer-bioactivecompoundprofiling | 30,000 compound dataset in U2OS cells                                     | 2                   | idr0016, idr0036 |
| cpg0014-jump-adipocyte                   |                                                                           |                     |                  |
| jump-pilot                               |                                                                           |                     |                  |
| jump                                     | CRISPR knockdown, ORF overexpression, and 120,000 compounds in U2OS cells |                     |                  |

## Downloading from CellPainting Gallery

See [Folder Structure](folder_structure.md) for a complete description of data organization in CellPainting gallery.
Note that for each dataset you can download just images, just extracted features and metadata, or both.
Note also that many datasets contain separate batches and you may want a subset of available batches.

## Publications using datasets in CellPainting Gallery
|     | First Author  | <div style="width:350px">Title</div>                                                                                                 | Year | <div style="width:150px">Publication URL</div>                           | Dataset Name in Gallery                  |
| --- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---- | ------------------------------------------------------------------------ | ---------------------------------------- |
| 1   | Gustafsdottir | Multiplex Cytological Profiling Assay to Measure Diverse Cellular States                                                             | 2013 | http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0080999 | cpg0012-wawer-bioactivecompoundprofiling |
| 2   | Wawer         | Toward performance-diverse small-molecule libraries for cell-based phenotypic screening using multiplexed high-dimensional profiling | 2014 | http://www.pnas.org/content/111/30/10911                                 | cpg0012-wawer-bioactivecompoundprofiling |
| 3   | Singh         | Morphological Profiles of RNAi-Induced Gene Knockdown Are Highly Reproducible but Dominated by Seed Effects                          | 2015 | http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0131370 |                                          |
| 4   | Bray          | A dataset of images and morphological profiles of 30 000 small-molecule treatments using the Cell Painting assay                     | 2017 | https://academic.oup.com/gigascience/article/6/12/1/2865213              | cpg0012-wawer-bioactivecompoundprofiling |
| 5   | Bray          | Cell Painting, a high-content image-based assay for morphological profiling using multiplexed fluorescent dyes                       | 2016 | https://pubmed.ncbi.nlm.nih.gov/27560178/                                |                                          |
| 6   | Rohban        | Systematic morphological profiling of human gene and allele function via Cell Painting                                               | 2017 | https://elifesciences.org/content/6/e24060                               |                                          |
| 7   | Caicedo       | Cell Painting predicts impact of lung cancer variants                                                                                | 2022 | https://www.molbiolcell.org/doi/10.1091/mbc.E21-11-0538                  |                                          |

## Contributing to CellPainting Gallery

See [Folder Structure](folder_structure.md) for the required folder structure of your data. See [Upload](upload.md) for a complete description of how to upload to the CellPainting gallery bucket.

Any data contributions to CellPainting Gallery must be accompanied by a pull request to this repository with updates to this README to add your dataset to [Available datasets](#available-datasets) and [Publications](#publications-using-datasets-in-cellpainting-gallery).

## Complementary Datasets

For other sources of publicly available CellPainting datasets we encourage you to explore:
- [Recursion](https://www.rxrx.ai)
- [Broad Bioimage Benchmark Collection (BBBC)](https://bbbc.broadinstitute.org)
- [Image Data Resource](https://idr.openmicroscopy.org)
