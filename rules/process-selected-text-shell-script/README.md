# Process Text with AppleScript

Process text with AppleScript on your Mac from a keyboard shortcut, passing entered text into a script and displaying the returned result when it finishes.

Another AppleScript can send its result through Set Clipboard to Text, Insert Text, or Write to File, creating a formatter, validator, converter, or other text-processing tool.

[Website preview and full setup](https://www.rulr.app/rules/process-text-applescript-mac/) · [Download process-selected-text-shell-script.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/process-selected-text-shell-script/process-selected-text-shell-script.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Pass entered text through AppleScript

This Rule demonstrates a text input flowing through a script and into a result panel. It is a base for a small formatter or converter when you want to review script output before deciding where to use it.

**When:** Press Option + R. **Do:** Ask for text, pass that input to Run AppleScript, and display the script's result. There is no If Condition. The supplied script simply returns its first argument unchanged; it does not yet format, validate, or convert the text.

## Configure and try it

1. Import with **Open this Rule in Rulr**, then review the hotkey and the input prompt. Change the prompt to describe your actual AppleScript task; the sample prompt still mentions a shell script.
2. Review the script and its input Variable. Keep the prompted value connected to the script input and the returned result connected to Show Text or Image.
3. Try the unchanged sample first by entering a short sentence. Confirm that the panel displays the same sentence. Cancel a second prompt and verify that processing stops.
4. Replace the script with your intended transformation and test representative input. Review the 30-second timeout if the script performs a longer task.

## Requirements and limits

The sample's components are available without Pro. Accessibility is needed if you record a replacement shortcut. A different script may require additional Automation permissions depending on the apps it controls.

The sample asks for input; it does not read the current selection or run a shell command. Script failure stops the flow before result display. For saving selected passages directly, use [Save Selected Text](https://www.rulr.app/rules/save-selected-text-mac/).

To run an existing compiled script on a schedule, use [Schedule AppleScript File](https://www.rulr.app/rules/run-scpt-file-mac/) and configure its actual file path. For native text processing, compare [Remove Emoji from Text](https://www.rulr.app/rules/remove-emojis-from-text-mac/) and [Extract Line-End Number](https://www.rulr.app/rules/remove-line-breaks-regex-mac/).

For an implemented alphabet-position conversion, [Letters and Alphabet Positions](https://www.rulr.app/rules/letters-to-numbers-mac/) converts A–Z to 1–26 and back, with input checks and a result panel.

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/process-text-applescript-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
