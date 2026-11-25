# Chrome Research Workspace

Open a Chrome research workspace with a keyboard shortcut, then load different research or writing tabs automatically based on the time of day.

The time-based branches can open different source URLs or lead into more Actions, extending the Rule into a writing setup, project launcher, or daily reading routine.

[Website preview and full setup](https://www.rulr.app/rules/chrome-research-workspace/) · [Download browser-research-flow.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/browser-research-flow/browser-research-flow.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Choose research tabs by session time

This Rule opens different Chrome pages for research and writing sessions. It demonstrates time Conditions after a keyboard Trigger, so the same shortcut can lead to different destinations without maintaining separate shortcuts for every session.

**When:** The configured hotkey is pressed. **Do:** Activate Chrome. **If:** The current time falls within 08:00–12:00, open Google Scholar and Notion; within 13:00–18:00, open Google Docs and Drive. Each matching branch also shows its session notification. Outside both intervals, Chrome is activated but neither tab group opens.

## Configure and try it

1. Import through **Open this Rule in Rulr**. Review and record the intended shortcut in the app before relying on the sample's displayed key label.
2. Adjust both start and end Conditions in each branch. Keep the paired Conditions together so each branch describes a time interval.
3. Replace the example URLs and notification text with your research and writing destinations. Allow Accessibility for Chrome activation, Automation for Chrome tabs, and Notifications for system alerts.
4. Test during a matching interval, or temporarily adjust its boundaries to include the current time. Confirm that only the intended group opens, then restore your preferred hours.

The time Conditions choose a tab group after you press the shortcut; they do not start a session at a scheduled hour. Compare [Open Chrome Work Tabs](https://www.rulr.app/rules/open-chrome-work-tabs-mac/) if every session should open the same URLs. See [Variables](https://www.rulr.app/capabilities/variables/) for current-time checks and the [AI Builder refinement walkthrough](https://www.rulr.app/posts/build-mac-automations-with-ai/#4-refine-the-rule-through-conversation) for reviewing a change to allowed hours.

## Requirements and limits

The sample's Trigger and Actions do not require Pro. Notifications are shown when Rulr is not frontmost and may also be affected by macOS notification settings.

This is a manually triggered workspace, not a scheduled launcher. Repeating the shortcut opens additional tabs. It does not restore a previous browser session or identify research pages automatically. For a fixed set without time branches, use [Open Chrome Work Tabs](https://www.rulr.app/rules/open-chrome-work-tabs-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/chrome-research-workspace/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
