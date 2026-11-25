# Media Manager

Open a Mac media control panel with Option + M. See detected music and video sources, select a player, and press Space to play or pause when control is available.

The Rule connects Hotkey Pressed to Show Media Manager with no Conditions or Action parameters. Replace the shortcut to suit your keyboard; source discovery and playback control depend on the app, browser, and permissions.

[Website preview and full setup](https://www.rulr.app/rules/control-media-playback-mac/) · [Download media-manager.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/media-manager/media-manager.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Choose which media source to control

When music, videos, and browser tabs are spread across your Mac, opening each player to pause or resume it interrupts what you are doing. This Rule opens Rulr's Media Manager so you can choose a detected source and use the panel's play/pause control.

The panel shows available titles alongside app names. Supported browser media pages appear as separate entries. Sources remembered after playback can remain in the list when paused, so you can return to them without starting playback again first.

**When:** Press Option + M. **If:** No Condition. **Do:** Show Media Manager. Opening the panel does not itself pause or resume anything. Click a row or use Up and Down to select it, press Space to request play/pause, and press Escape to dismiss the panel.

## Configure and try it

1. Choose **Open this Rule in Rulr** on a Mac running macOS 26 or later. Review the imported Rule, which starts disabled.
2. Keep Option + M or choose an unused shortcut in Hotkey Pressed. Show Media Manager has no parameters to configure.
3. Allow Accessibility for the hotkey, then enable the Rule. Start a song or video in an app or Chrome tab you use regularly.
4. Open the panel while the song or video is actually playing, and wait for its source to appear before pausing it. Select that source. If the panel requests access for playback, follow its permission guidance. Press Space and check that the selected player actually pauses; press it again to check resuming.
5. Try a second source and repeat with both players open. Confirm the behavior for your own apps before relying on the Rule during work or calls.

For Chrome tab discovery and control, allow Rulr to automate Google Chrome and enable **View → Developer → Allow JavaScript from Apple Events** in Chrome. Safari tab discovery also requires its Automation and JavaScript permissions, but Safari playback control is currently unavailable. Native playback may require Accessibility; controlling individual QuickTime movies can require QuickTime Player Automation access.

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/control-media-playback-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
