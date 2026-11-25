# Translate Clipboard

Translate clipboard text automatically on Mac whenever you copy a passage. Choose the target language and see the translation without a separate hotkey.

Clipboard Changed passes the copied text to Translate Text, which targets English in the sample. Change the target language after importing and enable the Rule when you want clipboard-driven translation.

[Website preview and full setup](https://www.rulr.app/rules/translate-clipboard-mac/) · [Download translate-clipboard.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/translate-clipboard/translate-clipboard.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Automatically translate text copied to your Mac clipboard

This Rule suits a reading session in which you repeatedly copy unfamiliar text. Its input comes from the clipboard event, so you do not need a separate Get Selected Text Action or a hotkey for each passage.

**When:** The clipboard changes. **Do:** Translate the event's text to English, then show the translated output as text. There is no If Condition to restrict the source app or skip particular content.

## Configure and try it

1. Import using **Open this Rule in Rulr** and choose the target language in Translate Text.
2. Complete the Translation Shortcut setup requested by Rulr before enabling the Rule.
3. Copy a short passage in another language and check the displayed translation. Copy a different passage to verify a second run.
4. Disable the Rule when you finish the reading session if you do not want ordinary copying to trigger it.

## Requirements and limits

Clipboard Changed requires Rulr Pro. Translate Text requires the Translation Shortcut dependency; supported languages and translation availability depend on that setup.

The sample handles text. It does not perform image OCR, save clipboard history, or replace the clipboard with the translation. Non-text clipboard changes may provide no useful text to translate. For translation only when you request it, use [Translate Selected Text](https://www.rulr.app/rules/translate-selected-text-mac/); for text inside images, use [Translate Screen Text](https://www.rulr.app/rules/translate-screen-text-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/translate-clipboard-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
