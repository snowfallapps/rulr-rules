# Window Switcher

Switch between open windows on Mac with a visual window picker. Press Option + Tab, choose the window you need, and bring it into focus with Rulr.

The sample opens a horizontal picker with no apps excluded. Choose your shortcut, layout, and app exclusions after importing to keep the list focused on the windows you use.

[Website preview and full setup](https://www.rulr.app/rules/mac-window-switcher/) · [Download window-switcher.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/window-switcher/window-switcher.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Switch between Mac windows with a visual picker

Use this Rule when several applications have multiple windows and cycling through apps is slower than choosing the exact window you need. The shortcut opens Rulr's interactive window switcher, where you select a window to bring it into focus.

Unlike switching between applications, the picker lets you choose a specific window exposed by an app. It is useful when the app you need has several windows open.

To choose between this Rule and a dedicated switching app, compare [Mac window switchers and AltTab alternatives](https://www.rulr.app/posts/mac-window-switchers/). The guide covers window previews, search, and browser-tab navigation so you can choose the features you need before importing.

**When:** Press Option + Tab, or your replacement shortcut. **Do:** Show Window Switcher. There is no If Condition. The sample uses a horizontal layout and an empty application-exclusion list, so it starts without a custom filter for your work apps.

## Configure and try it

1. Import using **Open this Rule in Rulr** and review Hotkey Pressed. Choose an unused combination if Option + Tab belongs to another window tool.
2. Review the switcher layout and excluded applications. Add exclusions if windows from a particular app should stay out of the picker.
3. Grant Accessibility access so Rulr can work with application windows and focus the selection. Keep a few ordinary windows open in different apps for your first trial.
4. Press the shortcut, choose a window, and verify that the intended window becomes active. Repeat with another app and check how exclusions affect the available choices.

Choose the switcher when you want to decide which window becomes active. To move a particular application's window after a monitor change, use [Monitor Workspace](https://www.rulr.app/rules/arrange-windows-monitor-mac/) instead. Review [Show Window Switcher](https://www.rulr.app/capabilities/actions/#action.window.show-window-switcher) for its settings, or read the [Mac automation guide](https://www.rulr.app/posts/mac-automation/) before connecting window Actions to other events.

## Requirements and limits

The sample's Trigger and Action are available without Pro. Accessibility is required for the switcher, not only for recording the hotkey.

The picker works with windows exposed by applications; it is not a browser tab search, document-content search, or saved-session restore tool. Application-specific window behavior can affect which entries are available. For navigating individual Chrome tabs rather than application windows, use [Search Chrome Windows and Tabs](https://www.rulr.app/rules/search-chrome-windows-tabs/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/mac-window-switcher/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
