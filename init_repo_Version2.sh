#!/usr/bin/env bash
set -e

# One-shot script to create the GitHub repository and push files.
# Requirements: gh (GitHub CLI) installed and authenticated, git installed.
# Usage: chmod +x init_repo.sh && ./init_repo.sh
#
# Edit OWNER and REPO as needed.

OWNER="anastasiadisfoivos-hub"
REPO="MacFinder"
COMMIT_MSG="Initial site commit"

if ! command -v gh >/dev/null 2>&1; then
  echo "gh (GitHub CLI) not found. Install from https://cli.github.com/ and run 'gh auth login'."
  exit 1
fi

if ! command -v git >/dev/null 2>&1; then
  echo "git not found. Install git and retry."
  exit 1
fi

# Ensure we're in repo root (script should be placed at repo root)
echo "Preparing repo locally..."

# Ensure docs/ contains the website content for GitHub Pages (project site)
if [ -d "website" ]; then
  mkdir -p docs
  cp -r website/* docs/ || true
fi

git init
git checkout -b main || git branch -M main
git add .
git commit -m "$COMMIT_MSG"

echo "Creating repository $OWNER/$REPO on GitHub..."
# Create repo (public)
gh repo create "$OWNER/$REPO" --public --source=. --remote=origin --push -y

# Configure Pages to use main:/docs (project site)
echo "Configuring GitHub Pages to serve from main:/docs ..."
gh api -X PUT /repos/"$OWNER"/"$REPO"/pages -f source.branch=main -f source.path="/docs" || true

echo "Repository created: https://github.com/$OWNER/$REPO"
echo "Pages (may take a minute): https://$OWNER.github.io/$REPO/"