# Research Capture

Save copied text to a research notes file on Mac whenever the clipboard changes. Rulr trims the text, adds a timestamp, and appends it to the file.

The sample monitors clipboard changes continuously and writes to `~/Documents/Research Notes.txt`. Select a writable file and enable it only when you want this collection behavior.

[Website preview and full setup](https://www.rulr.app/rules/save-clipboard-research-notes-mac/) · [Download research-capture.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/research-capture/research-capture.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## How this Rule works

A Clipboard Changed Trigger supplies its text to Transform Text, which trims it. Write to File appends a bullet, the result, the current date and time, and a newline; a notification follows. There is no Condition to filter sensitive or unrelated copies.

## Configure and try it

Choose a writable notes file and allow Notifications if you want feedback. Enable the Rule, copy a harmless test phrase with surrounding spaces, and inspect the appended entry. Disable it when you do not want clipboard changes logged.

## Requirements and limits

Clipboard Changed, Transform Text, and Write to File require Rulr Pro. The Rule does not capture a page URL or citation. Clipboard contents can include private information, so use a suitable destination and disable the Rule when appropriate.

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/save-clipboard-research-notes-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
