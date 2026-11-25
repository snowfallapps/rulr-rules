# USB App Launcher

Open an app automatically when a USB device connects to your Mac. Match your accessory's name and launch the utility or work app you use with it.

The sample matches names containing `USB` and launches Safari. Replace the broad name filter and select the app you use with your accessory after importing.

[Website preview and full setup](https://www.rulr.app/rules/open-app-usb-device-mac/) · [Download open-app-for-usb-device.rulr](https://github.com/snowfallapps/rulr-rules/raw/HEAD/rules/open-app-for-usb-device/open-app-for-usb-device.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Launch a Mac app when a USB device is connected

Use this Rule when connecting an accessory normally means opening the same utility or work app. The device-name Condition keeps the launch tied to the connection you care about.

**When:** A USB device connects. **If:** The event's Device Name contains `USB`. **Do:** Launch Safari. The sample performs a single app launch; it does not run an Apple Shortcut or pass device data into the app.

## Configure and try it

1. Import using **Open this Rule in Rulr** and replace `USB` with a distinctive part of the accessory's reported name.
2. Select the installed application you want to launch.
3. Enable the Rule, disconnect the accessory, and reconnect it. Check that the application opens.
4. Try a different USB device to confirm that the name Condition does not match too broadly. Adjust the filter if several accessories share the same name fragment.

## Requirements and limits

The sample's Trigger and Action are available without Pro and declare no special permission. The launched application may have its own device or permission requirements.

USB connection does not mean that a storage volume has mounted or that files are ready to read. This Rule does not import files, open a device-specific project, or identify accessories by serial number. For a routine implemented in Shortcuts, use [Run Shortcut for USB Device](https://www.rulr.app/rules/run-shortcut-usb-device-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/open-app-usb-device-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
