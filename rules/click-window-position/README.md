# Click a Window Position

Automatically move the pointer and click a configured position when a selected application window opens on your Mac.

Choose the application, window-relative position, mouse button, and click type after importing the Rule. Coordinate-based clicks can break when the window layout or application interface changes.

[Website preview and full setup](https://www.rulr.app/rules/click-window-position-mac/) · [Download click-window-position.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/click-window-position/click-window-position.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Click a position in a newly created window

Use this Rule for an application window whose useful control appears in a stable position. It moves the pointer relative to the window reported by the Trigger and performs a click there, reducing a repeated manual pointer movement.

**When:** The selected application creates a window. **If:** The event's application matches the configured app. **Do:** Move the pointer to the selected window-relative position, then click the current pointer location. The sample uses Safari, a 50% horizontal and 50% vertical position, and a single left click without modifiers.

## Configure and try it

1. Import with **Open this Rule in Rulr** and select the application in both the Trigger and application Condition.
2. Review Move Mouse. Keep its window source connected to the Trigger's Window Variable, then choose the percentage or coordinate position for your intended control.
3. Review the mouse button, click type, and modifiers in Click Mouse. Grant Accessibility access for window events and mouse control.
4. Test by opening a disposable window with a harmless target. Watch the pointer movement and resulting click before enabling the routine for normal work.

Before adapting this sample, compare its [Window Created Trigger](https://www.rulr.app/capabilities/#trigger.application-window.window-created) and [Input Actions](https://www.rulr.app/capabilities/actions/#actions-category-input) with the control you intend to click. If you ask AI Builder to change the target, follow the [review and testing walkthrough](https://www.rulr.app/posts/build-mac-automations-with-ai/) and recheck the coordinates in the actual application; a generated change does not establish that the control is ready.

## Requirements and limits

The window-created Trigger and mouse Actions require Rulr Pro. Window detection depends on the application exposing a standard accessible window.

A coordinate points to a location, not a named button. Different window sizes, toolbars, loading states, or interface changes can place another control under it. The sample has no delay or readiness check before clicking. Recheck the target after app updates. For sending an application's keyboard shortcut after launch, see [Press Keys When an App Launches](https://www.rulr.app/rules/press-keys-app-launch-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/click-window-position-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
