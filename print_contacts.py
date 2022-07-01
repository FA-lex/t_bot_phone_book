from from_phonebook import phonebook as ph

def print_contact(data = None):
    find_flug = False
    if data == None: 
        find_flug = True
        data = ph()
    if data == -1:
        print('-'*40)
        print('контакт не найден')
        print('-'*40)
        return data
    else:
        print('-'*40)
        for i in data:
            print('' if find_flug else i[0] , i[1], i[2], i[3], i[4])
        print('-'*40)



if __name__ == '__main__':
    print('-'*40)
    print_contact()
    print('-'*40)