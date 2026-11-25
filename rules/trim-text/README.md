# Trim Text

Trim unwanted spaces and line breaks from text on your Mac, then copy the cleaned result to the clipboard so it is ready to paste.

Transform Text can use another transformation, while Insert Text or Write to File can carry the result into pasted copy, notes, messages, or structured text.

[Website preview and full setup](https://www.rulr.app/rules/trim-copy-text-mac/) · [Download trim-text.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/trim-text/trim-text.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Remove whitespace around entered text

This Rule gives you a small text-cleaning prompt when a copied value has unwanted whitespace at its edges. You supply the text, Rulr applies Trim, and the cleaned result goes to the clipboard for use in another app.

**When:** The exact phrase `;rulr` is typed. **Do:** Ask for input, transform that input with Trim, and copy the transformed Text Result. There is no If Condition. The prompt is configured to stop the Rule when cancelled, so cancellation should not continue to the clipboard Action.

## Configure and try it

1. Import with **Open this Rule in Rulr** and review Text Typed. Replace the trigger with a distinctive phrase if `;rulr` conflicts with another routine.
2. Check the input prompt and keep Transform Text connected to the prompt's Input Variable. Keep Set Clipboard to Text connected to the transformation result.
3. Grant Accessibility access for the typed Trigger. Enable the Rule and enter the phrase in a temporary document.
4. Supply a value with spaces or line breaks before and after the meaningful text. Paste the result into a temporary note and compare it with the input. Try cancelling the prompt on a second run.

## Requirements and limits

Text Typed and Transform Text require Rulr Pro. The source is the text entered into the prompt; the sample does not automatically read a selection or the previous clipboard content.

Trim removes surrounding whitespace rather than rewriting internal spacing, fixing grammar, or changing letter case. Copying the result replaces the previous clipboard text without pasting it automatically. For encoding a clipboard value and inserting it directly, see [Paste URL-Encoded Text](https://www.rulr.app/rules/url-encode-paste-text-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/trim-copy-text-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
