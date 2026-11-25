# Copy Text from Your Screen

Copy text from images, screenshots, or apps visible on your Mac screen with one keyboard shortcut. OCR reads the text and puts it on your clipboard.

The sample recognizes the full screen, then copies the recognized Text output. Review the capture target and shortcut after importing; the result is ready to paste into your notes or document.

[Website preview and full setup](https://www.rulr.app/rules/copy-text-mac-screen/) · [Download copy-screen-text.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/copy-screen-text/copy-screen-text.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Use screen OCR to copy text you cannot select

For an existing image, you may only need macOS Live Text.

Use this Rule for visible labels, screenshots, or application content that you cannot highlight as ordinary text. It recognizes text from the configured screen capture target and copies the result so you can paste it into a note, message, or document.

**When:** Press the configured hotkey, initially Option + Space. **Do:** Recognize Text on Screen, then set the clipboard to the recognized Text output. There is no If Condition. The sample capture target is a full screen; it does not automatically limit recognition to the sentence or control you are looking at.

## Configure and try it

1. Import with **Open this Rule in Rulr** and choose a shortcut that is not already assigned to another Rule or app.
2. Review the capture target in Recognize Text on Screen. Choose the supported screen or area settings that fit the content you want.
3. Grant Screen Recording access when requested. Accessibility access is needed if you record a replacement shortcut.
4. Display a short, clearly readable sentence, run the Rule, and paste into a temporary document. Compare the copied text with the screen before using it elsewhere.

For image files arriving in a folder, choose [Extract Text from New Images](https://www.rulr.app/rules/extract-text-images-mac/) instead of capturing the screen. The [Recognize Text on Screen Action](https://www.rulr.app/capabilities/actions/#action.image.recognize-text-on-screen) lists the capture input and output; the [Mac automation guide](https://www.rulr.app/posts/mac-automation/) explains how to connect that output to another step.

## Requirements and limits

The sample's Actions are available without Pro. Screen Recording permission is needed even though the result is text rather than a saved screenshot.

OCR can misread small text, unusual fonts, or complex layouts and may capture other visible text within the target. The clipboard result replaces its previous text; it does not automatically paste or translate it. For translation after recognition, see [Translate Screen Text](https://www.rulr.app/rules/translate-screen-text-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/copy-text-mac-screen/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
