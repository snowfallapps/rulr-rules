# Confirm Before Shutdown

Use a keyboard shortcut to request shutdown on Mac with a confirmation dialog first. Cancelling the dialog stops the Rule before the shutdown Action.

The sample uses Option-Space and a generic confirmation message. Choose an unused shortcut and make the message explicit before enabling it.

[Website preview and full setup](https://www.rulr.app/rules/confirm-shutdown-keyboard-shortcut-mac/) · [Download safe-shutdown-hotkey.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/safe-shutdown-hotkey/safe-shutdown-hotkey.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## How this Rule works

When the shortcut is pressed, Show Confirmation displays a dialog. If it is cancelled, the Rule stops; otherwise Shut Down Computer runs. There is no Condition.

## Configure and try it

Choose an unused shortcut and change the dialog to clearly say it will shut down the Mac. Enable the Rule, press the shortcut, and test Cancel first. Save your work before testing confirmation.

## Requirements and limits

Show Confirmation requires Rulr Pro; the shortcut requires Accessibility. Confirming requests a real shutdown, and open apps or unsaved documents may affect the shutdown process.

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/confirm-shutdown-keyboard-shortcut-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
