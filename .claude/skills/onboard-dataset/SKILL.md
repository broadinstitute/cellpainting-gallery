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

### If context is provided

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

### If no context is provided

Use the `AskUserQuestion` tool to gather all required information interactively.

### Required Information

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

1. **Read the template** from `.claude/skills/onboard-dataset/templates/discussion_template.md`
   - This is based on the official template: https://github.com/broadinstitute/cellpainting-gallery/discussions/66
   - Enhanced with structured Dataset Information section for easier tracking

2. **Customize the template** with the information gathered:
   - Fill in all Dataset Information fields (identifier, contributor, assay type, size, components, type)
   - Fill in institution identifier
   - Fill in champion name (the maintainer using this skill, unless specified otherwise)
   - Check the first workflow item (prefixes.md updated)

3. **Create the discussion** using the helper script:
   - Use simple title format: `cpg####-tag` or `cpg####-tag (brief description)`
     - Examples from existing discussions:
       - `cpg0020-varchamp`
       - `cpg0029-chroma-pilot`
       - `cpg0016-JUMP (deep-learning generated profiles via Mesmer)`
   - First, write the customized template to a temporary file (e.g., `discussion_body.md`)
   - Then run the helper script:

   ```bash
   .claude/skills/onboard-dataset/scripts/create_discussion.sh \
     discussion_body.md \
     "cpg####-tag"
   ```

   The script will:
   - Properly escape the body content for GraphQL
   - Use the correct repository ID (`R_kgDOGULepQ`) and category ID (`DIC_kwDOGULepc4CZL49` for "Dataset descriptions")
   - Create the discussion via GitHub GraphQL API
   - Return the discussion URL and number

   **Optional**: If you need to verify category IDs or use a different category:

   ```bash
   gh api graphql -f query='
   query {
     repository(owner: "broadinstitute", name: "cellpainting-gallery") {
       id
       discussionCategories(first: 10) {
         nodes {
           id
           name
         }
       }
     }
   }'
   ```

   Then pass the custom IDs to the script:

   ```bash
   .claude/skills/onboard-dataset/scripts/create_discussion.sh \
     discussion_body.md \
     "Title" \
     "REPO_ID" \
     "CATEGORY_ID"
   ```

   **Result**: The script will display the discussion URL and number when successful

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

- If `gh` CLI is not available, the script will fail with a clear error message. Provide the template body and title for manual creation via GitHub web UI
- If `jq` is not installed, the script will fail with a clear error. Install it with `brew install jq` (macOS) or appropriate package manager
- If the script fails to create the discussion, it will display the GraphQL response for debugging
- If prefixes.md cannot be read, ask the maintainer to verify file location
- If the suggested tag violates naming conventions, suggest alternatives
- If unclear about any information, always ask rather than guess

## Files and Scripts You'll Use

- `documentation/prefixes.md` - Registry of all cpg identifiers
- `.claude/skills/onboard-dataset/templates/discussion_template.md` - GitHub Discussion template (based on [#66](https://github.com/broadinstitute/cellpainting-gallery/discussions/66))
- `.claude/skills/onboard-dataset/scripts/create_discussion.sh` - Helper script for creating GitHub discussions
- `.git/` - For git operations (checking branch, status)

## Commands You May Use

- `.claude/skills/onboard-dataset/scripts/create_discussion.sh` - Create GitHub discussion with proper escaping
- `gh api graphql` - Query/mutate GitHub data via GraphQL API (optional, script handles discussion creation)
- `git status` - Check repository state
- `git add` - Stage changes (only with maintainer approval)
- `gh repo view` - Verify repository details

Remember: This is Phase 1 only. Focus on gathering information, assigning identifiers, and setting up tracking. The maintainer will handle credentials, upload coordination, and validation in subsequent phases.
