# Contributing

Use [Issues](https://github.com/snowfallapps/rulr-rules/issues) for requests,
incorrect setup instructions, or reproducible problems with a sample. Link its
website detail page and include the Rulr and macOS versions involved.

The website owns the executable rule definitions and editorial documentation.
The `.rulr` file and selected README sections are mirrored together. Changes to
these generated files need to be incorporated into the website before they can
persist through the next sync. For wording specific to the GitHub README, edit
the title or introductory paragraph in `scripts/rule-readme-copy.json`. Please
describe the intended change in your PR.

Do not submit credentials, provider keys, private documents, personal file paths,
or device identifiers. Use portable examples and explain any setup required.
The App validates imported rules; a preview or successful JSON parse does not
prove that a rule ran successfully on a real Mac.

## Maintainers

Run `python scripts/sync_rules.py` to update from the public website catalog.
The daily workflow does the same without an external token. It fetches only
`https://www.rulr.app` URLs and verifies every rule's SHA-256 before writing files.
A missing catalog leaves the current mirror unchanged and reports a warning;
other download or validation failures stop the sync.

For initial setup, `python scripts/sync_rules.py --site-source /path/to/rulr-site`
reads the website's current metadata and Markdown. It still downloads and checks
every `.rulr` against the live website before publishing it. This mode does not
copy the website repository, history, or App source.

Folder names and rule filenames are stable IDs. Renaming a display title does
not rename a folder. Retired folders stay available for existing download links,
but disappear from the active root directory. Website import URLs are unchanged.
