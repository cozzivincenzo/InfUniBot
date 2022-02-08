  
import logging
import random

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.commands_buttons import *
from keyboards.inline.years_buttons import *
from loader import dp, bot
from config import file_animali, file_insulti



@dp.message_handler(commands=['bot'])
async def show_commands(message: Message):

    '''
    sendID = message.from_user
    await bot.send_message(chat_id=sendID['id'], text="  \U0001F5A5 LISTA COMANDI", reply_markup=commands)
    '''
    await message.reply(text="  \U0001F5A5 LISTA COMANDI", reply_markup=commands)


@dp.message_handler(commands=['test'])
async def show_commands(message: Message):

    await message.reply(text='Come hai scoperto questo comando? PARLA')

    '''await message.reply(
        "Ciao! Sono UniBot\n"
        "\nPer usarmi digita il comando /corsi e poi seleziona il semestre e il corso che ti interessa\n"
        "\nPer dubbi riguardo i canali contatta @KLS_01\n"
        "\nPer dubbi e/o segnalazioni di bug riguardanti il bot, contatta @Rcodi"
    )'''


@dp.callback_query_handler(text_contains="years")
async def years_query(call: CallbackQuery):

    '''await call.answer(cache_time=60)

    callback_data = call.data

    logging.info(f"{callback_data=}") '''

    await call.message.edit_text(text="Selezionare l'anno d'interesse")
    await call.message.edit_reply_markup(reply_markup=years)


@dp.message_handler(commands=['corsi'])
async def show_commands(message: Message):

    await message.reply(text="Selezionare l'anno d'interesse", reply_markup=years)


@dp.callback_query_handler(text_contains="info")
async def info_query(call: CallbackQuery):

    
    info = InlineKeyboardMarkup(row_width=1)

    back_button = InlineKeyboardButton(text="Indietro", callback_data="back_commands")
    info.insert(back_button)
    
    await call.message.edit_text(
        text=
        "Ciao! Sono InfUniBot\n"
        "\nPer dubbi riguardo i canali contatta @KLS_01\n"
        "\nPer dubbi e/o segnalazioni di bug riguardanti il bot, contatta @Rcodi"
        )

    
    await call.message.edit_reply_markup(reply_markup=info)

@dp.callback_query_handler(text_contains="back_commands")
async def back_commands(call: CallbackQuery):

    await call.message.edit_text(text="  \U0001F5A5 LISTA COMANDI")
    await call.message.edit_reply_markup(reply_markup=commands)

@dp.message_handler(commands=['bestemmia'])
async def show_commands(message: Message):

    animale = str(random.choice(open(file_animali).readlines()))
    animale = animale.strip("\n").lower()
    insulto = str(random.choice(open(file_insulti).readlines()))
    insulto = insulto.strip("\n").lower()
    bestemmia = 'Dio ' + animale + ' ' + insulto 

    await message.reply(text=bestemmia)

    '''await message.reply(
        "Ciao! Sono UniBot\n"
        "\nPer usarmi digita il comando /corsi e poi seleziona il semestre e il corso che ti interessa\n"
        "\nPer dubbi riguardo i canali contatta @KLS_01\n"
        "\nPer dubbi e/o segnalazioni di bug riguardanti il bot, contatta @Rcodi"
    )'''

