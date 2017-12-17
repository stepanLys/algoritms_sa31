import csv

FILENAME = 'db.csv'

def inputToDB():
    items = list()

    items.append(input('id:'))
    items.append(input('number:'))
    items.append(input('last_name:'))
    items.append(input('address:'))
    items.append(input('triger:'))
    items.append(input('arrears:'))

    print(items)

    with open(FILENAME, 'a', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(items)