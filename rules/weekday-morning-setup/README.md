# Morning Work Setup

Launch selected Mac apps automatically at a scheduled weekday time, with an optional web page and notification for a repeatable morning setup.

The Rule runs on its weekly schedule, launches the configured application, opens the configured URL in Safari, and shows a notification. Choose the schedule, app, and URL before enabling it.

[Website preview and full setup](https://www.rulr.app/rules/launch-apps-at-time-mac/) · [Download weekday-morning-setup.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/weekday-morning-setup/weekday-morning-setup.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Start a weekday workspace on a schedule

Use this Rule when your work session usually begins at a predictable time. It launches an application, opens a webpage, and posts a notification, providing a small scheduled starting routine that you can adapt to your own apps and destinations.

**When:** The weekly schedule reaches 09:00 on weekdays. **Do:** Launch Safari, open Google in Safari, and show the configured notification. There is no If Condition. The webpage and notification are included Actions in the sample; remove them explicitly if you only want an application launch.

## Configure and try it

1. Import through **Open this Rule in Rulr** and choose the days and time in the schedule Trigger. Review the displayed schedule on the Mac where it will run.
2. Select your application in Launch Application. Review the URL and application selected in Open URL separately; changing the launch app does not automatically change the browser Action.
3. Edit the notification text and sound, or remove the notification if it is unnecessary. Allow Notifications for Rulr if you retain it.
4. Set a temporary schedule a few minutes ahead while the Mac is awake and Rulr is running. Confirm the app, webpage, and notification, then restore your regular time.

## Requirements and limits

The sample's components are available without Pro. Selected apps must be installed, and the webpage may require network access or a login. System alerts also depend on macOS notification settings.

This routine does not wake a powered-off Mac, authenticate to work services, or restore a saved project. Keep Rulr available at the scheduled time and test your own sleep and wake routine. For manually starting an app group, see [Open Work Apps](https://www.rulr.app/rules/open-work-apps-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/launch-apps-at-time-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
