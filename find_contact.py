from from_phonebook import phonebook as data


def find_contact(contact, area):
    result = []
    for i in data():
        if i[area].lower() == contact.lower():
            result.append(i)
    if not result: return -1
    return result


def exist_contact(contact):
    for i in data():
        if i[1:3] == contact[1:3]: return True
    return False




if __name__ == '__main__':
    print(find_contact('Иванов'))
    print(find_contact('Иван', 'имя'))