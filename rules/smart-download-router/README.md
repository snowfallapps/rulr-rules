# Sort Downloads

Automatically organize your Downloads folder on Mac by file type. Move new images, PDFs, and archives into separate folders with an editable Rulr Rule.

Three filename Conditions route each matching arrival to its destination, using numbered names for conflicts. Choose the watched folder and all three destinations before enabling it; existing downloads are not processed automatically.

[Website preview and full setup](https://www.rulr.app/rules/sort-downloads-mac/) · [Download smart-download-router.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/smart-download-router/smart-download-router.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Sort new downloads into folders by file type

This Rule separates common downloads into image, PDF, and archive destinations. It is useful for an inbox workflow where pictures should go to a visual review folder, documents to a reading queue, and compressed files to an archive folder.

**When:** A direct item is added to the watched Downloads folder. **If:** Its filename matches one of three branches. **Do:** Move that item's path to the corresponding destination. The image branch matches PNG, JPEG, HEIC, and WebP names; the PDF branch checks `.pdf`; the archive branch matches ZIP, 7z, TAR, and GZ names.

## Configure and try it

1. Import with **Open this Rule in Rulr** and select the source folder on your Mac.
2. Review all three Move File or Folder Actions. The sample paths are Pictures/Inbox, Documents/PDF Inbox, and Downloads/Archives; select destinations that exist and suit your workflow.
3. Keep each Action connected to the Trigger's Item Path Variable and review the numbered-name conflict option.
4. Add disposable examples of an image, PDF, and archive. Confirm that each reaches its intended folder. Add an unrelated text file and check that it stays in Downloads.

Compare the other [Mac file automation tasks](https://www.rulr.app/rules/files-organization/) before adding more branches. [Folder Contents Changed](https://www.rulr.app/capabilities/#trigger.input.folder-contents-changed) provides the Item Path used by the move Actions; the [Mac automation guide](https://www.rulr.app/posts/mac-automation/#how-rulr-automates-your-mac) explains how event outputs and Conditions connect.

## Requirements and limits

Folder monitoring and moving files require Rulr Pro. Allow access to each folder involved. The Rule matches names, without inspecting file contents, unpacking archives, or sorting files already in the folder.

The watcher is not recursive, and an added-item event is not a guarantee that a download is complete. Try the browsers and download tools you normally use. For a narrower workflow with one destination, use [Organize Downloaded PDFs](https://www.rulr.app/rules/organize-downloaded-pdfs-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/sort-downloads-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
