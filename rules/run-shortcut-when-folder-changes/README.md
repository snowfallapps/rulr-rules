# Run Shortcut for Folder

Run an Apple Shortcut automatically when a new file is added to a watched folder on Mac. Choose the folder and Shortcut to start your file-processing task.

The sample watches Downloads for added items and runs your chosen Shortcut with a 30-second timeout. Connect the event's Item Path as input if your Shortcut needs the arriving file.

[Website preview and full setup](https://www.rulr.app/rules/watch-folder-run-shortcut-mac/) · [Download run-shortcut-when-folder-changes.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/run-shortcut-when-folder-changes/run-shortcut-when-folder-changes.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Watch a Mac folder and trigger an Apple Shortcut

Use this Rule when an Apple Shortcut already performs your file-processing task and you want changes in a folder to start it. Rulr provides the event trigger, while the selected Shortcut remains responsible for what happens afterward.

**When:** A direct item is added to the watched folder. **Do:** Run an Apple Shortcut. The sample has no If Condition, no selected Shortcut, and a 30-second timeout. It does not automatically pass the changed item's path as input; configure an input connection if your Shortcut needs that information.

## Configure and try it

1. Import with **Open this Rule in Rulr**, then select the folder to watch. The sample uses Downloads and the added change type.
2. Choose an existing Shortcut in Run Shortcut. Run it manually in the Shortcuts app first so you know its setup and permissions are complete.
3. Review whether the Shortcut expects input and connect the relevant Trigger Variable if needed. Adjust the timeout for the actual task.
4. Enable the Rule and add a disposable file. Verify the Shortcut's expected result, then repeat with a second item to check that separate arrivals behave as intended.

When extending this workflow, review the [folder Trigger's parameters and outputs](https://www.rulr.app/capabilities/#trigger.input.folder-contents-changed) separately from the Apple Shortcut's own settings. The [Mac automation guide](https://www.rulr.app/posts/mac-automation/#can-i-combine-apple-shortcuts-and-applescript-in-one-workflow) explains combining existing Shortcuts with other Rule Actions.

## Requirements and limits

Folder monitoring requires Rulr Pro. Folder access and any permissions requested by the chosen Shortcut must be available on this Mac.

The watcher covers direct children, not nested contents, and an event is not a download-completion guarantee. Multiple arriving items can produce multiple runs, so choose a Shortcut suitable for repeated invocation. For opening each new file directly, use [Open New Files](https://www.rulr.app/rules/open-new-files-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/watch-folder-run-shortcut-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
