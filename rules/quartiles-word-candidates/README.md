# Find Quartiles Word Candidates

Find Quartiles word candidates on Mac by entering the puzzle's 20 tiles. The Rule checks combinations against a local word list and opens a report showing words and their tile groupings.

Ask for Input collects the tiles, an embedded script finds dictionary matches, and Open File or Folder opens the report in TextEdit. Results are candidate words, not a verified daily Apple News answer list.

[Website preview and full setup](https://www.rulr.app/rules/quartiles-word-candidates-mac/) · [Download quartiles-word-candidates.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/quartiles-word-candidates/quartiles-word-candidates.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Find words you have not noticed

Use this while reviewing a Quartiles puzzle when you want word suggestions without automatically entering words or revealing the entire official list. You supply the visible tiles; the Rule searches combinations and leaves you to try candidates in the game.

**When:** Press Option + Q. **Do:** Ask for the 20 tiles, run the embedded candidate finder and open its report in TextEdit.

The finder considers ordered combinations of one to four distinct tile positions. It matches them against the local dictionary and records each candidate's tile pieces and positions. Identical tile text in two positions can be used twice because they are two separate tiles; a single position is never reused within a candidate.

## Configure and use

1. Import the disabled Rule and review Option + Q. Allow Accessibility for its shortcut. Run Shell Script requires Pro.
2. Check that `/usr/share/dict/words` is a readable UTF-8 word list with one word per line. If absent, choose an existing word-list file you are entitled to use and update `dictionaryPath` in the embedded source. No dictionary is downloaded or bundled.
3. Enable the Rule, open the puzzle and invoke it.
4. Enter exactly 20 tile strings separated by spaces or commas. Enter each tile as one item; do not split a multi-letter tile into individual letters.
5. Review the report in TextEdit and try candidate words yourself. Check your input if the report is empty or contains unexpected suggestions.

The input accepts English letters only, with one to twelve letters per tile. Cancelling the input stops the flow. A missing dictionary, invalid input or failed report write stops the Rule rather than opening an empty result as if it succeeded.

## Dependencies and execution

The finder is JavaScript for Automation embedded in Run Shell Script and launched through the macOS `osascript` utility. It is not a native Quartiles component and does not require Python, Node or an online service. The script reads your chosen local dictionary and writes the local report; it does not control News, submit answers or use the game's reveal command.

The Action has a 120-second timeout. The word list is limited to 12 million characters. This configuration has been checked against the component contract; it has not been run or verified in the Mac App in this change.

For alphabet-position exercises, use [Letters and Alphabet Positions](https://www.rulr.app/rules/letters-to-numbers-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/quartiles-word-candidates-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
