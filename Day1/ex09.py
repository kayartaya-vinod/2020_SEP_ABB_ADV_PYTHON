import json


def main():
    lst = []
    lst.append(dict(name='Vinod', email='vinod@vinod.co', city='Bangalore', married=True))
    lst.append(dict(name='Shyam', email='shyam@example.com', phones=['9876612893', '9282622123']))

    # print(lst)
    # strLst = json.dumps(lst)
    # print(strLst)
    with open('people.json', 'w') as f:
        json.dump(lst, f, indent=3)

    print('Data in JSON format written to file people.json')


def main():
    with open('iron-man-movies.json') as f:
        data = json.load(f)
        print(f'Total result = {data["totalResults"]}')

        for m in data["Search"]:
            print(m['Title'])


if __name__ == '__main__':
    main()
