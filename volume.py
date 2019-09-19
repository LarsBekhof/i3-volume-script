import subprocess
import re
import sys
from os import path
from os.path import expanduser

lastKnownVolumeFile = expanduser('~/.config/last-known-volume')
f = open(lastKnownVolumeFile, 'r')

# If there is no file create one
if not path.exists(lastKnownVolumeFile):
    f.write('')

# Run pactl command
result = subprocess.run(['pactl', 'list', 'sinks'], stdout=subprocess.PIPE).stdout.decode('utf-8')

# Split output by sinks
splitOutput = result.split('Sink #')

# Get the running sink
runningOutput = ''
for x in range(len(splitOutput)):
    if 'State: RUNNING' in splitOutput[x]:
        runningOutput = splitOutput[x]
        break

# These regexs can probably be more elegant
output = re.search('Volume:.*/.*([0-9]{2}|[0-9]%).*/', runningOutput)

lastKnownVolume = f.read()

if output is None:
    print(lastKnownVolume)
    sys.exit()

output = re.search('[0-9]*%', output.group(0))

volume = output.group(0).strip()

if output is None:
    print(lastKnownVolume)
    sys.exit()

f = open(lastKnownVolumeFile, 'w+')
f.write(volume)

print(volume)
