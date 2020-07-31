from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters


updater = Updater(token='1239064605:AAGND94K2INFwgN9WYVk2xRoDYsYaphlzC4', use_context=True) 
dispatcher = updater.dispatcher #handles the updates 


def start(update, context): 
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start) #the commands handler should listen to 

dispatcher.add_handler(start_handler) # register a start_handler 

def echo(update, context): 
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo) #any text, but commands
dispatcher.add_handler(echo_handler) #register ecgo_handler 

updater.start_polling()  #stars polling updates from trgm  
updater.idle() #stops the updater
    