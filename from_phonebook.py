import csv

def phonebook():
    phonebook = []
    with open("phonebook.csv", encoding = 'utf-8') as file:
        reader = csv.reader(file)
        for id in reader:
            phonebook.append(id)
    return phonebook

if __name__ == '__main__':
    print(phonebook())