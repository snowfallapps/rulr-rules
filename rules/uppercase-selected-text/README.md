# Uppercase Selected Text

Convert selected text to uppercase on Mac with one keyboard shortcut. Rulr transforms the selection and pastes the all-caps result into your editable field.

The Rule gets the selection, transforms its case, puts the result on the clipboard, and pastes it. Choose a shortcut after importing and use it in an editable text field where pasting replaces the selection.

[Website preview and full setup](https://www.rulr.app/rules/uppercase-selected-text-mac/) · [Download uppercase-selected-text.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/uppercase-selected-text/uppercase-selected-text.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Convert selected text to all caps with a Mac shortcut

Use this Rule when editing headings, labels, or short passages in an app that lacks a convenient uppercase command. The four Actions pass the text result forward, so the transformation applies to the selection you just made.

**When:** Press the configured hotkey, initially Option + Space. **Do:** Get Selected Text → Transform Text using uppercase → Set Clipboard → Paste Clipboard. There is no If Condition or app filter.

## Configure and try it

1. Import with **Open this Rule in Rulr** and choose an unused shortcut, especially if another imported Rule uses Option + Space.
2. Keep the uppercase transformation selected. Review the output references before changing the Action order.
3. Allow Accessibility and System Events Automation access for selection retrieval and pasting.
4. Select a short mixed-case phrase in an editable test document and run the shortcut. Check both the replacement and the clipboard before using it on important text.

## Requirements and limits

Transform Text requires Rulr Pro. Selection retrieval depends on the source app. The paste goes to the frontmost application's current insertion point or selection; keep focus on the intended field.

The Rule replaces the clipboard contents with the uppercase result and does not restore the previous clipboard. A read-only webpage cannot be edited by pasting. For whitespace cleanup of entered text instead, see [Trim Text](https://www.rulr.app/rules/trim-copy-text-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/uppercase-selected-text-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
