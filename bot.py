from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent



def start(update, context): 
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def echo(update, context): 
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
    
def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)
    
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Sorry, I didn\'t understand that command')

updater = Updater(token='1239064605:AAGND94K2INFwgN9WYVk2xRoDYsYaphlzC4', use_context=True) 
dispatcher = updater.dispatcher #handles the updates 
    
start_handler = CommandHandler('start', start) #the commands handler should listen to 
dispatcher.add_handler(start_handler) # register a start_handler 

caps_handler = CommandHandler('caps', caps) 
dispatcher.add_handler(caps_handler) #add CAPS-func

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo) #any text, but commands
dispatcher.add_handler(echo_handler) #register ecgo_handler 

inline_caps_handler = InlineQueryHandler(inline_caps) #inline mod handler
dispatcher.add_handler(inline_caps_handler)

unknown_handler = MessageHandler(Filters.command, unknown) #unknown commands
dispatcher.add_handler(unknown_handler)

updater.start_polling()  #stars polling updates from trgm  
updater.idle() #stops the updater

