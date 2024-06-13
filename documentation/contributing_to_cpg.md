# Contributing

We welcome contributions to the Cell Painting Gallery.

## Contributing to Documentation

If you would like to contribute to our documentation, please make a [Pull Request](https://github.com/broadinstitute/cellpainting-gallery/pulls).
We particularly welcome contributions to our list of [publications using data from the Cell Painting Gallery](publications.md) and to [workflows accessing the Cell Painting Gallery](workflows.md).

To ask a question that is not covered by our documentation, you are also welcome to create an [Issue](https://github.com/broadinstitute/cellpainting-gallery/issues) in the Cell Painting Gallery repository.
Please note that the Cell Painting Gallery is not a place to ask dataset-specific questions.
Instead, please direct such questions to the respective dataset repository linked in the [README](https://github.com/broadinstitute/cellpainting-gallery/README.md) or if no dataset repository, to the authors of any associated publication.

## Contributing Data to the Gallery

Contributions can be in the form of complete datasets or additions to extant datasets (e.g. segmentations or deep-learning generated profiles).
Please contact @erinweisbart or @shntnu to initiate discussion of a data contribution.

For new datasets, please include the following details in your contact:

1) assay used (standard Cell Painting or describe the variation. If you would like to contribute data from a derivative assay it must be useable for morphological profiling in that it stains/labels multiple cellular compartments/organelles.)
2) approximate data size
3) components you wish to contribute (all are described in [data structure](https://broadinstitute.github.io/cellpainting-gallery/data_structure.html)) (major components: `images`, `analysis`, `backend`, `load_data_csv`, `profiles`. optional components: `pipelines`, `qc`, etc.). Note that `metadata` is required.
4) institutional identifier to use for data (e.g. `broad`, `anonymous`)
5) suggested top level project tag. Typically this is a 1 word summary of the project (e.g. cpg0011-lipocyteprofiler, cpg0016-jump, cpg0022-cmqtl) and sometimes also includes the last name of the first author (e.g. cpg0010-caie-drugresponse, cpg0028-kelley-resistance, cpg0031-caicedo-cmvip)

For existing datasets, please  the following details include in your contact:

1) top-level project tag that your data corresponds to (e.g. `cpg0016-jump`)
2) approximate data size
3) components you wish to contribute

After approval, we will assign you a project identifier and create a new [Github Discussion](https://github.com/broadinstitute/cellpainting-gallery/discussions) to provide next steps and track data deposition.

## Preparing for data deposition

In preparation for transferring data, please perform all of the following steps:

### Remove special characters in folder names

To the maximum extent possible, please avoid the following in your folder names

- Whitespaces
- Special characters other than `_` and `-`

Please delete these characters if they are present in your folder names.

### Prepare project-specific naming

Reference [data structure](data_structure.md) for comprehensive information on folder structure and naming.
Your data must strictly comply with the data structure we have laid out.
Additionally it must include all, unblinded metadata.

### Validate your data

We are building a [data validator](http://github.com/broadinstitute/cpg/cpgdata) to check compliance with our required structure.
It is currently in alpha and for internal use but we plan to develop it to the point that contributors can use it to validate their data before deposition in the future.

### Create a pull-request

Any data contributions to Cell Painting Gallery must be accompanied by a pull request to the [Cell Painting Gallery repository](https://github.com/broadinstitute/cellpainting-gallery/) with updates to the README to add your dataset to [Available datasets](https://github.com/broadinstitute/cellpainting-gallery/README.md).
If your dataset is associated with a publication, please also edit [Publications](https://github.com/broadinstitute/cellpainting-gallery/docs/publications.md).
