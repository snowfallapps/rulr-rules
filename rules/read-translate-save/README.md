# Read, Translate, and Save

Translate a text file on a schedule on Mac and append the translated text to another file. The sample reads a research draft and translates it into English.

Choose the source file, destination file, target language, and schedule after importing. The sample appends results, so repeated runs add further entries.

[Website preview and full setup](https://www.rulr.app/rules/translate-text-file-schedule-mac/) · [Download read-translate-save.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/read-translate-save/read-translate-save.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## How this Rule works

The scheduled Trigger runs Read Text File, passes its contents to Translate Text, then appends the translation and a newline to the output file. There is no Condition or check for whether the source has changed.

## Configure and try it

Choose a readable text file and a separate writable output file, set the target language and schedule, and configure the required Translation Shortcut. Enable the Rule and check the output after a scheduled run; repeat with a small test file first.

## Requirements and limits

Read Text File and Write to File require Rulr Pro. Translation requires the Translation Shortcut. This processes text, not arbitrary document formats, and repeated runs append even if the source has not changed.

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/translate-text-file-schedule-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
