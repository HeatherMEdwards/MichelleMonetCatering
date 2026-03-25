# Feature Creation Process

## Overview

This document outlines the workflow for creating and implementing new features for MichelleMonetCatering.com.

## Workflow Summary

1. **Create GitHub Issue** - Document the feature or fix
2. **Create Branch** - `fix/N-short-slug` or `fix/N1-N2-N3` for multi-issue
3. **Implement Changes** - Edit `index.html` (or other files)
4. **Verify Locally** - Test with local server
5. **Commit** - With `Fix #N:` and `Closes #N` keywords
6. **Push & PR** - Push branch and create pull request

---

## Step 1: Create GitHub Issue

Create an issue describing the feature, fix, or exploratory work.

```bash
gh issue create --title "Your title" --body "## Overview
Description here

## Requirements
- [ ] Task 1
- [ ] Task 2
" --repo HeatherMEdwards/MichelleMonetCatering
```

**Issue templates:**

### Bug Fix
```markdown
## Issue
Description of the problem.

## Expected Behavior
What should happen.

## Steps to Reproduce
1. Go to...
2. Click on...
3. See error

## Screenshots (if applicable)
```

### New Feature
```markdown
## Overview
Brief description of the feature.

## Requirements
- [ ] Requirement 1
- [ ] Requirement 2

## Design Notes
Any design considerations.
```

### Exploratory Design
```markdown
## Goal
What you're trying to achieve or explore.

## Tasks
- [ ] Research current state
- [ ] Explore design options
- [ ] Prototype variations
- [ ] Get feedback
- [ ] Implement
```

---

## Step 2: Create Branch

### Single Issue
```bash
git checkout main
git pull
git checkout -b fix/N-short-slug
```

Examples:
- `fix/49-menu-categories`
- `fix/50-exploratory-design`
- `fix/38-ig-updates`

### Multi-Issue
```bash
git checkout main
git pull
git checkout -b fix/7-26-18-20-21
```

---

## Step 3: Implement Changes

### Primary Files
- `index.html` - Main site content
- `img/` - Images and assets
- CSS styles inline in `index.html`

### Finding Code
```bash
# Search for specific text
grep "Entradas" index.html
grep "Por Qué Elegirnos" index.html
grep "instagram.com" index.html
```

### Guidelines
- Match exact text from issue requirements
- Preserve HTML structure and attributes
- Update all occurrences (links, JSON-LD, etc.)
- Verify layout on desktop and mobile

---

## Step 4: Verify Locally

### Start Local Server
```bash
python3 -m http.server 8000
```

Open: **http://localhost:8000**

Stop: `Ctrl+C`

### Verification Checklist
- [ ] Text changes appear correctly
- [ ] Links work (WhatsApp, Instagram)
- [ ] Images load properly
- [ ] Layout looks correct on mobile
- [ ] No console errors

---

## Step 5: Commit Changes

### Single Issue
```
Fix #N: Short description

- Bullet point of changes made
- Another change

Closes #N
```

### Multiple Issues
```
Fix #7, #26, #18: Summary of changes

- #7: Change description
- #26: Change description
- #18: Change description

Closes #7, Closes #26, Closes #18
```

### Commit Command
```bash
git add .
git commit -m "Fix #N: Description"
```

---

## Step 6: Push & Create PR

### Push Branch
```bash
git push -u origin fix/N-short-slug
```

### Create Pull Request

**Simple (uses commit message):**
```bash
gh pr create --base main --head fix/N-short-slug --fill
```

**Custom title/body:**
```bash
gh pr create \
  --base main \
  --head fix/N-short-slug \
  --title "Fix #N: Description" \
  --body "## Summary
- Change 1
- Change 2

Closes #N"
```

### PR Options
- `--fill` - Use commit message as title/body
- `--body-file` - Use file for PR description
- Edit on GitHub - Create PR first, then add details manually

---

## Quick Reference

| Action | Command |
|--------|---------|
| Current branch | `git branch --show-current` |
| Switch to main | `git checkout main` |
| Update main | `git pull` |
| Create branch | `git checkout -b fix/N-slug` |
| Check status | `git status` |
| Stage & commit | `git add . && git commit -m "Fix #N: ..."` |
| Push branch | `git push -u origin fix/N-slug` |
| Create PR | `gh pr create --base main --head fix/N-slug --fill` |

---

## Common Issues

### Zsh "no matches found"
If you get `zsh: no matches found`, wrap the URL in quotes:
```bash
# Wrong
gh pr create --body-text https://...

# Correct
gh pr create --body-text "https://..."
```

### Auth Issues
If `gh` commands fail:
```bash
gh auth status
gh auth login
```

### Branch Already Exists
```bash
git checkout fix/N-slug
git pull
```

---

## Branch Naming

| Type | Pattern | Examples |
|------|---------|----------|
| Single issue | `fix/N-slug` | `fix/49-menu-categories` |
| Multi-issue | `fix/N1-N2-N3` | `fix/7-26-18-20-21` |
| Exploration | `fix/N-slug` | `fix/50-exploratory-design` |

---

## File Locations

| File | Purpose |
|------|---------|
| `index.html` | Main site content |
| `img/` | Images |
| `scripts/` | Build/utility scripts |
| `.cursor/skills/` | Workflow documentation |
