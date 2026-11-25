# Archive Screenshots

Move new Mac screenshots from a watched folder into an archive folder automatically, keeping the source folder easier to scan.

When a folder item is added, the Rule checks whether its name matches a screenshot file and moves the matching path to your archive. Choose the watched and archive folders before enabling it.

[Website preview and full setup](https://www.rulr.app/rules/archive-screenshots-mac/) · [Download archive-new-screenshots.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/archive-new-screenshots/archive-new-screenshots.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Archive new screenshots by filename

This Rule is useful when screenshots arrive alongside other downloads and you want to move them into a separate review folder. It handles new items as they appear, so you can continue capturing references without manually moving each matching image.

**When:** A direct item is added to the watched folder. **If:** Its name matches the sample screenshot pattern. **Do:** Move the event's item path to the archive destination. The pattern looks for `screenshot` followed by a PNG or JPEG extension, ignoring letter case. It identifies names rather than inspecting image contents.

## Configure and try it

1. Use **Open this Rule in Rulr** to import the sample, then choose the folder where your screenshots actually arrive. The default watched path is Downloads.
2. Set Move File or Folder to a separate archive folder. The sample destination also points to Downloads, so choose your actual archive before enabling the Rule.
3. Review the filename Condition against one of your screenshots. Localized names or a different capture app may require a different pattern.
4. Enable the Rule and add a disposable matching image. Confirm that it moves and that a nonmatching image stays in place.

## Requirements and limits

Folder monitoring and moving files require Rulr Pro. Rulr also needs access to the source and destination folders. The numbered-name conflict option preserves separate names when a destination name is already taken.

The watcher covers direct children, not nested subfolders, and does not process an existing screenshot collection on import. To organize several file types, use [Sort Downloads](https://www.rulr.app/rules/sort-downloads-mac/) instead.

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/archive-screenshots-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
