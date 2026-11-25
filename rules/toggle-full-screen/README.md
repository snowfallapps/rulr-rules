# Present New Video Windows

Automatically move new QuickTime Player windows to your presentation display on Mac, then request full screen. Open the video normally; there is no extra Rule shortcut to press.

Choose the video application in Window Created and your monitor in Move Window to Screen. Both Actions target the window supplied by the creation event, rather than whichever app later becomes focused.

[Website preview and full setup](https://www.rulr.app/rules/full-screen-keyboard-shortcut-mac/) · [Download toggle-full-screen.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/toggle-full-screen/toggle-full-screen.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Open the video on your presentation screen

**When:** A window is created by QuickTime Player. **Do:** Move Window to Screen moves that event's window to your chosen display, then Toggle Full Screen requests a full-screen transition. There is no script.

Use this when opening a video for a projector or second monitor. The system full-screen keyboard shortcut changes a focused window manually; this Rule reacts to the selected application's new windows.

## Configure and try it

1. Import the Rule and choose the video app in Window Created.
2. Select the actual presentation monitor in Move Window to Screen.
3. Keep both window targets connected to the Window Created output.
4. Allow Accessibility, enable the Rule and open a disposable video in a new normal window.
5. Confirm that this window moves to the chosen monitor and enters full screen. Create another window while a different app is focused to check the target.

## Requirements and limits

Window Created and Move Window to Screen require Pro; Toggle Full Screen does not. Allow Accessibility.

Every window-creation event reported for the chosen app can trigger the Rule, including non-document windows the app exposes. A missing display or unsupported window can stop the flow.

The move step rejects windows already in full screen, and the final Action toggles state rather than setting an unconditional on state. Avoid combining this Rule with another app feature that automatically makes the same window full screen.

For a manual layout on the current Desktop, see [Move Window to Left Half](https://www.rulr.app/rules/snap-window-left-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/full-screen-keyboard-shortcut-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
