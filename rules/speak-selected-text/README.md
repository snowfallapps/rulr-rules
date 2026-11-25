# Speak Selected Text

Type a configured trigger phrase on your Mac to retrieve selected text from a compatible frontmost app and read the passage aloud with Rulr.

Text Typed starts the Rule, Get Selected Text reads the selection from the frontmost application, and Speak Text reads it aloud. Choose a trigger phrase and use it with selected text in a compatible application.

[Website preview and full setup](https://www.rulr.app/rules/read-selected-text-aloud-mac/) · [Download speak-selected-text.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/speak-selected-text/speak-selected-text.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Speak text from the current selection

This Rule is a starting point for listening to a passage while reviewing a document. It retrieves text exposed by the frontmost app and passes that text directly to speech, without first saving the passage in a separate file.

**When:** The exact typed phrase `;speak` is detected. **Do:** Get Selected Text, then Speak Text using the retrieved Text output. There is no If Condition. This is a typed Trigger rather than a keyboard shortcut in the supplied sample.

## Configure and try it

1. Import with **Open this Rule in Rulr** and review Text Typed. Choose a distinctive phrase if you keep this Trigger.
2. Grant Accessibility and System Events Automation access for selected-text retrieval. Accessibility also supports the typed Trigger.
3. Test with a short, nonessential selection in an application that exposes selected text. Observe whether entering the trigger phrase changes or replaces that selection before Rulr reads it.
4. If typing interferes with the selection in your app, replace Text Typed with Hotkey Pressed and test the selection again. Confirm that the speech matches the passage and that your audio output is audible.

## Requirements and limits

Text Typed and Speak Text require Rulr Pro. Reading a selection depends on application support, and some apps may briefly use the clipboard to retrieve it.

The sample speaks the text it actually retrieves; it does not automatically read a whole document, recognize words in an image, or translate the passage. Typed-trigger compatibility needs checking in each target app. For translating accessible selected text instead, see [Translate Selected Text](https://www.rulr.app/rules/translate-selected-text-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/read-selected-text-aloud-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
