import csv
import from_phonebook 
from interface import print_report_new_contact as report

def create_contact(contact):
    phonebook = from_phonebook.phonebook()
    with open("phonebook.csv", "a", encoding='utf-8') as file:
        writer = csv.writer(file)
        for element in phonebook:
            id = int(element[0])+1
        contact[0] = id    
        writer.writerow(contact)
    report(contact)



if __name__ == '__main__':
    create_contact(['', 'Иван', 'Петров', '891234567877', ''])
    print(from_phonebook.phonebook())

# def create():
#     print('здесь модуль new_contact должен создавать новый контакт через запрос из интерфейса данных о контакте')