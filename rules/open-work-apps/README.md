# Open Work Apps

Open your work apps with one Mac keyboard shortcut during your chosen work hours, so Slack, Notion, Figma, or another app set is ready together.

Different Launch Application Actions and Conditions can turn the same shortcut into a meeting starter, study setup, design workspace, or another repeatable app-launch routine. To build your own routine through conversation, follow [How to Build Mac Automations with AI](https://www.rulr.app/posts/build-mac-automations-with-ai/).

[Website preview and full setup](https://www.rulr.app/rules/open-work-apps-mac/) · [Download open-work-apps.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/open-work-apps/open-work-apps.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Launch your chosen app set from one shortcut

This Rule brings a group of work applications into a single keyboard routine. It is useful when beginning a writing, design, or team session that consistently needs several apps, while allowing time Conditions to restrict when the shortcut performs the launches.

**When:** Press Option + W. **If:** The current time is before 12:00 or at or after 13:00. **Do:** Launch Slack, Notion, and Figma. The sample uses an OR match, so either time Condition allows the launches. It excludes the noon hour but does not restrict the Rule to weekdays or impose an evening end time.

## Configure and try it

1. Import with **Open this Rule in Rulr** and review the hotkey. Grant Accessibility if you need to record a different shortcut.
2. Select the applications installed on your Mac in each Launch Application Action. Remove apps you do not need or add further launch Actions for your own workspace.
3. Review both time Conditions and their match mode. Choose explicit boundaries and the appropriate AND or OR logic if your intended working hours differ from the sample.
4. Enable the Rule and test at an allowed time. Check that each application launches, then test the excluded interval by temporarily adjusting the Conditions and restoring them afterward.

## Requirements and limits

The sample's Trigger and Actions are available without Pro. Each selected app must be installed and available to the Mac user running Rulr.

Launching an app does not automatically log in, open a particular project, or restore window positions. This is a hotkey routine rather than a schedule. For a weekday launch time, see [Launch Apps at a Scheduled Time](https://www.rulr.app/rules/launch-apps-at-time-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/open-work-apps-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
