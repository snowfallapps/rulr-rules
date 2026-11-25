# Search Selected Text

Select text in a Mac app and open a web search for it with one keyboard shortcut, without manually copying and pasting the query.

The Rule reads the current selection, URL-encodes it, and opens the search URL in Google Chrome. Change the URL template to use Google, DuckDuckGo, or another search service.

[Website preview and full setup](https://www.rulr.app/rules/search-selected-text-mac/) · [Download search-selected-text.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/search-selected-text/search-selected-text.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Search a selection without copying it manually

Use this Rule when a name, phrase, or unfamiliar term in a document needs a web search. It turns the current selection into a query and opens the results in Chrome, removing the manual copy, new-tab, and paste sequence.

**When:** Press the chosen shortcut, initially Option + Space. **Do:** Get Selected Text, URL-encode that text, and append the encoded result to Google's search URL before opening a new Chrome tab. There is no If Condition. The encoding step keeps spaces and punctuation from being interpreted as URL structure.

## Configure and try it

1. Import with **Open this Rule in Rulr** and assign an unused hotkey if Option + Space is already reserved.
2. Review the URL in Open New Tab. If you choose another search engine, retain the encoded-result Variable and use that service's query URL format.
3. Allow Accessibility and System Events Automation for selection retrieval, plus Google Chrome Automation for opening the tab.
4. Select a short phrase in a compatible app and run the Rule. Compare the query shown by the search engine with your selection, then repeat with punctuation or spaces.

## Requirements and limits

Transform Text requires Rulr Pro. Selected-text retrieval depends on the frontmost app exposing a usable selection; some apps may briefly use the clipboard during retrieval.

The selected phrase becomes part of a request to your configured search service. The Rule does not search local files, guarantee the first result, or replace text in the original document. For keeping the selection in a local notes file instead, use [Save Selected Text](https://www.rulr.app/rules/save-selected-text-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/search-selected-text-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
