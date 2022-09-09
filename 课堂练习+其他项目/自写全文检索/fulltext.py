import os

dict = {}
URL = r"D:\A_thing\grade_two_study\python\threeCountry.txt"


def check():
    file = open(URL, encoding="UTF-8")
    lines = file.readlines()
    num_of_line = 1
    for line in lines:
        length = len(line)
        index = 0
        while index < length - 1:
            p = index + 1
            while line[index:p] in dict and p <= length:
                if line[index] == ' ':
                    break
                if p - index >= 2:
                    word = line[index:p]
                    dict[word] = dict[word] + ';' + 'in line of ' + str(num_of_line) + " and index = " + str(index)
                p = p + 1
            word = line[index:p]
            if word != " ":
                dict[word] = 'in line of ' + str(num_of_line) + " and index = " + str(index)
            index = index + 1
        num_of_line = num_of_line + 1


def start():
    check()

    print("total words: ", len(dict))

    # query
    while True:
        print("query: ", end="")
        word = input()
        if word in dict:
            for wh in dict[word].split(";"): # [:20]:  # 仅显示20个位置
                print("\t", wh)
            print("一共出现了" + str(len(dict[word].split(";"))) + "次")
        elif word == 'q':
            print("exit.")
            break
        else:
            print("none hit")


if __name__ == "__main__":
    start()
