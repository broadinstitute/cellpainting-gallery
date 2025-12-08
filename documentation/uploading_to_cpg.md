# Tutorial: Uploading to the Cell Painting Gallery

To preserve data integrity, any data going into the Cell Painting Gallery is first uploaded to a staging bucket, `staging-cellpainting-gallery`.
A gallery maintainer can then approve the staged data and initiate transfer to `cellpainting-gallery`.

```{warning}
These instructions are currently applicable for upload from a non-S3 source (such as an institutional server).
Transfer from S3 to S3 requires slightly more complicated credential setup so please let Erin/Shantanu know if your data is on S3 and they will provide additional instructions.
```

## 1. Get upload credentials

Upload credentials enable anyone with the credentials to upload to `staging-cellpainting-gallery`.

**Imaging Platform internal**: Email Erin/Shantanu to ask for credentials, letting them know the prefix you want to upload to.

**External source**: Your dataset will have an Imaging Platform champion.
That champion will contact Erin/Shantanu to request credentials and share them with you.

## 2. Install AWS CLI

Follow AWS documentation to [install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

## 3. Add your upload credentials to your AWS CLI config

Open the AWS CLI config file:

`nano ~/.aws/config` on Mac/Linux  
`notepad C:\Users\Administrator\.aws\config` on Windows

Add the following text at the bottom of the file:

```bash
[cpg-staging]
aws_access_key_id = {ACCESS_KEY_ID}
aws_secret_access_key = {SECRET_ACCESS_KEY}
region = us-east-1
output = json
```

The `aws_access_key_id` and `aws_secret_access_key` will be sent to you by Erin/Shantanu when they generate credentials.

## 4. Prepare your AWS CLI data transfer commands

Ensure that you have read [Contributing to the Cell Painting Gallery](/documentation/contributing_to_cpg.md) and [Data Structure](/documentation/data_structure.md).

Prepare your AWS CLI data transfer commands for upload to `staging-cellpainting-gallery` exactly mimicking the structure of `cellpainting-gallery`.
Depending upon how you have locally structured your data, you may need to generate multiple separate commands for transfer to the gallery.
They should follow the format of `aws s3 cp --recursive SOURCE DESTINATION --profile cpg-staging`.
(For single files, remove the `--recursive` flag.)

`SOURCE` is where the files are on your storage and can be a local absolute or relative path or can be an S3 location of your S3 bucket.  
`DESTINATION` is the S3 path within the `staging-cellpainting-gallery` (that should match `cellpainting-gallery`).

e.g.  

```bash
aws s3 cp --recursive /Users/eweisbar/Batch8_images s3://staging-cellpainting-gallery/cpg0123-example/broad/images/2024_04_01_Batch8/images/cpg-staging 
aws s3 cp --recursive /Users/eweisbar/Batch8_profiles s3://staging-cellpainting-gallery/cpg0123-example/broad/workspace/profiles/2024_04_01_Batch8/cpg-staging
```

## Alternative: S3 Access Grants (Beta)

This section only applies if your maintainer specifically set you up with S3 Access Grants.
If unsure, use the standard instructions above.

Maintainers: see [cellpainting-gallery-infra](https://github.com/broadinstitute/cellpainting-gallery-infra) (private) for onboarding setup.

S3 Access Grants provides temporary, prefix-scoped credentials. Each project prefix (e.g., `cpg0037-oasis`) has shared credentials that all contributors to that project use. Instead of steps 3-4 above, follow these steps:

### A1. Add your credentials

Your maintainer will provide you with AWS credentials (access key and secret key) for the Cell Painting Gallery AWS account.
These credentials are **shared** among all contributors to your project prefix.
They are **not** credentials from your own AWS account—use the ones provided to you.

Add them to `~/.aws/credentials`:

```ini
[cpg-staging]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```

### A2. Get temporary S3 credentials

Replace `YOUR_PREFIX` with your project's top-level prefix (e.g., `cpg0037-oasis`).

```bash
aws s3control get-data-access \
  --account-id 309624411020 \
  --target "s3://staging-cellpainting-gallery/YOUR_PREFIX/*" \
  --permission READWRITE \
  --duration-seconds 43200 \
  --region us-east-1 \
  --profile cpg-staging
```

This returns temporary credentials valid for 12 hours. Export them:

```bash
export AWS_ACCESS_KEY_ID=<AccessKeyId from output>
export AWS_SECRET_ACCESS_KEY=<SecretAccessKey from output>
export AWS_SESSION_TOKEN=<SessionToken from output>
```

### A3. Upload your data

With the exported credentials active, upload using standard AWS CLI commands (no `--profile` needed):

```bash
aws s3 sync /path/to/local/data s3://staging-cellpainting-gallery/YOUR_PREFIX/your/data/path/
```

You can upload to any sub-path within your assigned prefix. For example, if your prefix is `cpg0037-oasis`, you can upload to:
- `s3://staging-cellpainting-gallery/cpg0037-oasis/broad/images/...`
- `s3://staging-cellpainting-gallery/cpg0037-oasis/source_2/workspace/...`

If your credentials expire during a long upload, re-run step A2 to get fresh credentials.

### Troubleshooting

**Error: "not authorized to perform s3:GetDataAccess on resource ...us-west-2..."**

The Access Grants instance is in `us-east-1` only. Make sure your command includes `--region us-east-1`.

**Error: "No matching grant found" or "Access Denied" on a valid prefix**

Verify your `--target` path uses your project's top-level prefix (e.g., `cpg0037-oasis`).
The credentials are scoped to this prefix and all sub-paths within it.

---

## 7. Initiate transfer from staging to Gallery

Run your transfer commands to `staging-cellpainting-gallery`.

## 8. Verify transfer

Once the transfers are complete, verify the data transferred to `staging-cellpainting-gallery` completely by comparing file count betwen the source and the CPG path.
Get file count on S3 with:
`aws s3 ls --summarize --human-readable --recursive s3://staging-cellpainting-gallery/${PROJECT_NAME}/${SOURCE}$/path/to/data/`

After complete transfer, you (Imaging Platform internal) or your data champion (if external) need to verify that all the data is in a structure compliant with our [data structure requirements](data_structure.md).
(Currently this is done manually, though this will be programatic in the future.)

To verify if the transfer was successful, compare object counts between your source and destination.
Because of differences in the way file sizes are calculated between file systems and object storage, file size is not a reliable metric for comparison.
- Number of files on origin (for a file system): `find PATH/TO/YOUR/FILES  -type f | wc -l`
with
- Number of objects on the Staging bucket: `aws s3 ls s3://staging-cellpainting-gallery/$PROJECT_PREFIX/$SOURCE/$YOUR_FILES --recursive | wc -l`

>[!NOTE]
>To run the `aws s3 ls` command on the staging bucket, you need to have your temporary credentials active (see "Activate credentials" above).

Once verification is complete, let a Gallery maintainer (Erin, Shantanu) know that they should initiate transfer from staging to Gallery.
