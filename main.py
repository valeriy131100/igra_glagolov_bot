from telegram import Update
from telegram.ext import (Updater,
                          CommandHandler,
                          CallbackContext,
                          MessageHandler,
                          Filters)
from environs import Env


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Здравствуйте!')


def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)


if __name__ == '__main__':
    env = Env()
    env.read_env()
    telegram_token = env.str('TELEGRAM_TOKEN')
    updater = Updater(telegram_token)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler("start", start)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.text & ~Filters.command, echo)
    )

    updater.start_polling()
    updater.idle()
