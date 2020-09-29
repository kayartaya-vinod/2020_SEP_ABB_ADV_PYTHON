import shelve
from ex00 import Person


def main():
    with shelve.open('people') as db:
        # db['vinod@vinod.co'] = dict(name='Vinod', city='Bangalore', phone='9731424784')
        # db['shyam@xmpl.com'] = dict(name='Shyam', city='Bangalore')
        # db['john@xmpl.com'] = dict(name='John Smith', city='Dallas, Texas')
        # db['vinay@xmpl.com'] = Person(name='Vinay', city='Hassan', age=47)
        db['allen@example.com'] = Person(name='Allen', city='Washington', age=50)

    print('Data saved in people.db')


if __name__ == '__main__':
    main()
