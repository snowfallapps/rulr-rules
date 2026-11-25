# Monitor Workspace

Automatically move one app window to your chosen display when an external monitor connects to your Mac.

The Rule runs when the display layout changes, checks that more than one display is connected, and moves the selected app's last-used window to the target screen. Choose the application and display after importing it.

[Website preview and full setup](https://www.rulr.app/rules/arrange-windows-monitor-mac/) · [Download setup-windows-for-monitor.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/setup-windows-for-monitor/setup-windows-for-monitor.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Move an app window after a display change

This Rule helps place a frequently used application on another screen when your display setup changes. It is useful for a desk routine where connecting an external monitor should move one working window to a preferred display.

**When:** The display layout changes. **If:** The event reports more than one connected display. **Do:** Move the selected application's last-used window to the configured screen. The sample application is Safari and the screen value is `1`; review both on your own Mac rather than assuming that number identifies the monitor you want.

## Configure and try it

1. Import with **Open this Rule in Rulr** and select the application in Move Window to Screen.
2. Choose the intended screen from your connected display setup and review the last-used window selection. Open a window in that app before testing.
3. Grant Accessibility access so Rulr can move application windows. Enable the Rule, then connect your monitor or make a display-layout change.
4. Confirm which window moved and where it landed. Repeat after reconnecting the display, especially if you use several docks or different monitor arrangements.

Use this event-driven Rule for one window's display placement, and [Window Switcher](https://www.rulr.app/rules/mac-window-switcher/) for manually choosing an existing window. The [Display Layout Changed Trigger](https://www.rulr.app/capabilities/#trigger.system.display-layout-changed) exposes the display event; [Move Window to Screen](https://www.rulr.app/capabilities/actions/#action.window.move-to-screen) defines the movement. The [Mac automation guide](https://www.rulr.app/posts/mac-automation/#how-rulr-automates-your-mac) explains why the display-count Condition sits between them.

## Requirements and limits

The display-layout Trigger and window-moving Action require Rulr Pro. The target application must have a movable window, and the selected screen must be available when the Action runs.

The Trigger covers layout changes rather than one particular monitor's connection. A rearrangement can therefore run the Rule again whenever more than one display is present. The sample moves one selected window; it does not resize it, tile every app, or manage Spaces. For choosing among existing windows manually, use [Window Switcher](https://www.rulr.app/rules/mac-window-switcher/).

For built-in tiling and other ways to arrange windows, see the [Mac window manager comparison](https://www.rulr.app/posts/window-manager-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/arrange-windows-monitor-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
