---
name: michellemonet-issue-workflow
description: >
  Implements GitHub issues for the MichelleMonetCatering static site, including
  editing index.html, managing feature branches, committing with Fix/Closes
  messages, and opening pull requests via gh. Use whenever the user asks to
  "fulfill", "complete", or "implement" a numbered GitHub issue for this repo.
---

# Michelle Monet Catering Issue Workflow

## When to Use This Skill

Use this skill **only** in the `MichelleMonetCatering` repository when:

- The user says things like:
  - "fulfill issue #N"
  - "complete issue #N"
  - "implement issue #N"
  - "open a pull request for issue #N"
- The work is about:
  - Updating text, links, or layout in `index.html`
  - Tweaking gallery images, sections, or copy for the static site
  - Wiring a change to a GitHub issue with a branch, commit, and PR

Do **not** use this skill outside this repo or for non–issue-based tasks.

## High-Level Workflow

1. **Understand the issue**
2. **Create or select a feature branch**
3. **Edit the site (usually `index.html`)**
4. **Verify changes locally**
5. **Commit with `Fix #…` and `Closes #…`**
6. **Push the branch**
7. **Create a PR documenting the work**

Follow the detailed steps below.

## 1. Understand the Issue

1. If the user provides an issue number `N`, fetch it from GitHub:
   - Use `WebFetch` on  
     `https://github.com/HeatherMEdwards/MichelleMonetCatering/issues/N`.
2. Extract:
   - **Title**
   - **Body (requirements and example text)**
   - Any **checklist or specifics** (e.g., exact copy, URLs, or image filenames).
3. If the issue refers to existing issues (e.g., "Fix #22: …"), check those
   issues/PRs as needed to understand the context, but do not change them unless
   the user asks.

## 2. Branch Strategy

### Single-Issue Branch

For a single issue `N`:

- Branch name pattern:
  - `fix/N-short-slug`
  - Example: `fix/22-remove-monster-foot-cake`,
    `fix/38-ig-updates`.

Steps:

1. Ensure you are on `main` and up to date:
   - `git checkout main`
   - `git pull`
2. Create the branch:
   - `git checkout -b fix/N-short-slug`

### Multi-Issue Branch

When the user **explicitly** wants a single PR for multiple issues (e.g. `7, 26,
18, 20, 21`):

- Branch name pattern:
  - `fix/7-26-18-20-21`

Steps:

1. Ensure `main` is up to date.
2. `git checkout -b fix/7-26-18-20-21`
3. Implement *all* listed issues before committing.

## 3. Editing the Site

### Primary File

Most changes live in:

- `index.html` (hero, sections, copy, gallery, social links, schema JSON-LD)

### Finding Relevant Sections

Use `Grep` and `Read` to find:

- **Service descriptions** (Entradas, Guisados, Postres, Panes artesanales):
  - Search for `Entradas`, `Postres`, `Panes artesanales`, etc.
- **Por Qué Elegirnos**:
  - Search for `¿Por Qué Elegirnos?` or unique phrases mentioned in issues.
- **Instagram links**:
  - Search for `instagram.com` or specific profile names:
    - `letters_from_the_kitchen`
    - `michelle_monet_catering`
- **Gallery images**:
  - Search for `img/` and specific filenames or captions mentioned in issues.

### Making Changes

1. **Use precise replacements**:
   - Prefer `StrReplace` (or small `ApplyPatch` hunks) with the **full snippet**
     being replaced to avoid accidental matches.
2. **When changing copy**:
   - Match the **exact text** from the issue body.
   - Preserve HTML structure and attributes (classes, `loading`, `decoding`,
     `alt`).
3. **When removing an image**:
   - Remove the whole `<div class="gallery-item">…</div>` block.
   - Optionally delete the file from `img/` if the issue requires it.
4. **When updating URLs**:
   - Update **all occurrences**, including:
     - JSON-LD `sameAs` field
     - Header/contact bar icons
     - Welcome-section links
     - Footer links
5. **When changing gallery composition (reflow considerations)**:
   - Remember the gallery uses CSS grid; removing items will naturally shorten
     the last row (no literal “blank tiles”).
   - This is usually fine, but if the user wants a perfectly balanced grid:
     - Consider **combining multiple small gallery sections into one grid**.
     - Reorder or regroup photos so common viewport widths (e.g. 2 or 3
       columns) have rows that feel visually balanced.
   - Always verify on desktop and mobile after significant gallery changes.

## 4. Verify Locally

When the user wants to preview or when changes are non-trivial:

1. **Sync local `main` with GitHub first (to avoid stale content):**
   - If you are about to compare with the live site, always run:
     - `git checkout main`
     - `git pull`
   - This ensures you are not seeing old content locally (e.g. an image that was
     removed on GitHub but still present in your local `main`).
2. From the repo root, start a static server on an open port:
   - `python3 -m http.server 8000` (or another open port like `8003` if 8000 is
     already in use).
3. Navigate to:
   - `http://localhost:8000` (or the chosen port).
4. Check:
   - Text changes appear as expected.
   - Links (WhatsApp, Instagram) open the correct targets.
   - Gallery layout looks reasonable, with no broken images or unexpected items.
5. If the **live site and local preview differ** (for example, a removed image
   still shows locally):
   - Re-confirm you are on `main` and have run `git pull`.
   - Restart the local server and refresh the browser.
   - Only debug further once you are sure local `main` matches `origin/main`.

Stop the server with `Ctrl+C` in the terminal when done.

## 5. Commit Messages

### Single Issue

Format:

- **Title line**: `Fix #N: short description`
- **Body**:
  - Brief bullet list of key changes.
  - End with `Closes #N`.

Example:

```text
Fix #38: Update Instagram profile links to michelle_monet_catering

- Replace all letters_from_the_kitchen URLs in index.html with
  https://www.instagram.com/michelle_monet_catering/ including JSON-LD sameAs
  and all anchor tags.

Closes #38
```

### Multiple Issues in One Commit

Format:

- **Title line**: `Fix #7, #26, #18, #20, #21: short summary`
- **Body**:
  - Bullets grouped by issue.
  - End with: `Closes #7, Closes #26, Closes #18, Closes #20, Closes #21`.

Always ensure:

- The commit accurately summarizes **why** the change was made (tie it to the
  issue).
- The `Closes #…` lines match the actual issue numbers being addressed.

## 6. Pushing Branches

After committing:

1. Push and set upstream:
   - `git push -u origin fix/N-short-slug`
2. If push fails due to auth:
   - Instruct the user to:
     - Configure `gh auth login` or
     - Use a personal access token for HTTPS pushes.
   - Do **not** attempt to store or echo credentials.

## 7. Creating Pull Requests with `gh`

Use `gh pr create` when available and authenticated.

### Simple Case (Use Commit Message)

For a branch with a single well-structured commit:

```bash
gh pr create --base main --head fix/N-short-slug --fill
```

This uses the commit title/body as the PR title/body.

### Custom Title and Body

When you need a more detailed description (e.g., multiple issues):

1. Optionally create a PR description file in the repo root:
   - `PR_DESCRIPTION_7_26_18_20_21.md`, etc.
2. Run:

```bash
gh pr create \
  --base main \
  --head fix/7-26-18-20-21 \
  --title "Fix #7, #26, #18, #20, #21: padding and copy" \
  --body-file PR_DESCRIPTION_7_26_18_20_21.md
```

If CLI quoting is tricky, prefer `--fill` and then let the user adjust the
description manually on GitHub.

## 8. Closing Issues

- Ensure commit messages and/or PR descriptions include the correct
  **closing keywords**:
  - `Closes #N`
  - or `Fixes #N`
- Confirm that:
  - The PR base is `main`.
  - The branch contains only the intended changes for those issues (or the user
    has explicitly agreed to group them).

GitHub will automatically close the referenced issues when the PR is merged.

## Examples

### Example 1: Single Issue (IG Profile Update)

- User: "Please complete issue #38."
- Agent:
  1. Read issue #38 (IG updates) from GitHub.
  2. `git checkout main && git pull`.
  3. `git checkout -b fix/38-ig-updates`.
  4. Update all `letters_from_the_kitchen` URLs in `index.html` to
     `https://www.instagram.com/michelle_monet_catering/`, including JSON-LD.
  5. Preview locally if requested.
  6. Commit with `Fix #38: …` and `Closes #38`.
  7. `git push -u origin fix/38-ig-updates`.
  8. `gh pr create --base main --head fix/38-ig-updates --fill`.

### Example 2: Multiple Issues (Padding and Copy)

- User: "Please fulfill issues #7, 26, 18, 20 and 21."
- Agent:
  1. Read each issue from GitHub for exact copy.
  2. `git checkout main && git pull`.
  3. `git checkout -b fix/7-26-18-20-21`.
  4. Apply:
     - #7: Adjust section, CTA, and welcome padding/line-height.
     - #26: Convert Por Qué Elegirnos paragraph to bullet-style list.
     - #18/#20/#21: Update Entradas, Postres, Panes artesanales text.
  5. Commit with a combined `Fix #7, #26, #18, #20, #21: …` message and
     corresponding `Closes #…` lines.
  6. Push and open a PR summarizing all changes.

