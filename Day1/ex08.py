import csv


def main():
    with open('./employees.csv', 'r+') as f:
        reader = csv.reader(f, quotechar='"')
        for row in reader:
            print(row)

        writer = csv.writer(f)
        # writer.writerow([4, 'Vinay Kumar', 2999, 'Bangalore, India'])
        writer.writerows([
            [5, 'Kiran', 4000, 'Vasco, Goa'],
            [6, 'Kishore', 4000, 'Vasco, Goa']
        ])


if __name__ == '__main__':
    main()
