from aiogram import Router, F, types
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Дорогой коллега, поздравляю тебя с прохождением всех "
                         "этапов собеседования! Сегодня начинается твой путь в компании,"
                         " а я  – твой помощник, меня зовут BeeBot  и  моя задача помочь "
                         "тебе адаптироваться в компании.", reply_markup=kb.main)


@router.callback_query(F.data == 'info')
async def get_info(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Итак, что же нам нужно сделать в ближайшее время:\n"
                                     "1. Получить перечень документов;\n"
                                     "2. Собрать пакет документов;\n"
                                     "3. Знать дату выхода на работу и место работы;\n"
                                     "4. Написать своему HR о готовности документов и предоставить их.",
                                     reply_markup=kb.info)


@router.callback_query(F.data == 'docs')
async def get_docs(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Список необходимых документов для проверки СБ:\n"
                                  "1.Справка 086;\n"
                                  "2.Справка от МВД о несудимости.\n"
                                  "3.Анкета кандидата (приклеить одно фото);\n"
                                  "5.Фото цветные, 2 шт., размер 3Х4 см;\n"
                                  "6.Копия паспорта;\n"
                                  "7.Копия военного билета (для мужчин);\n"
                                  "8. Номер Beeline\n"
                                  "9. Электронное фото для прокси карты\n"
                                  "Все документы надо отдать своему HR или отправить скан версии.",
                                  reply_markup=kb.docs)


@router.callback_query(F.data == 'help')
async def get_help(callback: CallbackQuery):
    await callback.answer()
    await callback.message.reply("С чем именно мне вам помочь?",reply_markup=kb.help)


@router.callback_query(F.data == 'instruction_one')
async def get_instruction_one(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Справку можно заказать через терминал или в гос.портале: portal.tunduk.kg \n"
                                  "После заявки справка выдается в течении от 1-3 дней по адресу:"
                                  "Курманжан Датка, 115. Тел. (0312) 369-417, (0312) 369-418")


@router.callback_query(F.data == 'instruction_two')
async def get_instruction_two(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Медицинскую справку можно получить в поликлинике по "
                                  "месту прописки или в любом платном медицинском")


@router.callback_query(F.data == 'instruction_third')
async def get_instruction_two(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Для получения справок необходимо подойти к единую регистратуру в "
                                  "Республиканском центре психиатрии и наркологии. Адрес: Байтик Баатыра, 1а."
                                  " Либо можно заказать в гос. портале: portal.tunduk.kg")