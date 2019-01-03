import subprocess
import re

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
output = re.search('[0-9]*%', output.group(0))

print(output.group(0))
