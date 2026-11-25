# Remove Emoji from Text

Automatically remove common emojis when you copy text on Mac. The Rule checks the clipboard-change event for matching sequences, then replaces the copied text with the cleaned result.

Enable this only when you want matching copies cleaned automatically. The Condition prevents ordinary text and the already-cleaned result from entering the replacement flow.

[Website preview and full setup](https://www.rulr.app/rules/remove-emojis-from-text-mac/) · [Download remove-emoji-text.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/remove-emoji-text/remove-emoji-text.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Clean copied text before the next paste

**When:** Clipboard Changed fires. **If:** That event's Text matches the emoji-sequence expression. **Do:** Replace Text removes matching sequences from the event's text, then Set Clipboard to Text copies the result.

This is useful when gathering text for a plain report or data field that should omit emoji. Copy as usual; the Rule does not need a separate cleanup shortcut.

## Configure and try it

1. Import the Rule and review the matching Condition and replacement pattern.
2. Enable it and copy a disposable passage containing ordinary words, non-Latin characters and emoji.
3. Wait for execution, then paste into a separate blank document.
4. Confirm that the intended emoji are removed and the remaining text is preserved.
5. Copy ordinary text without emoji and confirm that the Condition skips it.
6. Disable the Rule when you want to preserve copied emoji.

## Requirements and limits

Clipboard Changed and Replace Text require Pro. This Rule does not read the current document selection or edit the source document.

Writing the cleaned result generates another clipboard event. The same Condition rejects that result when no matched emoji remain, so it does not repeatedly clean its own output.

The pattern targets common pictographs, joined sequences, modifiers, flag pairs and keycaps. Unicode support depends on macOS; unusual or new sequences may remain, and text-style pictographs may match.

Matching copies become plain text and lose source formatting. Cleanup runs asynchronously; pasting before it finishes can use the original content, and rapid consecutive copies need care.

For report-number extraction from copied text, see [Extract Line-End Number](https://www.rulr.app/rules/remove-line-breaks-regex-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/remove-emojis-from-text-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
