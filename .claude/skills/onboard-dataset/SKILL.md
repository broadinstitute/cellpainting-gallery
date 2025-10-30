---
name: onboard-dataset
description: Helps Cell Painting Gallery maintainers onboard new dataset contributions. Handles Phase 1 setup including assigning cpg identifiers, updating prefixes.md, and creating GitHub Discussion tracking issues. Use when a contributor contacts you about adding a new dataset or when you need to initiate the dataset contribution workflow.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - AskUserQuestion
---

# Dataset Onboarding Skill (Phase 1)

You are helping a Cell Painting Gallery maintainer onboard a new dataset contribution. This skill handles **Phase 1 only**: initial setup, identifier assignment, and tracking issue creation.

## Context

The Cell Painting Gallery follows a staging-to-production workflow. Contributors contact maintainers (@erinweisbart or @shntnu) to initiate contributions. Your job is to:
1. Gather contributor information
2. Assign a unique cpg#### identifier
3. Update the prefixes registry
4. Create a GitHub Discussion for tracking
5. Provide next steps

## Step 1: Gather Contributor Information

**First, check if the user has provided context** (email thread, message, etc.) in their initial request.

### If context is provided:
- **Parse the text** to extract:
  - Assay type (standard Cell Painting or variation)
  - Approximate data size
  - Components to contribute (images, analysis, backend, profiles, metadata, etc.)
  - Institution/affiliation
  - Suggested project names/tags
  - Contributor name/contact
  - Whether this is a new dataset or addition to existing dataset

- **Present what you found** with confidence levels, like:
  ```
  📧 Extracted from provided context:
  ✓ Assay type: [what you found]
  ✓ Data size: [what you found]
  ✓ Institution: [what you found]
  ? Project tag: [if ambiguous or unclear]
  ? Components: [if not explicitly listed]
  ```

- **Ask interactive questions ONLY for**:
  - Missing information
  - Ambiguous details that need clarification
  - Confirmation of assumptions

### If no context is provided:
Use the `AskUserQuestion` tool to gather all required information interactively.

### Required Information:

1. **Assay type**:
   - Standard Cell Painting
   - Variation (describe it)
   - Must label multiple cellular compartments/organelles

2. **Approximate data size**: Total size estimate (e.g., "5 TB", "500 GB")

3. **Components to contribute**:
   - Major (at least one required): `images`, `analysis`, `backend`, `load_data_csv`, `profiles`
   - Required: `metadata`
   - Optional: `pipelines`, `qc`, `profiles_assembled`, `segmentation`

4. **Institution identifier**:
   - Examples: `broad`, `anonymous`, `source_4`
   - Must be lowercase, can use underscores

5. **Suggested project tag**:
   - Typically 1-2 words describing the project
   - Examples: `jump`, `cmqtl`, `resistance`, `caie-drugresponse`
   - Sometimes includes author last name
   - Must be lowercase, use hyphens to separate words

6. **Contributor contact**: Name and/or GitHub handle

7. **Dataset type**: New dataset or addition to existing dataset?
   - If existing, which cpg#### prefix does it extend?

## Step 2: Assign cpg#### Identifier

1. **Read** `documentation/prefixes.md` to see all existing identifiers
2. **Find the next available cpg number**:
   - Parse the list (format: `cpg0000-tag`, `cpg0001-tag`, etc.)
   - Find highest number
   - Add 1 to get next available
3. **Format the full identifier**: `cpg####-suggested-tag`
   - Validate naming convention:
     - Lowercase letters only
     - Numbers allowed
     - Hyphens allowed (no underscores in tag portion)
     - No spaces or special characters
     - Max 64 characters total
4. **Show the maintainer** the proposed identifier and ask for confirmation

## Step 3: Update prefixes.md

1. **Add the new identifier** to `documentation/prefixes.md`
2. **Maintain numerical order** in the table
3. **Use the Edit tool** to add the line in the correct position
4. **Show the maintainer** what you added

## Step 4: Create GitHub Discussion

1. **Use the template structure** (based on discussion #66):

```markdown
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
Institution identifier = [institution identifier from Step 1]
Imaging Platform internal "champion" = [Maintainer name or specify if external]

**Workflow**
- [ ] Maintainer adds dataset identifier to [prefixes](https://github.com/broadinstitute/cellpainting-gallery/blob/main/documentation/prefixes.md) document.
- [ ] Champion or Contributor fills out the metadata collection form (https://airtable.com/shrVxz9DcoMlDoCBI)
- [ ] Champion checks that metadata completely filled out in Project Profiler Database (Imaging Platform internal use only)
- [ ] Champion asks Erin/Shantanu to  1) open the prefix for transfer to \`staging-cellpainting-gallery\` and 2) create credentials that allow upload. Each credential is for a single prefix on the staging bucket; multiple people can assume that same credential.

**Transfer data to \`staging-cellpainting-gallery\`**
Instructions for using the staging bucket credentials are [here](https://broadinstitute.github.io/cellpainting-gallery/uploading_to_cpg.html).
For each data subtype, Champion marks off as complete or explain why it is not being included:
- [ ] Image acquisition complete and uploaded (\`/images\`)
- [ ] Feature extraction complete and uploaded (\`/workspace/analysis\`)
- [ ] Backend complete and uploaded (\`/workspace/backend\`)
- [ ] Load_data complete and uploaded (\`/workspace/load_data_csv\`)
- [ ] Profiling complete and uploaded (\`/workspace/profiles\`)
- [ ] Metadata complete and uploaded (\`/workspace/metadata\`)

**Project completion**
These are the final steps to make a dataset fully public:
- [ ] Maintainer or champion Run [validation script](http://github.com/broadinstitute/cpg/cpgdata) to ensure data is completely uploaded (When script is out of alpha)
- [ ] Maintainer or champion updates cellpainting-gallery/README.md to add dataset to README.
- [ ] Maintainer transfers from \`staging-cellpainting-gallery\` to \`cellpainting-gallery\`.
- [ ] Erin/Shantanu disable staging prefix, delete data from staging, delete upload credentials.

Optional preparation for publication:
- [ ] Run Distributed-BioFormats2Raw to create .ome.zarr files
- [ ] Upload (meta)data to IDR (images remain hosted in cellpainting-gallery)
- [ ] Make IDR entry public

Once a paper is published:
- [ ] Maintainer or champion updates [Publications](https://github.com/broadinstitute/cellpainting-gallery/docs/publications.md) (In PR by data generator)
- [ ] Contributor adds the paper to https://github.com/cytodata/awesome-cytodata
```

2. **Customize the template** with the information gathered:
   - Fill in all Dataset Information fields (identifier, contributor, assay type, size, components, type)
   - Fill in institution identifier
   - Fill in champion name (the maintainer using this skill, unless specified otherwise)
   - Check the first workflow item (prefixes.md updated)

3. **Create the discussion** using the GitHub CLI:
   - Use title format: `[Dataset Contribution] cpg####-tag - Brief Description`
   - Use `gh` command to create the discussion in the repository
   - Category should be "Contributions" or "General" if Contributions doesn't exist

Example command:
```bash
gh discussion create \
  --repo broadinstitute/cellpainting-gallery \
  --title "[Dataset Contribution] cpg####-tag - Description" \
  --body "$(cat discussion_body.md)" \
  --category "General"
```

4. **Capture and display** the discussion URL to the maintainer

## Step 5: Generate Next Steps Summary

Provide the maintainer with a brief confirmation:

### ✅ Dataset onboarding initiated
- **Assigned**: cpg####-tag
- **Updated**: `documentation/prefixes.md`
- **Tracking**: [Discussion URL]

→ All dataset details and next steps are captured in the GitHub Discussion

## Important Notes

- **DO NOT** proceed to Phase 2 (credentials/upload) or Phase 3 (validation/transfer) - those are handled separately
- **DO NOT** commit changes to git without showing the maintainer first
- **DO NOT** push to remote - the maintainer will review and push when ready
- If the contributor is adding to an **existing dataset**, note that in the discussion and skip updating README.md (will be updated when complete)
- Always validate that the cpg number is unique before proceeding
- The tag portion of the identifier should be meaningful and memorable

## Error Handling

- If `gh` CLI is not available or fails, provide the template body and title for manual creation
- If prefixes.md cannot be read, ask the maintainer to verify file location
- If the suggested tag violates naming conventions, suggest alternatives
- If unclear about any information, always ask rather than guess

## Files You'll Need Access To:

- `documentation/prefixes.md` - Registry of all cpg identifiers
- `.git/` - For git operations (checking branch, status)

## Commands You May Use:

- `gh discussion create` - Create GitHub discussion
- `git status` - Check repository state
- `git add` - Stage changes (only with maintainer approval)
- `gh repo view` - Verify repository details

Remember: This is Phase 1 only. Focus on gathering information, assigning identifiers, and setting up tracking. The maintainer will handle credentials, upload coordination, and validation in subsequent phases.
