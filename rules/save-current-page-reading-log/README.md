# Save Current Page

Save the current Chrome tab URL to a text file on Mac with a keyboard shortcut. Rulr reads the active tab and appends its URL to your chosen log.

The sample uses Option-Space and a file in Downloads. Choose an unused shortcut and a writable log file after importing.

[Website preview and full setup](https://www.rulr.app/rules/save-chrome-url-reading-log-mac/) · [Download save-current-page-reading-log.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/save-current-page-reading-log/save-current-page-reading-log.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## How this Rule works

The hotkey starts Get Current Tab in Google Chrome, then Write to File appends the resulting URL. There is no Condition, page title, or separator configured in the sample.

## Configure and try it

Choose a shortcut and a writable destination file. Allow Accessibility and Automation access to Google Chrome, enable the Rule, open a Chrome page, and press the shortcut. Inspect the file; if you want entries separated by newlines, add a newline to the write content.

## Requirements and limits

Get Current Tab and Write to File require Rulr Pro. This works with Google Chrome, not an arbitrary browser, and saves the URL rather than an offline copy or a formatted citation.

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/save-chrome-url-reading-log-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
