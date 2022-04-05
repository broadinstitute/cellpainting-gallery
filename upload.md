# Uploading your data

You need to do 4 things

0. Follow naming conventions
1. Upload your images
2. Upload the output of CellProfiler
3. Upload the output of the profiling recipe

Once again, let's use Broad's data as an example to understand the folder structure we will use for JUMP.

## Follow naming conventions

### Remove special characters in folder names

To the maximum extent possible, please avoid the following in your folder names

- Whitespaces
- Special characters other than `_` and `-`

Please delete these characters if they are present in your folder names.

## Uploading your images

We want to upload the images from a single plate of data.

- The images live in the folder `BR00117035__2021-05-02T16_02_51-Measurement1`.
- The plate was acquired in the batch `2021_04_26_Batch1`
- Broad's prefix is `source_4`.

We first do a [dry run](https://en.wikipedia.org/wiki/Dry_run_(testing)).

Here's how you upload the plate of data using AWS CLI.

If the images live on disk, do this:

```sh
# TOP_LEVEL_FOLDER is the folder containing BR00117035__2021-05-02T16_02_51-Measurement1
TOP_LEVEL_FOLDER=/imaging/analysis/projects/2021_04_26_Production/2021_04_26_Batch1/images
PLATE=BR00117035__2021-05-02T16_02_51-Measurement1 # must not contain a whitespace; please rename if it does
PARTNER_PREFIX=source_4
BATCH=2021_04_26_Batch1
aws s3 sync \
  --dryrun \
  --profile jump-cp-role \
  --acl bucket-owner-full-control \
  "${TOP_LEVEL_FOLDER}"/${PLATE} \
  s3://cellpainting-gallery/jump/${PARTNER_PREFIX}/images/${BATCH}/images/${PLATE}
```

This will output a long list of commands, one for each file being transferred.

You can Ctrl-C after a few seconds, and then eyeball the commands to make sure that the paths look as expected.
E.g. here, we should expected something like this, one per file

```
(dryrun) upload: BR00117035__2021-05-02T16_02_51-Measurement1/Images/r01c01f01p01-ch1sk1fk1fl1.tiff to s3://cellpainting-gallery/jump/source_4/images/2021_04_26_Batch1/images/Images/r01c01f01p01-ch1sk1fk1fl1.tiff
```

[FIXME] If the images live on S3, first please ensure that you have indeed configured your AWS IAM role [here](https://github.com/jump-cellpainting/aws#steps-for-creating-a-aws-iam-role) using the configuration specified under "If your own data is stored on AWS", and then do this:

```sh
# TOP_LEVEL_FOLDER is the folder containing BR00117035__2021-05-02T16_02_51-Measurement1 images
# s3://imaging-platform/ is Broad's AWS bucket, but it will be different for each partner
TOP_LEVEL_FOLDER=s3://imaging-platform/projects/2021_04_26_Production/2021_04_26_Batch1/images
PLATE=BR00117035__2021-05-02T16_02_51-Measurement1 # must not contain a whitespace; please rename if it does
PARTNER_PREFIX=source_4
BATCH=2021_04_26_Batch1
aws s3 sync \
  --dryrun \
  --profile jump-cp-role \
  --acl bucket-owner-full-control \
  "${TOP_LEVEL_FOLDER}"/${PLATE} \
  s3://cellpainting-gallery/jump/${PARTNER_PREFIX}/images/${BATCH}/images/${PLATE}
```

Again, this will output a long list of commands, one for each file being transferred.
Ctrl-C after a few seconds and inspect commands to make sure the paths look right.

Once you've inspected it, do the actual run (i.e. not a dry-run) by running the above but without the `--dry-run` flag.

## Upload the output of CellProfiler

This section is nearly identical to "Uploading your images"

As before, we want to upload files for a single plate of data.

- The files live in the folder `BR00117035`.
- The plate was acquired in the batch `2021_04_26_Batch1`

If the files live on disk, do this for the measurements outputs (the contents of `workspace/analysis`):

```sh
# TOP_LEVEL_FOLDER is the folder containing BR00117035 measurement outputs
TOP_LEVEL_FOLDER=/imaging/analysis/projects/2021_04_26_Production/workspace/analysis/2021_04_26_Batch1
PLATE=BR00117035 # must not contain a whitespace; please rename if it does
PARTNER_PREFIX=source_4
BATCH=2021_04_26_Batch1
aws s3 sync \
  --dryrun \
  --profile jump-cp-role \
  --acl bucket-owner-full-control \
  "${TOP_LEVEL_FOLDER}"/${PLATE} \
  s3://cellpainting-gallery/jump/${PARTNER_PREFIX}/workspace/analysis/${BATCH}/${PLATE}
```

And then do this for the illumination functions (the contents of `images/${BATCH}/illum`):

```sh
# TOP_LEVEL_FOLDER is the folder containing BR00117035 illumination functions
TOP_LEVEL_FOLDER=/imaging/analysis/projects/2021_04_26_Production/2021_04_26_Batch1/illum/
PLATE=BR00117035 # must not contain a whitespace; please rename if it does
PARTNER_PREFIX=source_4
BATCH=2021_04_26_Batch1
aws s3 sync \
  --dryrun \
  --profile jump-cp-role \
  --acl bucket-owner-full-control \
  "${TOP_LEVEL_FOLDER}"/${PLATE} \
  s3://cellpainting-gallery/jump/${PARTNER_PREFIX}/images/${BATCH}/illum/${PLATE}
```

As you did in the previous section
- Check the output
- Change the command appropriately if the files live on S3
- do the actual run

## Upload the output of the profiling recipe

This section is nearly identical to "Upload the output of CellProfiler".

You only need to change path `s3://cellpainting-gallery/jump/${PARTNER_PREFIX}/workspace/analysis/${BATCH}/${PLATE}` to

- `s3://cellpainting-gallery/jump/${PARTNER_PREFIX}/workspace/profiles/${BATCH}/${PLATE}` for profiles (only well-level files)
- `s3://cellpainting-gallery/jump/${PARTNER_PREFIX}/workspace/backend/${BATCH}/${PLATE}` for backend (single-cell-level + well-level files + other output)
- `s3://cellpainting-gallery/jump/${PARTNER_PREFIX}/workspace/load_data_csv/${BATCH}/${PLATE}` for load_data_csv (LoadData CSV files)

The `metadata` folder has a different nesting structure (there is no plate-level structure)

```sh
# TOP_LEVEL_FOLDER is the folder containing metadata
TOP_LEVEL_FOLDER=/imaging/analysis/projects/2021_04_26_Production/workspace/
PARTNER_PREFIX=source_4
aws s3 sync \
  --dryrun \
  --profile jump-cp-role \
  --acl bucket-owner-full-control \
  "${TOP_LEVEL_FOLDER}"/metadata \
  s3://cellpainting-gallery/jump/${PARTNER_PREFIX}/workspace/metadata
```

The `quality_control` folder also has a different nesting structure (there is plate-level structure in some subfolders but not others)

```sh
# TOP_LEVEL_FOLDER is the folder containing quality_control
TOP_LEVEL_FOLDER=/imaging/analysis/projects/2021_04_26_Production/workspace/
PARTNER_PREFIX=source_4
aws s3 sync \
  --dryrun \
  --profile jump-cp-role \
  --acl bucket-owner-full-control \
  "${TOP_LEVEL_FOLDER}"/quality_control \
  s3://cellpainting-gallery/jump/${PARTNER_PREFIX}/workspace/quality_control
```

# Checking your upload

To check your images, do this:

```sh
PLATE=BR00117035__2021-05-02T16_02_51-Measurement1
PARTNER_PREFIX=source_4
BATCH=2021_04_26_Batch1
aws s3 ls \
  --profile jump-cp-role \
  --recursive \
  s3://cellpainting-gallery/jump/${PARTNER_PREFIX}/images/${BATCH}/images/
```

This will output the list of files.

You can Ctrl-C after a few seconds, and then eyeball the list to make sure that the paths look as expected.
E.g. here, we should expected something like this

```
2021-10-05 13:13:45    2555730 jump/source_4/images/2021_04_26_Batch1/images/BR00117035__2021-05-02T16_02_51-Measurement1/Images/r01c01f01p01-ch1sk1fk1fl1.tiff
...
```

You can check the other outputs (CellProfiler output and profiling recipe output) similarly:


```sh
PARTNER_PREFIX=source_4
BATCH=2021_04_26_Batch1

aws s3 ls \
  --profile jump-cp-role \
  --recursive \
  s3://cellpainting-gallery/jump/${PARTNER_PREFIX}/images/${BATCH}/illum/

aws s3 ls \
  --profile jump-cp-role \
  --recursive \
  s3://cellpainting-gallery/jump/${PARTNER_PREFIX}/workspace/profiles/${BATCH}/

aws s3 ls \
  --profile jump-cp-role \
  --recursive \
  s3://cellpainting-gallery/jump/${PARTNER_PREFIX}/workspace/backend/${BATCH}/

aws s3 ls \
  --profile jump-cp-role \
  --recursive \
  s3://cellpainting-gallery/jump/${PARTNER_PREFIX}/workspace/load_data_csv/${BATCH}/

aws s3 ls \
  --profile jump-cp-role \
  --recursive \
  s3://cellpainting-gallery/jump/${PARTNER_PREFIX}/workspace/metadata/

aws s3 ls \
  --profile jump-cp-role \
  --recursive \
  s3://cellpainting-gallery/jump/${PARTNER_PREFIX}/workspace/quality_control/

```

# Uploading multiple plates at one go
    
There are many ways of doing this; here is one approach that uses [GNU parallel](https://www.gnu.org/software/parallel/):

This uploads several plates from a batch and keeps a log of things.

```sh
TOP_LEVEL_FOLDER=s3://imaging-platform/projects/2021_04_26_Production/2021_04_26_Batch1/images
LIST_OF_PLATES_FROM_SAME_BATCH=plate_list.txt # each line in this text file contains a plate name (they must not contain a space; please rename if they do)
PARTNER_PREFIX=source_4
BATCH=2021_04_26_Batch1

mkdir -p log/${BATCH} # to log the output

parallel \
  -a ${LIST_OF_PLATES_FROM_SAME_BATCH} \
  --max-procs 4 \
  --eta \
  --joblog log/${BATCH}/upload.log \
  --results log/${BATCH}/upload \
  --files \
  --keep-order \
  aws s3 sync \
  --profile jump-cp-role \
  --acl bucket-owner-full-control \
  "${TOP_LEVEL_FOLDER}"/{1} \
  s3://cellpainting-gallery/jump/${PARTNER_PREFIX}/images/${BATCH}/images/{1}
```
