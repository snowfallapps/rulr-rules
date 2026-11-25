# Move Window to Left Half

Move and resize the focused window to the left half of your Mac screen with a keyboard shortcut. Use this Rule when you want a simple, repeatable window layout.

The Rule uses Set Window Layout with Focused Window and the left-half preset. Change the shortcut or choose another layout after importing.

[Website preview and full setup](https://www.rulr.app/rules/snap-window-left-mac/) · [Download snap-window-left.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/snap-window-left/snap-window-left.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Arrange the focused window

Replacing an AutoHotkey `WinMove` shortcut? The [AutoHotkey for Mac guide](https://www.rulr.app/posts/autohotkey-for-mac/) explains how to rebuild window hotkeys and what to change when selecting Mac windows and screens.

**When:** Press Option + Left Arrow. **Do:** Set Window Layout for the focused window using the left-half preset. There is no If Condition.

## Configure and try it

1. Import the Rule and review its Option + Left Arrow shortcut. Choose an unused combination if it conflicts with another app.
2. Grant Accessibility access to Rulr and enable the Rule.
3. Focus a window in another app, then press the shortcut. The window moves and resizes to the left half of its current screen's visible area.
4. To use a different arrangement, choose another preset in Set Window Layout.

## Requirements and limits

This Rule requires a Rulr version with Set Window Layout and Accessibility access. The target app must expose a window that can be moved and resized. Some windows may not support the requested dimensions, and full-screen windows are not supported.

The Rule snaps the focused window to the left half when the shortcut is pressed. It does not continuously arrange other windows, provide drag-to-snap controls, or restore a saved workspace. For a comparison of these approaches, see the [Mac window manager guide](https://www.rulr.app/posts/window-manager-mac/).

For a presentation on another monitor, [Present New Video Windows](https://www.rulr.app/rules/full-screen-keyboard-shortcut-mac/) reacts to new windows from your selected video app, moving each event's window to your configured display before toggling full screen.

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/snap-window-left-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
