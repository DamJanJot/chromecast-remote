# Chromecast Remote 

A lightweight terminal-based remote control for **Chromecast with Google TV / Android TV**, using **ADB over Wi-Fi**.

The idea is simple: run the script in a terminal and, while that terminal has keyboard focus, your computer keyboard becomes a remote for the TV.

No mouse, web interface, or additional app on the Chromecast is required.

## Features

The current version supports:

| Keyboard        | Chromecast / Google TV |
| --------------- | ---------------------- |
| `↑` `↓` `←` `→` | Navigate               |
| `Enter`         | OK / Select            |
| `Backspace`     | Back                   |
| `H`             | Home                   |
| `Space`         | Play / Pause           |
| `+`             | Volume up              |
| `-`             | Volume down            |
| `M`             | Mute                   |
| `N`             | Next                   |
| `P`             | Previous               |
| `Q`             | Quit the remote        |

The keyboard is captured only while the terminal running the remote has focus. Switch to another window and your keyboard behaves normally there.

## Requirements

* Linux or Ubuntu via WSL
* Python 3
* Android SDK Platform Tools (`adb`)
* Chromecast with Google TV or a compatible Android TV device
* Computer and Chromecast connected to the same local network
* Developer Options and Wireless Debugging enabled on the Chromecast

## 1. Install ADB

Download **Android SDK Platform Tools** for Linux from Google's official Android developer website.

Extract the archive and make sure `adb` is available from your terminal.

Check it with:

```bash
adb version
```

You should see information about the installed Android Debug Bridge version.

## 2. Enable Developer Options on Chromecast

On Google TV, open:

**Settings → System → About**

Find **Android TV OS build** and press the OK button several times until Developer Options are enabled.

Then go to:

**Settings → System → Developer options → Wireless debugging**

Enable **Wireless debugging**.

> Menu names can differ slightly depending on the Google TV / Android TV version.

## 3. Pair the computer

Inside **Wireless debugging**, select the option to pair a device using a pairing code.

The Chromecast will display something similar to:

```text
IP address & port:
192.168.0.3:36869

Wi-Fi pairing code:
528979
```

The values above are only examples. Use the current values displayed on your TV.

On the computer run:

```bash
adb pair 192.168.0.3:36869
```

ADB will ask for the pairing code:

```text
Enter pairing code:
```

Enter the six-digit code displayed on the Chromecast.

After successful pairing you should see a message similar to:

```text
Successfully paired
```

Pairing normally only needs to be performed once for a given computer unless the authorization is removed or reset.

## 4. Connect to the Chromecast

Go back to the main **Wireless debugging** screen.

It displays an IP address and port for the actual ADB connection, for example:

```text
192.168.0.3:41217
```

This port can be different from the pairing port.

Connect with:

```bash
adb connect 192.168.0.3:41217
```

Verify the connection:

```bash
adb devices -l
```

A successful connection should look similar to:

```text
192.168.0.3:41217    device    model:Chromecast
```

The important part is:

```text
device
```

This means the Chromecast is connected and authorized.

## 5. Run Chromecast Remote

Clone this repository:

```bash
git clone https://github.com/DamJanJot/chromecast-remote.git
cd chromecast-remote
```

Make the script executable:

```bash
chmod +x chromecast_remote.py
```

Run it:

```bash
./chromecast_remote.py
```

Alternatively:

```bash
python3 chromecast_remote.py
```

Keep the terminal window focused and use your keyboard as the Chromecast remote.

Press:

```text
q
```

to exit.

## How it works

The script reads keyboard input directly from the terminal and translates keys into Android key events.

For example, pressing the right arrow results in the equivalent of:

```bash
adb shell input keyevent KEYCODE_DPAD_RIGHT
```

Pressing Space sends:

```bash
adb shell input keyevent KEYCODE_MEDIA_PLAY_PAUSE
```

and Home corresponds to:

```bash
adb shell input keyevent KEYCODE_HOME
```

ADB sends those events over the local network directly to Android running on the Chromecast.

This means the project does **not** emulate an infrared remote and does not require line-of-sight to the TV.

## Troubleshooting

### `adb: command not found`

Android Platform Tools are either not installed or `adb` is not available in your `PATH`.

Check:

```bash
adb version
```

### Device is not connected

Check:

```bash
adb devices -l
```

If the Chromecast isn't listed, return to **Wireless debugging** on the TV and check its current IP address and port.

Then reconnect:

```bash
adb connect IP_ADDRESS:PORT
```

### The port changed

This is expected.

The ADB Wireless Debugging port may change, especially after restarting the Chromecast or toggling Wireless Debugging.

Check the current value on the Chromecast under:

**Developer options → Wireless debugging**

and reconnect using:

```bash
adb connect CURRENT_IP:CURRENT_PORT
```

### Pairing port vs connection port

These are not necessarily the same thing.

The address shown under **Pair device with pairing code** is used for:

```bash
adb pair IP:PORT
```

The address displayed on the main Wireless Debugging screen is used for:

```bash
adb connect IP:PORT
```

Don't assume that the pairing port can also be used as the normal connection port.

## Security

Wireless Debugging gives an authorized computer significant control over the Android device.

Only pair computers you trust.

If you no longer want a computer to have debugging access, remove it from the list of paired devices in the Chromecast's **Wireless debugging** settings.

Avoid exposing ADB ports outside your local network.

## Roadmap

Possible improvements:

* [ ] Automatically discover the connected Chromecast instead of hardcoding its IP and ADB port
* [ ] Automatically reconnect after the ADB port changes
* [ ] Show the currently active application
* [ ] Display `PLAYING`, `PAUSED`, and other media states
* [ ] Display currently playing media metadata
* [ ] Keyboard shortcuts for launching YouTube, Spotify, Netflix, and other apps
* [ ] Device status display
* [ ] Multiple Chromecast / Android TV support
* [ ] Configuration file
* [ ] Integration with home automation systems
* [ ] Habitat integration

## Tested device

Initial development and testing was performed with a Chromecast with Google TV running Android 14.

ADB reports the device platform as:

```text
device: sabrina
model: Chromecast
```

Other Android TV / Google TV devices supporting ADB Wireless Debugging may also work, but have not necessarily been tested.

## Why?

Because sometimes the best TV remote is the keyboard that's already under your hands.

And because turning a terminal into a Chromecast remote is more fun than it has any right to be.






---

<img width="357" height="396" alt="image" src="https://github.com/user-attachments/assets/bcb533ba-512f-44d6-b6d5-ce30bbe45b79" />


---
