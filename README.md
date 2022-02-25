# igra-glagolov-bot

[Telegram](https://telegram.org) и [Vk](https://vk.com)-боты на основе [DialogFlow](https://dialogflow.cloud.google.com) для автоматической поддержки пользователей Игра Глаголов.

[Пример vk-бота](https://vk.me/public210891605). [Пример telegram-бота](https://t.me/IgraGlagolovBot).

[![ezgif-2-5c2b124a81.gif](https://i.postimg.cc/6pMVWwCr/ezgif-2-5c2b124a81.gif)](https://postimg.cc/rDtRjBns)

## Установка
Вам понадобится установленный Python 3.6+ и git.

Склонируйте репозиторий:
```bash
$ git clone https://github.com/valeriy131100/igra_glagolov_bot
```

Создайте в этой папке виртуальное окружение:
```bash
$ cd igra_glagolov_bot
$ python3 -m venv venv
```

Активируйте виртуальное окружение и установите зависимости:
```bash
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Использование

### Переменные среды
Заполните файл .env.example и переименуйте его в .env или иным образом задайте переменные среды:
* TELEGRAM_TOKEN - токен бота Telegram. Можно получить у [@BotFather](https://t.me/BotFather).
* TELEGRAM_LOGGING_CHAT_ID - id чата телеграм, куда боты будут присылать логи в случае ошибок. Можно узнать у бота [@userinfobot](https://t.me/userinfobot).
* VK_TOKEN - токен от группы Вконтакте. Создайте группу [Вконтакте](https://vk.com), затем перейдите в настройки группы и в разделе Сообщения включите сообщения сообщества, а также в подразделе настройки ботов включите Возможности ботов. Далее перейдите в раздел Настройки - Работа с API, включите Longpoll, а также события для сообщений в лонгполле. Желательно указать версию API 5.131. Далее создайте ключ доступа и укажите галочку доступа к сообщениям.
* VK_GROUP_ID - id созданной группы Вконтакте. Можно узнать [здесь](https://regvk.com/id/).
* GOOGLE_APPLICATION_CREDENTIALS - путь до json-токена с аккаунтом приложения Google Cloud. Создайте приложение Google Cloud по [инструкции](https://cloud.google.com/dialogflow/es/docs/quick/setup). Далее на сайте [DialogFlow](https://dialogflow.cloud.google.com) создайте агента указав созданное ранее приложение Google Cloud. Далее по [инструкции](https://cloud.google.com/docs/authentication/getting-started) создайте сервисный аккаунт с правами Owner и получите его json-токен.

### Тренировка агента DialogFlow с помощью json-файла с заготовленными фразами
Вы можете загрузить заранее подготовленные фразы для бота в агент с помощью скрипта:
```bash
$ venv/bin/python load_intents.py [путь до json-файла]
```

<details>
<summary>Пример json-файла</summary>

```json
{
    "Устройство на работу": {
        "questions": [
            "Как устроиться к вам на работу?",
            "Как устроиться к вам?",
            "Как работать у вас?",
            "Хочу работать у вас",
            "Возможно-ли устроиться к вам?",
            "Можно-ли мне поработать у вас?",
            "Хочу работать редактором у вас"
        ],
        "answer": "Если вы хотите устроиться к нам, напишите на почту game-of-verbs@gmail.com мини-эссе о себе и прикрепите ваше портфолио."
    },
    "Забыл пароль": {
        "questions": [
            "Не помню пароль",
            "Не могу войти",
            "Проблемы со входом",
            "Забыл пароль",
            "Забыл логин",
            "Восстановить пароль",
            "Как восстановить пароль",
            "Неправильный логин или пароль",
            "Ошибка входа",
            "Не могу войти в аккаунт"
        ],
        "answer": "Если вы не можете войти на сайт, воспользуйтесь кнопкой «Забыли пароль?» под формой входа. Вам на почту прийдёт письмо с дальнейшими инструкциями. Проверьте папку «Спам», иногда письма попадают в неё."
    }
}
```

</details>

### Запуск vk-бота
Находясь в директории igra_glagolov_bot исполните:
```bash
$ venv/bin/python vk_bot.py
```

### Запуск telegram-бота
Находясь в директории igra_glagolov_bot исполните:
```bash
$ venv/bin/python telegram_bot.py
```

### Деплой на [Heroku](https://heroku.com/)

1. Зарегистрируйтесь и создайте приложение Heroku.
2. Соедините аккаунт Heroku и GitHub и выберите этот репозиторий.
3. Добавьте [этот](https://github.com/gerywahyunugraha/heroku-google-application-credentials-buildpack) билдпак.
4. Перейдите в раздел `Settings - Config Vars` и задайте те же переменные среды, что и для запуска локально, за исключением GOOGLE_APPLICATION_CREDENTIALS.
5. Переменную среды GOOGLE_APPLICATION_CREDENTIALS задайте по [инструкции](https://github.com/gerywahyunugraha/heroku-google-application-credentials-buildpack#usage).
6. Вернитесь к разделу `Deploy`, пролистните до самого конца и нажмите на кнопку `Deploy Branch`.
7. Перейдите в раздел `Resources` и запустите dyno для `vk-bot` и `telegram-bot`.
