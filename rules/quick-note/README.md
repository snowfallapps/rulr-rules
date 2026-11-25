# Quick Note

Take a quick note on Mac by typing a short trigger. Write your thought in a prompt and save it with a timestamp to a text file, ready for your next note.

The sample listens for `;note`, asks what you want to remember, writes your answer to the notes file, and shows a notification. Choose your own typed trigger and destination after importing.

[Website preview and full setup](https://www.rulr.app/rules/quick-note-text-file-mac/) · [Download quick-note.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/quick-note/quick-note.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Capture quick notes in a plain text file on Mac

Use this Rule to collect reminders or ideas in a plain text file while another app is open. The note comes from an input dialog, so you can write a new thought rather than needing to select existing text.

**When:** Type `;note` with exact case matching. **Do:** Ask for Input, append the answer to `~/Documents/Quick Notes.txt`, then show a notification. Each entry contains a bullet, the entered text, the current date and time, and a newline. There is no If Condition; cancelling the input stops the Rule.

## Configure and try it

1. Import with **Open this Rule in Rulr** and choose a typed trigger you do not normally use in documents.
2. Select a writable notes file in Write to File. Keep append-to-end mode to retain earlier notes.
3. Allow Accessibility for Text Typed and Notifications for the completion message.
4. Enable the Rule, type the trigger in a normal text field, and submit a test note. Inspect the file, then add another note to check the entry separation. Try cancelling the dialog as well.

## Requirements and limits

Text Typed and Write to File require Rulr Pro. The completion notification depends on macOS notification settings; inspect the file to confirm the saved content.

This writes to a local text file, rather than creating an Apple Notes Quick Note. It does not capture a source URL or selected passage. For collecting existing passages, use [Save Selected Text](https://www.rulr.app/rules/save-selected-text-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/quick-note-text-file-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
