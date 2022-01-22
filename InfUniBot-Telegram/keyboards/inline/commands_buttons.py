from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URLS

# KEYBOARD INIZIALE 
commands = InlineKeyboardMarkup(row_width=2,)

years_button = InlineKeyboardButton(text="Corsi \U0001F4D6", callback_data="years")
commands.insert(years_button)

alerts_button = InlineKeyboardButton(text="Avvisi \U000026A0", url=URLS['alerts'])
commands.insert(alerts_button)

donation_button = InlineKeyboardButton(text="Donazioni \U0001F381", url=URLS['buymeacoffe'])
commands.insert(donation_button)

info_button = InlineKeyboardButton(text="Info \U0001f916", callback_data="info")
commands.insert(info_button)
