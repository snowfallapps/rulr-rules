# Launch and Focus App

Open an app with a keyboard shortcut on Mac and bring it to the front. Pick your app and hotkey to launch it or return to it while working elsewhere.

The sample launches Google Chrome and then makes it frontmost. Select the same app in both Actions and choose a shortcut that fits your keyboard setup.

[Website preview and full setup](https://www.rulr.app/rules/launch-app-keyboard-shortcut-mac/) · [Download open-app-with-hotkey.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/open-app-with-hotkey/open-app-with-hotkey.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Create a keyboard shortcut to launch a Mac app

Use this Rule for an app you return to throughout the day, such as a browser or editor. The explicit activation Action brings the target app forward after the launch request.

Moving an app-launch hotkey from Windows? The [AutoHotkey for Mac migration guide](https://www.rulr.app/posts/autohotkey-for-mac/) maps a hotkey followed by `Run` to this launch-and-focus workflow and compares other Mac alternatives.

**When:** Press Option + Space. **Do:** Launch Application, then Make Application Frontmost, both targeting Google Chrome. There is no If Condition, time restriction, or show/hide toggle.

## Configure and try it

1. Import through **Open this Rule in Rulr** and replace Option + Space if it conflicts with an existing shortcut or another Rule.
2. Choose an installed app in Launch Application and select the same app in Make Application Frontmost.
3. Grant Accessibility for the hotkey and frontmost Action.
4. Enable the Rule and test once with the app closed. Switch to another app and test again with the target already running; check that it comes forward.

## Requirements and limits

The sample's components are available without Pro. The target application must be installed and launchable by the current Mac user.

The Rule targets one application. It does not select a particular document, create a new window, or search among open windows. To hide the same app on a second press, use [Toggle App Visibility](https://www.rulr.app/rules/toggle-app-visibility-mac/). To open several apps together with time Conditions, use [Open Work Apps](https://www.rulr.app/rules/open-work-apps-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/launch-app-keyboard-shortcut-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
