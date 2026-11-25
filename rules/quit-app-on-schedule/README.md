# Quit an App on a Schedule

Automatically quit a selected Mac application at a scheduled time, such as closing a work, communication, or entertainment app at the end of the day.

Choose the application and schedule after importing the Rule. The Rule checks that the app is running before asking it to quit normally.

[Website preview and full setup](https://www.rulr.app/rules/quit-app-on-schedule-mac/) · [Download quit-app-on-schedule.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/quit-app-on-schedule/quit-app-on-schedule.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Ask an app to quit at a chosen time

This Rule is useful for a repeatable end-of-session reminder expressed as an application action. It checks whether the selected app is running and requests a normal quit at the scheduled time, rather than requiring you to remember the same cleanup step each day.

**When:** The weekly schedule fires. **If:** Safari is running. **Do:** Quit Safari. The sample schedule is 09:00 on weekdays, so change it if you intend to close an app at the end of the day. The Condition and Quit Application Action must refer to the same intended application.

## Configure and try it

1. Import with **Open this Rule in Rulr** and select your days and time in the schedule Trigger.
2. Choose the target app in both the Running Applications Condition and Quit Application Action. Do not change only one of those fields.
3. Open the app with disposable work and set a temporary schedule a few minutes ahead while Rulr is running and the Mac is awake.
4. Observe the quit request, including any unsaved-document dialog. Test once with the app already closed to check the Condition, then restore the final schedule.

## Requirements and limits

The sample's components are available without Pro and declare no special permission. The app must be installed, and Rulr must be available to handle the schedule.

Normal quit can prompt for unsaved work or be delayed by an application. The Rule does not force termination, save every document, prevent relaunching, or enforce an app usage limit. For an inactivity-based routine instead of a fixed time, see [Mute and Close Apps When Idle](https://www.rulr.app/rules/mute-close-apps-mac-idle/).

To close several apps together, [Quit Open Apps](https://www.rulr.app/rules/quit-all-apps-mac/) uses a keyboard shortcut to list open apps and ask for confirmation before requesting normal quit. For an unresponsive frontmost app, [Recover a Stuck App](https://www.rulr.app/rules/force-quit-shortcut-mac/) asks for confirmation before force quitting and reopening that app.

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/quit-app-on-schedule-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
