# Close Work Apps

Quit companion apps automatically when a selected Mac app closes. The sample reacts to Safari quitting and asks Notes and TextEdit to quit.

Choose the main app and companion apps after importing. Review any unsaved work before trying the Rule.

[Website preview and full setup](https://www.rulr.app/rules/quit-companion-apps-mac/) · [Download close-companion-apps.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/close-companion-apps/close-companion-apps.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## How this Rule works

When Safari quits, two Quit Application Actions target Notes and TextEdit. There is no Condition, and this does not watch individual windows or determine which documents belong to a project.

## Configure and try it

Choose the main app in the Trigger and replace both companion apps with your own. Save work in those apps, enable the Rule, open them, and quit the main app. Confirm the intended apps receive the quit request.

## Requirements and limits

The Trigger and Actions do not require Pro or declare special permissions. An app can prompt about unsaved documents or otherwise delay quitting; this Rule does not save documents for you.

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/quit-companion-apps-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
