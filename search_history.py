import os
from collections import deque


def search(lines, pattern, history=5):
    prev_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, prev_lines
        prev_lines.append(line)


def gen_sometextfile():
    lines = ['The core of extensible programming is defining functions. ',
             'Python allows mandatory and optional arguments, ',
             'keyword arguments, and even arbitrary argument lists. ',
             'Experienced programmers in any other language can pick up',
             'Python very quickly, and beginners find the clean syntax and ',
             'indentation structure easy to learn. ',
             'Whet your appetite with our Python 3 overview.']
    with open('sometextfile.txt', 'a') as f:
        for line in lines:
            f.write(line + '\n')


if __name__ == '__main__':
    gen_sometextfile()
    search_history = 3

    with open('sometextfile.txt') as f:
        for line, prev_lines in search(f, 'Python', search_history):
            for pline in prev_lines:
                print(pline, end='')
            print(line, end='')
            print('=' * 60)

    os.system('rm sometextfile.txt')
