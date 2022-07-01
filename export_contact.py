from asyncore import write
import csv
import interface as inter

def export_contact_to_csv(contact):
    del contact[4]
    del contact[0]
    file = "take_contact.csv"
    with open(file, "w", encoding='utf-8') as data:
        writer = csv.writer(data)
        writer.writerow(contact)
    inter.print_export(contact, file)

def export_contact_to_txt(contact):
    del contact[4]
    del contact[0]
    file = "take_contact.txt"
    with open(file, "w", encoding='utf-8') as data:
        for i in contact:
            data.writelines(f'{i}\n')
    inter.print_export(contact, file)