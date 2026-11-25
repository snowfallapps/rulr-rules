# Focus Session

Start a focus timer on Mac with a keyboard shortcut. Confirm, close distracting apps, open your work folder, and get a reminder after your chosen work block.

The sample uses a 50-minute delay after opening Documents and TextEdit. Choose which apps to quit, your working folder, and the session length before enabling it.

[Website preview and full setup](https://www.rulr.app/rules/focus-session-timer-mac/) · [Download focus-session.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/focus-session/focus-session.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Start a focus timer and prepare your Mac workspace

Use this Rule to combine the setup and ending reminder for a focused writing or study period. A confirmation dialog comes before the app-closing Actions, so you can cancel without starting the session.

**When:** Press Option + F. **Do:** Ask for confirmation, quit Messages and Mail, open `~/Documents`, launch TextEdit, delay for 50 minutes, and show a completion notification with sound. There is no If Condition and no repeating work/break cycle.

## Configure and try it

1. Import using **Open this Rule in Rulr** and choose the shortcut. Review both Quit Application Actions before running the sample.
2. Select your work folder and writing or study app. Save work in apps you intend to close.
3. Adjust the Delay duration and update the confirmation text to match. Allow Accessibility for the hotkey and Notifications for the reminder.
4. Temporarily use a short delay to try the sequence. Check cancellation first, then confirm a session and inspect the setup and final notification. Restore your intended duration afterward.

## Requirements and limits

The sample's components are available without Pro. Rulr must keep running for the delayed notification, whose visibility and sound also depend on macOS settings.

This Rule quits the selected apps once; it does not block them from reopening, enable macOS Focus, or display a live countdown. It does not reopen the closed apps when the session ends. For closing an app at a fixed clock time, see [Quit an App on a Schedule](https://www.rulr.app/rules/quit-app-on-schedule-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/focus-session-timer-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
