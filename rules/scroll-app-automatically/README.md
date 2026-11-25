# Scroll an App Automatically

Automatically scroll a selected Mac application by a configured distance whenever it becomes frontmost.

Choose the application, pointer position, scroll direction, and distance after importing the Rule. The Rule moves the pointer into the target window before scrolling the content beneath it.

[Website preview and full setup](https://www.rulr.app/rules/scroll-app-automatically-mac/) · [Download scroll-app-automatically.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/scroll-app-automatically/scroll-app-automatically.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Scroll when a selected app becomes active

This Rule is a starting point for a reading routine in which switching into an app should move its content down by a fixed amount. It first places the pointer inside the focused window so the scroll targets the area beneath that position.

**When:** The selected application becomes frontmost. **Do:** Move the pointer to the focused window's center, then scroll down by the configured distance. There is no If Condition. The sample selects Safari and uses a distance of 600; review the value in the app for your actual content and scrolling behavior.

## Configure and try it

1. Import with **Open this Rule in Rulr** and select the application in the activation Trigger.
2. Review Move Mouse. Its sample position is 50% across and 50% down the focused window. Choose a position over the content pane you want to scroll.
3. Set the scroll direction and distance, then grant Accessibility access for mouse movement and scrolling.
4. Open a harmless long document in the selected app, switch away, and switch back. Observe which pane scrolls and how far. Repeat with the layouts you normally use.

## Requirements and limits

The mouse and scrolling Actions require Rulr Pro. The app needs a focused window with scrollable content beneath the configured pointer position.

The Rule performs a scroll on activation; it does not continuously auto-scroll, wait until you finish reading, or recognize the end of an article. Every activation can scroll again. Sidebars, overlays, and embedded panes may receive the scroll instead of the main page. For another routine using window-relative pointer positioning, see [Click a Window Position](https://www.rulr.app/rules/click-window-position-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/scroll-app-automatically-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
