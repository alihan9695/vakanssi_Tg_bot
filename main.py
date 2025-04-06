import asyncio
import logging
import sqlite3
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, KeyboardButton, BotCommand
)

TOKEN = "7261752570:AAFRvailBhXYgl8scYnc7XXbkXKL_TjAcTs"
HH_API_URL = "https://api.hh.kz/vacancies"
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# База данных
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS jobs (id INTEGER PRIMARY KEY, title TEXT, city TEXT, salary TEXT, description TEXT)''')
conn.commit()


# Обычное клавиатурное меню
def reply_main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔍 Найти работу")],
            [KeyboardButton(text="📄 Разместить вакансию")]
        ],
        resize_keyboard=True
    )


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Привет! Выбери действие:", reply_markup=reply_main_menu())


@dp.message()
async def handle_message(message: types.Message):
    text = message.text.lower()

    if message.text == "🔍 Найти работу":
        await message.answer("Введите должность (например, 'Программист'):")
        return

    elif message.text == "📄 Разместить вакансию":
        await message.answer("Введите вакансию в формате:\n`Должность - Город - Зарплата - Описание`")
        return

    # Обработка добавления вакансии
    if " - " in text:
        try:
            title, city, salary, description = text.split(" - ")
            cursor.execute("INSERT INTO jobs (title, city, salary, description) VALUES (?, ?, ?, ?)",
                           (title, city, salary, description))
            conn.commit()
            await message.answer("✅ Вакансия добавлена!")
        except:
            await message.answer("❌ Ошибка. Формат: Должность - Город - Зарплата - Описание")
    else:
        cursor.execute("SELECT title, city, salary, description FROM jobs WHERE LOWER(title) LIKE ?", (f"%{text}%",))
        results = cursor.fetchall()
        response = ""
        for job in results:
            response += f"📌 {job[0]} - {job[1]}\n💰 {job[2]}\n📝 {job[3]}\n\n"

        params = {"text": text, "area": 159}
        try:
            hh_response = requests.get(HH_API_URL, params=params).json()
            for job in hh_response.get("items", [])[:5]:
                response += (
                    f"📌 {job['name']}\n"
                    f"🏢 {job['employer']['name']}\n"
                    f"🌍 {job['area']['name']}\n"
                    f"💰 {job.get('salary', {}).get('from', 'Не указана')}\n"
                    f"🔗 [Подробнее]({job['alternate_url']})\n\n"
                )
        except:
            response += "⚠ Ошибка при получении вакансий с hh.kz."

        await message.answer(response or "❌ Вакансий не найдено.")


async def main():
    await bot.set_my_commands([
        BotCommand(command="start", description="Главное меню"),
    ])
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

