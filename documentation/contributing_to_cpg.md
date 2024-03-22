# Contributing

We welcome contributions to the Cell Painting Gallery.

## Contributing to Documentation

If you would like to contribute to our documentation, please make a [Pull Request](https://github.com/broadinstitute/cellpainting-gallery/pulls).
We particularly welcome contributions to our list of [publications using data from the Cell Painting Gallery](publications.md) and to [workflows accessing the Cell Painting Gallery](workflows.md).

To ask a question that is not covered by our documentation, you are also welcome to create an [Issue](https://github.com/broadinstitute/cellpainting-gallery/issues) in the Cell Painting Gallery repository.
Please note that dataset-specific questions should be directed to the respective dataset repository linked in the [README](https://github.com/broadinstitute/cellpainting-gallery/README.md).

## Contributing Data to the Gallery

Contributions can be in the form of complete datasets or additions to extant datasets (such as segmentations or deep-learning generated profiles).
Please contact @erinweisbart or @shntnu to initiate discussion of a data contribution.
After receiving approval, you will receive a detailed contribution workflow customized for your data contribution.

To be approved, your dataset must required to meet the following requirements:

### Assay structure

All datasets in the Cell Painting Gallery are from a published Cell Painting Assay version or a close derivative.
If you would like to contribute data from a derivative assay it must be useable for morphological profiling in that it stains/labels multiple cellular compartments/organelles.

### Accompanying information

Any data contributions to Cell Painting Gallery must be accompanied by a pull request to the [Cell Painting Gallery repository](https://github.com/broadinstitute/cellpainting-gallery/) with updates to the README to add your dataset to [Available datasets](https://github.com/broadinstitute/cellpainting-gallery/README.md).
If your dataset is associated with a publication, please also edit [Publications](https://github.com/broadinstitute/cellpainting-gallery/docs/publications.md).

### Data structure

#### Remove special characters in folder names

To the maximum extent possible, please avoid the following in your folder names

- Whitespaces
- Special characters other than `_` and `-`

Please delete these characters if they are present in your folder names.

#### Prepare project-specific naming

Reference [data structure](data_structure.md) for comprehensive information on folder structure and naming.
Your data must strictly comply with the data structure we have laid out.
Additionally it must include all, unblinded metadata.

If your new dataset is approved for inclusion, we will assign you a project identifier.
Your source name can be your institution or it can be anonymized.

#### Validate your data

Use our [data validator](http://github.com/broadinstitute.org/cpg) to validate that your data complies with our required structure.
