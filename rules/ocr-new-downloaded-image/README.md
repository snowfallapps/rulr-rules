# Extract Text from New Images

Extract text from new images automatically on Mac. Watch a folder for PNG, JPEG, HEIC, and WebP files, then use OCR to display the recognized text.

The sample watches Downloads, checks each arriving filename, and passes the matching file path to image OCR. Choose your image inbox after importing; this Rule displays the result without saving or copying it automatically.

[Website preview and full setup](https://www.rulr.app/rules/extract-text-images-mac/) · [Download ocr-new-downloaded-image.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/ocr-new-downloaded-image/ocr-new-downloaded-image.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Automate image OCR for a watched folder

This Rule turns an image inbox into a text review workflow. When a new receipt image, screenshot, or reference picture arrives, it recognizes the image's text and displays the result in Rulr so you can check it without opening a separate OCR tool.

**When:** A direct item is added to Downloads. **If:** Its filename matches a PNG, JPEG, HEIC, or WebP extension. **Do:** Recognize text in the event's Item Path, then show the recognized text in a panel. The display receives the OCR output rather than a fixed sample sentence.

## Configure and try it

1. Import with **Open this Rule in Rulr** and choose the folder where your image files arrive.
2. Review the image-name Condition and keep the OCR source connected to the Trigger's Item Path.
3. Check that Show Text or Image uses the recognized Text output. Enable the Rule and add a clear image containing a short sentence you can compare with the result.
4. Try another image with your usual language and layout. Confirm that a nonmatching document does not enter the image branch.

Use this folder workflow for incoming image files, and [Copy Text from Your Screen](https://www.rulr.app/rules/copy-text-mac-screen/) for content already visible in an app. Check [Recognize Text in Image](https://www.rulr.app/capabilities/actions/#action.image.recognize-text-in-image) for the Action's input and Text output. To adapt the displayed result into a different workflow, follow the [AI Builder review and refinement steps](https://www.rulr.app/posts/build-mac-automations-with-ai/#3-review-it-on-the-visual-canvas) and verify that later Actions consume the OCR result.

## Requirements and limits

Folder monitoring and image OCR require Rulr Pro, plus access to the selected folder. This workflow reads image files; it does not capture the screen or extract every page of a PDF.

Recognition can lose punctuation, line order, or characters in small or blurred text. The watcher is not recursive and does not process the existing folder contents automatically. To capture visible text directly, use [Copy Text from Your Screen](https://www.rulr.app/rules/copy-text-mac-screen/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/extract-text-images-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
