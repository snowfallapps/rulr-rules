# Copy Page as Markdown Link

Copy the current Chrome page as a Markdown link containing its page title and URL, ready to paste into notes, documentation, or an issue tracker.

Press the chosen hotkey to read the active page title and URL in Chrome, format them as a Markdown link, and place the result on the clipboard.

[Website preview and full setup](https://www.rulr.app/rules/copy-page-markdown-link-mac/) · [Download copy-page-as-markdown-link.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/copy-page-as-markdown-link/copy-page-as-markdown-link.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Make a reference link for your notes

This Rule creates a Markdown reference from the current Chrome page, useful when collecting sources for documentation or a research note. It combines the document title and URL so you can paste a labeled link without writing the Markdown syntax yourself.

**When:** Press Option + M, or your replacement shortcut. **Do:** Run JavaScript in the active Chrome tab to format its title and URL, then place the script's result on the clipboard. There is no If Condition. The script escapes brackets and backslashes in the title and wraps the URL in angle brackets.

## Configure and try it

1. Import through **Open this Rule in Rulr** and review the hotkey. Accessibility access is needed if you record a different shortcut.
2. Allow Rulr to control Google Chrome through macOS Automation permission. Chrome must also permit JavaScript from Apple Events for the script Action to work.
3. Open an ordinary webpage in Chrome, run the Rule, and paste into a Markdown editor or a plain text note.
4. Check that both the label and destination describe the active page. Test a title containing punctuation and verify the link in your intended Markdown renderer.

For a research session that also opens your source pages, compare [Chrome Research Workspace](https://www.rulr.app/rules/chrome-research-workspace/). Review the [Scripting Actions](https://www.rulr.app/capabilities/actions/#actions-category-scripting) before changing the JavaScript, and use the [AI Builder review steps](https://www.rulr.app/posts/build-mac-automations-with-ai/#3-review-it-on-the-visual-canvas) to inspect any proposed change to link formatting.

## Requirements and limits

Run JavaScript requires Rulr Pro. Some browser pages do not allow ordinary page scripts, so use a standard webpage for initial testing. Review Chrome's Apple Events JavaScript setting if Automation access alone does not resolve a script error.

The sample copies a link, without downloading the article or creating a full citation with author and publication date. It also replaces the prior clipboard text. For an unformatted address, see [Copy Current Chrome URL](https://www.rulr.app/rules/copy-current-chrome-url-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/copy-page-markdown-link-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
