# Keep Current Finder Window

Clear other Finder windows on Mac with Option + 7 while keeping the window you are using. The Rule closes Finder windows behind that front window.

Bring the Finder window you want to keep to the front first. The script snapshots windows with an index greater than one and closes those windows, leaving the front window and its tabs open.

[Website preview and full setup](https://www.rulr.app/rules/close-all-finder-windows-mac/) · [Download close-finder-windows.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/close-finder-windows/close-finder-windows.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Keep the folder you are working in

**When:** Press Option + 7. **If:** Finder is frontmost. **Do:** Run AppleScript to capture the Finder windows behind its front window, then close those other windows.

This is useful after browsing many folders: keep the current working location and clear the clutter. It differs from Option-Command-W, which closes the current window along with the others.

## Configure and try it

1. Open three ordinary Finder windows in disposable folders.
2. Bring the one you want to keep to the front.
3. Import the Rule, review Option + 7 and allow Finder Automation.
4. Enable it and press the shortcut with Finder still frontmost.
5. Confirm that the front window remains and the other windows close. Try again with one window; nothing else should close.

## Requirements and limits

Run AppleScript does not require Pro. The Rule needs Finder Automation access. Rulr's native All Windows target cannot express “all except the front window,” which is why this adapted workflow uses a small Finder script.

The script targets Finder's window order, including windows reported on other Spaces. It closes tabs contained in the other windows but keeps the retained window's tabs. It does not delete files, quit Finder or restore closed browsing state.

For a named folder from the current selection, use [Group Selected Files](https://www.rulr.app/rules/new-folder-hotkey-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/close-all-finder-windows-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
