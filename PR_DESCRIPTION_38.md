Fixes #38 and #5: Update Instagram profile links

## Summary
This PR updates all Instagram links for the site to use the official `michelle_monet_catering` profile and ensures the mobile/hero/footer links no longer point to a non-existent profile.

## Changes
- Replaced all `https://www.instagram.com/letters_from_the_kitchen` URLs in `index.html` with `https://www.instagram.com/michelle_monet_catering/`.
- Updated the JSON-LD `sameAs` entry so structured data also points at the new Instagram profile.
- Updated:
  - Header contact bar Instagram icon link
  - Welcome section “Síguenos en Instagram” link
  - Footer Instagram link

## Why
- **#38 IG updates**: Align all Instagram links with the new official profile.
- **#5 Instagram mobile link**: On mobile, the previous profile could return “profile doesn’t exist.” Using the single canonical profile URL fixes this for all devices.

## Testing
- [ ] Header Instagram icon opens `https://www.instagram.com/michelle_monet_catering/`.
- [ ] Welcome section “Síguenos en Instagram” link opens the same profile.
- [ ] Footer Instagram link opens the same profile.
- [ ] Instagram links work on mobile as well as desktop.

Closes #38
Closes #5
