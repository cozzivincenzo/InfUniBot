from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URLS

md = InlineKeyboardMarkup(row_width=2,)

nicotera = InlineKeyboardButton(text="Nicotera", url=URLS["nicotera"])
md.insert(nicotera)

hub = InlineKeyboardButton(text="Hub", url=URLS["hubmd"])
md.insert(hub)

course = InlineKeyboardButton(text="Videolezioni", url=URLS["MD"] )
md.insert(course)

back_lenzi = InlineKeyboardButton(text="Indietro", callback_data="first_year_first_semester_callback")
md.insert(back_lenzi)