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

headers = {
    "accept": "application/json",
    "x-apikey": "API_KEY"}

bot = Bot(
    token=BOT_TOKEN)
dp = Dispatcher()
form_router = Router()

class Form(StatesGroup):
    waiting_for_ip = State()

class Quest_IP(StatesGroup):
    q_ans1 = State()
    q_ans2 = State()
    q_ans3 = State() 

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



@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(
        text=f'Привет, {markdown.hbold(message.from_user.full_name)}. Функционал этого бота реализован через <a href="https://www.virustotal.com/gui/home/search">API VirusTotal</a>,базу данных ФСТЭК и других ресурсов, которые могут помочь вам в работе, что позволяет ему проверять файлы, ссылки и IP-адреса с помощью 70 антивирусов одновременно. Просто отправьте сюда данные, и Вы получите подробный отчет о наличии вирусов и угроз. \n /help для текущих комманд.',
        parse_mode=ParseMode.HTML,
    )

@dp.message(Command('help'))
async def handle_help(message: types.Message):  
    text = markdown.text(
        'На данный момент я могу следующее:',
        'Вы можете отправить <b><u>ФАЙЛ</u></b> чтобы проверить его на содержание вирусов и получить рекомендации по защите от них\n',
        'Так же можно <b><u>отправить IP</u></b> для его проверки в нескольких антивирусах после чего можно получить помощь по работе с подозрительным IP\n ',
        'Если вам нужно проверить сайт, просто <b><u>отправьте на него ссылку</u></b> и я скажу вам опасен ли он и что нужно делать если вы перешли по этой ссылке\n'
        '<b>/checksoft</b> - проверка в Базе ФСТЭК и других надёжных источников вашего ПО на наличие уязвимостей и дальнейшей помощи их устранения',
        sep='\n',
    )
    await message.answer(
        text=text,
        parse_mode=ParseMode.HTML,
    )

@dp.message(F.text.regexp(r'\b(?:(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){3}(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\b').as_('digits'))
async def scan_ip_adress(message: types.Message, state: FSMContext, digits:Match[str]) -> None:
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    ip_adress = message.text
    result = VTfunction.scan_ip(API_KEY,ip_adress)
    result_text = viewtext.view_ip_text(result)
    await message.reply(result_text,
                         parse_mode='HTML',
                         reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text='Да'),
                    KeyboardButton(text='Нет'),
                ],
            ],
            resize_keyboard=True,
        ),
    )
    await state.set_state(Quest_IP.q_ans1)
    await message.answer(TEXT['Quest_IP1'],)

@form_router.message(Quest_IP.q_ans1, F.text == "Да")
async def task_yes(message: types.Message, state: FSMContext) -> None:

    await state.set_state(Quest_IP.q_ans3)
    await message.reply(
        'Ответ по принятию решений',
        reply_markup = ReplyKeyboardRemove(),
    )

@form_router.message(Quest_IP.q_ans1, F.text == "Нет")
async def task_no(message: types.Message, state: FSMContext) -> None:

    data = await state.get_data()
    await state.clear()
    await message.answer(
        'Следующий вопрос',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text='Да'),
                    KeyboardButton(text='Нет'),
                ],
            ],
            resize_keyboard=True,
        ),
    )

@form_router.message(Quest_IP.q_ans1)
async def process_unknown_write_bots(message: types.Message) -> None:
    await message.reply("Я не понимаю тебя.")
    
@dp.message(F.document)
async def handle_document(message: types.Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
     
    document = message.document
    file_id = document.file_id

    # Получение информации о файле
    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path

    # Скачивание файла
    file = await bot.download_file(file_path)
    
    # Вычисление SHA-256 хеша файла
    sha256_hash = hashlib.sha256()
    sha256_hash.update(file.read())  # Обновление хеша содержимым файла
    hash_digest = sha256_hash.hexdigest()
    report = VTfunction.get_file_report(API_KEY, hash_digest)

    await message.reply(f"SHA-256 хеш файла <b><i>{document.file_name}</i></b>: <b><u>{hash_digest}</u></b>, отправляем его на проверку.")
    await message.answer(f"Отчет VirusTotal:\n{report}")
    if report == 'Отчет не найден на VirusTotal':
        await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT)
        await bot.send_document(chat_id=message.chat.id,document=FSInputFile('C:/hate/AIOGBOT/Sendlers/RecomendationZeroDay.pdf'), caption=f'Вероятно, этот файл не содержит никаких вирусов, но всегда есть вероятность вируса нулевого дня, высылаю вам рекомендации для защиты от него.')

@dp.message(F.text.regexp(r'https?://(?:www\.)?\S+\.\S+'))
async def get_url(message: types.Message):
    domain_pattern = r'\b(?:(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?)\b'
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    text = message.text
    print(text)
    domain = re.search(domain_pattern, text)
    print(domain)
    strdomain = domain.group() # текстовый вид домена
    await message.answer(strdomain)
    print(strdomain)
    res_domain = VTfunction.scan_domain(API_KEY, strdomain)
    res_text_domain = viewtext.view_text_domain(res_domain)
    # Использовать группу 1 для домена
    await message.answer(res_text_domain)

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