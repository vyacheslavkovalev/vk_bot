from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll
from settings import settings

try:
    vk_session = VkApi(token=settings.bot_token)
    vk = vk_session.get_api()
    group_id = vk.groups.getById()[0]['id']
    longpoll = VkBotLongPoll(vk_session, group_id)
except Exception as error:
    print(f'Ошибка авторизации - {error}. Проверьте BOT_TOKEN.')
