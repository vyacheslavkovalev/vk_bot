from dataclasses import dataclass
from vk_api.bot_longpoll import VkBotMessageEvent
from const import vk

@dataclass
class User:
    def __init__(self, event: VkBotMessageEvent):
        self.user_id: int = event.obj.message['from_id']
        self.first_name: str = vk.users.get(user_ids=(self.user_id))[0]['first_name']
        self.last_name: str  = vk.users.get(user_ids=(self.user_id))[0]['last_name']
