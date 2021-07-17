import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from loader import dp, bot



@dp.message_handler(commands=['info'])
async def show_commands(message: Message):


    await message.reply(
        "Ciao! Sono InfUniBot\n"
        "\nPer dubbi riguardo i canali contatta @KLS_01\n"
        "\nPer dubbi e/o segnalazioni di bug riguardanti il bot, contatta @Rcodi"
    )
