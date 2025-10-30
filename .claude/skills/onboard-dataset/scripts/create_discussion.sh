#!/bin/bash
# create_discussion.sh - Create a GitHub Discussion for dataset onboarding
#
# Usage: create_discussion.sh <body_file> <title> [repo_id] [category_id]
#
# Arguments:
#   body_file    - Path to markdown file containing the discussion body
#   title        - Discussion title (e.g., "cpg####-tag" or "cpg####-tag (description)")
#   repo_id      - GitHub repository ID (default: R_kgDOGULepQ for broadinstitute/cellpainting-gallery)
#   category_id  - Discussion category ID (default: DIC_kwDOGULepc4CZL49 for "Dataset descriptions")

set -e  # Exit on error

# Default values
DEFAULT_REPO_ID="R_kgDOGULepQ"
DEFAULT_CATEGORY_ID="DIC_kwDOGULepc4CZL49"

# Parse arguments
BODY_FILE="${1}"
TITLE="${2}"
REPO_ID="${3:-$DEFAULT_REPO_ID}"
CATEGORY_ID="${4:-$DEFAULT_CATEGORY_ID}"

# Validate inputs
if [[ -z "$BODY_FILE" ]] || [[ -z "$TITLE" ]]; then
    echo "Error: Missing required arguments" >&2
    echo "" >&2
    echo "Usage: $0 <body_file> <title> [repo_id] [category_id]" >&2
    echo "" >&2
    echo "Example:" >&2
    echo "  $0 discussion_body.md 'cpg0023-test'" >&2
    exit 1
fi

if [[ ! -f "$BODY_FILE" ]]; then
    echo "Error: Body file not found: $BODY_FILE" >&2
    exit 1
fi

# Check for required commands
if ! command -v gh &> /dev/null; then
    echo "Error: gh CLI is not installed or not in PATH" >&2
    exit 1
fi

if ! command -v jq &> /dev/null; then
    echo "Error: jq is not installed or not in PATH" >&2
    exit 1
fi

# Prepare the body with proper JSON escaping
BODY=$(jq -Rs . < "$BODY_FILE")

# Create the GraphQL mutation
RESPONSE=$(gh api graphql -f query="
mutation {
  createDiscussion(input: {
    repositoryId: \"$REPO_ID\"
    categoryId: \"$CATEGORY_ID\"
    title: $(echo "$TITLE" | jq -R .)
    body: $BODY
  }) {
    discussion {
      url
      id
      number
    }
  }
}")

# Extract and display the discussion URL
DISCUSSION_URL=$(echo "$RESPONSE" | jq -r '.data.createDiscussion.discussion.url')
DISCUSSION_NUMBER=$(echo "$RESPONSE" | jq -r '.data.createDiscussion.discussion.number')

if [[ "$DISCUSSION_URL" != "null" ]] && [[ -n "$DISCUSSION_URL" ]]; then
    echo "✅ Discussion created successfully!"
    echo "   URL: $DISCUSSION_URL"
    echo "   Number: #$DISCUSSION_NUMBER"
    exit 0
else
    echo "❌ Failed to create discussion" >&2
    echo "Response: $RESPONSE" >&2
    exit 1
fi
