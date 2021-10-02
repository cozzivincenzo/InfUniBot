import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.first_year_buttons import *
from keyboards.inline.second_year_buttons import *
from keyboards.inline.commands_buttons import *

from loader import dp, bot

@dp.message_handler(Command("corsi"))
async def show_courses(message: Message):


    await message.answer(text="Selezionare l'anno d'interesse",
                         reply_markup=years)


@dp.callback_query_handler(text_contains="first_year_callback")
async def first_year_query(call: CallbackQuery):

    await call.message.edit_text(text="Selezionare il semestre d'interesse")
    await call.message.edit_reply_markup(reply_markup=first_year_keyboard)


@dp.callback_query_handler(text_contains="second_year_callback")
async def second_year_query(call: CallbackQuery):


    await call.message.edit_text(text="Selezionare il semestre d'interesse")
    await call.message.edit_reply_markup(reply_markup=second_year_keyboard)

'''@dp.callback_query_handler(text_contains="third_year")
async def third_year_query(call: CallbackQuery):


    await call.message.edit_text(text="Selezionare il semestre d'interesse")
    await call.message.edit_reply_markup(reply_markup=third_year)'''

@dp.callback_query_handler(text_contains="back_commands")
async def back_commands(call: CallbackQuery):

    await call.message.edit_text(text="  \U0001F5A5 LISTA COMANDI")
    await call.message.edit_reply_markup(reply_markup=commands)
    
