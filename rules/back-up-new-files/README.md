# Project Backup

Automatically copy matching new files to another folder on Mac while keeping the originals. Choose a watched folder, filename filter, and backup destination.

The sample watches Downloads, matches names containing `Project`, and copies each matching event path to a separate destination. Choose your source, name filter, and backup folder after importing.

[Website preview and full setup](https://www.rulr.app/rules/copy-new-files-backup-mac/) · [Download back-up-new-files.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/back-up-new-files/back-up-new-files.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Automatically copy matching files between Mac folders

Use this Rule for project exports or deliveries that need a second local copy. It copies rather than moves the matching item, so the original remains available in the source folder.

**When:** An item is added or renamed in `~/Downloads`. **If:** The event's filename contains `Project`. **Do:** Copy File to `~/Documents/Project Backups`, using a numbered name if the destination name already exists. The two Triggers feed the same matching and copy path.

## Configure and try it

1. Import with **Open this Rule in Rulr** and set the watched folder in both the added and renamed Triggers.
2. Replace `Project` with the filename text that identifies the files you want to copy.
3. Select an existing writable backup folder outside the watched source and review the name-conflict policy.
4. Enable the Rule and add a disposable matching file. Confirm the original remains and the copy appears. Rename a test item to a matching name, then try a nonmatching name to check both event paths and the filter.

## Requirements and limits

Folder Contents Changed requires Rulr Pro; Copy File itself is available without Pro. Rulr needs access to both folders.

This is an event-driven extra copy, with no explicit wait for a file still being written. It is not a full backup system: there is no version retention, deletion propagation, existing-folder scan, or monitoring of later content edits. Repeated matching events can create additional numbered copies. For triggering your own processing instead, see [Run Shortcut for Folder](https://www.rulr.app/rules/watch-folder-run-shortcut-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/copy-new-files-backup-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
