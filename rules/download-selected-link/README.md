# Download and Reveal a Link

Download a selected link on your Mac with a keyboard shortcut, confirm the download, and reveal the finished file in Finder when it is ready.

Move File or Folder and Rename File or Folder can follow the download, allowing each result to enter a project folder, asset archive, or another file-organizing flow.

[Website preview and full setup](https://www.rulr.app/rules/download-selected-link-mac/) · [Download download-selected-link.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/download-selected-link/download-selected-link.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Confirm a download from selected text

This Rule is a starting point for downloading a URL selected in another app. It reads text, applies the sample's filter, asks for confirmation, and reveals a successfully downloaded file in Finder so you can inspect the result.

**When:** Press Option + D. **Do:** Get Selected Text. **If:** That text contains `download`, continue to confirmation, Download from URL, and Reveal in Finder. The filter is a literal substring check, not a general URL validator. Many valid download addresses will not pass it until you change the Condition.

## Configure and try it

1. Import with **Open this Rule in Rulr** and review the shortcut and the `download` Condition. Replace the filter with criteria appropriate to your source links.
2. Select a destination folder; the sample uses Downloads. Review the 60-second download timeout and progress display.
3. Grant Accessibility and System Events Automation access for reading selected text. Use a compatible app where the selected content is the complete URL, not just a link's visible label.
4. Try a small public test file. First cancel the confirmation, then repeat and approve it. Check that only the successful run downloads and reveals a file.

## Requirements and limits

The confirmation and download Actions require Rulr Pro, plus access to the destination folder. The download is configured to stop the flow on failure, so Finder reveal depends on a successful file-path output.

This sample does not scrape a webpage for links or reproduce a browser's authenticated session. An incomplete selection, login page, or expired URL can fail. For organizing downloaded results afterward, see [Sort Downloads](https://www.rulr.app/rules/sort-downloads-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/download-selected-link-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
