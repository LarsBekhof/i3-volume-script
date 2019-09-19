# i3-volume-script
A script to get the volume from the running pulse audio sink. Mind you this is the RUNNING sink NOT the default sink. So only the sink audio is playing over. If there is no running sink a dash will be displayed.

# Dependencies
- pulseaudio
- python3.5 or greater

# How to use
This script is meant to be used with i3blocks

```
[volume]
command=python3 /path/to/script/volume.py
label=♫
interval=1
```
