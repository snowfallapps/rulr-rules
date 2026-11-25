# Translate Screen Text

Translate text on your Mac screen with a keyboard shortcut, including text in images or screenshots. Rulr captures it, runs OCR, and shows the translation.

The sample captures the full screen and translates the recognized text into English. Review the capture target, choose your target language, and complete the Translation Shortcut setup after importing.

[Website preview and full setup](https://www.rulr.app/rules/translate-screen-text-mac/) · [Download translate-screenshot.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/translate-screenshot/translate-screenshot.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Translate screenshot and image text visible on screen

This Rule is useful when text is visible but cannot be selected normally, such as a screenshot or an application label. It captures the configured screen target, recognizes the image's text, translates it, and displays a result panel.

**When:** Press the configured hotkey, initially Option + Space. **Do:** Capture Screen or Window, recognize text in the captured image, translate that Text output into English, and show the translated result. There is no If Condition. The sample capture target is a full screen rather than a manually selected phrase.

## Configure and try it

1. Import with **Open this Rule in Rulr** and review the shortcut and screen capture target. Choose a distinct hotkey and an appropriate capture area for your workflow.
2. Review the target language in Translate Text. The sample uses English; select another available language if needed.
3. Grant Screen Recording permission and complete the Translation Shortcut setup requested by Rulr for macOS System Translate. Grant Accessibility if recording a replacement shortcut requires it.
4. Display a short sentence in a clear font, run the Rule, and compare the recognized and translated meaning with the source. Test your usual language and layout before using longer material.

If you need the source text without translation, use [Copy Text from Your Screen](https://www.rulr.app/rules/copy-text-mac-screen/). Compare [Recognize Text in Image](https://www.rulr.app/capabilities/actions/#action.image.recognize-text-in-image) with the capture step to see which output feeds recognition. The [AI Builder guide](https://www.rulr.app/posts/build-mac-automations-with-ai/#3-review-it-on-the-visual-canvas) explains how to review a multi-step Rule before enabling it.

## Requirements and limits

Recognize Text in Image requires Rulr Pro. Screen capture permission and the translation setup are separate requirements; granting one does not complete the other.

OCR mistakes can carry into the translation, especially with small text or mixed columns. The sample displays the result without copying it, inserting it into another app, or replacing text on the screen. For text that can already be selected, see [Translate Selected Text](https://www.rulr.app/rules/translate-selected-text-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/translate-screen-text-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
