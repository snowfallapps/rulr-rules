# Press Keys When an App Launches

Automatically press a configured key or keyboard shortcut after a selected application launches on your Mac.

Choose the app and recorded key sequence after importing the Rule. It brings the application forward before sending the keys, so the result depends on the app's active window and current keyboard shortcuts.

[Website preview and full setup](https://www.rulr.app/rules/press-keys-app-launch-mac/) · [Download press-keys-when-app-launches.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/press-keys-when-app-launches/press-keys-when-app-launches.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Send a shortcut after an app starts

This Rule is useful when opening an application is regularly followed by the same keyboard command. It combines a launch event, application activation, a brief delay, and a recorded key sequence into one routine.

**When:** The selected app launches. **Do:** Bring that app forward, wait one second, and press the configured keys. There is no If Condition. The sample watches TextEdit and sends Command + S, so its visible result depends on the document and save state at the time of the keypress.

## Configure and try it

1. Import through **Open this Rule in Rulr** and choose your application in both the launch Trigger and Activate Application Action.
2. Record or select the intended key sequence in Type Text or Press Keys. Confirm that the same shortcut performs your desired command when pressed manually in that app.
3. Review the delay. One second is a starting value, not a guarantee that a document or network workspace has finished loading. Grant Accessibility access for activation and key simulation.
4. Save your work, quit the selected app, and relaunch it for a controlled test. Check which window receives the command and adjust the sequence or delay if needed.

## Requirements and limits

The key-simulation Action requires Rulr Pro. The selected application must be installed, and its keyboard command must be available in the active context.

The Rule responds to a launch rather than every switch back to an already running app. Another app taking focus during the delay can also affect input. It does not identify controls by name or verify that the command succeeded. For opening a project location on launch instead, see [Open Project Folder](https://www.rulr.app/rules/open-project-folder-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/press-keys-app-launch-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
