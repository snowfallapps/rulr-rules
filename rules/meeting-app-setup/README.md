# Meeting Mode

When FaceTime launches, this Rule checks the current audio output name, opens Notes, sets the volume, and brings FaceTime forward.

The sample uses 25% volume when the output name contains `AirPods` and 15% otherwise. Choose your meeting app, notes app, device name, and preferred levels after importing.

[Website preview and full setup](https://www.rulr.app/rules/meeting-mode-audio-mac/) · [Download meeting-app-setup.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/meeting-app-setup/meeting-app-setup.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## How this Rule works

A FaceTime launch starts the Rule. The two Conditions check whether the current output name contains `AirPods`; both branches open Notes and activate FaceTime, but use different volume levels. This checks the output name, not whether you have joined a call.

## Configure and try it

Choose your meeting app in both the Trigger and Activate Application Action, and select the app you want for notes. Change the name in both Conditions and set a comfortable volume in each branch. Allow Accessibility for app activation, then launch the meeting app with each output selected and check the result.

## Requirements and limits

The Trigger and Actions do not require Pro. Accessibility is required to activate the app. Volume affects the current output; the Rule does not switch devices or arrange windows.

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/meeting-mode-audio-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
