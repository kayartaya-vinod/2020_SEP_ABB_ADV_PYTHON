import shelve


def main():
    email = input('Enter email to search: ')
    with shelve.open('people') as db:
        if email in db:
            print(f'Data = {db[email]}')
        else:
            print(f'No data found for email {email}')


if __name__ == '__main__':
    main()
