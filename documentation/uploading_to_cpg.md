# Tutorial: Uploading to the Cell Painting Gallery

To preserve data integrity, any data going into the Cell Painting Gallery is first uploaded to a private staging bucket, `staging-cellpainting-gallery`.
A gallery maintainer must approve the staged data and can then initiate transfer to the public `cellpainting-gallery`.

```{warning}
These instructions are currently applicable for upload from a non-S3 source (such as an institutional server).
Transfer from S3 to S3 requires slightly more complicated credential setup so please let Erin/Shantanu know if your data is on S3 and they will provide additional instructions.
```

## 1. Prepare data

Ensure that you have read [Contributing to the CPG](https://broadinstitute.github.io/cellpainting-gallery/contributing_to_cpg.html) and have performed the appropriate "Preparation for Data Deposition."

## 2. Install AWS CLI

Follow AWS documentation to [install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

## 3. Request upload credentials

Upload credentials enable anyone with the credentials to upload to `staging-cellpainting-gallery`.
Email Erin/Shantanu to ask for credentials, letting them know the prefix you want to upload to.
(Maintainers: see [cellpainting-gallery-infra](https://github.com/broadinstitute/cellpainting-gallery-infra?tab=readme-ov-file#setting-up-access-for-a-new-prefix) (private) for onboarding setup.)

## 4. Get temporary AWS credentials

Your maintainer will provide you with AWS credentials (access key and secret key) for the Cell Painting Gallery AWS account.
These credentials are **shared** among all contributors to your project prefix.
(If you have AWS credentials from your own AWS account, note that these are different. Use these, **not** your own credentials for the following steps.)

The credentials that you are sent by Erin/Shantanu allow you access to S3 Access Grants. S3 Access Grants provides temporary, prefix-scoped credentials that allow actual upload to the CPG. Each assigned prefix has shared credentials — either READWRITE for uploading data, or READ for verification and read-only access. Your prefix is usually a top-level project prefix that includes your source (e.g., `cpg0037-oasis/broad`) but in some cases may be a nested sub-path (e.g., `cpg0016-jump/source_2/workspace/segmentation`). Your maintainer will tell you which prefix you have access to.

Enter the following into your terminal, replacing `YOUR_ACCESS_KEY` and `YOUR_SECRET_KEY` with the credentials sent to you and `YOUR_PREFIX` with the prefix your credentials are scoped to.

```bash
export AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY
export AWS_SECRET_ACCESS_KEY=YOUR_SECRET_KEY

aws s3control get-data-access \
  --account-id 309624411020 \
  --target "s3://staging-cellpainting-gallery/YOUR_PREFIX/*" \
  --permission READWRITE \
  --duration-seconds 43200 \
  --region us-east-1
```

This returns temporary credentials valid for 12 hours. Copy the values from the output and export them.
These replace the credentials from step A1—make sure to export all three values, including `AWS_SESSION_TOKEN`:

```bash
export AWS_ACCESS_KEY_ID=<AccessKeyId from output>
export AWS_SECRET_ACCESS_KEY=<SecretAccessKey from output>
export AWS_SESSION_TOKEN=<SessionToken from output>
```

## 5. Upload your data

With the exported credentials active, upload using standard AWS CLI commands:

```bash
aws s3 sync /path/to/local/data s3://staging-cellpainting-gallery/YOUR_PREFIX/your/data/path/ --region us-east-1
```

You can upload to any sub-path within your assigned prefix. For example, if your prefix is `cpg0037-oasis`, you can upload to:
- `s3://staging-cellpainting-gallery/cpg0037-oasis/broad/images/...`
- `s3://staging-cellpainting-gallery/cpg0037-oasis/source_2/workspace/...`

If your credentials expire during a long upload, re-run step A2 to get fresh credentials and then re-run the same `aws s3 sync` command—it will skip files already uploaded.

### Troubleshooting

`Error: "not authorized to perform s3:GetDataAccess on resource ...us-west-2..."`

The Access Grants instance is in `us-east-1` only. Make sure your command includes `--region us-east-1`.

`Error: "No matching grant found" or "Access Denied" on a valid prefix`

Verify your `--target` path matches your assigned prefix exactly.
The credentials are scoped to this prefix and all sub-paths within it.

## 6. Verify transfer

Once the transfers are complete, verify the data transferred to `staging-cellpainting-gallery` completely by comparing file count betwen the source and the CPG path.

Get file count on S3 with:
`aws s3 ls --summarize --human-readable --recursive s3://staging-cellpainting-gallery/${PROJECT_NAME}/${SOURCE}$/path/to/data/ --profile cpg-staging`

After complete transfer, you (Imaging Platform internal) or your data champion (if external) need to verify that all the data is in a structure compliant with our [data structure requirements](data_structure.md).
(Currently this is done manually, though this will be programatic in the future.)

To verify if the transfer was successful, compare object counts between your source and destination.
Because of differences in the way file sizes are calculated between file systems and object storage, file size is not a reliable metric for comparison.
- Number of files on origin (for a file system): `find PATH/TO/YOUR/FILES  -type f | wc -l`
with
- Number of objects on the Staging bucket: `aws s3 ls s3://staging-cellpainting-gallery/${PROJECT_NAME}/${SOURCE}$/path/to/data/ --recursive --profile cpg-staging | wc -l`

Once verification is complete, let a Gallery maintainer (Erin, Shantanu) know that they should initiate transfer from staging to Gallery.
