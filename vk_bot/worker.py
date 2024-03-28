from typing import List
import schedule
from vk_api.utils import get_random_id
from blanks import MessageText
from db import Database


def send_news(db: Database, vk):
    users_ids = db.get_ids()
    for id in users_ids:
        try:
            vk.messages.send(
                    user_id=id,
                    random_id=get_random_id(),
                    message=MessageText.TEST_MAIL
                )
        except:
            db.delete_user(id)
            print("Ошибка отправки сообщения у id " + str(id))


def newsletter(users_ids: List[int], vk):
    schedule.every().hour.at(':00').do(send_news, users_ids, vk)
    while True:
        schedule.run_pending()
