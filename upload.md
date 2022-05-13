# Uploading your data

Note: At present, only a few individuals – those with access to instructions [here](https://github.com/jump-cellpainting/aws#creating-an-aws-role-to-access-s3-buckets) – have the ability to upload data to `s3://cellpainting-gallery`.

You need to do 5 things:

0. Set up AWS
1. Follow naming conventions
2. Upload your images
3. Upload the outputs of CellProfiler
4. Upload the outputs of the profiling recipe

## 0. Set up AWS

### Install AWS CLI

[FIXME] Write this up

### Set up AWS credentials

Follow the instructions [here](https://github.com/jump-cellpainting/aws#creating-an-aws-role-to-access-s3-buckets).

## 1. Follow naming conventions

### Remove special characters in folder names

To the maximum extent possible, please avoid the following in your folder names

- Whitespaces
- Special characters other than `_` and `-`

Please delete these characters if they are present in your folder names.

### Prepare project-specific naming

Reference [folder_structure.md](folder_structure.md) for comprehensive information on folder structure and naming.
You will need to know the project directory and project-specific nesting that you will be uploading into.

## 2. Uploading your images

### Test upload of a single plate

Before running the entire upload, test that you have your upload set up correctly with a dry run of a single plate.

For our example test plate:
- The images live in the folder `BR00117035__2021-05-02T16_02_51-Measurement1`.
- The plate was acquired in the batch `2021_04_26_Batch1`
- We are uploading into the project directory `jump`
- Our project-specific nesting is `source_4`.

We first do a [dry run](https://en.wikipedia.org/wiki/Dry_run_(testing)).

Here's how you upload the plate of data using AWS CLI.

If the images live on your local disk, your TOP_LEVEL_FOLDER will be a relative or absolute path on your file system.
If the images are already in your own bucket in S3, your TOP_LEVEL_FOLDER will instead be an S3 URI such as s3://your-bucket/projects/2021_04_26_Production/2021_04_26_Batch1/images

```sh
# TOP_LEVEL_FOLDER is the folder containing BR00117035__2021-05-02T16_02_51-Measurement1
TOP_LEVEL_FOLDER=/imaging/analysis/projects/2021_04_26_Production/2021_04_26_Batch1/images
PLATE=BR00117035__2021-05-02T16_02_51-Measurement1 # must not contain a whitespace; please rename if it does
PROJECT_DIRECTORY=jump
PROJECT_NESTING=source_4
BATCH=2021_04_26_Batch1
aws s3 sync \
  --dryrun \
  --profile jump-cp-role \
  --acl bucket-owner-full-control \
  --metadata-directive REPLACE \
  "${TOP_LEVEL_FOLDER}"/${PLATE} \
  s3://cellpainting-gallery/${PROJECT_DIRECTORY}/${PROJECT_NESTING}/images/${BATCH}/images/${PLATE}
```

This will output a long list of commands, one for each file being transferred.

You can Ctrl-C after a few seconds, and then eyeball the commands to make sure that the paths look as expected.
e.g. here, we should expected something like this, one per file

```
(dryrun) upload: BR00117035__2021-05-02T16_02_51-Measurement1/Images/r01c01f01p01-ch1sk1fk1fl1.tiff to s3://cellpainting-gallery/jump/source_4/images/2021_04_26_Batch1/images/Images/r01c01f01p01-ch1sk1fk1fl1.tiff
```

### Upload images

Once you've inspected it, do the actual run (i.e. not a dry run) by running the command above but without the `--dryrun` flag.
If you have multiple plates you will need to repeat the command for each plate or see [Uploading multiple plates at one go](upload.md#uploading-multiple-plates-at-once) for information on batch uploading.

## 3. Upload the outputs of CellProfiler

This section is nearly identical to [Uploading your images](upload.md#2-uploading-your-images).
As you did in the previous section:
- Start a dryrun
- Check the dryrun output
- Do the actual run

### Upload analysis files

These are the files output by the analysis pipeline.
If the images live on your local disk, your TOP_LEVEL_FOLDER will be a relative or absolute path on your file system.
If the images are already in your own bucket in S3, your TOP_LEVEL_FOLDER will instead be an S3 URI such as s3://your-bucket/projects/2021_04_26_Production/workspace/analysis/2021_04_26_Batch1

As before, we want to upload files for a single plate of data.
For our example plate most variables are the same with the change that
- The files live in the plate folder `BR00117035`

```sh
# TOP_LEVEL_FOLDER is the folder containing BR00117035 measurement outputs
TOP_LEVEL_FOLDER=/imaging/analysis/projects/2021_04_26_Production/workspace/analysis/2021_04_26_Batch1
PLATE=BR00117035 # must not contain a whitespace; please rename if it does
PROJECT_DIRECTORY=jump
PROJECT_NESTING=source_4
BATCH=2021_04_26_Batch1
aws s3 sync \
  --dryrun \
  --profile jump-cp-role \
  --acl bucket-owner-full-control \
  --metadata-directive REPLACE \
  "${TOP_LEVEL_FOLDER}"/${PLATE} \
  s3://cellpainting-gallery/${PROJECT_DIRECTORY}/${PROJECT_NESTING}/workspace/analysis/${BATCH}/${PLATE}
```

### Upload illumination functions

These are the files output by the illumination correction pipeline.
If the images live on your local disk, your TOP_LEVEL_FOLDER will be a relative or absolute path on your file system.
If the images are already in your own bucket in S3, your TOP_LEVEL_FOLDER will instead be an S3 URI such as s3://your-bucket/projects/2021_04_26_Production/2021_04_26_Batch1/images/2021_04_26_Batch1/illum

```sh
# TOP_LEVEL_FOLDER is the folder containing BR00117035 illumination functions
TOP_LEVEL_FOLDER=/imaging/analysis/projects/2021_04_26_Production/2021_04_26_Batch1/illum/
PLATE=BR00117035 # must not contain a whitespace; please rename if it does
PROJECT_DIRECTORY=jump
PROJECT_NESTING=source_4
BATCH=2021_04_26_Batch1
aws s3 sync \
  --dryrun \
  --profile jump-cp-role \
  --acl bucket-owner-full-control \
  --metadata-directive REPLACE \
  "${TOP_LEVEL_FOLDER}"/${PLATE} \
  s3://cellpainting-gallery/${PROJECT_DIRECTORY}/${PROJECT_NESTING}/images/${BATCH}/illum/${PLATE}
```

## 4. Upload the outputs of the profiling recipe

This section is nearly identical to [Uploading your images](upload.md#2-uploading-your-images).
As you did in the previous section:
- Start a dryrun
- Check the dryrun output
- Do the actual run

### Upload profiles, backend, and load_data_csv folders

The commands for uploading the `profiles`, `backend`, and `load_data_csv` folders are the same as the command for uploading the `analysis` folder, as described in the [previous section](upload.md#upload-analysis-files), with the following replacements:

The destination S3 path `s3://cellpainting-gallery/${PROJECT_DIRECTORY}/${PROJECT_NESTING}/workspace/analysis/${BATCH}/${PLATE}` becomes

- `s3://cellpainting-gallery/${PROJECT_DIRECTORY}/${PROJECT_NESTING}/workspace/profiles/${BATCH}/${PLATE}` for profiles (only well-level files)
- `s3://cellpainting-gallery/${PROJECT_DIRECTORY}/${PROJECT_NESTING}/workspace/backend/${BATCH}/${PLATE}` for backend (single-cell-level + well-level files + other output)
- `s3://cellpainting-gallery/${PROJECT_DIRECTORY}/${PROJECT_NESTING}/workspace/load_data_csv/${BATCH}/${PLATE}` for load_data_csv (LoadData CSV files)

Make sure that you also change your source path for each command.

### Upload metadata folder

The `metadata` folder has a different nesting structure (there is no plate-level structure).

```sh
# TOP_LEVEL_FOLDER is the folder containing metadata
TOP_LEVEL_FOLDER=/imaging/analysis/projects/2021_04_26_Production/workspace/
PROJECT_DIRECTORY=jump
PROJECT_NESTING=source_4
aws s3 sync \
  --dryrun \
  --profile jump-cp-role \
  --acl bucket-owner-full-control \
  --metadata-directive REPLACE \
  "${TOP_LEVEL_FOLDER}"/metadata \
  s3://cellpainting-gallery/${PROJECT_DIRECTORY}/${PROJECT_NESTING}/workspace/metadata
```

### Upload quality_control folder

The `quality_control` folder also has a different nesting structure (there is plate-level structure in some subfolders but not others).

```sh
# TOP_LEVEL_FOLDER is the folder containing quality_control
TOP_LEVEL_FOLDER=/imaging/analysis/projects/2021_04_26_Production/workspace/
PROJECT_DIRECTORY=jump
PROJECT_NESTING=source_4
aws s3 sync \
  --dryrun \
  --profile jump-cp-role \
  --acl bucket-owner-full-control \
  --metadata-directive REPLACE \
  "${TOP_LEVEL_FOLDER}"/quality_control \
  s3://cellpainting-gallery/${PROJECT_DIRECTORY}/${PROJECT_NESTING}/workspace/quality_control
```

### Upload other folders

If you have other folders that need to be uploaded (e.g. `assay_dev`, `pipelines`, `segmentation`), use similar commands, paying attention to whether the folder has plate-level structure or not.

# Checking your upload

## Check upload paths

To check that your images were uploaded to the correct paths, output the file list in the cellpainting-gallery bucket.

```sh
PLATE=BR00117035__2021-05-02T16_02_51-Measurement1
PROJECT_DIRECTORY=jump
PROJECT_NESTING=source_4
BATCH=2021_04_26_Batch1
aws s3 ls \
  --profile jump-cp-role \
  --recursive \
  s3://cellpainting-gallery/${PROJECT_DIRECTORY}/${PROJECT_NESTING}/images/${BATCH}/images/
```

You can Ctrl-C after a few seconds, and then eyeball the list to make sure that the paths look as expected.
e.g. here, we should expected something like this

```
2021-10-05 13:13:45    2555730 jump/source_4/images/2021_04_26_Batch1/images/BR00117035__2021-05-02T16_02_51-Measurement1/Images/r01c01f01p01-ch1sk1fk1fl1.tiff
...
```

You can check the other outputs (CellProfiler output and profiling recipe output) similarly:


```sh
PROJECT_DIRECTORY=jump
PROJECT_NESTING=source_4
BATCH=2021_04_26_Batch1

aws s3 ls \
  --profile jump-cp-role \
  --recursive \
  s3://cellpainting-gallery/${PROJECT_DIRECTORY}/${PROJECT_NESTING}/images/${BATCH}/illum/

aws s3 ls \
  --profile jump-cp-role \
  --recursive \
  s3://cellpainting-gallery/${PROJECT_DIRECTORY}/${PROJECT_NESTING}/workspace/profiles/${BATCH}/

aws s3 ls \
  --profile jump-cp-role \
  --recursive \
  s3://cellpainting-gallery/${PROJECT_DIRECTORY}/${PROJECT_NESTING}/workspace/backend/${BATCH}/

aws s3 ls \
  --profile jump-cp-role \
  --recursive \
  s3://cellpainting-gallery/${PROJECT_DIRECTORY}/${PROJECT_NESTING}/workspace/load_data_csv/${BATCH}/

aws s3 ls \
  --profile jump-cp-role \
  --recursive \
  s3://cellpainting-gallery/${PROJECT_DIRECTORY}/${PROJECT_NESTING}/workspace/metadata/

aws s3 ls \
  --profile jump-cp-role \
  --recursive \
  s3://cellpainting-gallery/${PROJECT_DIRECTORY}/${PROJECT_NESTING}/workspace/quality_control/

```

## Check upload completion

If your paths look correct but you have any reason to suspect that your uploads are incomplete, you can confirm complete upload in multiple ways.

The simplest way to confirm complete transfer is to run the `aws s3 sync` command again.
Your terminal will pause while it checks that each file has transferred and then will either initiate transfer of any missing files or return nothing if the transfer was indeed complete.

# Uploading multiple plates at once.

There are many ways of doing this.

One approach uses [GNU parallel](https://www.gnu.org/software/parallel/):
This uploads several plates from a batch and keeps a log of things.

```sh
TOP_LEVEL_FOLDER=s3://imaging-platform/projects/2021_04_26_Production/2021_04_26_Batch1/images
LIST_OF_PLATES_FROM_SAME_BATCH=plate_list.txt # each line in this text file contains a plate name (they must not contain a space; please rename if they do)
PROJECT_DIRECTORY=jump
PROJECT_NESTING=source_4
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
  --metadata-directive REPLACE \
  "${TOP_LEVEL_FOLDER}"/{1} \
  s3://cellpainting-gallery/${PROJECT_DIRECTORY}/${PROJECT_NESTING}/images/${BATCH}/images/{1}
```

Because the longer your upload takes the more likely there is to be an interruption, a second approach to multi-plate upload is to use a terminal multiplexer that will complete the upload through interruptions.
We often use [tmux](https://github.com/tmux/tmux/wiki).
To use this approach, run the original upload commands without ${PLATE} at the end of either the source or destination paths to upload all plate folders within the BATCH folder.
