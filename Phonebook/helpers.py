def add_friend(friends, messages, filename, name, number):
    new_name = {name: number}
    friends.update(new_name)
    with open(filename, 'a') as f:
        f.write(f"{name} {number}\n")
    return messages["SuccessfulEntry"] + "\n"


def search_friend(friends, name):
    return f"=== {friends[name]} ===" + "\n"


def get_phonebook(filename):
    with open(filename, 'r') as p:
        phonebookList = p.readlines()
        PHONEBOOKDICT = {}
        for contact in phonebookList:
            contact = contact.replace("\n", "")
            result = contact.split()
            key = result[0]
            value = result[1]
            CONTACT1 = {key: value}
            PHONEBOOKDICT.update(CONTACT1)
    return(PHONEBOOKDICT)