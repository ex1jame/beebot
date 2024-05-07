from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Далее", callback_data='info')]])

info = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Получить перечень документов", callback_data='docs')]])

docs = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Помощь со справками", callback_data='command_help')],
                                             [InlineKeyboardButton(text="Дальше",callback_data='command_next')]])

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
