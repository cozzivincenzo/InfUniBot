import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.courses_buttons import *
from keyboards.inline.commands_buttons import *
from keyboards.inline.md_buttons import *

from loader import dp, bot

@dp.message_handler(Command("corsi"))
async def show_courses(message: Message):


    await message.answer(text="Selezionare il semestre d'interesse",
                         reply_markup=courses)


@dp.callback_query_handler(text_contains="first_semester")
async def first_semester_query(call: CallbackQuery):

    '''await call.answer(cache_time=60)

    callback_data = call.data

    logging.info(f"{callback_data=}")'''

    await call.message.edit_text(text="Ecco i corsi del primo semestre")
    await call.message.edit_reply_markup(reply_markup=first_keyboard)


@dp.callback_query_handler(text_contains="second_semester")
async def second_semester_query(call: CallbackQuery):

    await call.message.edit_text(text="Ecco i corsi del secondo semestre")
    await call.message.edit_reply_markup(reply_markup=second_keyboard)


'''@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.answer("Strunz, che mi chiami a fare se poi mi cancelli?", show_alert=True)

    await call.message.delete()
'''

@dp.callback_query_handler(text_contains="back_semester")
async def back_semester(call: CallbackQuery):

    await call.message.edit_text(text="Selezionare il semestre d'interesse")
    await call.message.edit_reply_markup(reply_markup=courses)

@dp.callback_query_handler(text_contains="back_commands")
async def back_commands(call: CallbackQuery):

    await call.message.edit_text(text="  \U0001F5A5 LISTA COMANDI")
    await call.message.edit_reply_markup(reply_markup=commands)

@dp.callback_query_handler(text_contains="MD")
async def md_query(call: CallbackQuery):

    await call.message.edit_text(text="Wow quanti link per MD eh? Mannaggia a Lenzi")
    await call.message.edit_reply_markup(reply_markup=md)
    
