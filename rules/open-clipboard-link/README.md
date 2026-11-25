# Open Clipboard Link

Open a link from your Mac clipboard in Safari after reviewing the URL. Copy a complete web address from a message or document, then run the Rule to check and open it.

The Rule snapshots and trims the current clipboard text, checks for a single HTTP or HTTPS link and asks for confirmation. It opens that same captured link without rereading the clipboard.

[Website preview and full setup](https://www.rulr.app/rules/open-clipboard-link-mac/) · [Download open-clipboard-link.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/open-clipboard-link/open-clipboard-link.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Open a copied address from a message

A colleague may send a web address as plain text rather than a clickable link. Copy that address, invoke this Rule from your current app and review it before opening a Safari tab. You do not have to switch browsers, focus the address bar, paste and submit it yourself.

**When:** Press Option + O. **Do:** Read and trim the current clipboard text. **If:** It has the form of one HTTP or HTTPS URL with no spaces. **Do:** Show the captured address for confirmation, then open it in a new Safari tab if you continue.

The input comes from the clipboard, not a fixed website stored in the Rule. The Condition filters out ordinary copied paragraphs before showing an opening prompt.

## Configure it

1. Import the disabled Rule and review Option + O.
2. Allow Accessibility and Automation for Safari. Transform Text requires Pro.
3. Enable it, copy a complete web address and invoke the Rule.
4. Check the address in the confirmation. Cancel to leave Safari unchanged, or continue to open it.
5. Copy ordinary text and invoke it again; the URL Condition should skip the opening step.

## Clipboard and URL limits

This Rule opens only the current copied link. It does not open a clipboard-history window, restore previous copies or let you select older items. If you are looking for that history behavior, this Rule does not provide it.

The expression checks the URL's basic shape, not whether a destination exists or is trustworthy. Multiple links, unencoded spaces, `mailto:` and local file paths do not pass. A malformed HTTP URL can pass the initial pattern and still fail when Safari opens it.

The clipboard is left unchanged. The opening Action uses the captured result even if another app updates the clipboard while the confirmation is visible. A successful open request is not proof the page loaded.

For copied text going into a document instead, use [Paste as Plain Text](https://www.rulr.app/rules/paste-without-formatting-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/open-clipboard-link-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
