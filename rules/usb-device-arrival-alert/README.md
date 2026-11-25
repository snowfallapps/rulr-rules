# USB Device Alert

Get a notification when a matching USB device connects to your Mac. The Rule checks the reported device name and includes it in the alert.

The sample matches names containing `USB`. Replace this broad substring with a distinctive part of your device name.

[Website preview and full setup](https://www.rulr.app/rules/usb-device-connection-alert-mac/) · [Download usb-device-arrival-alert.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/usb-device-arrival-alert/usb-device-arrival-alert.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## How this Rule works

A USB connection triggers the Rule. A Condition checks whether the reported device name contains `USB`, and Show Notification displays that name with a sound when the condition matches.

## Configure and try it

Edit the name filter and allow Notifications. Enable the Rule, disconnect and reconnect the device, and check the alert. Try a different device to see whether the substring is too broad.

## Requirements and limits

The Trigger and notification Action do not require Pro. Notification settings affect delivery. This matches a name substring rather than a serial number and does not establish that a storage volume has mounted.

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/usb-device-connection-alert-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
