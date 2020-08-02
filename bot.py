# timerbot
import logging
from telegram.ext import Updater, CommandHandler

#enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('Hi, use /set <seconds> to set timer')
    
def alarm(context):
    job = context.job
    context.bot.send_message(job.context, text='Beep')
    
def set_timer(update, context):
    chat_id = update.message.chat_id
    try:
        due = int(context.args[0])
        if due < 0:
            update.message.reply_text('Sorry, we can not go back to the future!')
            return
        
        if 'job' in context.chat_data:
            old_job = context.chat_data['job']
            old_job.schedule_removal()
        new_job = context.job_queue.run_once(alarm, due, context=chat_id)
        context.chat_data['job'] = new_job
        
        update.message.reply_text('Timer successfully set!')
        
    except(IndexError, ValueError):
        update.message.reply_text('Usage: /set <seconds>')
        
def unset(update, context):
    if 'job' not in context.chat_data:
        update.message.reply_text('U have no active timer')
        return
    job = context.chat_data['job']
    job.schedule_removal()
    del context.chat_data['job']
    
    update.message.reply_text('Timer successfully unset!')
    
def main():
    updater = Updater('1239064605:AAGND94K2INFwgN9WYVk2xRoDYsYaphlzC4', use_context=True)
    
    #get the dispatcher to register handlers 
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', start))
    dp.add_handler(CommandHandler('set', set_timer,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler('unset', unset, pass_chat_data=True))
    
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()