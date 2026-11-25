# Extract Line-End Number

Automatically show a report number when you copy text containing slash-digits at a line ending on Mac. The Rule checks the clipboard-change event before extracting the first matching number.

Extract Text reads the event's text and returns capture group 1. Ordinary copied text is skipped, and the Rule leaves the clipboard unchanged.

[Website preview and full setup](https://www.rulr.app/rules/remove-line-breaks-regex-mac/) · [Download replace-text-newlines.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/replace-text-newlines/replace-text-newlines.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Read a reference number while copying a report

**When:** Clipboard Changed fires. **If:** The event's Text contains slash-digits followed by a line break or the end of text. **Do:** Extract Text returns the first matching number, and Show Text or Image displays it.

The Condition and extraction use this newline-aware expression:

```text
/(\d+)(?=\R|$)
```

For example, copying a report line ending in reference/123 shows 123 without an extra extraction shortcut. Capture group 1 omits the slash and newline.

## Configure and try it

1. Import the Rule and review both copies of the pattern, the first-match setting and capture group 1.
2. Enable it and copy a disposable line ending in reference/123.
3. Confirm that the result panel shows 123.
4. Try the same line with a trailing newline and then without one.
5. Copy ordinary text with no match; the Condition should skip the extraction.
6. Adjust both patterns together for your actual report format.

## Requirements and limits

Clipboard Changed and Extract Text require Pro. The Rule does not modify the clipboard, remove line breaks or edit the source document.

Only the first matching number is displayed. A space after the digits prevents this pattern from matching that line ending. A newline previously removed by another tool cannot be detected; the end-of-text alternative covers a final number without a newline.

Every matching clipboard-change event can show a panel, so enable this only when useful for the reports you are processing. For automatic content cleanup, compare [Remove Emoji from Text](https://www.rulr.app/rules/remove-emojis-from-text-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/remove-line-breaks-regex-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
