import subprocess
import os


def try_ping(num: str, link: str):
    if os.name == 'nt':
        arg = '-n'
    else:
        arg = '-с'
    res = subprocess.Popen(['ping', arg, num, link],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, errors = res.communicate()
    print(output)


if __name__ == '__main__':
    try_ping('5', 'www.google.com')
