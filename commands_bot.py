# from telegram import Update, Bot
import interface as inter
import print_contacts as contacts
import find_contact as f
import action_contact as action
import new_contact


def start(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Вас приветствует телефонный справочник\n\
        /info - ")
    else:
        context.bot.send_message(update.effective_chat.id, f"{' '.join(arg)}")


def info(update, context):
    context.bot.send_message(update.effective_chat.id, "Телефонный спрвочник\nPhonebook-v1.0")

def main_menu():
    print('-'*40)
    print('Выберите команду:\n1-вывести телефонную книгу в терминал\n2-найти контакт\n3-создать новый контакт\nлюбая другая - выход из программы')
    print('-'*40)
    try:
        result_request = int(input())
    except:
        return exit()
    return result_request

def message(update, context):
    text = update.message.text
    if text.lower() == 'привет':
        context.bot.send_message(update.effective_chat.id, 'И тебе привет..')
    else:
        context.bot.send_message(update.effective_chat.id, 'я тебя не понимаю')


def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, 'Ты несешь какую-то дичь...')