def main():
    # f = open('names.txt')
    # content = f.read()
    # content = f.readlines()

    # while True:
    #     content = f.readline()
    #     if len(content) == 0:
    #         break
    #
    #     print(content, end='')

    # f.close()

    with open('names.txt') as f:
        for line in f:
            print(line, end='')


if __name__ == '__main__':
    main()
