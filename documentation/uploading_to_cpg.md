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

## 7. Initiate transfer from staging to Gallery

Run your transfer commands to `staging-cellpainting-gallery`.

## 8. Verify transfer

Once the transfers are complete, verify the data transferred to `staging-cellpainting-gallery` completely by comparing file count betwen the source and the CPG path.
Get file count on S3 with:
`aws s3 ls --summarize --human-readable --recursive s3://staging-cellpainting-gallery/${PROJECT_NAME}/${SOURCE}$/path/to/data/`

After complete transfer, you (Imaging Platform internal) or your data champion (if external) need to verify that all the data is in a structure compliant with our [data structure requirements](data_structure.md).
(Currently this is done manually, though this will be programatic in the future.)
Once verification is complete, let a Gallery maintainer (Erin, Shantanu) know that they should initiate transfer from staging to Gallery.
