import html
import logging
from textwrap import dedent

import telegram

logger = logging.getLogger('telegram-log-handler-logger')


class TelegramBotLogHandler(logging.Handler):
    def __init__(self, bot: telegram.Bot, chat_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot
        self.chat_id = chat_id

    def emit(self, record):
        log_entry = html.escape(self.format(record))

        if record.levelno > logging.WARNING:
            start_text = 'Бот упал с ошибкой'
        else:
            start_text = 'Бот сообщает, что'

        try:
            self.bot.send_message(
                chat_id=self.chat_id,
                text=dedent(
                    f'''
                    {start_text}:
                    <pre>{log_entry}</pre>
                    '''
                ),
                parse_mode='HTML'
            )
        except Exception:
            logger.warning("Can't send log message to telegram chat")
            return

