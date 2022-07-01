import csv
import from_phonebook 
from interface import print_report_change_contact as report
from interface import get_change as changed_info


def change_contact(data):
    phonebook = from_phonebook.phonebook()
    changed = changed_info()
    contact = data
    with open("phonebook.csv", "w", encoding='utf-8') as file:
        writer = csv.writer(file)
        for element in phonebook:
            if element == contact:
                contact[changed[0]] = changed[1]
                element = contact
            writer.writerow(element)
    report(contact)



if __name__ == '__main__':
    change_contact(['3', 'Иван', 'Петров', '891234567877', ''])
    # changed_info[0] = 3
    # changed_info[1] = 'Иванушка'

    print(from_phonebook.phonebook())
