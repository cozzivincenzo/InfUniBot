from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URLS

# KEYBOARD INIZIALE 
first_year_keyboard = InlineKeyboardMarkup(row_width=2,)

first_year_first_semester = InlineKeyboardButton(text="1° Semestre", callback_data="first_year_first_semester_callback")
first_year_keyboard.insert(first_year_first_semester)

first_year_second_semester = InlineKeyboardButton(text="2° Semestre", callback_data="first_year_second_semester_callback")
first_year_keyboard.insert(first_year_second_semester)

back_button = InlineKeyboardButton(text="Indietro", callback_data="back_years")
first_year_keyboard.insert(back_button)

# FINE KEYBOARD INIZIALE

# KEYBOARD DEL PRIMO SEMESTRE

first_year_first_semester_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="ADE \U0001F4D0", url=URLS['ADE']),
        InlineKeyboardButton(text="PR1 \U0001F4BB", url=URLS['PR1']), #\U0001F4BB
        InlineKeyboardButton(text="MD \U0001F522", callback_data="MD")
    ],
    [
        InlineKeyboardButton(text="OFA \U0000270D", url=URLS['OFA']),
    ],
    [
        InlineKeyboardButton(text="Indietro", callback_data="first_back_semester"),
    ]
])

# FINE KEYBOARD DEL PRIMO SEMESTRE

# KEYBOARD DEL SECONDO SEMESTRE

first_year_second_semester_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="PSD \U0001F4BB", url=URLS['PSD']),
        InlineKeyboardButton(text="MMI \U0001F522", url=URLS['MMI']),
        InlineKeyboardButton(text="ANAL \U0001F4C9", url=URLS['ANAL'])
    ],
    [
        InlineKeyboardButton(text="Indietro", callback_data="first_back_semester"),
    ]
])

# FINE KEYBOARD DEL SECONDO SEMESTRE