# Encode Selected Text

URL encode selected text on Mac, including LF line breaks as %0A, and copy the result to the clipboard. The Rule reads the selection, transforms it, and copies the encoded text.

The sample uses Option-Space. Choose a shortcut that does not conflict with another app and select text in a supported app before running it.

[Website preview and full setup](https://www.rulr.app/rules/url-encode-selected-text-mac/) · [Download url-encode-selected-text.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/url-encode-selected-text/url-encode-selected-text.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## How this Rule works

When the shortcut is pressed, Get Selected Text feeds Transform Text with URL Encode selected. Set Clipboard then stores the transformed output. There is no Condition, automatic paste, or URL opening step.

## Configure and try it

Choose an unused shortcut, grant Accessibility and Automation access to System Events, then select a short phrase in a supported app. Press the shortcut and paste the clipboard into a text field to check the encoded result.

## Requirements and limits

Transform Text requires Rulr Pro. Selection access depends on the frontmost app and macOS permissions. The Rule replaces the clipboard contents; it does not modify the selected text.

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/url-encode-selected-text-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
