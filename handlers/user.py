from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.keyboards import game_kb
from lexicon.lexicon import LEXICON_RU
from parser import baits_for_random_fish, baits_for_other, baits_for_small_fish, result, load_parsing_results

user_router = Router()

@user_router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU["/start"], reply_markup=game_kb)

@user_router.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU["/help"], reply_markup=game_kb)

#Хендлер срабатывает на любую из кнопок
@user_router.message(F.text.in_([LEXICON_RU["parse"], LEXICON_RU["other_fish"],
                                 LEXICON_RU["small_fish"], LEXICON_RU["sea_fish"]]))
async def process_parse_command(message: Message):
    if message.text == LEXICON_RU["parse"]:
        await message.answer(LEXICON_RU["wait_parsing"])
        result()
        await message.answer(LEXICON_RU["end_parsing"])
    elif message.text == LEXICON_RU["other_fish"]:
        results = baits_for_other(load_parsing_results())
        message_text = "\n".join([f"{item[0]} - {item[1]}" for item in results])
        await message.answer(message_text)
    elif message.text == LEXICON_RU["small_fish"]:
        results = baits_for_small_fish(load_parsing_results())
        message_text = "\n".join([f"{item[0]} - {item[1]}" for item in results])
        await message.answer(message_text)
    else:
        results = baits_for_random_fish((load_parsing_results()))
        message_text = "\n".join([f"{item[0]} - {item[1]}" for item in results])
        await message.answer(message_text)
