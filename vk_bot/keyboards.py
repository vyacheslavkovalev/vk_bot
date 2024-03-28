from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from blanks import ButtonText


def keyboard_period():
    keyboard = VkKeyboard(inline=True)
    keyboard.add_callback_button(
        label=ButtonText.DAY,
        color=VkKeyboardColor.SECONDARY,
        payload={'type': 'DAY'}
    )
    keyboard.add_line()
    keyboard.add_callback_button(
        label=ButtonText.WEEK,
        color=VkKeyboardColor.SECONDARY,
        payload={'type': 'WEEK'}
    )
    keyboard.add_line()
    keyboard.add_callback_button(
        label=ButtonText.MONTH,
        color=VkKeyboardColor.SECONDARY,
        payload={'type': 'MONTH'}
    )
    return keyboard.get_keyboard()
