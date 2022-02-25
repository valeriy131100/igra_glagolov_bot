import json

from google.cloud import dialogflow
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
    session_client = context.bot_data['dialogflow_session_client']
    project_id = context.bot_data['dialogflow_project_id']

    session = session_client.session_path(project_id, update.message.chat_id)

    text_input = dialogflow.TextInput(
        text=update.message.text,
        language_code='ru-RU'
    )

    query_input = dialogflow.QueryInput(
        text=text_input
    )

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    update.message.reply_text(
        response.query_result.fulfillment_text
    )


if __name__ == '__main__':
    env = Env()
    env.read_env()
    telegram_token = env.str('TELEGRAM_TOKEN')
    updater = Updater(telegram_token)

    dispatcher = updater.dispatcher

    bot_data = dispatcher.bot_data
    bot_data['dialogflow_session_client'] = dialogflow.SessionsClient()

    google_credentials_path = env.str('GOOGLE_APPLICATION_CREDENTIALS')

    with open(google_credentials_path, 'r') as credentials_file:
        credentials = json.load(credentials_file)
        bot_data['dialogflow_project_id'] = credentials['project_id']

    dispatcher.add_handler(
        CommandHandler("start", start)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.text & ~Filters.command, echo)
    )

    updater.start_polling()
    updater.idle()
