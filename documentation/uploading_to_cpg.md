# Tutorial: Uploading to the Cell Painting Gallery

To preserve data integrity, any data going into the Cell Painting Gallery is first uploaded to a staging bucket, `staging-cellpainting-gallery`.
A gallery maintainer can then approve the staged data and initiate transfer to `cellpainting-gallery`.

## 1. Get upload credentials

Upload credentials enable anyone with the credentials to upload to `staging-cellpainting-gallery`.
They are generated on a per-prefix basis so each credential set can only be used for upload to a single prefix.
Upload credentials are generated through [cytoskel](https://github.com/broadinstitute/cytoskel/tree/main).

**Imaging Platform internal**: Email Ank to ask for credentials, letting him know the prefix you want to upload to.

**External source**: Your dataset will have an Imaging Platform champion.
That champion will contact Ank to request credentials and share them with you.

## 2. Install AWS CLI

Follow AWS documentation to [install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

## 3. Install jq

Follow the jq documention to [install jq](https://jqlang.github.io/jq/download/).

>[!NOTE]
>If you need to upload files to the Gallery from an institutional server and don't have permissions to install sowftware there, run this step in your local computer and check the note in **step 6 and 7**.

## 4. Add your upload credentials to your AWS CLI config

Open the AWS CLI config file:

`nano ~/.aws/config` on Mac/Linux  
`notepad C:\Users\Administrator\.aws\config` on Windows

Add the following text at the bottom of the file:

```bash
[cpg_staging]
aws_access_key_id = {ACCESS_KEY_ID}
aws_secret_access_key = {SECRET_ACCESS_KEY}
region = us-east-1
output = json
```

>[!NOTE]
>If you need to upload files to the Gallery from an institutional server youe need to perform this step both on the server AND on your local computer.

## 5. Prepare your AWS CLI data transfer commands

Ensure that you have read [Contributing to the Cell Painting Gallery](/documentation/contributing_to_cpg.md) and [Data Structure](/documentation/data_structure.md).

Prepare your AWS CLI data transfer commands for upload to `staging-cellpainting-gallery` exactly mimicking the structure of `cellpainting-gallery`.
Depending upon how you have locally structured your data, you may need to generate multiple separate commands for transfer to the gallery.
They should follow the format of `aws s3 sync SOURCE DESTINATION --profile cpg_staging --acl bucket-owner-full-control`.
(For single files, use `aws s3 cp` instead of `aws s3 sync`.)

The `--profile` flag tells AWS CLI to use the credentials that are specific for uploading to `staging-cellpainting-gallery`.  
The `--acl` flag gives the Cell Painting Gallery full ownership of the uploaded files.  
`SOURCE` is where the files are on your storage and can be a local absolute or relative path or can be an S3 location of your S3 bucket.  
`DESTINATION` is the S3 path within the `staging-cellpainting-gallery` (that should match `cellpainting-gallery`).

e.g.  

```bash
aws s3 sync /Users/eweisbar/Batch8_images s3://staging-cellpainting-gallery/cpg0123-example/broad/images/2024_04_01_Batch8/images/ --profile cpg_staging --acl bucket-owner-full-control 
aws s3 sync /Users/eweisbar/Batch8_profiles s3://staging-cellpainting-gallery/cpg0123-example/broad/workspace/profiles/2024_04_01_Batch8/ --profile cpg_staging --acl bucket-owner-full-control
```

>[!NOTE]
>If you are working on an institutional server and can't run `aws s3 sync`, try using `aws s3 cp --recursive` instead

## 6. Create `create_credentials.sh`

Create `create_credentials.sh` file on your computer and [copy in the code from cytoskel](https://github.com/broadinstitute/cytoskel/blob/aws_docs/cytoskel/docs/access_cpg_staging.md#create-file-called-s3_credentialssh).

Edit the code copied from cytoskel so that the `*` in the `--target` line matches your prefix.
e.g.  `--target "s3://staging-cellpainting-gallery/*" \` becomes `--target "s3://staging-cellpainting-gallery/cpg0016-jump" \` for upload to `cpg0016-jump`.

>[!NOTE]
>If you are working on an institutional server, run this step in your local computer only.

## 7. Run your transfer commands

Activate your credentials with `source ./create_credentials.sh`.
(Note that if you have saved your `source create_credentials.sh` files into a different location than you are currently navigated into, you will need to instead run `source /path/to/create_credentials.sh` with your correct file location.)
This activates your credentials for 12 hours (the maximum duration).

>[!NOTE]
>If you need to upload files to the Gallery from an institutional server you might not be able to run `source /path/to/create_credentials.sh` in the server. 
>
>Instead, run the command locally in your computer (which should have both `aws cli` and `jq` installed) and copy the generated environmental variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and `AWS_SESSION_TOKEN`) over to your session in the server.
>You can check the value of these variables by using `echo`:
>- `echo $AWS_ACCESS_KEY_ID` <-- *variable_1*
>- `echo $AWS_SECRET_ACCESS_KEY` <-- *variable_2*
>- `echo $AWS_SESSION_TOKEN` <-- *variable_3*
>
>Then, in your session in the server, set those same environmental variables (replace each of the variables using the values copied from your local computer):
>```bash
>AWS_ACCESS_KEY_ID=variable_1
>AWS_SECRET_ACCESS_KEY=variable_2
>AWS_SESSION_TOKEN=variable_3
>```

Run your transfer commands to `staging-cellpainting-gallery`.

## 8. Initiate transfer from staging to Gallery

Once the transfers are complete, either you (Imaging Platform internal) or your data champion (if external) must verify the data transferred to `staging-cellpainting-gallery` is complete.
(Currently this is done manually, though this will be programatic in the future.)
Once verification is complete, let a Gallery maintainer (Erin, Shantanu, Ank) know that they should initiate transfer from staging to Gallery.
