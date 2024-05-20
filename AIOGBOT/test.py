import asyncio, requests, json, base64, hashlib, datetime, re, aiohttp, io, logging, sys
import pandas as pd
from config import TEXT
from html import escape

from textview import viewtext 
from functions import VTfunction 

from aiogram.fsm.context import FSMContext
from aiogram.methods.send_document import SendDocument
from magic_filter import RegexpMode
from re import Match
from aiogram.fsm.state import State, StatesGroup
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown
from aiogram.enums import ParseMode, ChatAction
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from aiogram.types import FSInputFile

from utils.commands import set_commands


from config import BOT_TOKEN, API_KEY, TEXT, COUNTRY_CODE



bot = Bot(
    token=BOT_TOKEN)
dp = Dispatcher()
form_router = Router()

df = pd.read_excel('C:/hate/AIOGBOT/ExclTables/dfstek.xlsx')

# Заполнение NaN значений в столбце 'Название ПО' и 'Версия ПО' пустыми строками
df['Название ПО'].fillna('', inplace=True)
df['Версия ПО'].fillna('', inplace=True)

# Проверка на наличие NaN значений в столбцах 'Название ПО' и 'Версия ПО'
print("NaN values in 'Название ПО' after fillna: ", df['Название ПО'].isna().sum())
print("NaN values in 'Версия ПО' after fillna: ", df['Версия ПО'].isna().sum())

# Вывод списка столбцов для диагностики
print("Columns in the DataFrame:", df.columns.tolist())

# Определение состояний
class Soft(StatesGroup):
    info = State()

# Команда для запуска проверки ПО
@dp.message(Command('checksoft'))
async def ask_soft_name(message: Message, state: FSMContext):
    await state.set_state(Soft.info)
    await message.answer('Введите названия ПО и их версии в формате "ПО1, версия1; ПО2, версия2; ..."')

# Обработка введенной информации о ПО
@dp.message(Soft.info)
async def process_info(message: Message, state: FSMContext):
    input_data = message.text
    soft_pairs = input_data.split(';')

    for pair in soft_pairs:
        try:
            soft_name, soft_version = pair.split(',')
            soft_name = soft_name.strip()
            soft_version = soft_version.strip()

            # Объединяем столбцы 'Название ПО' и 'Версия ПО' для поиска
            combined_column = df['Название ПО'] + " " + df['Версия ПО']
            pattern = re.compile(rf'{re.escape(soft_name)}.*{re.escape(soft_version)}', re.IGNORECASE)
            matches = combined_column.str.contains(pattern, na=False)
            result = df[matches]

            if not result.empty:
                solution = escape(str(result['Ссылки на источники'].iloc[0]))
                type_po = escape(str(result['Тип ПО'].iloc[0]))
                vulnerability = escape(str(result['Описание уязвимости'].iloc[0]))
                vulnerability_type = escape(str(result['Класс уязвимости'].iloc[0]))
                date = escape(str(result['Дата выявления'].iloc[0]))
                cvss_2_0 = escape(str(result['CVSS 2.0'].iloc[0]))
                cvss_3_0 = escape(str(result['CVSS 3.0'].iloc[0]))
                cwe_description = escape(str(result['Описание ошибки CWE'].iloc[0]))
                cwe_type = escape(str(result['Тип ошибки CWE'].iloc[0]))
                vul_solution = escape(str(result['Возможные меры по устранению'].iloc[0]))
                
                otvet = TEXT['Soft_text'].format(
                    combined_column=escape(f"{soft_name} {soft_version}"),
                    solution=solution, 
                    type_po=type_po, 
                    vulnerability_type=vulnerability_type, 
                    cvss_2_0=cvss_2_0, 
                    cvss_3_0=cvss_3_0,
                    date=date, 
                    cwe_type=cwe_type, 
                    cwe_description=cwe_description, 
                    vulnerability=vulnerability, 
                    vul_solution=vul_solution
                )
                await message.answer(otvet, parse_mode=ParseMode.HTML)
            else:
                await message.answer(f'{soft_name} версия {soft_version}: информация не найдена.')
        except ValueError as ve:
            print(f"ValueError: {ve}")
            await message.answer('Ошибка в формате ввода данных. Убедитесь, что данные введены корректно.')
        except KeyError as ke:
            print(f"KeyError: {ke}")
            await message.answer(f'Ошибка: столбец {ke} не найден в данных.')
        except Exception as e:
            print(f"Exception: {e}")
            await message.answer(f'Произошла ошибка: {e}')

    await state.clear()

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token=BOT_TOKEN,
        parse_mode = ParseMode.HTML,
    )
    dp.include_router(form_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())   