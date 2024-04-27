from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Далее",callback_data='info')]])

info = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Получить перечень документов",callback_data='docs')]])

docs = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Помощь со справками",callback_data='help')],
                                             [InlineKeyboardButton(text="Дальше",callback_data='step_one')]])


help = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Инструкция по получению справки о несудимости",callback_data='instruction_one')],
                                             [InlineKeyboardButton(text='Инструкция по получению справки формы 086',callback_data='instruction_two')],
                                             [InlineKeyboardButton(text='Инструкция по получению справки с нарко и психдиспансера', callback_data='instruction_third')]])

