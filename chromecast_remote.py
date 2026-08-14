#!/usr/bin/env python3

import os
import sys
import tty
import termios

DEVICE = "192.168.0.3:41217"

def adb_key(key):
    os.system(
        f"adb -s {DEVICE} shell input keyevent {key} "
        "> /dev/null 2>&1"
    )

def read_key():
    ch = sys.stdin.read(1)

    if ch == "\x1b":
        ch2 = sys.stdin.read(1)

        if ch2 == "[":
            ch3 = sys.stdin.read(1)

            return {
                "A": "UP",
                "B": "DOWN",
                "C": "RIGHT",
                "D": "LEFT",
            }.get(ch3, "ESC")

        return "ESC"

    return ch


print("""
=================================
       CHROMECAST REMOTE
=================================

Strzalki    sterowanie
Enter       OK
Backspace   Wstecz

h           Home
m           Mute
+           Glosniej
-           Ciszej

Spacja      Play / Pause
n           Next
p           Previous

q           Wyjscie

=================================
""")

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

try:
    tty.setraw(fd)

    while True:
        key = read_key()

        if key == "q":
            break

        elif key == "UP":
            adb_key("KEYCODE_DPAD_UP")

        elif key == "DOWN":
            adb_key("KEYCODE_DPAD_DOWN")

        elif key == "LEFT":
            adb_key("KEYCODE_DPAD_LEFT")

        elif key == "RIGHT":
            adb_key("KEYCODE_DPAD_RIGHT")

        elif key in ("\r", "\n"):
            adb_key("KEYCODE_DPAD_CENTER")

        elif key in ("\x7f", "\x08"):
            adb_key("KEYCODE_BACK")

        elif key == "h":
            adb_key("KEYCODE_HOME")

        elif key == " ":
            adb_key("KEYCODE_MEDIA_PLAY_PAUSE")

        elif key == "+":
            adb_key("KEYCODE_VOLUME_UP")

        elif key == "-":
            adb_key("KEYCODE_VOLUME_DOWN")

        elif key == "m":
            adb_key("KEYCODE_VOLUME_MUTE")

        elif key == "n":
            adb_key("KEYCODE_MEDIA_NEXT")

        elif key == "p":
            adb_key("KEYCODE_MEDIA_PREVIOUS")

finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    print("\nPilot zakonczony.")
