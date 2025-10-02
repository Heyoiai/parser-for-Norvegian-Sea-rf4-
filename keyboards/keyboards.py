from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from lexicon.lexicon import LEXICON_RU

button_1 = KeyboardButton(text=LEXICON_RU['parse'])
button_2 = KeyboardButton(text=LEXICON_RU['other_fish'])
button_3 = KeyboardButton(text=LEXICON_RU['small_fish'])
button_4 = KeyboardButton(text=LEXICON_RU['sea_fish'])

game_kb = ReplyKeyboardMarkup(
    keyboard=[[button_1], [button_2], [button_3], [button_4]], resize_keyboard=True
)