import asyncio, requests, json, base64, hashlib
import logging 
import pandas as pd
import io
import aiohttp
import re

from aiogram.methods.send_document import SendDocument
from magic_filter import RegexpMode
from re import Match
from aiogram.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown
from aiogram.enums import ParseMode, ChatAction
from aiogram.types import FSInputFile
from utils.commands import set_commands

from config import BOT_TOKEN, API_KEY, RECAPTCHA_KEY

def get_file_report(API_KEY, hash_digest):
    url = f'https://www.virustotal.com/api/v3/files/{hash_digest}'
    headers = {'x-apikey': API_KEY}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        report_data = response.json()
        if 'attributes' in report_data:
            scan_results = report_data['attributes']['last_analysis_results']
            result_string = "\n".join([f"{engine}: {result}" for engine, result in scan_results.items()])
            return result_string
        else:
            return 'Отчет не найден на VirusTotal'
    else:
        return 'Ошибка при получении отчета с VirusTotal'
    

def scan_ip(API_KEY, ip_adress):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_adress}"
    headers = {"x-apikey": API_KEY}
    response = requests.get(url, headers=headers)
    return response.json()

def scan_domain(API_KEY, strdomain):
    url = f'https://www.virustotal.com/api/v3/domains/{strdomain}'
    headers = {
    "accept": "application/json",
    "x-apikey": API_KEY,
    }
    response = requests.get(url, headers=headers)
    print(response.json())
    return response.json()