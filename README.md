# i3-volume-script
A script to get the volume from the running pulse audio sink

# Dependencies
- pulseaudio
- python3

# How to use
This script is meant to be used with i3blocks

```
[volume]
command=pactl list sinks | grep -o -E "([0-9]{2}%)|([0-9]{3}%)"
label=♫
interval=1
```
