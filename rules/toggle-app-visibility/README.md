# Toggle App Visibility

Use one keyboard shortcut to show or hide a selected running app on your Mac, keeping its windows available without quitting the app or closing documents.

Choose the application and hotkey after importing the Rule. The Action changes visibility without quitting the app or closing its windows.

[Website preview and full setup](https://www.rulr.app/rules/toggle-app-visibility-mac/) · [Download toggle-app-visibility.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/toggle-app-visibility/toggle-app-visibility.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Show or hide one app with the same shortcut

This Rule gives a frequently used application its own visibility shortcut. It is useful for keeping a reference browser or utility available when needed, then moving its windows out of view without quitting the app.

**When:** Press the configured hotkey, initially Option + Space. **Do:** Toggle the selected application's visibility. There is no If Condition. The sample targets Safari: a visible application is hidden, while a hidden application is shown.

## Configure and try it

1. Import with **Open this Rule in Rulr** and select the application in Toggle Application Visibility. Choose an app installed on your Mac rather than leaving Safari unless that is your intended target.
2. Review the hotkey and assign a unique combination. Several Gallery samples use Option + Space, so change it when combining them.
3. Grant Accessibility if you need to record the replacement shortcut. Launch the target application and open an ordinary window before testing.
4. Press the shortcut and check that the app hides. Press it again and verify that it reappears with its existing work. Try the routine from another frontmost app as well.

## Requirements and limits

Toggle Application Visibility requires Rulr Pro. The Action itself declares no additional special permission, though recording a shortcut uses Accessibility access.

Hiding is an application visibility change. It does not close documents, quit the app, silence its audio, or prevent notifications. The sample also has no separate Launch Application Action; test with a running app rather than treating this as a launcher. For choosing among several open application windows, use [Window Switcher](https://www.rulr.app/rules/mac-window-switcher/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/toggle-app-visibility-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
