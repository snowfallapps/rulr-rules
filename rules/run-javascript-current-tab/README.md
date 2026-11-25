# Run Tab JavaScript

Run JavaScript in the active Chrome tab on Mac with a keyboard shortcut and display the result. The sample evaluates `document.title`.

Choose an unused shortcut and review the script before running it. The sample targets Google Chrome and uses a 30-second timeout.

[Website preview and full setup](https://www.rulr.app/rules/run-javascript-chrome-tab-mac/) · [Download run-javascript-current-tab.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/run-javascript-current-tab/run-javascript-current-tab.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## How this Rule works

The hotkey runs the configured JavaScript in the current Chrome tab. Show Text or Image receives the result and displays it. There is no Condition and no automatic handling for other browsers.

## Configure and try it

Choose a shortcut, grant Accessibility and Automation access to Google Chrome, and review the JavaScript. Open a suitable Chrome tab, press the shortcut, and compare the displayed result with the page title. Chrome may require JavaScript from Apple Events to be enabled.

## Requirements and limits

Run JavaScript in Chrome requires Rulr Pro. Browser settings and the current page can affect execution. Only run scripts you understand; scripts may change the current page.

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/run-javascript-chrome-tab-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
