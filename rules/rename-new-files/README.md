# Automatically Rename New Files on Mac

Rename files automatically as they arrive in a Mac folder you choose. Set the replacement name in Rulr and use numbered filenames to handle name conflicts.

Folder Contents Changed passes each new item's path to Rename File or Folder. The sample uses the literal name `Processed File`; replace it with your intended name before enabling the Rule.

[Website preview and full setup](https://www.rulr.app/rules/rename-new-files-mac/) · [Download rename-new-files.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/rename-new-files/rename-new-files.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Rename files automatically when they arrive in a folder

This Rule starts a naming workflow when an item appears in a folder. It is useful as a base for a controlled intake folder where incoming files need a recognizable name before you review or organize them elsewhere.

**When:** A direct item is added to the watched folder. **Do:** Pass its Item Path to Rename File or Folder. There is no filename or file-kind Condition in the sample. The configured replacement is the literal text `Processed File`, with numbered names used to resolve conflicts; it is not a date or project naming scheme.

## Configure and try it

1. Import through **Open this Rule in Rulr** and select a temporary intake folder for your first trial.
2. Review the replacement name and conflict handling in Rename File or Folder. Replace the sample text with the name you actually want; add supported Variables if you need a dynamic value.
3. Keep the source connected to the folder Trigger's Item Path so it refers to the arriving item.
4. Enable the Rule and add disposable files one at a time. Inspect their resulting names, extensions, and conflict behavior before using valuable documents.

## Requirements and limits

Folder monitoring and renaming require Rulr Pro and access to the watched folder. Because the sample has no file-kind filter, review how it should handle folder additions too. Add an explicit Condition if only a particular type should be renamed.

The Rule does not batch-rename the folder's existing contents or recursively watch subfolders. For moving files into different destinations rather than changing their names, use [Sort Downloads](https://www.rulr.app/rules/sort-downloads-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/rename-new-files-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
