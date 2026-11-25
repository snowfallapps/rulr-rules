# Schedule AppleScript File

Run a saved .scpt AppleScript file on a Mac schedule, such as a report-preparation script that reads Numbers and creates Calendar events.

Configure the trusted file path in the Run AppleScript Action's Arguments, then choose your schedule. The sample is disabled and scheduled for weekdays at 09:00; it includes no report-processing script of its own.

[Website preview and full setup](https://www.rulr.app/rules/run-scpt-file-mac/) · [Download run-chosen-applescript.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/run-chosen-applescript/run-chosen-applescript.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Automate a script you already maintain

**When:** The configured weekday schedule fires. **Do:** Run AppleScript loads your configured file from disk and runs it. The file is read on each execution, so later changes to that file do not need to be pasted back into the Rule.

A report, calendar or maintenance script can run without opening Script Editor each time. The Rule supplies scheduling and file loading; your script supplies the actual work.

## Configure and try it

1. Choose a trusted .scpt or .applescript file that you already understand and have run manually.
2. In Run AppleScript, add a text Argument containing its absolute path or a path beginning with ~/.
3. Review the embedded loader and set the days and time in the Trigger.
4. Start with a harmless script and a temporary near-future schedule while the Mac is awake.
5. Enable the Rule, inspect its execution and verify the chosen script's expected result before restoring the intended schedule.

## Requirements and limits

Run AppleScript does not require Pro. The loader stops with a configuration error if no file path Argument is present. This imported sample needs your actual file path before it can run.

The file can request Automation or folder access. Only load scripts you trust. The loader supplies no arguments to your saved script and has a 120-second timeout. It does not wake a sleeping Mac or guarantee compiled-script compatibility across macOS versions.

The direct Rulr script-file picker and this compiled-file loader have different format support. For entered text processing, see [Process Text with AppleScript](https://www.rulr.app/rules/process-text-applescript-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/run-scpt-file-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
