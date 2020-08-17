import sys
import readchar
import subprocess

print('Choose which browser you want to use for this link: (f)irefox or (c)hromium.')
url = sys.argv[1]
print(url)

char = readchar.readchar()
print(char)
executable = {
    'f': 'firefox',
    'c': 'chromium',
}[char]
subprocess.Popen(['nohup', executable, url],
         stdout=subprocess.PIPE,
         stderr=subprocess.STDOUT)
