from telegram.ext import Updater
from telegram.ext import CommandHandler


updater = Updater(token='1239064605:AAGND94K2INFwgN9WYVk2xRoDYsYaphlzC4', use_context=True) 
dispatcher = updater.dispatcher #handles the updates 


def start(update, context): 
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('start', start) #the commands handler should listen to 

dispatcher.add_handler(start_handler) # register a handler 

updater.start_polling()  #stars polling updates from trgm  
updater.idle() #stops the updater 