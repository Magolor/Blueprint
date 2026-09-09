---
name: template-pr-gui
description: Read when a GUI-related pull request needs screenshot evidence.
---

# GUI evidence

## Summary

Required for every GUI-related PR, including GUI fixes or refactors that intend
no visible change. Include actual screenshots of the affected interface with
captions identifying the scenario and revision. For an existing interface,
show before and after with matching viewport, theme, data, and state. For a
new interface, show the implemented result and identify that no baseline exists.
Cover the changed states and consequential responsive or theme behavior. Add a
short recording when motion or interaction matters; it supplements screenshots.

## Capture and share

Use GitHub-accessible attachments or repository-hosted image links with alt text;
local filesystem paths do not work for remote reviewers. Remove secrets and
private data. If capture is blocked, state the blocker and missing evidence in
the draft; do not substitute mockups or claim the evidence is complete. Obtain
an explicit waiver before treating the PR as ready without required evidence.

Use a compact state-by-theme or before/after image table when it helps comparison. Screenshots demonstrate rendered states; tests or interaction checks establish behavior.

