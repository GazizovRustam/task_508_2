import pickle
def main():
    with open('USA.txt', 'r') as f:
        with open('capital.txt', 'r') as fc:

            desc = f.readlines()
            tmp = fc.readlines()
            ansi = {}
            my_list = []
            my_listTmp = []

            for n in desc:
                my_list.append(n.strip('\n'))

            for j in tmp:
                my_listTmp.append(j.strip('\n'))

            for ch in range(len(my_list)):
                ansi[my_list[ch]] = my_listTmp[ch]

            file = open('file.dat', 'wb')
            pickle.dump(ansi, file)

            


if __name__ == "__main__":
    main()