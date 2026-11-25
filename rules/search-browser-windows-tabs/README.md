# Chrome Window Manager

Search open Chrome windows and tabs from one Mac keyboard shortcut, then switch directly to the page you need without scanning every browser window.

This starting point can be extended with Chrome Actions that open, close, or navigate tabs for research, focused reading, or client workflows.

[Website preview and full setup](https://www.rulr.app/rules/search-chrome-windows-tabs/) · [Download search-browser-windows-tabs.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/search-browser-windows-tabs/search-browser-windows-tabs.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Find a page across Chrome windows

When research, documentation, and project tabs are spread across several Chrome windows, it can be hard to remember where a page is open. This Rule gives you one keyboard shortcut to open Rulr's searchable Chrome window and tab manager, so you can find a page and switch to it without checking each window separately.

**When:** Press Option + Space, the shortcut included in this Rule. **Do:** Open the Chrome window and tab manager. There is no If condition in this sample, so the shortcut runs the Action directly. The manager also offers controls to create, reload, or close Chrome windows and tabs; opening the Rule does not automatically perform those operations.

## Set up and test

1. Use **Open this Rule in Rulr** above to import the Rule into the app on your Mac.
2. Review the **Hotkey Pressed** Trigger. The default is Option + Space; choose another shortcut if you already use it for a launcher or another app.
3. Allow Rulr to control **Google Chrome** when macOS requests Automation permission. If you record a different shortcut, grant **Accessibility** access for shortcut recording. You can review both permissions under **System Settings → Privacy & Security**.
4. Open a few Chrome tabs in more than one window, and make sure the Rule is enabled in Rulr. Press your chosen shortcut to open the manager.
5. Search for a page you have open and select it. Confirm that Chrome switches to the intended tab and window. Repeat with a page in another window to check the workflow you will use day to day.

Choose this Rule for a page that is already open. Use [Open Chrome Work Tabs](https://www.rulr.app/rules/open-chrome-work-tabs-mac/) for a fixed set of destinations, or [Chrome Research Workspace](https://www.rulr.app/rules/chrome-research-workspace/) when the destination group depends on the time. The [Show Window and Tab Manager Action](https://www.rulr.app/capabilities/actions/#action.integration.chrome.show-window-and-tab-manager) lists the component requirements. For combining browser tasks with other steps, see the [Mac automation guide](https://www.rulr.app/posts/mac-automation/).

## Requirements and limits

This sample is for Google Chrome on Mac. It does not search Safari tabs, browsing history, bookmarks, or the contents of every webpage. It helps you navigate windows and tabs that are already open; it does not save or restore a browser session.

The Action has no parameters to fill in, so the main setup choices are the shortcut and required permissions. If the manager does not open, check that the Rule is enabled and the shortcut is not assigned elsewhere. If you cannot record a replacement shortcut, review Accessibility access. If Chrome cannot be controlled, review its Automation permission for Rulr.

For a different task, such as opening a fixed set of research pages, browse the [web and browsing Rules](https://www.rulr.app/rules/web-browsing/). You can also [explore Rulr's capabilities](https://www.rulr.app/capabilities/) before extending this Rule with additional Actions.

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/search-chrome-windows-tabs/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
