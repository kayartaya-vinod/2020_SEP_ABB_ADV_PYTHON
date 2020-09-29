import marshal


def write_data():
    lst = []
    lst.append(dict(name='Vinod', email='vinod@vinod.co', age=47))
    lst.append(dict(name='Shyam', email='shyam@xmpl.com', age=47))
    lst.append(dict(name='John', email='john@acme.com', age=55))

    with open('people.backup', 'wb') as file:
        marshal.dump(lst, file)

    print('Data saved in file people.backup')


def read_data():
    with open('people.backup', 'rb') as file:
        data = marshal.load(file)
        for p in data:
            print(p)


if __name__ == '__main__':
    # write_data()
    read_data()
