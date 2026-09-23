import asyncio
import json
import logging
from datetime import datetime

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
    LabeledPrice, PreCheckoutQuery, SuccessfulPayment
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import BOT_TOKEN, LESSONS, WELCOME_MESSAGE, HELP_MESSAGE, PAYMENT_METHOD, ADMIN_ID
from database import init_db, save_user, save_payment, is_lesson_purchased, get_user_purchases, mark_lesson_accessed

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Инициализация БД при старте
init_db()


# ============ КОМАНДЫ ============

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user = message.from_user
    save_user(user.id, user.username, user.first_name, user.last_name)

    # Главное меню с кнопками
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📚 Список уроков", callback_data="show_lessons")],
        [InlineKeyboardButton(text="🎓 Мои уроки", callback_data="my_lessons")],
        [InlineKeyboardButton(text="❓ Помощь", callback_data="help")]
    ])

    await message.answer(
        WELCOME_MESSAGE,
        reply_markup=keyboard,
        parse_mode="Markdown"
    )


@dp.message(Command("lessons"))
async def cmd_lessons(message: types.Message):
    await show_lessons(message)


@dp.message(Command("my_lessons"))
async def cmd_my_lessons(message: types.Message):
    await show_my_lessons(message)


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(HELP_MESSAGE, parse_mode="Markdown")


# ============ КОЛБЭКИ (КНОПКИ) ============

@dp.callback_query(F.data == "show_lessons")
async def show_lessons(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()

    for lesson_id, lesson in LESSONS.items():
        price_display = f"{lesson['price_stars']} ⭐" if PAYMENT_METHOD == "stars" else f"{lesson['price_rub']} ₽"
        builder.add(InlineKeyboardButton(
            text=f"{lesson['name']} - {price_display}",
            callback_data=f"lesson_{lesson_id}"
        ))

    builder.add(InlineKeyboardButton(text="◀️ Назад в меню", callback_data="back_to_menu"))
    builder.adjust(1)

    await callback.message.edit_text(
        "📚 *Выберите урок для оплаты:*\n\nПосле оплаты вы получите ссылку на Zoom-конференцию.",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )
    await callback.answer()


@dp.callback_query(F.data == "my_lessons")
async def show_my_lessons(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    purchases = get_user_purchases(user_id)

    if not purchases:
        await callback.message.edit_text(
            "🎓 *У вас пока нет оплаченных уроков*\n\nВыберите урок через /lessons и оплатите его.",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="📚 Смотреть уроки", callback_data="show_lessons")],
                [InlineKeyboardButton(text="◀️ Назад", callback_data="back_to_menu")]
            ]),
            parse_mode="Markdown"
        )
        await callback.answer()
        return

    text = "🎓 *Ваши оплаченные уроки:*\n\n"
    keyboard = InlineKeyboardBuilder()

    for lesson_id, zoom_link, paid_at in purchases:
        lesson = LESSONS.get(lesson_id, {"name": f"Урок {lesson_id}"})
        date = paid_at[:10]
        text += f"📘 *{lesson['name']}*\n   Оплачен: {date}\n"
        keyboard.add(InlineKeyboardButton(
            text=f"🚪 Войти на урок {lesson_id}",
            callback_data=f"access_{lesson_id}"
        ))

    keyboard.add(InlineKeyboardButton(text="◀️ Назад в меню", callback_data="back_to_menu"))
    keyboard.adjust(1)

    await callback.message.edit_text(
        text,
        reply_markup=keyboard.as_markup(),
        parse_mode="Markdown"
    )
    await callback.answer()


@dp.callback_query(F.data == "help")
async def show_help(callback: types.CallbackQuery):
    await callback.message.edit_text(
        HELP_MESSAGE,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="◀️ Назад", callback_data="back_to_menu")]
        ]),
        parse_mode="Markdown"
    )
    await callback.answer()


@dp.callback_query(F.data == "back_to_menu")
async def back_to_menu(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📚 Список уроков", callback_data="show_lessons")],
        [InlineKeyboardButton(text="🎓 Мои уроки", callback_data="my_lessons")],
        [InlineKeyboardButton(text="❓ Помощь", callback_data="help")]
    ])
    await callback.message.edit_text(
        WELCOME_MESSAGE,
        reply_markup=keyboard,
        parse_mode="Markdown"
    )
    await callback.answer()


@dp.callback_query(F.data.startswith("lesson_"))
async def lesson_detail(callback: types.CallbackQuery):
    lesson_id = callback.data.split("_")[1]
    lesson = LESSONS.get(lesson_id)

    if not lesson:
        await callback.answer("Урок не найден")
        return

    user_id = callback.from_user.id
    already_purchased = is_lesson_purchased(user_id, lesson_id)

    price_stars = lesson['price_stars']
    price_rub = lesson['price_rub']

    text = f"""
📘 *{lesson['name']}*

{lesson['description']}

💰 *Цена:* 
   • {price_stars} Telegram Stars
   • {price_rub} ₽

После оплаты вы получите ссылку на Zoom-урок и доступ навсегда.
    """

    keyboard = InlineKeyboardBuilder()

    if already_purchased:
        keyboard.add(InlineKeyboardButton(text="✅ Уже оплачено (войти)", callback_data=f"access_{lesson_id}"))
    else:
        if PAYMENT_METHOD == "stars":
            keyboard.add(
                InlineKeyboardButton(text=f"⭐ Оплатить {price_stars} Stars", callback_data=f"pay_{lesson_id}_stars"))
        else:
            keyboard.add(InlineKeyboardButton(text=f"💳 Оплатить {price_rub} ₽", callback_data=f"pay_{lesson_id}_rub"))

    keyboard.add(InlineKeyboardButton(text="◀️ Назад к урокам", callback_data="show_lessons"))

    await callback.message.edit_text(
        text,
        reply_markup=keyboard.as_markup(),
        parse_mode="Markdown"
    )
    await callback.answer()


@dp.callback_query(F.data.startswith("access_"))
async def give_zoom_access(callback: types.CallbackQuery):
    lesson_id = callback.data.split("_")[1]
    user_id = callback.from_user.id
    lesson = LESSONS.get(lesson_id)

    if not lesson:
        await callback.answer("Урок не найден")
        return

    if not is_lesson_purchased(user_id, lesson_id):
        await callback.answer("❌ Урок не оплачен. Сначала оплатите его.", show_alert=True)
        return

    zoom_link = lesson['zoom_link']
    mark_lesson_accessed(user_id, lesson_id)

    await callback.message.answer(
        f"🎉 *Доступ к уроку «{lesson['name']}» открыт!*\n\n"
        f"🔗 *Ссылка на Zoom:*\n{zoom_link}\n\n"
        f"📅 Уроки проходят по расписанию. Если у вас есть вопросы, напишите педагогу: @nigina_teacher",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🚪 Открыть Zoom", url=zoom_link)],
            [InlineKeyboardButton(text="◀️ К моим урокам", callback_data="my_lessons")]
        ])
    )
    await callback.answer("Ссылка на Zoom отправлена!")


# ============ ОПЛАТА (TELEGRAM STARS) ============

@dp.callback_query(F.data.startswith("pay_"))
async def process_payment(callback: types.CallbackQuery):
    parts = callback.data.split("_")
    lesson_id = parts[1]
    method = parts[2] if len(parts) > 2 else "stars"

    lesson = LESSONS.get(lesson_id)
    if not lesson:
        await callback.answer("Урок не найден")
        return

    user_id = callback.from_user.id

    # Проверка, не куплен ли уже
    if is_lesson_purchased(user_id, lesson_id):
        await callback.answer("Вы уже оплатили этот урок!", show_alert=True)
        return

    if method == "stars":
        # Оплата через Telegram Stars
        prices = [LabeledPrice(label=lesson['name'], amount=lesson['price_stars'])]

        await bot.send_invoice(
            chat_id=user_id,
            title=f"Оплата урока: {lesson['name']}",
            description=lesson['description'],
            payload=f"lesson_{lesson_id}",
            provider_token="",  # Для Stars не нужен
            currency="XTR",  # XTR = Telegram Stars
            prices=prices,
            start_parameter="payment_start",
            need_shipping_address=False,
            is_flexible=False
        )
        await callback.answer("Счет отправлен! Нажмите «Оплатить».")
    else:
        # TODO: ЮKassa интеграция (по желанию)
        await callback.answer("Оплата в рублях временно недоступна. Используйте Telegram Stars.", show_alert=True)


# Обработка предварительной проверки платежа
@dp.pre_checkout_query()
async def pre_checkout_query(pre_checkout_q: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


# Обработка успешного платежа
@dp.message(F.successful_payment)
async def successful_payment(message: types.Message):
    payment = message.successful_payment
    user_id = message.from_user.id

    # Парсим payload (lesson_1)
    payload = payment.invoice_payload
    lesson_id = payload.split("_")[1]

    lesson = LESSONS.get(lesson_id)
    if not lesson:
        await message.answer("Ошибка: урок не найден. Обратитесь в поддержку.")
        return

    # Сохраняем платеж в БД
    save_payment(
        user_id=user_id,
        lesson_id=lesson_id,
        payment_id=payment.telegram_payment_charge_id,
        amount=payment.total_amount,
        currency=payment.currency,
        zoom_link=lesson['zoom_link']
    )

    # Отправляем Zoom-ссылку
    await message.answer(
        f"✅ *Оплата успешно получена!*\n\n"
        f"📘 *{lesson['name']}*\n\n"
        f"🔗 *Ваша ссылка на Zoom:*\n{lesson['zoom_link']}\n\n"
        f"Сохраните эту ссылку. Вы также можете найти её в разделе /my_lessons.\n\n"
        f"До встречи на уроке! 🎉",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🚪 Открыть Zoom", url=lesson['zoom_link'])],
            [InlineKeyboardButton(text="📚 Другие уроки", callback_data="show_lessons")]
        ])
    )

    # Уведомление админу (если указан)
    if ADMIN_ID:
        await bot.send_message(
            ADMIN_ID,
            f"💰 Новая оплата!\n"
            f"Пользователь: @{message.from_user.username or message.from_user.first_name}\n"
            f"Урок: {lesson['name']}\n"
            f"Сумма: {payment.total_amount} {payment.currency}"
        )

    logger.info(f"Payment successful: user={user_id}, lesson={lesson_id}")


# ============ ЗАПУСК ============

async def main():
    print("🤖 Бот запущен!")
    print(f"Username: @{(await bot.get_me()).username}")
    print("Используйте команду /start в Telegram")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())