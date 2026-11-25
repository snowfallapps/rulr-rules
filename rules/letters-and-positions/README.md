# Letters and Alphabet Positions

Convert letters to numbers on Mac with A1Z26, where A=1 through Z=26, or convert a list of positions back to letters. Enter HELLO to get 8 5 12 12 15, or enter those positions to get HELLO.

The Rule asks for input, passes it to an embedded AppleScript and shows the result. It does not read or modify a Numbers or Excel workbook.

[Website preview and full setup](https://www.rulr.app/rules/letters-to-numbers-mac/) · [Download letters-and-positions.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/letters-and-positions/letters-and-positions.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Use letters as numbers in an alphabet exercise

**When:** Press Option + L. **Do:** Ask for Input collects English letters or space-separated positions, Run AppleScript converts them, then Show Text or Image displays the result.

Use it for alphabet-position exercises or preparing a value to use in a spreadsheet. Unlike a shortcut remap, the Rule performs the conversion itself.

## Configure and try it

1. Import the Rule, review Option + L and choose an unused shortcut if needed.
2. Enable it and enter HELLO. Check that the panel displays 8 5 12 12 15.
3. Run it again and enter 8 5 12 12 15. Check that it displays HELLO.
4. Try a single letter or position, then cancel the input prompt to stop the flow.
5. Review any input error instead of treating it as a conversion result.

## Requirements and limits

Ask for Input, Run AppleScript and Show Text or Image do not require Pro. The hotkey Trigger requires Accessibility access. The conversion has no external dependency and does not automate a spreadsheet application.

Letters must be English A–Z; letter case is ignored and spaces are skipped. Numeric input must use integer positions from 1 to 26 separated by spaces. The script rejects decimals, punctuation and out-of-range positions, and limits each input to 200 characters to keep the displayed result bounded.

This is an alphabet-position conversion. AA becomes 1 1, not spreadsheet column 27. It does not turn a numeric string into a word's meaning, use another writing system or edit workbook cells.

The result is displayed without replacing the clipboard. For a different text transformation, see [Process Text with AppleScript](https://www.rulr.app/rules/process-text-applescript-mac/).

For the separate Apple News word puzzle, see [Find Quartiles Word Candidates](https://www.rulr.app/rules/quartiles-word-candidates-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/letters-to-numbers-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
