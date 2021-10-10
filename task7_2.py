import helpers_1
from dictionary import MESSAGES

print(MESSAGES["Commands"])
filename = 'phonebook.txt';
FRIENDS = helpers_1.get_phonebook(filename)

while True:
    to_do = input("Выбери действие: ")
    to_do_upper = to_do.upper()
    if to_do_upper == "ADD":
        name = input("Напиши имя твоей подруги: ")
        if name == "":
            print(MESSAGES["ForgotToEnterName"] + "\n")
            continue
        name = name.capitalize()
        if name in FRIENDS.keys():
            print(MESSAGES["AlreadyInThePhonebook"] + "\n")
        else:
            number = input("Добавь номер ее телефона: ")
            if number == "":
                print(MESSAGES["ForgotToEnterNumber"] + "\n")
                continue
            try:
                number = int(number)
                print(helpers_1.add_friend(FRIENDS, MESSAGES, filename, name, number))
            except ValueError:
                print(MESSAGES["OnlyNumbers"] + "\n")
                continue

        print(MESSAGES["Commands"])

    elif to_do_upper == "SEARCH":
        name = input("Чей номер ты хочешь найти?: ")
        if name == "":
            print(MESSAGES["ForgotToEnterName"] + "\n")
            continue
        name = name.capitalize()
        if FRIENDS == {}:
            print(MESSAGES["PhonebookIsEmpty"] + "\n")
        elif name not in FRIENDS.keys():
            print(MESSAGES["NoResult"] + "\n")
        else:
            print(helpers_1.search_friend(FRIENDS, name))
        print(MESSAGES["Commands"])

    elif to_do == "EXIT":
        print(MESSAGES["Bye"] + "\n")
        break

    else:
        print(MESSAGES["InvalidInput"] + "\n")
        print(MESSAGES["Commands"])