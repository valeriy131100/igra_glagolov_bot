import telegram
from google.cloud import dialogflow
from telegram import Update
from telegram.ext import (Updater,
                          CommandHandler,
                          CallbackContext,
                          MessageHandler,
                          Filters)
from environs import Env

import config
from dialogflow_workers import get_dialogflow_answer
from telegram_log_handler import TelegramBotLogHandler


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Здравствуйте!')


def handle_conversation(update: Update, context: CallbackContext):
    session_client = context.bot_data['dialogflow_sessions_client']

    dialogflow_answer = get_dialogflow_answer(
        text=update.message.text,
        session_client=session_client,
        session_id=update.message.chat_id
    )
    update.message.reply_text(
        dialogflow_answer.fulfillment_text
    )


if __name__ == '__main__':
    env = Env()
    env.read_env()
    updater = Updater(config.telegram_token)
    updater.dispatcher.logger.addHandler(
        TelegramBotLogHandler(
            telegram.Bot(config.telegram_token),
            config.telegram_logging_chat_id
        )
    )

    dispatcher = updater.dispatcher

    bot_data = dispatcher.bot_data
    bot_data['dialogflow_sessions_client'] = dialogflow.SessionsClient()

    dispatcher.add_handler(
        CommandHandler("start", start)
    )
    dispatcher.add_handler(
        MessageHandler(
            Filters.text & ~Filters.command,
            handle_conversation
        )
    )

    updater.start_polling()
    updater.idle()
