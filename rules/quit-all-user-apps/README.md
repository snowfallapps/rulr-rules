# Quit Open Apps

Quit open apps together on Mac with a keyboard shortcut and a confirmation. Option + 8 lists eligible apps and requests normal quit after you approve, keeping Finder, Rulr and Script Editor open.

Change Hotkey Pressed to an unused combination and review the script's exclusions. Apps can ask you to save documents or decline to quit; the Rule does not force termination.

[Website preview and full setup](https://www.rulr.app/rules/quit-all-apps-mac/) · [Download quit-all-user-apps.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/quit-all-user-apps/quit-all-user-apps.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## How to quit all open apps on Mac together

At the end of a work session, save your documents and use one shortcut to review the apps you want to close. You do not need to quit a particular application first.

**When:** Press Option + 8. **Do:** Run AppleScript takes a snapshot of regular GUI apps and presents their names. Choosing **Quit Apps** requests normal termination for the listed apps. Cancel is the default choice.

Finder, Rulr and Script Editor stay open. The batch covers eligible open apps, rather than every process on the Mac, and each app can show its own save dialog.

## Configure and try it

1. Import the disabled Rule and review Option + 8. Choose an unused combination if needed.
2. Review the script's excluded application bundle identifiers and save your work before trying the flow.
3. Allow Accessibility access for the hotkey and enable the Rule.
4. Press the shortcut, review the app list and choose **Cancel** first; those apps should stay open.
5. For a deliberate trial, open disposable apps without unsaved work, press the shortcut again and confirm.
6. Answer any save dialogs and check which apps remain. An app that declines or delays quitting can stay open.

To run this at a session boundary instead, replace Hotkey Pressed with Application Quits and choose your main work app. Any reported quit of that app, including an unexpected exit, can then trigger the confirmation. The downloadable sample uses the manual shortcut.

## Requirements and limits

Hotkey Pressed and Run AppleScript do not require Pro. Accessibility access is needed for the shortcut. No apps are force killed.

The app list is captured before confirmation. Check it before approving: it includes regular GUI apps rather than an inferred project membership.

Finder, Rulr and Script Editor are excluded. Menu-bar-only utilities, background agents and apps launched after the snapshot are not included. An accepted quit request does not guarantee completed termination; apps can display save dialogs or decline.

For a stuck app that needs force termination and reopening, use [Recover a Stuck App](https://www.rulr.app/rules/force-quit-shortcut-mac/). To close selected companion tools after a particular app exits, see [Close Work Apps](https://www.rulr.app/rules/quit-companion-apps-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/quit-all-apps-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
