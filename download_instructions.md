# Downloading from Cell Painting Gallery

Before downloading from the Cell Painting Gallery, please read our comprehensive description of [folder structure](folder_structure.md) so that you understand the structure of the data you will be downloading.

We provide below instructions for downloading data using AWS CLI with some additional information on listing files with boto3.
You are welcome to use other tools but we cannot provide help/support for using them.

## Setup

Install AWS CLI and optionally boto3.

### AWS CLI

The Amazon Web Services Command Line Interface (AWS CLI) is a unified tool to manage AWS services from the command line.
AWS provides more information on AWS CLI [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html).
Before using AWS CLI you will need to [install it](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html), following AWS instructions.

### boto3

Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python.
AWS provides more information on boto3 [here](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html).
Before using boto3, you will need to [install it](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html), following AWS instructions.

### Preparation

Before initiating a download, consider what kind and how much data you need.
Most datasets have both images and profiles.
Most datasets have multiple batches.
Not all datasets and not all batches have been described in a publication.
Browse the data to determine the batch/plate/file names that you would like to download.

The easiest way to browse the data is [to do use a storage browser](https://stackoverflow.com/a/72143198/1094109).
You can also list the data.

## Listing the CellPainting Gallery

### Listing with AWS CLI

```bash
DATASET=cpg0000-jump-pilot
aws s3 ls s3://cellpainting-gallery/${DATASET}/ --no-sign-request
```

Though AWS S3 is object storage, listing will return the available prefixes up to the next '/', similar to returning a folder list.
You may want to perform subsequent listing, appending prefixes always with a '/' at the end of the S3 path, until you have browsed to your desired depth.
If nothing is returned after your list command then you have entered a prefix that does not exist - check for typos.

e.g.

```bash
DATASET=cpg0000-jump-pilot
aws s3 ls s3://cellpainting-gallery/${DATASET}/source_4/workspace/load_data_csv/ --no-sign-request
```

### Listing with boto3

```python
### Listing by "folder" ###

import boto3

# This allows access without needing AWS credentials
from botocore import UNSIGNED
from botocore.config import Config
s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))

prefix='cpg0000-jump-pilot' #e.g. 'cpg0000-jump-pilot/source_4/workspace/load_data_csv'

pages = paginator.paginate(
    Bucket='cellpainting-gallery',
    Delimiter='/',
    Prefix=f"{prefix}/")
fullprefix_list = []
for page in pages:
    for k in page['CommonPrefixes']:
        fullprefix_list.append(k['Prefix'][:-1])
folder_list = [x.replace(f'{path}/','') for x in fullprefix_list]

print (fullprefix_list)
print (folder_list)
```

Though AWS S3 is object storage, listing with `Delimiter='/'` will return the available prefixes up to the next '/', similar to returning a folder list.
Without the delimiter a list of every single object with that prefix is returned (see below for example).
You may want to perform subsequent listing, editing your prefix with increasingly nested "folders".
The `fullprefix_list` returns a list of complete prefixes within the `prefix` you passed (e.g. `['cpg0000-jump-pilot/source_4/workspace/load_data_csv/2020_11_04_CPJUMP1', 'cpg0000-jump-pilot/source_4/workspace/load_data_csv/2020_11_18_CPJUMP1_TimepointDay1', 'cpg0000-jump-pilot/source_4/workspace/load_data_csv/2020_11_19_TimepointDay4']`) while the `folder_list` returns just the "subfolders" in a list (e.g. `['2020_11_04_CPJUMP1', '2020_11_18_CPJUMP1_TimepointDay1', '2020_11_19_TimepointDay4']`)

```python
### Listing all files ###

import boto3

# This allows access without needing AWS credentials
from botocore import UNSIGNED
from botocore.config import Config
s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
paginator = s3.get_paginator('list_objects_v2')

prefix='cpg0000-jump-pilot' #e.g. 'cpg0000-jump-pilot/source_4/workspace/load_data_csv/2020_11_04_CPJUMP1/BR00116991'

# Uses a paginator to allow listing of more than 1,000 objects
pages = paginator.paginate(Bucket='cellpainting-gallery', Prefix=path)
fullfile_list = []
for page in pages:
    for k in page['Contents']:
        fullfile_list.append(k['Key'])
file_list = [x.replace(f'{path}/','') for x in fullfile_list]

print (file_list)
```

This will list all files with a prefix no matter the subsequent "nesting".
The `fullfile_list` returns a list of complete files (i.e. all objects) within the `prefix` you passed (e.g. `['cpg0000-jump-pilot/source_4/workspace/load_data_csv/2020_11_04_CPJUMP1/BR00116991/load_data.csv', 'cpg0000-jump-pilot/source_4/workspace/load_data_csv/2020_11_04_CPJUMP1/BR00116991/load_data_with_illum.csv']`) while the `file_list` returns just the file names in a list (e.g. `['load_data.csv', 'load_data_with_illum.csv']`)

## Downloading data with AWS CLI

### Downloading a whole dataset

Perhaps the simplest download command is to download a whole dataset.
However, before doing so, we encourage you to look carefully at the [README](README.md) so that you are aware of the size of the dataset that you are downloading.

In your terminal, navigate into the folder that you would like to download into.
Run the following command to see a listing of all files that would be downloaded with your command.
If your source and destination paths are as expected, remove `--dryrun` from the command and run it again.

```bash
DATASET=cpg0000-jump-pilot
aws s3 cp --recursive s3://cellpainting-gallery/${DATASET}/ . --no-sign-request --dryrun
```

### Downloading data subsets

In your terminal, navigate into the folder that you would like to download into.
Use the the provided [folder structure](folder_structure.md) documentation and browse the data with a storage browser or [by listing](#listing-the-cellpainting-gallery) to determine the path (i.e. prefix) you would like to download.

Below we provide several examples of download commands.

We suggest you always first run download commands with the `--dryrun` command to see a listing of all files that would be downloaded with your command.
If your source and destination paths are as expected, remove `--dryrun` from the command and run it again.

If you would like to download a subset of data with a common prefix (i.e. folder nesting) then use the `--include` and `--exclude` flags in your command.
We suggest the format of `--exclude "*" --include "*yourfilter*"` to exclude all files from the download command and then include only the files that have your specified filter.

The copy command examples provided follow the format of `aws s3 cp --recursive` SOURCE DESTINATION `--no-sign-request --dryrun`.
When files download, they will maintain any folder structure below the prefix that you are downloading from.
You can create/define additional folders by editing the DESTINATION.

e.g. download a single plate of images

```bash
aws s3 cp --recursive s3://cellpainting-gallery/cpg0000-jump-pilot/source_4/images/2020_11_04_CPJUMP1/images/BR00116991__2020-11-05T19_51_35-Measurement1/ . --no-sign-request --dryrun
```

e.g. download all platemaps to a platemap folder

```bash
aws s3 cp --recursive s3://cellpainting-gallery/cpg0000-jump-pilot/source_4/workspace/metadata/platemaps/ platemap/ --no-sign-request --dryrun
```

e.g. download all backends that are in .csv format to a backend folder

```bash
aws s3 cp --recursive s3://cellpainting-gallery/cpg0000-jump-pilot/source_4/workspace/backend/ backend/ --exclude "*" --include "*.csv" --no-sign-request --dryrun
```
