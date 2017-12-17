import csv

FILENAME = 'db.csv'


def openf(FILENAME, format):
    with open(FILENAME, format, newline="") as file:
        reader = list(csv.reader(file))
    return reader

reader = openf(FILENAME, 'r')

def sortDB(n, t):
    if n == 1: n = 0
    elif n == 2: n = 2
    reader.sort(key=lambda i: i[n], reverse=t)

def parse():
    for i in range(len(reader)):
        reader[i][0] = int(reader[i][0])

    n = int(input('Sort by id (1), name (2): '))
    t = int(input('Ascending (0), decreasing (1): '))

    sortDB(n, t)
    # print(type(reader))

    print('\tid\t\tnumber\t\tlast_name\t\taddress\t\ttriger\t\tarrears')
    for i in reader:
        print('\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}'.format(i[0], i[1], i[2], i[3], i[4], i[5]))

def search():
    sortDB(2, 0)

    word = input('Input name: ').lower()

    for i in range(len(reader)):
        if word in reader[i][2].lower():
            print(reader[i])