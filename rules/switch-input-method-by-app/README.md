# Switch Input Method

Automatically switch your Mac input method or input source by app, such as using English in a code editor and Chinese in a messaging app.

Choose the applications and installed keyboard input source after importing the Rule. Add or replace application Conditions when different apps should switch the Mac keyboard language automatically.

[Website preview and full setup](https://www.rulr.app/rules/switch-input-method-by-app-mac/) · [Download switch-input-method-by-app.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/switch-input-method-by-app/switch-input-method-by-app.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Use one input source in selected apps

This Rule changes the keyboard input source when you switch into particular applications. It is useful when your browser or design tools should use a predictable typing layout regardless of what you were using in the previous app.

**When:** The frontmost application changes. **If:** The new app is Safari, Google Chrome, or Figma. **Do:** Switch the input source to ABC. The application Conditions use OR matching, so any listed app starts the same Action. The sample does not assign a different language to each app.

## Configure and try it

1. Import with **Open this Rule in Rulr** and replace or remove the application Conditions to match the apps you use.
2. Select an input source installed on your Mac in Switch Input Method. The sample identifier represents Apple's ABC keyboard layout.
3. Keep OR matching when any one of the listed applications should trigger the switch. Use separate branches or Rules if different apps need different input sources.
4. Enable the Rule, switch to a different input source, and activate one matching app. Check the macOS input indicator and type in a temporary field. Repeat with an app outside the list.

## Requirements and limits

The sample's Trigger and Action are available without Pro and declare no special permission. The chosen input source must already be installed and enabled on the Mac.

The Rule switches the system's active input source; it does not translate text, change a document's language, or restore the previous input source when you leave the matched app. It runs on application changes rather than individual text-field focus. For inserting a reusable phrase, see [Text Expansion](https://www.rulr.app/rules/text-expansion-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/switch-input-method-by-app-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
