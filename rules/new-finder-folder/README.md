# Group Selected Files

Group selected Finder files into a new named folder on Mac with Option + 3. The Rule asks for the folder name and moves the captured selection into it.

Select items in one Finder folder first. The Rule keeps the new folder beside those items, rejects an existing destination name and reveals the resulting folder.

[Website preview and full setup](https://www.rulr.app/rules/new-folder-hotkey-mac/) · [Download new-finder-folder.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/new-finder-folder/new-finder-folder.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Put a Finder selection into a named folder

**When:** Press Option + 3. **If:** Finder is frontmost. **Do:** Run AppleScript to snapshot the selection, check that the items share a parent, ask for a name, create that folder and move the selected items into it.

Use it to collect the files for a handoff or project without creating a folder, renaming it and dragging the selection separately. The built-in Control-Command-N also groups a Finder selection; this Rule supplies an explicit name prompt and checks its destination before moving.

## Configure and try it

1. In a disposable folder, select two or three test files.
2. Import the Rule, review the shortcut and allow Finder Automation when requested.
3. Enable it, focus Finder and press Option + 3.
4. Enter a new folder name and choose **Create and Move**.
5. Confirm that the selected items moved into the new folder and unselected items stayed put. Try Cancel and an existing name separately.

## Requirements and limits

Run AppleScript does not require Pro. The script handles Finder's live selection because the current native file Actions do not expose a selected-file collection.

This moves existing items, rather than copying or backing them up. An empty selection or items from different parent folders are rejected. Permissions or a failed move can leave a partially completed operation; inspect the folders before retrying.

The folder stays inside the original parent. It is not moved one directory upward.

For incoming files instead of a selection, see [Mac file automation](https://www.rulr.app/rules/files-organization/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/new-folder-hotkey-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
