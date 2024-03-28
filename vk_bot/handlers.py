from pathlib import Path
from vk_api.bot_longpoll import VkBotEventType, VkBotMessageEvent
from vk_api.utils import get_random_id

from const import vk
from blanks import ButtonText, MessageText, cities
from model import User
from keyboards import keyboard_period
from db import Database


path_project = str(Path('__file__').absolute().parent)
path_data = f'{path_project}/data'

db = Database(f'{path_data}/my_database.db')


def handle_update(event):
    if isinstance(event, VkBotMessageEvent) and event.obj.peer_id == event.obj.from_id:
        try:
            attachments = event.object.message['attachments']
        except TypeError:
            attachments = []
        user = User(event)
        if not db.user_exists(user.user_id):
            db.add_user(user)
            if attachments!=[]:
                handle_error(user)
            else:
                handle_start(user)
                return
        message = event.obj.message['text'].strip().title()
        if (
                (
                event.type == VkBotEventType.MESSAGE_NEW
                or event.type == VkBotEventType.MESSAGE_REPLY
                )
                and attachments==[]
                and message in ButtonText.START
            ):
            handle_start(user)
        elif (
                (
                event.type == VkBotEventType.MESSAGE_NEW
                or event.type == VkBotEventType.MESSAGE_REPLY
                )
                and attachments==[]
                and message not in cities
            ):
            handle_not_found(user)
        else:
            handle_period(user.user_id, message)
    if event.type == VkBotEventType.MESSAGE_EVENT and event.obj.peer_id == event.obj.from_id:
        if event.obj.payload.get('type') in dir(ButtonText):
            pass # Необходимо обработать callback от кнопок


def handle_error(user: User):
    try:
        vk.messages.send(
                user_id=user.user_id,
                random_id=get_random_id(),
                message=MessageText.ERROR
            )
    except:
        print("Ошибка отправки сообщения у id " + str(user.user_id))


def handle_start(user: User):
    try:
        vk.messages.send(
             user_id=user.user_id,
             random_id=get_random_id(),
             message=MessageText(FIRST_NAME=user.first_name).start_text())
    except:
        print("Ошибка отправки сообщения у id " + str(user.user_id))

def handle_not_found(user: User):
    try:
        vk.messages.send(
                user_id=user.user_id,
                random_id=get_random_id(),
                message=MessageText.DEFAULT
            )
    except:
        print("Ошибка отправки сообщения у id " + str(user.user_id))

def handle_period(user_id: int, message: str):
    vk.messages.send(
                user_id=user_id,
                random_id=get_random_id(),
                keyboard=keyboard_period(),
                message=MessageText(CITY=message).period_text()
            )
