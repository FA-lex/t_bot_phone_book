from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from token_bot import token as my_token
from commands_bot import *

bot = Bot(token=my_token)
updater = Updater(token=my_token, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)
message_handler = MessageHandler(Filters.text, message)
unknown_handler = MessageHandler(Filters.command, unknown) #/game

dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(message_handler)
dispatcher.add_handler(unknown_handler)

print("server_started")

updater.start_polling()
updater.idle()
