# Batch Prefix Files

Batch rename matching files in a Mac folder by adding a prefix on a schedule. This Rulr Rule starts with a preview so you can review the proposed names before applying changes.

Set the folder path in the included script, choose an extension and prefix, then review the timer. The script is embedded in the Rule; a separate download is available below for Terminal use.

[Website preview and full setup](https://www.rulr.app/rules/batch-rename-files-mac/) · [Download batch-prefix-files.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/batch-prefix-files/batch-prefix-files.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## How this Rule works

- **When:** Timed Repeat runs every 30 minutes, between 00:00 and 24:00 by default.
- **If:** There is no Condition node. The script filters matching files and checks destination conflicts before renaming.
- **Do:** Run Shell Script invokes the embedded Bash script. It previews the names by default; setting its mode to `apply` adds the prefix to matching filenames.

For example, `invoice.pdf` becomes `project-invoice.pdf`. Files already beginning with the same prefix are skipped, including files that had that prefix before the first run. New matching files can be handled on later runs.

The imported Rule is disabled. Its folder setting is empty, so it will report an error until you set an existing absolute folder path. It does not download code or install a script when it runs.

## Configure and try it

1. Add the Rule to Rulr and leave it disabled while configuring it.
2. Open **Do → Run Shell Script → Script**. Keep **text script** mode and edit only the four settings at the top initially:

```bash
folder="/absolute/path/to/Rename Demo"
mode="preview"
extension="pdf"
prefix="project-"
```

3. Choose a disposable folder containing copies of a few PDFs. Enter its absolute path inside the quotes; do not use `~`. For paths containing a literal dollar sign, backtick, backslash, or quote, use appropriate shell quoting rather than pasting them unchanged into double quotes.
4. Keep `preview` while testing. The extension has no leading dot and is case sensitive. The prefix accepts letters, digits, hyphens, and underscores.
5. Review **When → Timed Repeat**. You can temporarily shorten the interval to one minute. Leave the optional script Argument empty, the timeout at 30 seconds, and **Stop this flow if unsuccessful** enabled.
6. Enable the Rule and enter Inspect Mode. Wait for a timer run, confirm success, and check that preview has left filenames unchanged. Disable the Rule before editing again.
7. Review the complete preview in Terminal using the download below if needed. When satisfied, change `mode="preview"` to `mode="apply"`, enable the Rule for a test, and verify the filenames and contents on disk.
8. Disable the Rule after testing. Before recurring use, select the intended folder, keep a backup, and choose an interval longer than the expected runtime.

The rest of the embedded script implements matching, conflict checks, and moves. You do not need to replace it or install a separate file to use this Rule. Changes to your embedded copy are local; downloading a newer website script does not update an imported Rule automatically.

## Requirements and limits

Run Shell Script requires **Rulr Pro**, and Rulr requires macOS 26 or later. Rulr must have access to the selected folder; a successful Terminal run does not prove the app has the same access. The text script explicitly invokes `/bin/bash` because the Action's outer interpreter is `/bin/sh`.

Only ordinary, non-hidden files in the folder's first level are processed. Subfolders and symbolic links are skipped. Passing `pdf` leaves `.PDF` unchanged. The script preserves the rest of the name and file contents; it does not number files, replace text, or read a Finder selection.

Apply checks all planned destinations before starting and refuses existing files, directories, or symbolic links. A directory lock coordinates other instances of this script. Keep the folder unchanged during a batch: Finder and other programs do not honor that lock. Interrupted runs or external changes can leave a partially completed batch; there is no automatic rollback. A forced termination may leave a lock requiring review before another run.

Rulr captures at most 1,024 bytes of script output, and Execution Logs redact script text. Use Terminal for a complete preview of a large folder, and verify actual files rather than treating an Action's success as a complete rename history.

For individual new arrivals instead of existing folder contents, use [Rename New Files](https://www.rulr.app/rules/rename-new-files-mac/). Explore more tasks in [Mac file automation](https://www.rulr.app/rules/files-organization/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/batch-rename-files-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
