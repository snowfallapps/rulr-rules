# Low Battery Alert

Show a notification and speak a warning when your Mac battery falls to or below a configured threshold, so you can notice low power while working.

When the battery level reaches the configured threshold, the Rule shows a notification and speaks the warning aloud. Adjust the threshold and notification behavior to fit how you work away from power.

[Website preview and full setup](https://www.rulr.app/rules/low-battery-alert-mac/) · [Download low-battery-warning.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/low-battery-warning/low-battery-warning.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Add a spoken low-battery reminder

This Rule combines a visual notification with a spoken message when your Mac battery reaches a low level. It is useful when you work away from power and want an additional reminder that does not depend only on noticing the battery icon.

**When:** The battery level falls to or below 20%. **Do:** Show a notification and speak the configured text. There is no If Condition. The sample notification title and spoken message say `Low Battery Alert`; replace the generic notification content with instructions useful to you.

## Configure and try it

1. Import using **Open this Rule in Rulr** and review the threshold in Battery Level Changed. Choose a level that leaves enough time for your normal next step.
2. Edit the notification title, body, and sound setting. Review the Speak Text content separately so the spoken warning says what you intend.
3. Allow Notifications for Rulr and make sure your audio output and volume let you hear the speech.
4. Test the notification and speech Actions before relying on the battery event. To observe the full flow, use a suitable threshold and let the battery cross it while Rulr is running.

## Requirements and limits

Speak Text requires Rulr Pro. The Mac must expose battery-level information. System notification visibility also depends on macOS notification settings and whether Rulr is frontmost.

The Trigger represents a threshold crossing rather than a repeating alarm every minute while the battery remains low. The Rule does not plug in power, save documents, enable Low Power Mode, or shut the Mac down. For a separate routine when you step away, see [Mute and Close Private Apps When Idle](https://www.rulr.app/rules/mute-close-apps-mac-idle/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/low-battery-alert-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
