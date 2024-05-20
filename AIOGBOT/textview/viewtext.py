import config
import datetime
import re

from aiogram.types import FSInputFile, ReplyKeyboardMarkup, KeyboardButton

from config import TEXT,COUNTRY_CODE

def find_ip_adress(text):
    pattern = r'\b(?:(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){3}(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\b'
    ip_adress = re.findall(pattern, text)
    try:
        return ip_adress[0]
    except:
        return None
    
def view_ip_text(result) -> str:
    bad_find = result['data']['attributes']['last_analysis_stats']['malicious']
    nofind = result['data']['attributes']['last_analysis_stats']['undetected']
    warn_find = result['data']['attributes']['last_analysis_stats']['suspicious']
    try:
        as_owner = result['data']['attributes']['as_owner']
    except KeyError:
        as_owner = 'None'
    try:
        last_scan = result['data']['attributes']['last_analysis_date']
        dt = datetime.datetime.fromtimestamp(last_scan)
        last_scan = dt.strftime('%Y-%m-%d %H:%M:%S')
    except KeyError:
        date = datetime.datetime.now()
        last_scan = date.strftime('%Y-%m-%d %H:%M:%S')
    print(result)
    try:
        country = result['data']['attributes']['country']
        country = config.COUNTRY_CODE[country]
    except KeyError:
        country = "None"
    try:
        network = result['data']['attributes']['network']
    except KeyError:
        network = '-'
    ip_adress = result['data']['id']
    return TEXT['ip_address_info'].format(bad_find=bad_find, warn_find=warn_find, nofind=nofind,ip_adress=ip_adress, network=network, country=country,as_owner = as_owner,last_scan=last_scan)

class ButtonText:
    answer_IP1 = 'Да'
    answer_IP11 = 'Нет'

def answer_quest_IP():
    button1 = KeyboardButton(text = ButtonText.answer_IP1)
    button2 = KeyboardButton(text = ButtonText.answer_IP11)
    buttons_row = [button1,button2]
    ipKeyboard = ReplyKeyboardMarkup(keyboard = [buttons_row])
    return ipKeyboard

def view_text_domain(res_domain):
    error = res_domain.get('error')
    if error:
        if error.get('code') == 'NotFoundError':
            return 'not_found'
    bad_find = res_domain['data']['attributes']['last_analysis_stats']['malicious']
    nofind = res_domain['data']['attributes']['last_analysis_stats']['undetected']
    warn_find = res_domain['data']['attributes']['last_analysis_stats']['suspicious']
    last_scan = res_domain['data']['attributes']['last_analysis_date']
    dt = datetime.datetime.fromtimestamp(last_scan)
    last_scan = dt.strftime('%Y-%m-%d %H:%M:%S')
    domain = res_domain['data']['id']
    try:
        creation_date = res_domain['data']['attributes']['creation_date']
        dt = datetime.datetime.fromtimestamp(creation_date)
        creation_date = dt.strftime('%Y-%m-%d')
    except KeyError:
        creation_date = '-'
    return TEXT['domain'].format(bad_find=bad_find, warn_find=warn_find, nofind=nofind,
                                               domain=domain, last_scan=last_scan, creation_date=creation_date)