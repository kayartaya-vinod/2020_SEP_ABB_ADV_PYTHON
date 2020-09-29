from ex00 import Person
import pickle


def main():
    lst = []
    lst.append(Person(name='Vinod', email='vinod@vinod.co', age=47))
    lst.append(Person(name='Shyam', email='shyam@xmpl.com', age=47))
    lst.append(Person(name='John', email='john@acme.com', age=55))

    with open('people.pkl', 'wb') as file:
        pickle.dump(lst, file)
    # print(pickle.dumps(lst))

    print('Data saved in file people.pkl')


if __name__ == '__main__':
    main()
