<!-- Dataset onboarding discussion template
     This is the authoritative template for dataset contribution discussions.
     Previously maintained at: https://github.com/broadinstitute/cellpainting-gallery/discussions/66

     Enhanced with structured Dataset Information section for maintainer workflow.
-->

## Dataset Information

- **Identifier**: cpg####-tag
- **Contributor**: [name/contact]
- **Assay Type**: [Standard Cell Painting / variation description]
- **Approximate Size**: [size estimate]
- **Components**: [images, analysis, backend, profiles, metadata, etc.]
- **Type**: [New dataset / Addition to cpg####]

Profile/data repo = [Link to profile/data repo or TBD]
Publication/analysis repo = [Link to publication/analysis repo or TBD]
Imaging Platform project tag = [YYYY_MM_DD_ProjectName] DELETE IF EXTERNAL CONTRIBUTOR
Institution identifier = [institution identifier]
Imaging Platform internal "champion" = [Maintainer name or specify if external]

**Workflow**

- [ ] Maintainer adds dataset identifier to [prefixes](https://github.com/broadinstitute/cellpainting-gallery/blob/main/documentation/prefixes.md) document.
- [ ] Champion or Contributor fills out the metadata collection form (<https://airtable.com/shrVxz9DcoMlDoCBI>)
- [ ] Champion checks that metadata completely filled out in Project Profiler Database (Imaging Platform internal use only)
- [ ] Champion asks Erin/Shantanu to  1) open the prefix for transfer to `staging-cellpainting-gallery` and 2) create credentials that allow upload. Each credential is for a single prefix on the staging bucket; multiple people can assume that same credential.

**Transfer data to `staging-cellpainting-gallery`**
Instructions for using the staging bucket credentials are [here](https://broadinstitute.github.io/cellpainting-gallery/uploading_to_cpg.html).
For each data subtype, Champion marks off as complete or explain why it is not being included:

- [ ] Image acquisition complete and uploaded (`/images`)
- [ ] Feature extraction complete and uploaded (`/workspace/analysis`)
- [ ] Backend complete and uploaded (`/workspace/backend`)
- [ ] Load_data complete and uploaded (`/workspace/load_data_csv`)
- [ ] Profiling complete and uploaded (`/workspace/profiles`)
- [ ] Metadata complete and uploaded (`/workspace/metadata`)

**Project completion**
These are the final steps to make a dataset fully public:

- [ ] Maintainer or champion Run [validation script](http://github.com/broadinstitute/cpg/cpgdata) to ensure data is completely uploaded (When script is out of alpha)
- [ ] Maintainer or champion updates cellpainting-gallery/README.md to add dataset to README.
- [ ] Maintainer transfers from `staging-cellpainting-gallery` to `cellpainting-gallery`.
- [ ] Erin/Shantanu disable staging prefix, delete data from staging, delete upload credentials.

Optional preparation for publication:

- [ ] Run Distributed-BioFormats2Raw to create .ome.zarr files
- [ ] Upload (meta)data to IDR (images remain hosted in cellpainting-gallery)
- [ ] Make IDR entry public

Once a paper is published:

- [ ] Maintainer or champion updates [Publications](https://github.com/broadinstitute/cellpainting-gallery/docs/publications.md) (In PR by data generator)
- [ ] Contributor adds the paper to <https://github.com/cytodata/awesome-cytodata>
