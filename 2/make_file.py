#! /usr/bin/env python
# charset: utf-8
"""
1 mb   = 1 000 000 bytes
100 mb = 100 000 000 bytes
"""

import os

MB = 403857600

def main():
    st = 'I like Python, it is my favorite language! '
    big_file = open('very_big.txt', 'a')
    folder_size = os.path.getsize(big_file.name)

    while folder_size <= MB:                              # 100 mb
        big_file.write(st)
        folder_size = os.path.getsize(big_file.name)

    big_file.close()

    print(str(folder_size) + ' bytes')

if __name__ == '__main__':
    main()