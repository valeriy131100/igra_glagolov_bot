import random

import vk_api as vk
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

import config


def echo(event, vk_api):
    vk_api.messages.send(
        user_id=event.message.from_id,
        message=event.message.text,
        random_id=random.getrandbits(31) * random.choice([-1, 1])
    )


if __name__ == "__main__":
    vk_session = vk.VkApi(token=config.vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkBotLongPoll(vk_session, group_id=config.vk_group_id)
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW and event.from_user:
            echo(event, vk_api)
