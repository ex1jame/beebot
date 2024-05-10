from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Далее", callback_data='info')]])

info = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Получить перечень документов", callback_data='docs')]])

docs = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Помощь со справками", callback_data='command_help')],
                     [InlineKeyboardButton(text="Дальше", callback_data='command_next')]])

help = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Инструкция по получению справки о несудимости", callback_data='instruction_one')],
    [InlineKeyboardButton(text='Инструкция по получению справки формы 086', callback_data='instruction_two')],
    [InlineKeyboardButton(text='Инструкция по получению справки с нарко и психдиспансера',
                          callback_data='instruction_third')]])

step_one = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Дальше")]],
                               resize_keyboard=True,
                               input_field_placeholder="Нажмите дальше для работы с BeeBot")

yes_or_no = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Да", callback_data='yes_docs')],
                                                  [InlineKeyboardButton(text="Нет", callback_data='no_docs')]])

delete_keybord = ReplyKeyboardRemove()

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ивенты"), KeyboardButton(text="Офисы")],
        [KeyboardButton(text="Плюшки"), KeyboardButton(text="Увлечения")],
        [KeyboardButton(text="Библиотека"), KeyboardButton(text="Bbox")],
        [KeyboardButton(text="Этикет")],
    ],
    row_width=2,
    input_field_placeholder="Приятной смерти"
)

ivents = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Family Day", callback_data='family_day')],
                                               [InlineKeyboardButton(text="День Влюбленных",callback_data='love_day')],
                                               [InlineKeyboardButton(text="BeeStyle",callback_data='beestyle_day')]])
