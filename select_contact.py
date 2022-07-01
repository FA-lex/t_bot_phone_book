import interface as inter

def select_contact(data):
    s = inter.select_contact()
    for i in data:
        if int(i[0]) == s: selected_contact = i
    inter.print_selected_contact(selected_contact)
    return selected_contact


if __name__ == '__main__':
    data = [['0', 'Иван', 'Иванов', '891234567879', 'работа'], ['3', 'Никита', 'Иванов', '891234567878', '']]
    select_contact(data)