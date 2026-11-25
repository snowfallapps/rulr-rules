# Text Expansion

Set up a text expander Rule on Mac to insert reusable replies, addresses, or signatures when you type a short trigger. Choose your phrase and text in Rulr.

The sample matches `;addr` and inserts your configured text into the frontmost app. It has no explicit step to delete the typed abbreviation; check how it behaves in your writing app before relying on automatic replacement.

[Website preview and full setup](https://www.rulr.app/rules/text-expansion-mac/) · [Download text-expansion.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/text-expansion/text-expansion.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Set up text expansion for repeated phrases

Use this Rule for a phrase you enter repeatedly, such as a reply, short address, or signature. A distinctive typed trigger starts an Insert Text Action so you can maintain the reusable content in one place rather than copying it from a reference note.

**When:** The exact phrase `;addr` is typed. **Do:** Insert the configured text into the frontmost application. There is no If Condition. The sample replacement content is `Text Expansion`; replace that demonstration value with your own phrase before using the Rule in real documents.

## Configure and try it

1. Import through **Open this Rule in Rulr** and review the Text Typed phrase and case-matching setting. Choose a trigger unlikely to appear in ordinary writing.
2. Edit Insert Text with your intended content. Begin with a short sentence so the result is easy to inspect.
3. Grant Accessibility access for the typed Trigger and text insertion. Enable the Rule and place the cursor in a temporary document in your usual writing app.
4. Type the trigger and check the full resulting text, including whether the trigger phrase remains and where the content is inserted. Repeat in other apps you intend to use.

## Requirements and limits

Text Typed requires Rulr Pro. The receiving app must support the simulated insertion behavior, and secure fields or app-specific input handling can behave differently.

The supplied flow contains a Trigger and insertion Action, without an explicit step to select or delete the typed abbreviation. Verify the result rather than assuming every app will replace it as a conventional snippet tool would.

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/text-expansion-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
