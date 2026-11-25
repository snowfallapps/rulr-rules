# Read an Article Hands-Free

Automatically press the Spacebar on Mac to advance a long Safari article while reading hands-free. Every 30 seconds, the Rule checks Safari and the chosen article URL before sending one Space press.

Choose your article and reading interval before enabling. Switching to another app or a different article skips new matching events; the Rule never clicks the mouse.

[Website preview and full setup](https://www.rulr.app/rules/auto-press-spacebar-mac/) · [Download repeat-spacebar-reading.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/repeat-spacebar-reading/repeat-spacebar-reading.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Repeat Space for a reading task

Read a long Safari article while taking notes on paper or sitting away from the keyboard. This Rule presses Space at a fixed interval to move down the article one screen at a time.

Safari uses Space to move down one screen, as documented in [Apple's Safari keyboard shortcuts](https://support.apple.com/guide/safari/keyboard-shortcuts-and-gestures-cpsh003/mac). The timer performs that repeated operation for you; it does not replace a single shortcut with another shortcut.

**When:** Every 30 seconds. **If:** Safari is frontmost. **Do:** Read the active tab URL. **If:** That URL equals the article you chose and Safari is still frontmost. **Do:** Press Space once to advance the article.

## Choose the article and pace

1. Import the disabled Rule. In the article URL Condition, replace the demonstration Mac automation guide URL with your article's exact URL.
2. Adjust Timed Repeat from 30 seconds to your reading pace. It is a timer, not an estimate of whether you finished reading.
3. Allow Accessibility and Automation for Safari. Timed Repeat, Get Current Tab and Type Text or Press Keys require Pro.
4. Open the chosen article in Safari and focus its body. Reader mode can help remove forms and other controls; use it only if the page supports it.
5. Enable the Rule, watch its first advance and adjust the interval if needed.
6. Switch tabs or apps to pause matching events. Disable the Rule when you finish reading.

## Scope and focus

The URL comparison is exact, including a trailing slash or query string. The sample URL is `https://www.rulr.app/posts/mac-automation/`; it does not match every Safari tab. Returning to the chosen article resumes matching timer events until you disable the Rule.

Keep focus on the article, not the address bar, a search field or a button. The Rule checks the app and tab URL, not the focused webpage element. A change of focus during an already started event can still affect where that Space press goes.

The Rule does not detect the end of an article, wait for reading progress, produce smooth scrolling, or press Space and click simultaneously. Review the first few advances on your chosen page before relying on the timer.

For a different text task, see [Letters and Alphabet Positions](https://www.rulr.app/rules/letters-to-numbers-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/auto-press-spacebar-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
