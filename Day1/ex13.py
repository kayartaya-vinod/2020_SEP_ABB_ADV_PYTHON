import pickle


def main():
    with open('people.pkl', 'rb') as file:
        data = pickle.load(file)
        for p in data:
            # print(p)
            p.print_info()


if __name__ == '__main__':
    main()
