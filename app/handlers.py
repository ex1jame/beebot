import asyncio

from aiogram import Router, F

from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb
from app.utils.states import states_texts, ConfirmationState, add_states_texts, send_message_after_delay

router = Router()


@router.message(F.photo)
async def get_photo(message: Message, state: FSMContext):
    await message.answer(f"id{message.photo[-1].file_id}")


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


@router.callback_query(F.data == 'command_help')
async def get_help(callback: CallbackQuery):
    await callback.answer()
    await callback.message.reply("С чем именно мне вам помочь?", reply_markup=kb.help)


@router.callback_query(F.data == 'command_next')
async def next_step(callback: CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await callback.answer()
        await state.set_state(1)  # Установка начального состояния 1
        await callback.message.answer(states_texts[1])
        await callback.message.answer(add_states_texts[1])
        scheduled_message = "Привет! Ты собрал все документы?"
        # Запланировать отправку сообщения через 5 дней
        delay_days = 5
        await asyncio.create_task(send_message_after_delay(callback.from_user.id, scheduled_message, delay_days))
    else:
        current_state = int(current_state)  # Преобразование текущего состояния в число
        next_state = str(current_state + 1)
        await state.set_state(next_state)  # Установка следующего состоянияdfsdf


@router.callback_query(F.data == 'instruction_one')
async def get_instruction_one(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Справку можно заказать через терминал или в гос.портале: portal.tunduk.kg \n"
                                  "После заявки справка выдается в течении от 1-3 дней по адресу:"
                                  "Курманжан Датка, 115. Тел. (0312) 369-417, (0312) 369-418", reply_markup=kb.step_one)


@router.callback_query(F.data == 'instruction_two')
async def get_instruction_two(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Медицинскую справку можно получить в поликлинике по "
                                  "месту прописки или в любом платном медицинском", reply_markup=kb.step_one)


@router.callback_query(F.data == 'instruction_third')
async def get_instruction_third(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Для получения справок необходимо подойти к единую регистратуру в "
                                  "Республиканском центре психиатрии и наркологии. Адрес: Байтик Баатыра, 1а."
                                  " Либо можно заказать в гос. портале: portal.tunduk.kg", reply_markup=kb.step_one)


@router.message(F.text == 'Дальше')
async def next_step(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await state.set_state(1)  # Установка начального состояния 1
        await message.answer(states_texts[1])
        await message.answer(add_states_texts[1], reply_markup=kb.delete_keybord)
        scheduled_message = "Привет! Ты собрал все документы?"
        # Запланировать отправку сообщения через 5 дней
        delay_days = 5
        await asyncio.create_task(send_message_after_delay(message.chat.id, scheduled_message, delay_days))

    else:
        current_state = int(current_state)  # Преобразование текущего состояния в число
        next_state = current_state + 1
        await state.set_state(next_state)  # Установка следующего состояния
        # await bot.delete_message(message.chat.id, message.message_id)
        if next_state == 2:
            await message.answer(states_texts[2])
            await message.answer(add_states_texts[2])
        elif next_state == 3:
            # Отправляем фотографию и текст
            await message.answer(states_texts[3])
            await message.answer_photo(
                photo='AgACAgIAAxkBAAICtGYvuip5z8PgMJHOQamly42gVGPrAAII2zEbRCyASQKbWDGvFjGTAQADAgADeAADNAQ',
                caption=add_states_texts[3])
            await message.answer(add_states_texts[4])
            # функцию
        elif next_state == 4:
            await message.answer(states_texts[4], reply_markup=kb.menu_keyboard)
            await message.answer(add_states_texts[5])
        else:
            await message.answer("Больше нет текстов для отображения.")


@router.callback_query(F.data == 'yes_docs')
async def get_yes_docs(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("Отлично!", reply_markup=kb.step_one)


@router.callback_query(F.data == 'no_docs')
async def get_yes_docs(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("Поторопись,чтобы мы успели оформить тебя")
    scheduled_message = "Привет! Ты собрал все документы?"
    # Запланировать отправку сообщения через 5 дней
    delay_days = 5
    await asyncio.create_task(send_message_after_delay(callback.from_user.id, scheduled_message, delay_days))


@router.message(F.text == 'Ивенты')
async def get_events(message: Message, state: FSMContext):
    await message.answer("Лучше один раз увидеть, чем сто раз "
                         "услышать. Поэтому посмотри какие ивенты"
                         "проходят в нашей Компании и почему мы так"
                         "любим нашу корпоративную культуру."
                         "Надеюсь ты проникнешься тем, что нас"
                         "объединяет и делает сильной командой.",reply_markup=kb.ivents)


@router.callback_query(F.data == "family_day")
async def get_family_day(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(add_states_texts[6])
