# top_errors
simple .py script to show the top 10x journactl errors for linux

## Install instructions
download `top_errors.py`

`chmod +x top_errors.py`

`./top_errors.py`

### Output:
```
user@lt-fedora-ws:~/Projects/top_errors$ ./top_errors.py 
Top 10 most frequent error/warning messages:

(65x) Dec 28 19:16:50 fedora kernel: ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20240827/psobject-220)
(3x) Dec 28 19:17:08 lt-fedora-ws gsd-media-keys[1971]: gvc_mixer_card_get_index: assertion 'GVC_IS_MIXER_CARD (card)' failed
(2x) Dec 28 19:16:55 lt-fedora-ws kernel: nvidia-modeset: WARNING: GPU:0: Unable to read EDID for display device DP-4
(2x) Dec 28 19:17:01 lt-fedora-ws gsd-sharing[1940]: Failed to StopUnit service: GDBus.Error:org.freedesktop.DBus.Error.Spawn.ChildExited: Process org.freedesktop.systemd1 exited with status 1
(2x) Dec 28 19:17:02 lt-fedora-ws gsd-media-keys[1971]: gvc_mixer_card_get_index: assertion 'GVC_IS_MIXER_CARD (card)' failed
(2x) Dec 28 19:17:09 lt-fedora-ws gnome-shell[2645]: Window manager warning: Overwriting existing binding of keysym 31 with keysym 31 (keycode a).
(2x) Dec 28 19:17:09 lt-fedora-ws gnome-shell[2645]: Window manager warning: Overwriting existing binding of keysym 32 with keysym 32 (keycode b).
(2x) Dec 28 19:17:09 lt-fedora-ws gnome-shell[2645]: Window manager warning: Overwriting existing binding of keysym 33 with keysym 33 (keycode c).
(2x) Dec 28 19:17:09 lt-fedora-ws gnome-shell[2645]: Window manager warning: Overwriting existing binding of keysym 34 with keysym 34 (keycode d).
(2x) Dec 28 19:17:09 lt-fedora-ws gnome-shell[2645]: Window manager warning: Overwriting existing binding of keysym 36 with keysym 36 (keycode f).
```
