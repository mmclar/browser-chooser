import sys
import readchar
import subprocess

ESC = 27

browsers = {
    'p': ('Firefox (personal)', ['firefox', '-P', 'mmclar', '{url}']),
    'w': ('Firefox (work)', ['firefox', '-P', 'work', '{url}']),
}

url = sys.argv[1] if len(sys.argv) > 1 else ''
print(url)
print('Choose which browser you want to use for this link:')
for key, (name, _) in browsers.items():
    print(f'{key}: {name}')

while True:
    try:
        _, params = browsers[(c := readchar.readchar())]
        subprocess.Popen(['nohup'] + [formatted for p in params if (formatted := p.format(url=url))],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        break
    except KeyError:
        if ord(c) in (ESC,):
            print('Exiting')
            sys.exit(0)
        print(f'Invalid choice. Please choose one of [{", ".join(browsers.keys())}]')
