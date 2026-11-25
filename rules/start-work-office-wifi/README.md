# Office Work Mode

Open apps and websites automatically when your Mac joins a chosen Wi-Fi network. Set morning and afternoon app groups for your office or home work routine.

Set your network name, apps, URLs, and working hours after importing. The sample checks the connected SSID, then opens the tools for the matching time window.

[Website preview and full setup](https://www.rulr.app/rules/open-apps-wifi-mac/) · [Download start-work-office-wifi.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/start-work-office-wifi/start-work-office-wifi.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Launch work apps when you connect to a Wi-Fi network

This Rule combines a network event with two time-based branches. It is useful when arriving at a workplace means opening a predictable set of apps, and your morning and afternoon routines differ.

**When:** A network connects. **If:** Its SSID equals `Office`. From 08:00 inclusive to 12:00 exclusive, **Do:** Launch Slack and Notion, then open Google Calendar in Safari. From 13:00 inclusive to 18:00 exclusive, launch Slack and Figma, then open Notion's website in Safari. Each time window uses AND Conditions.

## Configure and try it

1. Import with **Open this Rule in Rulr** and replace `Office` with your Wi-Fi network's SSID.
2. Choose installed apps and the public or personal work URLs you intend to open. Review both branches separately.
3. Adjust the time boundaries for your local routine. There is no weekday Condition in this sample.
4. Enable the Rule and reconnect to the chosen network during a matching time window. Check the expected apps and pages; try a different network to check the SSID filter.

## Requirements and limits

The sample's components are available without Pro and declare no special permission. Websites still require any normal sign-in.

The network event must provide an SSID matching the Condition. Joining another network or connecting outside both windows launches nothing. Crossing 08:00 or 13:00 while already connected does not itself trigger the Rule. Reconnecting may launch the tools again. For a time-driven routine, see [Launch Apps at a Scheduled Time](https://www.rulr.app/rules/launch-apps-at-time-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/open-apps-wifi-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
