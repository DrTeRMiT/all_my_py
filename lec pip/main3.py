from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *




app = ApplicationBuilder().token('6104816242:AAFFwLZ024X69vdsFVX1lqy8yzFdG6Rd3j0').build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
print("server start") 
app.run_polling()