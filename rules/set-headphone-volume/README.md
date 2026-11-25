# Set Volume by Audio Device

Set Mac volume automatically when the audio output device changes, using different levels for AirPods and speakers and opening Spotify when needed.

Additional device-name branches can pair Set Volume and Launch Application Actions with meetings, music, office speakers, or headphones.

[Website preview and full setup](https://www.rulr.app/rules/set-volume-audio-device-mac/) · [Download set-headphone-volume.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/set-headphone-volume/set-headphone-volume.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Apply volume when the output device changes

This Rule is useful when headphones and speakers need different starting volume levels. It reacts to the audio output device selected by macOS, checks its name, and applies the corresponding branch rather than requiring you to adjust volume manually after every switch.

**When:** The audio output device changes. **If:** Its name contains `AirPods`, set volume to 20 and launch Spotify. In the separate `Speakers` branch, set volume to 30. Devices matching neither name receive no Action from the sample.

## Configure and try it

1. Import with **Open this Rule in Rulr** and review the exact names macOS reports for your audio outputs.
2. Replace the name fragments in the Conditions with values that identify your devices. Choose distinct matches if each device should use only one branch.
3. Set comfortable volume levels and review the Spotify launch Action. Select an installed music app, remove that step, or keep Spotify if it belongs in your routine.
4. Enable the Rule and switch outputs using macOS Sound controls. Check the resulting volume and whether the intended app launches. Try an unmatched device too.

To change the device itself rather than only its volume, compare [Switch Audio Output](https://www.rulr.app/rules/switch-audio-output-mac/). The [Variables library](https://www.rulr.app/capabilities/variables/) lists audio state values, and the [Mac automation guide](https://www.rulr.app/posts/mac-automation/) shows how device events and Conditions fit into a Rule.

## Requirements and limits

The sample's components are available without Pro and declare no special permission. The music app must be installed if you retain its launch Action, and the output device must support the requested volume change.

The Rule responds to an output-device change, not merely a Bluetooth connection. It does not connect headphones, start playback, or maintain a continuous volume limit. For choosing an output with a manual shortcut first, use [Switch Audio Output](https://www.rulr.app/rules/switch-audio-output-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/set-volume-audio-device-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
