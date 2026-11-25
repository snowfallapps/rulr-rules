# Automatically Sort Downloaded PDFs on Mac

Organize PDFs as they arrive in your Mac Downloads folder. This Rulr rule checks each new filename for the .pdf extension and moves matching files to your chosen folder.

When a new folder item is added, the Rule checks whether its name ends in `.pdf` and moves the matching path. Choose the watched Downloads folder and PDF destination before enabling it.

[Website preview and full setup](https://www.rulr.app/rules/organize-downloaded-pdfs-mac/) · [Download organize-downloaded-pdfs.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/organize-downloaded-pdfs/organize-downloaded-pdfs.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Give new PDFs a destination

Use this Rule when reports, invoices, or reference PDFs accumulate in Downloads and belong in one predictable folder. It moves a newly added matching item, keeping that document available in your chosen destination rather than requiring a separate Finder cleanup session.

**When:** A direct item is added to the watched folder. **If:** The item name ends in `.pdf`. **Do:** Move the path supplied by the folder event. The Condition checks the filename; it does not read the document or decide whether it is an invoice, report, or another kind of PDF.

## Configure and try it

1. Import with **Open this Rule in Rulr**, then choose the Downloads folder you want to monitor.
2. Choose a different PDF destination in Move File or Folder. Both sample paths initially point to Downloads, so the destination needs your attention before enabling the Rule.
3. Review the `.pdf` Condition and numbered-name conflict setting. Keep the event's Item Path Variable as the source so each run moves the new item.
4. Enable the Rule and add a disposable PDF. Check the destination, then add a non-PDF file to confirm it stays in the source folder.

## Requirements and limits

Folder monitoring and moving files require Rulr Pro and access to both folders. The watcher observes direct items, without recursively processing subfolders or moving PDFs that were already present before you enabled it.

A filename suffix does not validate a PDF's contents or prove a browser has finished writing it. Test your normal download workflow before relying on automatic moves. For separate image and archive destinations, see [Sort Downloads](https://www.rulr.app/rules/sort-downloads-mac/).

[Compare Rulr and Hazel for Mac file automation](https://www.rulr.app/posts/hazel-alternative/)

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/organize-downloaded-pdfs-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
