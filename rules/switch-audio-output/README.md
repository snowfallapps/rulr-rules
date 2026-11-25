# Switch Audio Output on Mac with a Keyboard Shortcut

Use a keyboard shortcut to switch your Mac audio output to a chosen speaker, pair of headphones, or display without opening Sound settings.

Select one connected output device and choose the hotkey after importing. Each press requests that device; the sample does not cycle between devices or change the volume.

[Website preview and full setup](https://www.rulr.app/rules/switch-audio-output-mac/) · [Download switch-audio-output.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/switch-audio-output/switch-audio-output.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Set a keyboard shortcut for your audio output device

To change the output once, open **System Settings → Sound → Output** and select the device. If the device is missing there, connect it and check the list again before assigning it in Rulr. See [Apple’s guide to sound output settings](https://support.apple.com/guide/mac-help/mchlp2256/mac).

Use this Rule when you often switch to the same speaker, headphones, or display audio device. A keyboard shortcut requests the selected output without opening Control Center and choosing the device manually each time.

**When:** Press the chosen hotkey, initially Option + Space. **Do:** Switch Audio Output Device. There is no If Condition. The sample has no device selected, so choosing an output is a required setup step after import rather than an optional customization.

## Configure and try it

1. Import with **Open this Rule in Rulr** and connect the audio device you want to use.
2. Select that device in Switch Audio Output Device. Review the choice on each Mac where you import the Rule, since available devices differ by machine and connection.
3. Assign an unused hotkey. Grant Accessibility access if you need to record a different combination.
4. Start quiet test audio, run the shortcut, and check the selected output in macOS Sound settings. Confirm that sound reaches the intended device. Disconnect it and review how the routine behaves when it is unavailable.

## Requirements and limits

The sample's Trigger and Action are available without Pro. The chosen device must be connected and available to macOS when the Action runs.

This Rule chooses one output device; it does not cycle through a device list, connect Bluetooth headphones, switch microphone input, or set a volume level. It also has no automatic fallback device configured. For applying volume after macOS changes output devices, see [Set Headphone Volume](https://www.rulr.app/rules/set-volume-audio-device-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/switch-audio-output-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
