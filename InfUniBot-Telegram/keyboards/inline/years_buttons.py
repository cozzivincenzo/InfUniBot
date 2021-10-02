from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URLS

# KEYBOARD INIZIALE 
years = InlineKeyboardMarkup(row_width=2,)

first_year = InlineKeyboardButton(text="1° Anno", callback_data="first_year_callback")
years.insert(first_year)

second_year = InlineKeyboardButton(text="2° Anno", callback_data="second_year_callback")
years.insert(second_year)

back_button = InlineKeyboardButton(text="Indietro", callback_data="back_commands")
years.insert(back_button)
