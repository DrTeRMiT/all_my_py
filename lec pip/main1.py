from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands1 import *

updater = Updater('6104816242:AAFFwLZ024X69vdsFVX1lqy8yzFdG6Rd3j0')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))


print('server start')
updater.start_polling()
updater.idle()