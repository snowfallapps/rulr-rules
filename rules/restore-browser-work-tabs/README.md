# Restore Work Tabs

Start a work session on your Mac with one keyboard shortcut that activates Google Chrome and opens your configured work or research URLs in new tabs.

The Rule activates Google Chrome and opens each saved URL in a new tab. Choose the shortcut and tab URLs that make up your work or research workspace; this opens configured tabs rather than restoring a previous browser session.

[Website preview and full setup](https://www.rulr.app/rules/open-chrome-work-tabs-mac/) · [Download restore-browser-work-tabs.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/restore-browser-work-tabs/restore-browser-work-tabs.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Open a repeatable set of work pages

Use this Rule when the same two or more websites begin a work session. A single shortcut brings Chrome forward and opens the configured URLs, letting you start from a known set of destinations rather than finding bookmarks individually.

**When:** Press the chosen hotkey, initially Option + Space. **Do:** Activate Google Chrome and run two Open New Tab Actions. There is no If Condition. Both sample URLs are Google, so replace each one with a different work page if you want a useful workspace.

## Configure and try it

1. Import with **Open this Rule in Rulr** and choose a shortcut that does not conflict with your launcher or another Rule.
2. Edit each Open New Tab URL. Add or remove tab Actions to match the pages you need, keeping their order easy to understand.
3. Allow Accessibility access for application activation and Automation access for Google Chrome. Chrome must be installed on the Mac where you use the Rule.
4. Run the shortcut and verify that each configured address opens. Run it again deliberately to see how repeated invocations affect your tab list.

Keep this Rule when you want the same addresses on every run. If morning research and afternoon writing need different pages, start with [Chrome Research Workspace](https://www.rulr.app/rules/chrome-research-workspace/) instead. The [AI Builder guide](https://www.rulr.app/posts/build-mac-automations-with-ai/) shows how to request and review Conditions; check the [Chrome Actions](https://www.rulr.app/capabilities/actions/#action.integration.chrome.open-new-window) before adding browser operations.

## Requirements and limits

The sample's components are available without Pro. Opening pages can still require network access and an existing login in Chrome; the Rule does not sign in to services for you.

Each run creates new tabs. It does not deduplicate existing tabs, restore a saved session, recover closed windows, or reproduce a previous layout. If you mainly need to find an already open page, use [Search Chrome Windows and Tabs](https://www.rulr.app/rules/search-chrome-windows-tabs/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/open-chrome-work-tabs-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
