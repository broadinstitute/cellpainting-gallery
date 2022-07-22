---
name: Data Immediately Public
about: For datasets that can be made public immediately
title: YYYY_MM_DD_Dataset_Name
labels: ''
assignees: ''

---

Segmentation/ Feature extraction is being performed by (Cimini lab / Carpenter-Singh lab)  
Profile creation is being performed by (Cimini lab / Carpenter-Singh lab)  
Data can be public in RODA Immediately

Update as generated:  
[Link to profile repo]  
[Link to publication repo]  
[cellpainting-gallery identifier]  

- [ ] Metadata completely filled out in Project Profiler Database (Imaging Platform internal use only)
- [ ] Segmentation/Feature extraction complete
- [ ] Profiling complete

Transfer to CellPainting Gallery:
- [ ] Upload data to RODA (is private by default)
- [ ] Run validation script to ensure completion
- [ ] Update cellpainting-gallery/README.md
- [ ] Make RODA entry public

If data is being published, prepare for publication:
- [ ] Run Distributed-BioFormats2Raw to create .ome.zarr files
- [ ] Upload (meta)data to IDR (images remain hosted in cellpainting-gallery).

Once published:
- [ ] Make IDR entry public
- [ ] Update cellpainting-gallery/README.md and open-data-registry/cellpainting-gallery.yml to reflect publication
- [ ] Move this Issue from cellpainting-gallery-private to cellpainting-gallery. This step can be performed at an earlier point if it needs inputs from an external collaborator.
