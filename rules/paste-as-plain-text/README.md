# Paste URL-Encoded Text

Press Option–E on your Mac to URL-encode clipboard text for a query parameter and insert the encoded result at the cursor in the frontmost app.

The Rule passes Current Clipboard Text through Transform Text with URL Encode, then sends the encoded output to Insert Text. Enable Accessibility permission for insertion and change the hotkey after import if Option–E is already in use.

[Website preview and full setup](https://www.rulr.app/rules/url-encode-paste-text-mac/) · [Download paste-as-plain-text.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/paste-as-plain-text/paste-as-plain-text.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Paste clipboard text as a URL value

Use this Rule while preparing a query parameter or another URL value from text already on the clipboard. It converts that text with URL Encode, then inserts the transformed result at the current insertion point in your frontmost application.

**When:** Press Option + E. **Do:** Transform Current Clipboard Text using URL Encode, then Insert Text from the transformed Text Result. There is no If Condition. For example, a space in `hello world` becomes `%20`, producing `hello%20world` for a URL value.

## Configure and try it

1. Import with **Open this Rule in Rulr**. Review the shortcut, particularly if Option + E is used by your keyboard layout or another tool.
2. Keep Transform Text connected to Current Clipboard Text and set to URL Encode. Keep Insert Text connected to the transform's result rather than the original clipboard Variable.
3. Allow Accessibility permission for insertion and for recording a replacement shortcut if needed.
4. Copy a short phrase, place the cursor in a temporary text document, and run the Rule. Inspect the inserted output before trying it in the URL editor or form where you intend to use it.

## Requirements and limits

Transform Text requires Rulr Pro. The clipboard must contain text, and the receiving application must accept insertion at the current cursor position.

This sample is an encoding workflow. For pasting without the original styling, try the destination app's built-in Paste and Match Style command. This Rule does not decode a URL or decide whether an already encoded value should be encoded again. For trimming entered text instead of URL encoding, see [Trim Text](https://www.rulr.app/rules/trim-copy-text-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/url-encode-paste-text-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
