# Save Selected Text

Save selected text from a Mac app to a notes file with one keyboard shortcut, without switching away from the current document or webpage.

Choose the shortcut and destination text file after importing the Rule. Each run gets the current selection and appends it to the end of that file.

[Website preview and full setup](https://www.rulr.app/rules/save-selected-text-mac/) · [Download save-selected-text.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/save-selected-text/save-selected-text.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Append selected passages to a notes file

This Rule is useful for collecting short passages while reading documentation or reviewing a document. It appends the current selection to a text file, so you can build a local reading queue without moving between the source app and a notes editor.

**When:** Press the configured hotkey, initially Option + Space. **Do:** Get Selected Text, then Write to File using append-to-end mode. There is no If Condition. The sample destination is `~/Downloads/Rulr Notes.txt`; each run supplies the selection as the content to append.

## Configure and try it

1. Import through **Open this Rule in Rulr** and choose a shortcut that does not conflict with another app or Rule.
2. Select the actual destination file in Write to File and keep append-to-end mode if you want to retain earlier entries.
3. Allow Accessibility and System Events Automation access for selection retrieval, and ensure Rulr can write to the destination.
4. Select a short test passage in a compatible app, run the shortcut, and inspect the file. Repeat with a different passage to verify that the previous content remains and the new content is appended.

## Requirements and limits

Write to File requires Rulr Pro. Reading a selection depends on the source application's support, and some apps may briefly use the clipboard as part of retrieval.

The sample saves selected text only. It does not automatically include the source URL, title, timestamp, or separators between entries; add those to the content if your note format needs them. It also does not capture text from an image. For visible text that cannot be selected, use [Copy Text from Your Screen](https://www.rulr.app/rules/copy-text-mac-screen/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/save-selected-text-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
