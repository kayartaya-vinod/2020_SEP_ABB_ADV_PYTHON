import json


def main():
    lst = []
    lst.append(dict(name='Vinod', email='vinod@vinod.co', city='Bangalore', married=True))
    lst.append(dict(name='Shyam', email='shyam@example.com', phones=['9876612893', '9282622123']))

    vinay_phones = {'928272622', '287273636'}  # set is not json serializable; convert it to list or tuple
    lst.append(dict(name='Vinay', emails=('vinay@xmpl.com', ), phones=list(vinay_phones)))

    # print(lst)
    # strLst = json.dumps(lst)
    # print(strLst)
    with open('people.json', 'w') as f:
        json.dump(lst, f, indent=3)

    print('Data in JSON format written to file people.json')


def main_():
    with open('iron-man-movies.json') as f:
        data = json.load(f)
        print(f'Total result = {data["totalResults"]}')

        for m in data["Search"]:
            print(m['Title'])


if __name__ == '__main__':
    main()
