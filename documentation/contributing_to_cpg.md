# Contributing

We welcome contributions to the Cell Painting Gallery.

## Contributing to Documentation

If you would like to contribute to our documentation, please make a [Pull Request](https://github.com/broadinstitute/cellpainting-gallery/pulls).
We particularly welcome contributions to our list of [publications using data from the Cell Painting Gallery](publications.md) and to [workflows accessing the Cell Painting Gallery](workflows.md).

To ask a question that is not covered by our documentation, you are also welcome to create an [Issue](https://github.com/broadinstitute/cellpainting-gallery/issues) in the Cell Painting Gallery repository.
Please note that the Cell Painting Gallery is not a place to ask dataset-specific questions.
Instead, please direct such questions to the respective dataset repository linked in [Complete Datasets](complete_datasets.md) or if no dataset repository, to the authors of any associated publication.

## Contributing Data to the Gallery

Contributions can be in the form of complete datasets or additions to extant datasets (e.g. segmentations or deep-learning generated profiles).
Please contact @erinweisbart or @shntnu to initiate discussion of a data contribution.

For new datasets, please include the following details in your email:

**Required information:**

1. **Assay type**: Standard Cell Painting (6 stains: Hoechst 33342/DNA, Concanavalin A/ER, SYTO 14/nucleoli & RNA, Phalloidin/actin, WGA/Golgi & plasma membrane, MitoTracker Deep Red/mitochondria) or describe the variation. Variations must include at least 3 of the 6 canonical stains.
2. **Approximate data size**: Total size estimate (e.g., "5 TB", "500 GB")
3. **Components you wish to contribute**: All components are described in [data structure](data_structure.md). Major components include: `images`, `analysis`, `backend`, `load_data_csv`, `profiles`. Optional components: `pipelines`, `qc`, etc. Note that `metadata` is required.
4. **Institutional identifier**: This will be used in the data path structure (e.g., `cpg####-tag/broad/` or `cpg####-tag/anonymous/`). Examples: `broad`, `anonymous`, `edinburgh`
5. **Suggested project tag**: We will assign the cpg number but are happy to take suggestions for the tag portion. The tag is typically 1-2 words summarizing the project (e.g., `jump`, `cmqtl`, `lipocyteprofiler`) and sometimes includes the first author's last name (e.g., `caie-drugresponse`, `kelley-resistance`, `caicedo-cmvip`)

For existing datasets, please include the following details in your email:

1. **Top-level project tag** that your data corresponds to (e.g., `cpg0016-jump`)
2. **Approximate data size**: Total size estimate
3. **Components you wish to contribute**

After initial contact, maintainers will:

1. Review your contribution proposal and confirm you can format your metadata to our requirements (particularly for `load_data_csv` and `metadata` folders - see [data structure](data_structure.md))
2. Assign you a project identifier (for new datasets)
3. Provide staging bucket upload credentials
4. Create a [Github Discussion](https://github.com/broadinstitute/cellpainting-gallery/discussions) using our [discussion template](https://github.com/broadinstitute/cellpainting-gallery/discussions/66) to track your data deposition

Maintainers may use automated workflows or manual processes for this onboarding step.

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

Any data contributions to Cell Painting Gallery must be accompanied by a pull request to the [Cell Painting Gallery repository](https://github.com/broadinstitute/cellpainting-gallery/) with updates to the README to add your dataset to [Available datasets](https://github.com/broadinstitute/cellpainting-gallery/blob/main/README.md).
If your dataset is associated with a publication, please also edit [Publications](https://github.com/broadinstitute/cellpainting-gallery/blob/main/documentation/publications.md).
