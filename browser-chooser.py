import sys
import readchar
import subprocess

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
        _, params = browsers[readchar.readchar()]
        subprocess.Popen(['nohup'] + [p.format(url=url) for p in params],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        break
    except:
        print(f'Invalid choice. Please choose one of [{", ".join(browsers.keys())}]')
