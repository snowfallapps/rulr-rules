# Offline Alert

Get an audible alert when your Mac reports a network disconnection. The Rule shows a notification and speaks a short message.

The sample notification says the Rule ran successfully and the spoken message is `Offline Alert`. Edit them to suit your needs.

[Website preview and full setup](https://www.rulr.app/rules/network-disconnection-alert-mac/) · [Download warn-when-offline.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/warn-when-offline/warn-when-offline.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## How this Rule works

A Network Disconnected Trigger runs Show Notification with sound and Speak Text. There is no Condition or connectivity test against a specific website.

## Configure and try it

Edit the notification and spoken message, allow Notifications, and enable the Rule. Test by disconnecting the network and listening for the alert; reconnect afterward.

## Requirements and limits

Speak Text requires Rulr Pro. The Trigger reports a network disconnection; it does not diagnose an internet outage or verify that a remote service is reachable.

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/network-disconnection-alert-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
