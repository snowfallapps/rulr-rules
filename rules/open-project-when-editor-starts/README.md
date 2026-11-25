# Open Project Folder

Automatically open a project folder when a selected editor, terminal, or other working app launches on your Mac.

Choose the application, project folder, and app used to open it. The Rule responds only to the selected application's launch event.

[Website preview and full setup](https://www.rulr.app/rules/open-project-folder-mac/) · [Download open-project-when-editor-starts.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/open-project-when-editor-starts/open-project-when-editor-starts.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Open a folder when your working app launches

This Rule pairs an application's launch with the folder you usually need next. For example, starting a writing app can open your reference folder so project documents are available without navigating through Finder each time.

**When:** The selected application launches. **Do:** Open a configured folder using the default application. There is no If Condition. The sample watches TextEdit and opens Downloads; those are starting values to replace with the app and project location on your Mac.

## Configure and try it

1. Import with **Open this Rule in Rulr**, then select the application in the launch Trigger. Use the installed app you actually start for the project.
2. Choose the project folder in Open File or Folder. Review the opening application: Default normally lets macOS decide, while a specific compatible app can provide a different result.
3. Enable the Rule, save any work, quit the selected application, and launch it again. Check that the chosen folder opens.
4. Switch away from the app and back without quitting it. This should not be treated as another launch event; choose an activation Trigger instead if that is the workflow you want.

## Requirements and limits

The selected app must be installed and the folder must exist with access available to Rulr. The sample's components are available without Pro and declare no additional special permission.

Opening a folder does not automatically load a particular editor workspace, start a development server, or restore project windows. Those tasks need their own supported Actions. To start several applications together from a keyboard shortcut, see [Open Work Apps](https://www.rulr.app/rules/open-work-apps-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/open-project-folder-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
