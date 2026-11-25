# Microphone Change Alert

Get a Mac microphone change notification showing the new default input's name. Notice audio input switches while connecting a headset or recording equipment.

The Rule listens for Audio Input Device Changed and inserts the new device name into its notification. Customize the title, message, or sound after importing to suit your recording or meeting setup.

[Website preview and full setup](https://www.rulr.app/rules/microphone-change-alert-mac/) · [Download show-microphone-change.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/show-microphone-change/show-microphone-change.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Get notified when your Mac's default microphone changes

Use this Rule when connecting a headset or audio interface may change the Mac's default microphone. The notification gives you a visible cue to check the input before continuing a call or recording.

**When:** The audio input device changes. **Do:** Show a notification titled `Microphone Change Alert` with `Microphone changed to:` followed by the event's Device Name. Sound is enabled. There is no If Condition limiting notifications to a particular microphone.

## Configure and try it

1. Import with **Open this Rule in Rulr** and review the notification text. Preserve the Device Name Variable if you want to see which input was reported.
2. Choose whether the notification should play a sound, especially if you use the Rule while recording.
3. Allow Notifications for Rulr and enable the Rule.
4. Change the system's default audio input between two available devices and check the reported name. Repeat in the opposite direction to confirm both changes are visible.

## Requirements and limits

The sample's components are available without Pro. The Trigger declares no microphone recording permission; it observes the input-device change rather than recording audio. Notification visibility depends on macOS settings.

The Rule does not select a microphone, measure input levels, or change a meeting app's own input setting. An app that explicitly selects another microphone may differ from the system default. For output-device control, see [Switch Audio Output](https://www.rulr.app/rules/switch-audio-output-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/microphone-change-alert-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
