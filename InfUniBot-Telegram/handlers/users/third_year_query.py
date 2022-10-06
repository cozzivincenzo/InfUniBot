import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.years_buttons import *
from keyboards.inline.third_year_buttons import *

from loader import dp, bot

@dp.callback_query_handler(text_contains="third_year_first_semester_callback")
async def first_semester_query(call: CallbackQuery):

    await call.message.edit_text(text="Ecco i corsi del primo semestre")
    await call.message.edit_reply_markup(reply_markup=third_year_first_semester_keyboard)
    

@dp.callback_query_handler(text_contains="third_year_second_semester_callback")
async def second_semester_query(call: CallbackQuery):

    
    tmp_keyboard = InlineKeyboardMarkup(row_width=1)

    back_button = InlineKeyboardButton(text="Indietro", callback_data="third_back_semester")
    tmp_keyboard.insert(back_button)
    
    await call.message.edit_text(
        text=
        "Non così in fretta, giovane padawan \U0001F480 \n"
        )

    
    await call.message.edit_reply_markup(reply_markup=tmp_keyboard)

    ### CODICE DA DECOMMENTARE ALL'INIZIO DEL SECONDO SEMESTRE ##

    '''
        await call.message.edit_text(text="Ecco i corsi del secondo semestre")
        await call.message.edit_reply_markup(reply_markup=third_year_second_semester_keyboard) 
    '''
    
@dp.callback_query_handler(text_contains="third_year_choose_callback")
async def choose_query(call: CallbackQuery):

    await call.message.edit_text(text="Ecco i corsi degli esami a scelta")
    await call.message.edit_reply_markup(reply_markup=third_year_choose_keyboard) 


'''@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.answer("Strunz, che mi chiami a fare se poi mi cancelli?", show_alert=True)

    await call.message.delete()
'''

@dp.callback_query_handler(text_contains="third_back_semester")
async def third_back_semester(call: CallbackQuery):

    await call.message.edit_text(text="Selezionare il semestre d'interesse")
    await call.message.edit_reply_markup(reply_markup=third_year_keyboard)

@dp.callback_query_handler(text_contains="back_years")
async def back_commands(call: CallbackQuery):

    await call.message.edit_text(text="Selezionare l'anno d'interesse")
    await call.message.edit_reply_markup(reply_markup=years)

    
