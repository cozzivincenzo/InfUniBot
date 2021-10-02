from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URLS

# KEYBOARD INIZIALE 
second_year_keyboard = InlineKeyboardMarkup(row_width=2,)

second_year_first_semester = InlineKeyboardButton(text="1° Semestre", callback_data="second_year_first_semester_callback")
second_year_keyboard.insert(second_year_first_semester)

'''second_year_second_semester = InlineKeyboardButton(text="2° Semestre", callback_data="second_year_second_semester_callback")
second_year_keyboard.insert(second_year_second_semester)'''

back_button = InlineKeyboardButton(text="Indietro", callback_data="back_years")
second_year_keyboard.insert(back_button)

# FINE KEYBOARD INIZIALE

# KEYBOARD DEL PRIMO SEMESTRE

second_year_first_semester_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="POO \U0001F4D0", url=URLS['POO']),
        InlineKeyboardButton(text="BD \U0001F4BB", url=URLS['BD']), 
        InlineKeyboardButton(text="SO \U0001F522", url=URLS['SO'])
    ],
    [
        InlineKeyboardButton(text="Indietro", callback_data="back_semester"),
    ]
])

# FINE KEYBOARD DEL PRIMO SEMESTRE

# KEYBOARD DEL SECONDO SEMESTRE

second_year_second_semester_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="PSD \U0001F4BB", url=URLS['PSD']),
        InlineKeyboardButton(text="MMI \U0001F522", url=URLS['MMI']),
        InlineKeyboardButton(text="ANAL \U0001F4C9", url=URLS['ANAL'])
    ],
    [
        InlineKeyboardButton(text="Indietro", callback_data="back_semester"),
    ]
])

# FINE KEYBOARD DEL SECONDO SEMESTRE