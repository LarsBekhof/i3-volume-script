import subprocess
import re
import sys

lastKnownVolumeFile = '/home/lars/Code/i3-volume-script/.last-known-volume'

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

lastKnownVolume  = open(lastKnownVolumeFile).read()

if output is None or len(output.group(0).strip()) == 0:
    print(lastKnownVolume)
    sys.exit()

output = re.search('[0-9]*%', output.group(0))

if output is None or len(output.group(0).strip()) == 0:
    print(lastKnownVolume)
    sys.exit()

f = open(lastKnownVolumeFile, 'w+')
f.write(output.group(0))

print(output.group(0))
