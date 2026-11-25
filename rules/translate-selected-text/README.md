# Translate Selected Text

Translate selected text on your Mac by typing a short trigger, then display the English translation without leaving the app you are working in.

The final display can give way to Insert Text, Set Clipboard to Text, or Write to File, extending the flow into inline translation, writing, or replies.

[Website preview and full setup](https://www.rulr.app/rules/translate-selected-text-mac/) · [Download translate-selected-text.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/translate-selected-text/translate-selected-text.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Translate text exposed by the frontmost app

Use this Rule as a base for checking a short passage in another language. It reads an application's selected text, translates the retrieved value into English, and presents the result in Rulr rather than altering the original document.

**When:** The exact phrase `;translate` is typed. **Do:** Get Selected Text, translate that Text output, and display the translated text. There is no If Condition. The default target language is English, and the supplied Trigger is typed text rather than a hotkey.

## Configure and try it

1. Import using **Open this Rule in Rulr** and review the Trigger phrase and target language.
2. Grant Accessibility and System Events Automation for retrieving the selection. Complete the Translation Shortcut setup requested by Rulr for macOS System Translate.
3. Test a short selection in a compatible application. Check whether typing `;translate` changes the selection before Get Selected Text can read it.
4. If the phrase replaces or disturbs selected text in your app, change the Trigger to Hotkey Pressed. Select the passage again, invoke the new shortcut, and compare the displayed translation with the intended source.

## Requirements and limits

Text Typed requires Rulr Pro. Selection retrieval depends on the source app exposing text, and some apps may briefly use the clipboard. Translation also needs the configured macOS translation workflow and a supported language.

The Rule displays the result; it does not automatically replace the passage, copy the translation, or translate an entire document. Review important wording yourself, particularly after an empty or unexpected selection. For visible text that cannot be selected, use [Translate Screen Text](https://www.rulr.app/rules/translate-screen-text-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/translate-selected-text-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
