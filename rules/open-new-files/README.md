# Open New Files

Open each new file in its default application when it is added directly to a watched folder on your Mac, while leaving added folders unopened.

The Rule listens for an added folder item, checks that the changed item is a file, and opens its path with the default application. Choose a watched folder and test with a safe sample file before enabling it.

[Website preview and full setup](https://www.rulr.app/rules/open-new-files-mac/) · [Download open-new-files.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/open-new-files/open-new-files.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Open incoming files in their default app

Use this Rule for a small review inbox where each new document should open as soon as it arrives. It saves a trip to Finder when another workflow places a report or reference file in a folder you are actively watching.

**When:** A direct item is added to the selected folder. **If:** The event is an addition and the item kind is a file. **Do:** Open the Trigger's Item Path with its default application. The two Conditions keep folder additions from being opened by the sample.

## Configure and try it

1. Import using **Open this Rule in Rulr**, then choose the folder in Folder Contents Changed. The sample uses Downloads; a dedicated review folder is often easier to control.
2. Keep the change type set to added and review the file-kind Condition.
3. Review Open File or Folder. Its source should remain the event's Item Path, and its application choice should be Default unless you want a particular compatible app.
4. Enable the Rule and add a harmless text document. Confirm that the right app opens it. Add a folder separately and confirm that the Rule does not open it.

## Requirements and limits

Folder monitoring requires Rulr Pro. Rulr needs access to the watched folder, and macOS needs a suitable application for the file type.

The sample does not recursively monitor subfolders, open the existing contents on import, or wait for a browser's download-complete signal. Avoid using a busy general download folder until you have tested the behavior. For running your own processing steps instead of opening files, see [Run Shortcut for Folder](https://www.rulr.app/rules/watch-folder-run-shortcut-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/open-new-files-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
