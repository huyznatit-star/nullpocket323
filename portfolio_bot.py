import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

logging.basicConfig(level=logging.INFO)

API_TOKEN = "8936825970:AAGy8mODq8kNGydq9jT1U6OGTmNvpNhteIE"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

def get_main_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="🛡️ Чекеры", callback_data="checkers"),
        InlineKeyboardButton(text="📊 Парсеры", callback_data="parsers"),
    )
    builder.row(
        InlineKeyboardButton(text="🎮 Фермы", callback_data="farms"),
        InlineKeyboardButton(text="🤖 Автоматизация", callback_data="auto"),
    )
    builder.row(
        InlineKeyboardButton(text="💰 Прайс-лист", callback_data="price"),
        InlineKeyboardButton(text="📞 Связаться", callback_data="contact"),
    )
    return builder.as_markup()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "👋 Привет! Я бот-портфолио.\n"
        "Я сам — пример того, что мы умеем делать.\n\n"
        "Выбери категорию, чтобы увидеть примеры работ:",
        reply_markup=get_main_keyboard()
    )

@dp.callback_query(lambda c: c.data == "checkers")
async def show_checkers(call: types.CallbackQuery):
    text = (
        "🛡️ <b>Чекеры (проверка и анализ)</b>\n\n"
        "🔹 <b>Dota 2 Inventory Checker</b>\n"
        "Смотрит инвентарь всех игроков в матче в реальном времени и показывает его стоимость.\n"
        "Использует Game State Integration + Steam API.\n\n"
        "🔹 <b>Steam Account Checker</b>\n"
        "Проверяет аккаунты на валидность, наличие игр, VAC-баны, уровень Steam.\n"
        "Массовый прогон с прокси.\n\n"
        "🔹 <b>CS2 Float Checker</b>\n"
        "Оценивает износ скинов (float value) прямо из инвентаря или базы данных.\n"
        "Помогает трейдерам быстро находить выгодные позиции."
    )
    await call.message.edit_text(text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
    ]))
    await call.answer()

@dp.callback_query(lambda c: c.data == "parsers")
async def show_parsers(call: types.CallbackQuery):
    text = (
        "📊 <b>Парсеры и сбор данных</b>\n\n"
        "🔹 <b>Telegram User Parser</b>\n"
        "Собирает всех участников каналов/чатов: ID, username, телефон, активность.\n"
        "Выгрузка в CSV/Excel.\n\n"
        "🔹 <b>Steam Market Parser</b>\n"
        "Мониторит цены на скины, кейсы, стикеры. Отправляет уведомления при падении цены.\n"
        "Можно использовать для снайпинга.\n\n"
        "🔹 <b>Dota 2 Match Parser</b>\n"
        "Собирает историю матчей, статистику героев, винрейты. Полезно для аналитики."
    )
    await call.message.edit_text(text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
    ]))
    await call.answer()

@dp.callback_query(lambda c: c.data == "farms")
async def show_farms(call: types.CallbackQuery):
    text = (
        "🎮 <b>Игровые фермы</b>\n\n"
        "🔹 <b>CS2 Case Farm</b>\n"
        "Фарм кейсов и скинов на сотнях аккаунтов одновременно.\n"
        "Поддержка прокси, авто-принятие дропа.\n\n"
        "🔹 <b>Steam Card Farmer</b>\n"
        "Фарм коллекционных карточек без установки игр.\n"
        "Повышение уровня Steam, продажа карточек на маркете.\n\n"
        "🔹 <b>Индивидуальные фермы под заказ</b>\n"
        "Разрабатываем любые игровые фермы по вашему ТЗ.\n"
        "Dota 2, Rust, GTA V и другие игры."
    )
    await call.message.edit_text(text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
    ]))
    await call.answer()

@dp.callback_query(lambda c: c.data == "auto")
async def show_auto(call: types.CallbackQuery):
    text = (
        "🤖 <b>Автоматизация</b>\n\n"
        "🔹 <b>Telegram Auto-Poster</b>\n"
        "Автопостинг из VK, Twitter, YouTube в Telegram-каналы.\n"
        "Чистит водяные знаки, ставит хештеги, работает по расписанию.\n\n"
        "🔹 <b>Discord Auto-Moderator</b>\n"
        "Авто-модерация чатов: бан спамеров, фильтр мата, капча для новеньких.\n\n"
        "🔹 <b>Crypto Trading Bot</b>\n"
        "Авто-трейдинг на Binance, Bybit. Арбитраж, мониторинг курсов."
    )
    await call.message.edit_text(text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
    ]))
    await call.answer()

@dp.callback_query(lambda c: c.data == "price")
async def show_price(call: types.CallbackQuery):
    text = (
        "💰 <b>Примерные цены</b>\n\n"
        "• Простой бот/парсер — от 3 000 ₽\n"
        "• Средний проект — от 10 000 ₽\n"
        "• Комплексная система — от 30 000 ₽\n\n"
        "Сроки:\n"
        "• Простое — 1-2 дня\n"
        "• Среднее — 3-5 дней\n"
        "• Крупное — от недели\n\n"
        "Точная цена после обсуждения ТЗ."
    )
    await call.message.edit_text(text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
    ]))
    await call.answer()

@dp.callback_query(lambda c: c.data == "contact")
async def show_contact(call: types.CallbackQuery):
    text = (
        "📞 <b>Связаться со мной</b>\n\n"
        "Telegram: @nullbyte211\n"
        "По вопросам разработки и сотрудничества.\n\n"
        "Пиши, обсудим твой проект."
    )
    await call.message.edit_text(text, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
    ]))
    await call.answer()

@dp.callback_query(lambda c: c.data == "back")
async def go_back(call: types.CallbackQuery):
    await call.message.edit_text(
        "👋 Привет! Я бот-портфолио.\n"
        "Я сам — пример того, что мы умеем делать.\n\n"
        "Выбери категорию, чтобы увидеть примеры работ:",
        reply_markup=get_main_keyboard()
    )
    await call.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())