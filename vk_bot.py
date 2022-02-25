import random

import vk_api as vk
from google.cloud.dialogflow import SessionsClient
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

import config
from dialogflow_workers import get_dialogflow_answer


if __name__ == "__main__":
    vk_session = vk.VkApi(token=config.vk_token, api_version='5.131')
    vk_api = vk_session.get_api()
    longpoll = VkBotLongPoll(vk_session, group_id=config.vk_group_id)
    session_client = SessionsClient()

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW and event.from_user:
            project_id = config.dialogflow_project_id
            dialogflow_answer = get_dialogflow_answer(
                    text=event.message.text,
                    session_client=session_client,
                    session_id=event.message.from_id
            )
            if dialogflow_answer:
                vk_api.messages.send(
                    user_id=event.message.from_id,
                    message=dialogflow_answer,
                    random_id=random.getrandbits(31) * random.choice([-1, 1])
                )
