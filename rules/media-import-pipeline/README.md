# Import Media

Automatically separate new photos and videos into different folders on Mac. Watch one incoming folder and move matching media files by their extensions.

The sample watches Downloads and uses filename extensions to select an image or video branch. Choose your source and both destination folders after importing; name conflicts use numbered filenames.

[Website preview and full setup](https://www.rulr.app/rules/sort-photos-videos-mac/) · [Download media-import-pipeline.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/media-import-pipeline/media-import-pipeline.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Sort incoming photos and videos into separate folders

Use this Rule for a folder that receives mixed media exports or downloads. Both branches use the path from the folder event, so each move applies to the arriving item rather than a fixed example file.

**When:** An item is added to `~/Downloads`. **If:** Its name matches PNG, JPG, JPEG, HEIC, or WebP, **Do:** Move it to `~/Pictures/Media`. A separate branch matches MOV, MP4, or M4V and moves it to `~/Movies/Imports`. Both regular expressions ignore case and match the end of the filename.

## Configure and try it

1. Import through **Open this Rule in Rulr** and choose the folder that receives your media files.
2. Select existing, writable destination folders in both Move Actions. Keep destinations separate from the watched source.
3. Review the extension patterns and numbered-name conflict policy. The Actions move files out of the source.
4. Enable the Rule and add disposable image and video copies. Check each destination, then add an unsupported file type to confirm it stays in the source. Try a duplicate filename as well.

## Requirements and limits

Folder Contents Changed and Move File or Folder require Rulr Pro. Rulr needs access to the source and destinations.

The Rule routes files by name; it does not inspect media contents, sort by capture date, convert formats, or import into the Photos library. Existing files are not a backfill job, and no explicit wait for unfinished downloads is configured. For routing PDFs and archives alongside images, see [Sort Downloads](https://www.rulr.app/rules/sort-downloads-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/sort-photos-videos-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
