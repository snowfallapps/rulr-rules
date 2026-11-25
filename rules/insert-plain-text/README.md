# Paste as Plain Text

This Rulr Rule demo uses Option + V on Mac to convert the current clipboard item to plain text and insert it into the frontmost app. Import and enable the Rule to use this separate shortcut alongside normal Command + V paste.

The sample uses Option + V to run Convert to Plain Text on Current Clipboard Content, then passes its Plain Text output to Insert Text. Choose another shortcut if needed.

[Website preview and full setup](https://www.rulr.app/rules/paste-without-formatting-mac/) · [Download insert-plain-text.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/insert-plain-text/insert-plain-text.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## A Rulr Rule for clipboard text without source formatting

When copying styled text into notes, email or a document, choose whether to keep the source formatting. This Rule adds a separate plain-text paste shortcut alongside normal paste:

- **Command + V (⌘V):** Paste normally using the destination app's existing command.
- **Option + V (⌥V):** Convert the current clipboard text to plain text and insert it at the cursor in the frontmost app.

Copy formatted text from a webpage or document, focus an editable field in the app you want to paste into, and press Option + V. No destination app is fixed in the Rule; keep your destination focused until insertion finishes.

**When:** Press Option + V. **If:** No Condition; the Rule runs whenever its shortcut is pressed while enabled. **Do:** Convert Current Clipboard Content to plain text, then insert the Plain Text output.

The second Action uses the first Action's output. Insert Text sends the converted text as keyboard input to the focused app; the destination field must accept that input. It does not invoke the app's Paste and Match Style command.

## Configure and try it

1. Import the Rule using **Open this Rule in Rulr**. Choose another shortcut if Option + V conflicts with your keyboard layout or another app.
2. Confirm Convert to Plain Text uses Current Clipboard Content and Insert Text uses the conversion's Plain Text output.
3. Allow Accessibility access, enable the Rule, and copy a formatted passage from a webpage or document.
4. Place the cursor in a temporary editable document and press the shortcut. Compare the inserted words with the original and check that the source styling has been removed. The destination can still apply its own font, size, or color.

## Requirements and limits

The Rule requires a version of Rulr that includes Convert to Plain Text and Accessibility access for insertion. It accepts one clipboard item containing supported plain text, RTF, or HTML. Content with image or file data is rejected even if a text representation is also present; multiple clipboard items are not supported. It does not extract text from images or read the contents of copied files.

Conversion removes source styling. It does not correct grammar, trim spaces, or join line breaks from copied PDFs. The destination controls the appearance of the inserted text, so plain text can still take on the surrounding paragraph's formatting.

The sample converts and immediately inserts text when you press its shortcut. It does not remap Command + V or make every paste plain text automatically. To extend the Rule, use the Plain Text output as input to another Action.

Check insertion in the apps and fields you plan to use. Sending keyboard input does not confirm that the destination accepted it.

For Paste and Match Style, Word and Google Docs shortcuts, or a TextEdit fallback, see [Paste without formatting on Mac: shortcuts and fixes](https://www.rulr.app/posts/paste-without-formatting-mac/).

For a copied URL, use [Open Clipboard Link](https://www.rulr.app/rules/open-clipboard-link-mac/) to review it before opening Safari. Neither Rule stores clipboard history.

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/paste-without-formatting-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
