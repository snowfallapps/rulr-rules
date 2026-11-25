# Clear Clipboard When Away

Clear old copied content from the current Mac clipboard after five minutes of system inactivity. The Rule replaces it with the harmless text EMPTY when you step away.

Choose the idle threshold after importing. This reacts to time without user input, rather than requiring you to remember a cleanup shortcut.

[Website preview and full setup](https://www.rulr.app/rules/clear-clipboard-mac/) · [Download clear-current-clipboard.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/clear-current-clipboard/clear-current-clipboard.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Replace copied content when you step away

**When:** System Idle reaches five minutes. **Do:** Set Clipboard to Text replaces the current item with EMPTY. There is no script, shortcut or confirmation.

Use it as a cleanup step for content that should not remain ready for accidental pasting after a break. It replaces any current copied item, including an image or file reference.

## Configure and try it

1. Import the Rule and review the five-minute idle threshold and EMPTY marker.
2. Temporarily choose a shorter interval for a deliberate trial.
3. Enable the Rule, copy a disposable phrase and stop using the mouse and keyboard until the threshold is reached.
4. Resume and paste into a blank document. Confirm that EMPTY is pasted instead of the old phrase.
5. Restore the intended idle threshold.

## Requirements and limits

The Trigger and Set Clipboard to Text do not require Pro or declare special permissions.

System inactivity is not the time since copying, app inactivity or screen lock. A later copy does not start a dedicated clipboard timer; the Trigger follows system user-input activity. Sleeping or shutting down the Mac is not a guaranteed cleanup opportunity.

The marker replaces the current content rather than producing a zero-byte pasteboard. It does not securely erase previous copies, other devices or third-party clipboard-manager history. The prior clipboard item cannot be recovered through this Rule.

For cleaning the content of newly copied text instead, see [Remove Emoji from Text](https://www.rulr.app/rules/remove-emojis-from-text-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/clear-clipboard-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
