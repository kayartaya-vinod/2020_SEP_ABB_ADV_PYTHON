import multiprocessing as mp
import os


def add_person(people, person):
    people.append(person)
    print(f'[{os.getpid()}] Added person data {person} to shared list')


def print_people(people):
    print(f'[{os.getpid()}] Here are the people data:')
    for p in people:
        print(f'Name={p["name"]}, City={p["city"]}')


def main():
    data = [
        {'name': 'Vinod', 'city': 'Bangalore'},
        {'name': 'Shyam', 'city': 'Shimoga'}
    ]
    new_person = dict(name='John', city='Dallas')

    with mp.Manager() as manager:
        shared_data = manager.list(data)
        p1 = mp.Process(target=add_person, args=(shared_data, new_person))
        p1.start()
        p1.join()

        print('-' * 50)

        p2 = mp.Process(target=print_people, args=(shared_data,))
        p2.start()
        p2.join()


if __name__ == '__main__':
    main()
