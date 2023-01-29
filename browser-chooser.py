import sys
import readchar
import subprocess

ESC = 27

browsers = {
    'p': ('Firefox (personal)', ['firefox', '-P', 'mmclar', '{url}']),
#    'w': ('Firefox (work)', ['firefox', '-P', 'work', '{url}']),
#    'c': ('Chrome', ['google-chrome', '{url}']),
}

url = sys.argv[1] if len(sys.argv) > 1 else ''

def openByChar(c):
    _, params = browsers[c]
    subprocess.Popen(['nohup'] + [formatted for p in params if (formatted := p.format(url=url))],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    sys.exit()

# If there's only one choice, open it
if len(browsers) == 1:
    openByChar(next(iter(browsers)))

print(url)
print('Choose which browser you want to use for this link:')
for key, (name, _) in browsers.items():
    print(f'{key}: {name}')

while True:
    try:
        openByChar(readchar.readchar())
    except KeyError:
        if ord(c) in (ESC,):
            print('Exiting')
            sys.exit(0)
    print(f'Invalid choice. Please choose one of [{", ".join(browsers.keys())}]')

