# -*- coding: UTF-8
import parse_cvs
import input_csv

def main():
    parse_cvs.parse()
    input_csv.inputToDB()
    parse_cvs.search()


if __name__ == '__main__':
    main()
