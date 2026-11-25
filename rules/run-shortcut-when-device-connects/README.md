# Run Shortcut for USB Device

Run an Apple Shortcut automatically when a matching USB device connects to your Mac, without opening the Shortcuts app first.

Choose the USB device match and Shortcut after importing the Rule. When that device connects, Rulr checks its name and runs the selected Shortcut.

[Website preview and full setup](https://www.rulr.app/rules/run-shortcut-usb-device-mac/) · [Download run-shortcut-when-device-connects.rulr](https://github.com/snowfallapps/rulr-rules/raw/refs/heads/main/rules/run-shortcut-when-device-connects/run-shortcut-when-device-connects.rulr) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

## Start a Shortcut when a USB device connects

Use this Rule for a device-specific setup routine, such as beginning a task when a USB accessory becomes available. It listens for the connection, filters the device's reported name, and starts an Apple Shortcut that you choose.

**When:** A USB device connects. **If:** Its Device Name contains `USB`. **Do:** Run Shortcut. The default filter is deliberately broad and the Shortcut is not selected, so both fields need review. The sample timeout is 30 seconds, and no device information is passed as Shortcut input by default.

## Configure and try it

1. Import with **Open this Rule in Rulr** and review the name Condition. Replace `USB` with a distinctive part of the device name you want to match.
2. Choose an existing Shortcut in Run Shortcut. Run it manually in the Shortcuts app first and complete any permissions or configuration it needs.
3. Review the timeout and any input required by your Shortcut. Connect an appropriate Trigger Variable if the task depends on device information.
4. Enable the Rule, disconnect the accessory, and reconnect it. Check the Shortcut's expected result, then try another device to verify the filter is selective enough.

## Requirements and limits

The sample's components are available without Pro and declare no special permission. The chosen Shortcut can have its own app, folder, or system requirements.

A USB connection is not the same as a mounted storage volume being ready. The Rule does not automatically copy files, identify every accessory uniquely, or wait for a drive mount. For starting processing from file arrivals instead, see [Run Shortcut for Folder](https://www.rulr.app/rules/watch-folder-run-shortcut-mac/).

---

This README reuses selected sections of the [official Rule Detail](https://www.rulr.app/rules/run-shortcut-usb-device-mac/).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
