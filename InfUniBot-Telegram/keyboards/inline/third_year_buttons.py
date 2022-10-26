from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URLS

# KEYBOARD INIZIALE 
third_year_keyboard = InlineKeyboardMarkup(row_width=2,)

third_year_first_semester = InlineKeyboardButton(text="1° Semestre", callback_data="third_year_first_semester_callback")
third_year_keyboard.insert(third_year_first_semester)

third_year_second_semester = InlineKeyboardButton(text="2° Semestre", callback_data="third_year_second_semester_callback")
third_year_keyboard.insert(third_year_second_semester)

third_year_choose = InlineKeyboardButton(text="Esami a scelta", callback_data="third_year_choose_callback")
third_year_keyboard.insert(third_year_choose)

third_year_choose = InlineKeyboardButton(text="Accompagnamento al lavoro", url=URLS['LAVORO'])
third_year_keyboard.insert(third_year_choose)

back_button = InlineKeyboardButton(text="Indietro", callback_data="back_years")
third_year_keyboard.insert(back_button)

# FINE KEYBOARD INIZIALE

# KEYBOARD DEL PRIMO SEMESTRE

third_year_first_semester_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        
        InlineKeyboardButton(text="PD \U0001F4BB", url=URLS['PD']), 
        InlineKeyboardButton(text="IS \U0001F522", url=URLS['IS'])
        
    ],
    [
        InlineKeyboardButton(text="Indietro", callback_data="third_back_semester"),
    ]
])

# FINE KEYBOARD DEL PRIMO SEMESTRE

# KEYBOARD DEL SECONDO SEMESTRE

third_year_second_semester_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="RO \U0001F4D0", url=URLS['POO']),
        InlineKeyboardButton(text="ETC \U0001F522", url=URLS['SO'])
    ],
    [
        InlineKeyboardButton(text="Indietro", callback_data="third_back_semester"),
    ]
])


# FINE KEYBOARD DEL SECONDO SEMESTRE
# KEYBOARD ESAMI A SCELTA

third_year_choose_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="PA \U0001F4BB", url=URLS['PRA']),
        InlineKeyboardButton(text="Fisica \U0001F522", url=URLS['Fisica']),
        InlineKeyboardButton(text="FIA \U0001F522", url=URLS['FIA'])
    ],
    [
        InlineKeyboardButton(text="Musimathics \U0001F522", url=URLS['MM']),
        InlineKeyboardButton(text="Mobile \U0001F522", url=URLS['MP'])
    ],
    [
        InlineKeyboardButton(text="Indietro", callback_data="third_back_semester"),
    ]
])

# FINE KEYBOARD ESAMI A SCELTA

