
def main_menu():
    print('-'*40)
    print('Выберите команду:\n1-вывести телефонную книгу в терминал\n2-найти контакт\n3-создать новый контакт\nлюбая другая - выход из программы')
    print('-'*40)
    try:
        result_request = int(input())
    except:
        return exit()
    return result_request


def get_find():
    try:
        param = int(input('По какому параметру будем искать? 1-имя, 2-фамилия или 3-номер\nлюбая другая - в главное меню\n_'))
    except:
        return False
    value = input('Что будем искать? \n_')
    return (value, param)

def action_contact():
    print('1 - изменить контакт\n2 - удалить контакт\n3 - поделиться контактом\n0 - выйти в главное меню\nлюбая другая - выход из программы')
    print('Выберите дальнейшее действие с контактом: ')
    try:
        result_request = int(input())
    except:
        return exit()
    return result_request if 0 <= result_request <= 3 else exit()

def select_contact():
    return int(input('выберите контакт:'))

def print_selected_contact(selected_contact):
    print(f'выбран контакт: {selected_contact[1]}, {selected_contact[2]}, {selected_contact[3]}, {selected_contact[4]}\n'+'-'*40)

def print_report_delete_contact(contact):
    print(f'контакт: {contact[1]}, {contact[2]}, {contact[3]}, {contact[4]}: удален\n'+'-'*40)

def print_report_change_contact(contact):
    print(f'контакт изменен на: {contact[1]}, {contact[2]}, {contact[3]}, {contact[4]}\n'+'-'*40)

def print_report_new_contact(contact):
    print(f'создан контакт: {contact[1]}, {contact[2]}, {contact[3]}, {contact[4]}\n'+'-'*40)

def print_export(contact, file):
    print(f'контакт: {contact[0]}, {contact[1]}, {contact[2]} передан в файл: {file} \n'+'-'*40)

def get_change():
    print('выберите что надо изменить:\n1-имя\n2-фамилию\n3-телефон\n4-коментарий\n0-отмена')
    flag = False
    while not flag:
        try:
            area = int(input())
        except:
            print('введите цифру от 1 до 4')
        if 0 < area <= 4: flag = True
    changed_area =input('введите новые данные: ')
    return (area, changed_area)


def get_new_contact():
    print('-'*40)
    first_name = input('введите имя:')
    last_name = input('введите фамилию:')
    phone = input('введите телефон:')
    cometary = input('введите коментарий:')
    print('-'*40)
    return ['', first_name, last_name, phone, cometary]


def get_type_file():
    print('в каком из форматов будем экспортировать контакт? 1-.csv 2-.txt, что-нибудь другое-отмена')
    try:
        type = int(input())
        return type if 0 < type <= 2 else type/0
    except:
        print('введите цифру 1 или 2')


def create_dubl():
    try:
        dubl = int(input('Такой контакт уже есть. Хотите сделать дубликат? 1-да, что-нибудь другое-отмена'))
        return True if dubl == 1 else dubl/0
    except:
        print('Вы отменили создание контакта')
        return False
    
    
   

if __name__ == '__main__':
    print(main_menu())
    print(get_find())
    print(action_contact())