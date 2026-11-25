# Dark Mode Keyboard Shortcut for Mac

Set up a keyboard shortcut to turn on Dark Mode on your Mac without opening System Settings. Import this Rulr rule and choose the key combination you want to use.

Launch Application Actions can follow Set System Appearance, extending the shortcut into an evening routine or an app workspace that opens in Dark appearance.

[Website preview and full setup](https://www.rulr.app/rules/mac-dark-mode-keyboard-shortcut/) · [Download turn-on-dark-mode-with-shortcut.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/turn-on-dark-mode-with-shortcut/turn-on-dark-mode-with-shortcut.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Set macOS appearance to Dark

Use this Rule when you want a deliberate keyboard command for Dark appearance. It changes the system setting directly, which is useful before an evening work session or when you want to change appearance without navigating through System Settings.

Press Option + D to set macOS appearance to Dark from the app you are using.

**When:** Press Option + D, or your replacement shortcut. **Do:** Set System Appearance to Dark. There is no If Condition. The configured value is fixed: pressing the shortcut again keeps Dark appearance rather than toggling back to Light.

## Configure and try it

1. Import through **Open this Rule in Rulr** and review Hotkey Pressed. Choose another combination if Option + D is already assigned to a different app or Rule.
2. Review Set System Appearance and confirm that the selected value is Dark. Grant System Events Automation permission when macOS requests it.
3. Grant Accessibility if you need to record a replacement shortcut. Enable the Rule and start with macOS set to Light appearance for a visible first test.
4. Press the shortcut and check both System Settings and an app that follows the system theme. Press it again to confirm that it remains Dark. Restore your preferred appearance manually when finished testing.

## Requirements and limits

The sample's Trigger and Action are available without Pro. System Events Automation access is needed for the appearance change.

This changes the macOS appearance setting, not every application's independent theme preference. Apps with their own fixed Light or Dark setting may look unchanged. It also does not schedule sunset changes, dim the display, enable Night Shift, or create a two-way toggle. For a different keyboard-controlled utility routine, see [Toggle App Visibility](https://www.rulr.app/rules/toggle-app-visibility-mac/).

To connect a hotkey to other system or application tasks, see the [Mac automation examples](https://www.rulr.app/posts/mac-automation/#mac-automation-examples). That guide explains how Triggers and Actions fit together and links to separate Rules for audio output, apps, and files.

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/mac-dark-mode-keyboard-shortcut/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
