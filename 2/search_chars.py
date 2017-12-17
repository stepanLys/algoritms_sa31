#! /usr/bin/env python
# charset: utf-8

import os

MB = 104857600

def wordIndex(s, n):
    string = ' '.join(str(x) for x in s[:n-1])
    length = len(string)

    return ('In this string - \t ' + string + ' \t\n ' + str(length) + ' chars')

def main():
    f = open('big.txt', 'r')
    file = f.read().split(' ')
    index = int(input('Please, input word index: '))

    file_size = os.path.getsize(f.name)
    # print(file_size, MB)

    if file_size <= MB and index <= len(file) and index > 0 and len(file) > 0:
        print(wordIndex(file, index))
    else:
        print('Error!!!')

    f.close()

if __name__ == '__main__':
    main()