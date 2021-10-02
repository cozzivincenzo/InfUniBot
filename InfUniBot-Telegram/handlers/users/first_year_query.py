import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.years_buttons import *
from keyboards.inline.first_year_buttons import *
from keyboards.inline.md_buttons import *

from loader import dp, bot

@dp.callback_query_handler(text_contains="first_year_first_semester_callback")
async def first_semester_query(call: CallbackQuery):

    '''await call.answer(cache_time=60)

    callback_data = call.data

    logging.info(f"{callback_data=}")'''

    await call.message.edit_text(text="Ecco i corsi del primo semestre")
    await call.message.edit_reply_markup(reply_markup=first_year_first_semester_keyboard)


@dp.callback_query_handler(text_contains="first_year_second_semester_callback")
async def second_semester_query(call: CallbackQuery):

    await call.message.edit_text(text="Ecco i corsi del secondo semestre")
    await call.message.edit_reply_markup(reply_markup=first_year_second_semester_keyboard)


'''@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.answer("Strunz, che mi chiami a fare se poi mi cancelli?", show_alert=True)

    await call.message.delete()
'''

@dp.callback_query_handler(text_contains="back_semester")
async def back_semester(call: CallbackQuery):

    await call.message.edit_text(text="Selezionare il semestre d'interesse")
    await call.message.edit_reply_markup(reply_markup=first_year_keyboard)

@dp.callback_query_handler(text_contains="back_years")
async def back_commands(call: CallbackQuery):

    await call.message.edit_text(text="Selezionare l'anno d'interesse")
    await call.message.edit_reply_markup(reply_markup=years)

@dp.callback_query_handler(text_contains="MD")
async def md_query(call: CallbackQuery):

    await call.message.edit_text(text="Wow quanti link per MD eh? Mannaggia a Lenzi")
    await call.message.edit_reply_markup(reply_markup=md)
    
