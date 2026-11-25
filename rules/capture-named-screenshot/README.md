# Capture and Name Screenshot

Capture a Mac screen region, name it and save it to your chosen folder with Option + 9. The Rule asks for the filename immediately after capture.

Choose the destination in Move File or Folder after importing; it initially uses Downloads. The flow uses native capture, input, rename, move and reveal Actions, without watching a screenshots folder.

[Website preview and full setup](https://www.rulr.app/rules/screenshot-macro-mac/) · [Download capture-named-screenshot.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/capture-named-screenshot/capture-named-screenshot.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Name the screenshot while its purpose is fresh

**When:** Press Option + 9. **Do:** Capture Screen or Window lets you select an area at execution time. Ask for Input collects the filename, Rename appends .png, Move saves it into the configured destination, and Reveal shows the saved image.

This suits bug reports, receipts or research captures that need a meaningful name. It avoids hunting for a newly created screenshot and renaming it afterward.

## Configure and try it

1. Import the Rule and choose the destination in Move File or Folder.
2. Allow Screen Recording and folder access, review the shortcut and enable it.
3. Press Option + 9 and select a harmless screen region.
4. Enter a filename without .png, then confirm.
5. Inspect the named PNG in the destination. Try an existing name to confirm that the Rule stops instead of replacing it.

## Requirements and limits

Rename and Move require Pro; capture, input and reveal do not. The default target is Capture on Run. You can select a different supported capture target in the Action.

This adaptation uses one configured capture mode and stops on a duplicate name. It does not include a loop that repeatedly asks for a different name. Cancelling the name prompt leaves the captured image in its temporary location.

A failed capture, rename or move stops the flow. The Rule does not perform OCR or redact content. For recognized text, use [Copy Text from Your Screen](https://www.rulr.app/rules/copy-text-mac-screen/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/screenshot-macro-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
