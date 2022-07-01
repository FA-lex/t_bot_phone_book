import csv
import from_phonebook 
from interface import print_report_delete_contact as report

def del_contact(id):
    phonebook = from_phonebook.phonebook()
    with open("phonebook.csv", "w", encoding='utf-8') as file:
        writer = csv.writer(file)
        for element in phonebook:
            if element != id: writer.writerow(element)
    report(id)



if __name__ == '__main__':
    del_contact(['3', 'Иван', 'Петров', '891234567877', ''])
    print(from_phonebook.phonebook())
