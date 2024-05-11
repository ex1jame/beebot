import asyncio

from aiogram import Router, F

from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, InputMediaPhoto, sticker , sticker_set


import app.keyboards as kb
from app.utils.states import states_texts, ConfirmationState, add_states_texts, send_message_after_delay, \
    send_message_after_delay2

router = Router()



@router.message(F.video)
async def get_video_id(message: Message):
    if message.video:
        video_id = message.video.file_id
        await message.reply(f"ID вашего видео: {video_id}")


@router.message(F.photo)
async def get_photo(message: Message, state: FSMContext):
    await message.answer(f"id{message.photo[-1].file_id}")


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Дорогой коллега, поздравляю тебя с прохождением всех "
                         "этапов собеседования!"
                         " Сегодня начинается твой путь в компании,"
                         " а я  – твой помощник, меня зовут BeeBot  и  моя задача помочь "
                         "тебе адаптироваться в компании",
                         reply_markup=kb.main)


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
            await message.answer_video(video="BAACAgIAAxkBAAIHW2Y-HCU86x8dpGX_0jo64H_c8KrKAAIxSAACuYjxSUG0u3auXQcgNQQ")
            await message.answer_video(video="BAACAgIAAxkBAAIHXWY-HJgAAVNP3RUkw9UMBvAT-bnSHgACOkgAArmI8Umh63yvI4rvBzUE")
            await message.answer(add_states_texts[4], reply_markup=kb.delete_keybord)
            scheduled_message = ("Привет! Как твои дела?\n"
                                 "Твой Buddy на связи")

            delay_days = 1
            await asyncio.create_task(send_message_after_delay2(message.chat.id, scheduled_message, delay_days))
            await message.answer(add_states_texts[5], reply_markup=kb.menu_keyboard)
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
                         "объединяет и делает сильной командой.", reply_markup=kb.ivents)


@router.callback_query(F.data == "family_day")
async def get_family_day(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(add_states_texts[6])


@router.callback_query(F.data == "love_day")
async def get_love_day(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(add_states_texts[7])


@router.callback_query(F.data == "beestyle_day")
async def get_beestyle_day(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Хочу подробнее рассказать о нашей традиции Beestyle:\n"
                                  "Beestyle - это флешмоб, когда мы приходим на работу в тематической одежде.\n"
                                  "У нас в компании уже прошли:\n"
                                  "BeeStyle - ХЭЛЛОУИН-ДЭЙ\n"
                                  "BeeStyle - ДЕНЬ ЦВЕТНЫХ НОСКОВ\n"
                                  "BeeStyle - ДЕНЬ ЦВЕТНЫХ РУБАШЕК\n"
                                  "Beestyle ДЕНЬ ЧЕРНО-ЖЕЛТЫХ BEELINE НОСКОВ!\n"
                                  "Обязательно участвуй с командой в Beestyle флешмобе!\n")
    photo_ids = [
        "AgACAgIAAxkBAAIJQmY-bUdh4R9dRKpgzV_lrKGa21REAAK42zEbuYjxSWooKlQjoEVaAQADAgADeAADNQQ",
        "AgACAgIAAxkBAAIJRGY-bWhHigNt3vnTjkaLhJkUaul4AAK62zEbuYjxSdBq5qdshtYzAQADAgADeQADNQQ",


    ]
    media = [InputMediaPhoto(media=photo_id) for photo_id in photo_ids]
    await callback.message.answer_media_group(media)


@router.message(F.text == "Офис")
async def get_offices(message: Message):
    await message.answer_photo(
        photo="AgACAgIAAxkBAAIHrWY-IjW15vvSvObp6QTEbFwvAAGtaQACHtoxG7mI8UmvQHctunWX_QEAAwIAA3kAAzUE",
        caption=add_states_texts[8], reply_markup=kb.offices)


@router.callback_query(F.data == "capsule_sky")
async def get_capsule_sky(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(
        photo="AgACAgIAAxkBAAIIBGY-QR3yy232RD4tSmMy_s6XYGWSAAKn2jEbuYjxSRJMNNAQio8MAQADAgADeQADNQQ",
        caption=add_states_texts[9]
    )


@router.callback_query(F.data == "locker_sky")
async def get_capsule_sky(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(
        photo="AgACAgIAAxkBAAIIBmY-Qbi_t_c2lZQ99l0tvlUEbSM7AAKo2jEbuYjxSWQ6OPrLmS-UAQADAgADeQADNQQ",
        caption=add_states_texts[10]
    )


@router.callback_query(F.data == "sky_lab")
async def get_capsule_sky(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(
        photo="AgACAgIAAxkBAAIICGY-QhLCBI6CZu701JJZHsGqRWVSAAKs2jEbuYjxSZyGzsQBqWt3AQADAgADeQADNQQ",
        caption=add_states_texts[11]
    )


@router.callback_query(F.data == "relax_sky")
async def get_relax_sky(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "Конечно же, важно и то, чтобы"
        "сотрудники могли отвлекаться от работы."
        "Именно поэтому у нас в SKY X есть кухни,"
        "зоны отдыха, террасы и даже своя"
        "кофейня, где ты всегда можешь купить"
        "свежий кофе или чай."
    )
    photo_ids = [
        "AgACAgIAAxkBAAIIa2Y-SuMs2kCKKaucTUG0_afEHqlgAALY2jEbuYjxSXrnn9LaxlJBAQADAgADeQADNQQ",
        "AgACAgIAAxkBAAIIy2Y-ZH6Rpm0mjKfYrJfBrROl7AHsAAJz2zEbuYjxSeKVuZgvdWPQAQADAgADeQADNQQ",
        "AgACAgIAAxkBAAIIzWY-ZJJ3ahbvSDx23BtuNO8wY4NaAAJ02zEbuYjxSXy1S1tbyemJAQADAgADeQADNQQ",
        "AgACAgIAAxkBAAIIz2Y-ZKY8jzN593vvpRg0N48ZMaPjAAJ12zEbuYjxSeyu0IohtUckAQADAgADeQADNQQ",
        "AgACAgIAAxkBAAII0WY-ZLuaStPphNxudzoISZgCK9pyAAJ32zEbuYjxSdisRUBCLpKEAQADAgADeQADNQQ"

    ]
    media = [InputMediaPhoto(media=photo_id) for photo_id in photo_ids]
    await callback.message.answer_media_group(media)


#
# # Отправляем текстовое сообщение офисов после группы фотографий
# await message.answer(offices_text)


@router.message(F.text == "Увлечения")
async def get_hobbies(message: Message):
    await message.answer_photo(
        photo="AgACAgIAAxkBAAIJKWY-aFR1T17Q3jfC0uRqprXcrcbWAAKQ2zEbuYjxSffeHlwhNW0RAQADAgADeQADNQQ",
        caption="Мы стремимся к тому, чтобы у наших сотрудников был баланс\n"
                "между работой и личными увлечениями. Мы верим, что такой\n"
                "сотрудник заинтересован в том, чтобы его работа приносила\n"
                "лучший результат Компании. Именно поэтому мы развиваем\n"
                "систему клубов, которые предоставляют коллегам простор для\n"
                "развития в самых разных направлениях:\n"
                "•Шахматы\n"
                "•Стретчинг\n"
                "•Настольный теннис\n"
                "•Футбол\n"
                "Уверен, что ты найдешь себе занятие по душе."
    )


@router.message(F.text == "Библиотека")
async def get_library(message: Message):
    await message.answer("Обучение и развитие сотрудников – один из важнейших элементов"
                         "корпоративной культуры. Мы предоставляем доступ к лучшим"
                         "площадкам для онлайн обучения:\n"
                         "Корпоративной библиотеке Alpina, в которой тебе будут доступны"
                         "1000 книг, самого разного направления.\n"
                         "А также к платформе Courserа, где ты сможешь пройти курсы от"
                         "топовых университетов и компаний\n"
                         "У нас еще есть живая библиотека на 2-м этаже. Ты можешь брать"
                         "книги и прокачивать свои знания.\n"
                         "Мы с удовольствием тебе это все покажем, когда увидимся в"
                         "нашем офисе. До скорой встречи!\n")
    await message.answer_photo(
        photo="AgACAgIAAxkBAAIJLmY-a-LIBDWSr2lhsP-u_RZPtQ7zAAKP2zEbuYjxSXbhA6rUgdP6AQADAgADeQADNQQ"
    )


@router.message(F.text == "Bbox")
async def get_bbox(message: Message):
    await message.answer("Также Компания запустила систему не материальной"
                         "мотивации Benefit box или же BBox. Это альтернативное"
                         "предложение для сотрудников, которым не подходят условия"
                         "добровольного медицинского страхования (ДМС)."
                         "В BBox вы сами выбираете услугу, которая может быть"
                         "предложена со льготными условиями:"
                         "Абонемент в зал, оплата за проезд в общественном транспорте"
                         "или же сервисы саморазвития.")
