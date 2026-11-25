# Recover a Stuck App

Recover a stuck Mac app with Option + 1: confirm its name, force quit that specific application and reopen it automatically.

The Rule snapshots the frontmost application before showing a confirmation. It keeps Finder, Rulr and Script Editor out of the recovery path and never force quits without confirmation.

[Website preview and full setup](https://www.rulr.app/rules/force-quit-shortcut-mac/) · [Download open-force-quit.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/open-force-quit/open-force-quit.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Recover the app that stopped responding

**When:** Press Option + 1 while the affected app is frontmost. **Do:** Run AppleScript to capture that app, show its name and ask for confirmation. On approval, it force terminates that process, waits up to five seconds for termination and reopens the captured bundle identifier.

This is a recovery sequence, rather than another way to open the system Force Quit chooser. It handles reopening so you do not have to find the app again afterward.

## Configure and try it

1. Import the Rule and review the shortcut and recovery script.
2. Save work before trying it. Focus a disposable app such as a test TextEdit session.
3. Enable the Rule, press Option + 1 and check the application name in the dialog.
4. Choose **Cancel** first; the target should stay open.
5. For an intentional recovery attempt, choose **Force Quit and Reopen**. Verify that the named application closes and reopens.

## Requirements and limits

Run AppleScript does not require Pro. This Rule uses AppKit because Rulr's normal Quit Application Action does not provide force termination or dynamic relaunch.

Force quit can lose unsaved changes. Reopening does not guarantee restored documents, tabs or work. If termination is not observed, the script stops without reopening. Finder, Rulr and Script Editor are excluded.

If the whole Mac or Rulr is unresponsive, use the system recovery controls. For normal cleanup, use [Quit Open Apps](https://www.rulr.app/rules/quit-all-apps-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/force-quit-shortcut-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
