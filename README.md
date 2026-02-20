# Cell Painting Gallery

This page provides a guide to the datasets that are available in the Cell Painting Gallery, hosted by the AWS Registry of Open Data (RODA): <https://registry.opendata.aws/cellpainting-gallery>

## Citation/license

All the data is released with CC0 1.0 Universal (CC0 1.0).
Still, professional ethics require that you cite the appropriate resources/publications, listed in the [complete datasets](https://broadinstitute.github.io/cellpainting-gallery/complete_datasets) page, when using individual datasets, along with our Nature Methods publication announcing the Cell Painting Gallery ([Weisbart et al., 2024](https://doi.org/10.1038/s41592-024-02399-z)).
For example,

> We used the dataset `cpg0000` ([Chandrasekaran et al., 2022](https://doi.org/10.1101/2022.01.05.475090)), available from the Cell Painting Gallery ([Weisbart et al., 2024](https://doi.org/10.1038/s41592-024-02399-z)) on the Registry of Open Data on AWS (<https://registry.opendata.aws/cellpainting-gallery/>).

Please also acknowledge the Registry of Open Data (RODA) on AWS for their support in hosting the data, e.g., "We thank the AWS Open Data Sponsorship Program for sponsoring data storage."

## Documentation

Please see [our documentation](https://broadinstitute.github.io/cellpainting-gallery/) for extensive supporting information.

It includes:

- [how to browse gallery data](https://broadinstitute.github.io/cellpainting-gallery/browsing_data)
- [how to download gallery data](https://broadinstitute.github.io/cellpainting-gallery/download_instructions.html) (with AWS CLI, Quilt, or dataset-specific tools)
- [how to contribute to the gallery](https://broadinstitute.github.io/cellpainting-gallery/contributing_to_cpg)

## Complete datasets

All datasets are generated using the canonical Cell Painting assay unless indicated otherwise. Several updates to that protocol exist ([Cell Painting wiki](https://github.com/carpenterlab/2022_Cimini_NatureProtocols/wiki)).

Most prefixes within the Cell Painting Gallery are for unique Cell Painting datasets that contain images, extracted features, and metadata.
However, some prefixes are re-analyses of other datasets and may not contain images.

The datasets are stored with the prefix indicated by the dataset name.
e.g. the first dataset is located at `s3://cellpainting-gallery/cpg0000-jump-pilot` and can be listed using AWS CLI `aws s3 ls --no-sign-request s3://cellpainting-gallery/cpg0000-jump-pilot/` (note the `/` at the end).
See [browsing data](https://broadinstitute.github.io/cellpainting-gallery/browsing_data) in our documentation for more information on viewing the gallery in a browser and examples of how to list files using AWS CLI or boto3.

The datasets' accession numbers are the first seven characters of the dataset name.
e.g. the accession number of the first dataset is `cpg0000`.

For datasets without formal publications, please cite the [Cell Painting Gallery paper](https://doi.org/10.1038/s41592-024-02399-z) and any reference listed below.

See the [complete datasets](https://broadinstitute.github.io/cellpainting-gallery/complete_datasets) page for the full list of datasets, including descriptions, references, sizes, and protocols.

