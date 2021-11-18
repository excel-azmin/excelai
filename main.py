from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from telegram import Update



def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def bop(update: Update, context: CallbackContext):
    print(update)
    url = get_url()
    # chat_id = update.message.chat_id
    update.message.reply_photo(photo=url)



def greet_user(update: Update, context: CallbackContext):
    update.message.reply_text('hello')


def hi(update : Update, context: CallbackContext):
    update.message.reply_text("Hello! How are your? ")


def main():
    updater = Updater('2119152360:AAHhm_J6DE_zzwLtsECipsIoFi8A7l2CwSQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    dp.add_handler(CommandHandler('hi', hi))
    dp.add_handler(CommandHandler('start', greet_user))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
