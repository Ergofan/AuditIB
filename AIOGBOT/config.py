
BOT_TOKEN = ""
API_KEY = ""
HYBRID_KEY = ""

RECAPTCHA_KEY = '6Lelh9spAAAAAJo9f0ckVrJHtVvz0RzriXVmnIzy'

TEXT = {
    'ip_address_info': """
<b>🔎 Обнаружения:</b>\n\n
❌ Обнаружения: {bad_find}\n
⚠️Подозрения: {warn_find}\n
✅Не обнаружено: {nofind}\n\n
• Адрес: {ip_adress}\n
• Сеть: {network}\n
• Страна: {country}\n
• Провайдер: {as_owner}\n
• Последнее сканирование: {last_scan}\n\n
• <b><a href="https://www.virustotal.com/gui/ip-address/{ip_adress}">Ссылка на подробный отчет.</a></b>
""",
    'domain':"""
<b>🔎 Обнаружения:</b>\n\n
❌ Обнаружения: {bad_find}\n
⚠️Подозрения: {warn_find}\n
✅Не обнаружено: {nofind}\n\n
• Домен: {domain}\n
• Последнее сканирование: {last_scan}\n
• Дата создания: {creation_date}\n\n
• <b><a href="https://www.virustotal.com/gui/domain/{domain}">Ссылка на VirusTotal</a></b>
""",
   'Quest_IP1': """
<b>Были ли признаки DDOS-атаки при выявлении этого IP?</b>
""",
    'Soft_text':"""
<b>ПО: {combined_column}</b>\n\n
❓<b>Информация: </b>{solution}\n\n
<b>• Тип ПО: </b>{type_po}\n
<b>• Класс уязвимости: </b>{vulnerability_type}\n\n
<b>• CVSS 2.0: </b>{cvss_2_0}\n
<b>• CVSS 3.0: </b>{cvss_3_0}\n
<b>Дата выявления:</b> {date}\n
<b>Тип ошибки CWE:</b> {cwe_type}\n\n
<b>Описание ошибки CWE: </b>{cwe_description}\n
<b>Описание уязвимости: </b>{vulnerability}\n
<b>Возможные меры по устранению: </b>{vul_solution}\n

"""
}

COUNTRY_CODE = {
    "AF": "Afghanistan 🇦🇫",
    "AL": "Albania 🇦🇱",
    "DZ": "Algeria 🇩🇿",
    "AD": "Andorra 🇦🇩",
    "AO": "Angola 🇦🇴",
    "AR": "Argentina 🇦🇷",
    "AM": "Armenia 🇦🇲",
    "AU": "Australia 🇦🇺",
    "AT": "Austria 🇦🇹",
    "AZ": "Azerbaijan 🇦🇿",
    "BS": "Bahamas 🇧🇸",
    "BH": "Bahrain 🇧🇭",
    "BD": "Bangladesh 🇧🇩",
    "BB": "Barbados 🇧🇧",
    "BY": "Belarus 🇧🇾",
    "BE": "Belgium 🇧🇪",
    "BZ": "Belize 🇧🇿",
    "BJ": "Benin 🇧🇯",
    "BT": "Bhutan 🇧🇹",
    "BO": "Bolivia 🇧🇴",
    "BA": "Bosnia and Herzegovina 🇧🇦",
    "BW": "Botswana 🇧🇼",
    "BR": "Brazil 🇧🇷",
    "BN": "Brunei 🇧🇳",
    "BG": "Bulgaria 🇧🇬",
    "BF": "Burkina Faso 🇧🇫",
    "BI": "Burundi 🇧🇮",
    "KH": "Cambodia 🇰🇭",
    "CM": "Cameroon 🇨🇲",
    "CA": "Canada 🇨🇦",
    "CF": "Central African Republic 🇨🇫",
    "TD": "Chad 🇹🇩",
    "CL": "Chile 🇨🇱",
    "CN": "China 🇨🇳",
    "CO": "Colombia 🇨🇴",
    "KM": "Comoros 🇰🇲",
    "CG": "Congo 🇨🇬",
    "CD": "Democratic Republic of the Congo 🇨🇩",
    "CR": "Costa Rica 🇨🇷",
    "HR": "Croatia 🇭🇷",
    "CU": "Cuba 🇨🇺",
    "CY": "Cyprus 🇨🇾",
    "CZ": "Czech Republic 🇨🇿",
    "DK": "Denmark 🇩🇰",
    "DJ": "Djibouti 🇩🇯",
    "DO": "Dominican Republic 🇩🇴",
    "EC": "Ecuador 🇪🇨",
    "EG": "Egypt 🇪🇬",
    "SV": "El Salvador 🇸🇻",
    "GQ": "Equatorial Guinea 🇬🇶",
    "ER": "Eritrea 🇪🇷",
    "EE": "Estonia 🇪🇪",
    "ET": "Ethiopia 🇪🇹",
    "FJ": "Fiji 🇫🇯",
    "FI": "Finland 🇫🇮",
    "FR": "France 🇫🇷",
    "GA": "Gabon 🇬🇦",
    "GM": "Gambia 🇬🇲",
    "GE": "Georgia 🇬🇪",
    "DE": "Germany 🇩🇪",
    "GH": "Ghana 🇬🇭",
    "GR": "Greece 🇬🇷",
    "GT": "Guatemala 🇬🇹",
    "GN": "Guinea 🇬🇳",
    "GW": "Guinea-Bissau 🇬🇼",
    "GY": "Guyana 🇬🇾",
    "HT": "Haiti 🇭🇹",
    "HN": "Honduras 🇭🇳",
    "HU": "Hungary 🇭🇺",
    "IS": "Iceland 🇮🇸",
    "IN": "India 🇮🇳",
    "ID": "Indonesia 🇮🇩",
    "IR": "Iran 🇮🇷",
    "IQ": "Iraq 🇮🇶",
    "IE": "Ireland 🇮🇪",
    "IL": "Israel 🇮🇱",
    "IT": "Italy 🇮🇹",
    "JM": "Jamaica 🇯🇲",
    "JP": "Japan 🇯🇵",
    "JO": "Jordan 🇯🇴",
    "KZ": "Kazakhstan 🇰🇿",
    "KE": "Kenya 🇰🇪",
    "KP": "North Korea 🇰🇵",
    "KR": "South Korea 🇰🇷",
    "KW": "Kuwait 🇰🇼",
    "KG": "Kyrgyzstan 🇰🇬",
    "LA": "Laos 🇱🇦",
    "LV": "Latvia 🇱🇻",
    "LB": "Lebanon 🇱🇧",
    "LS": "Lesotho 🇱🇸",
    "LR": "Liberia 🇱🇷",
    "LY": "Libya 🇱🇾",
    "LI": "Liechtenstein 🇱🇮",
    "LT": "Lithuania 🇱🇹",
    "LU": "Luxembourg 🇱🇺",
    "MK": "North Macedonia 🇲🇰",
    "MG": "Madagascar 🇲🇬",
    "MW": "Malawi 🇲🇼",
    "MY": "Malaysia 🇲🇾",
    "MV": "Maldives 🇲🇻",
    "ML": "Mali 🇲🇱",
    "MT": "Malta 🇲🇹",
    "MR": "Mauritania 🇲🇷",
    "MU": "Mauritius 🇲🇺",
    "MX": "Mexico 🇲🇽",
    "FM": "Micronesia 🇫🇲",
    "MD": "Moldova 🇲🇩",
    "MC": "Monaco 🇲🇨",
    "MN": "Mongolia 🇲🇳",
    "ME": "Montenegro 🇲🇪",
    "MA": "Morocco 🇲🇦",
    "MZ": "Mozambique 🇲🇿",
    "MM": "Myanmar 🇲🇲",
    "NA": "Namibia 🇳🇦",
    "NR": "Nauru 🇳🇷",
    "NP": "Nepal 🇳🇵",
    "NL": "Netherlands 🇳🇱",
    "NZ": "New Zealand 🇳🇿",
    "NI": "Nicaragua 🇳🇮",
    "NE": "Niger 🇳🇪",
    "NG": "Nigeria 🇳🇬",
    "NO": "Norway 🇳🇴",
    "OM": "Oman 🇴🇲",
    "PK": "Pakistan 🇵🇰",
    "PW": "Palau 🇵🇼",
    "PA": "Panama 🇵🇦",
    "PG": "Papua New Guinea 🇵🇬",
    "PY": "Paraguay 🇵🇾",
    "PE": "Peru 🇵🇪",
    "PH": "Philippines 🇵🇭",
    "PL": "Poland 🇵🇱",
    "PT": "Portugal 🇵🇹",
    "QA": "Qatar 🇶🇦",
    "RO": "Romania 🇷🇴",
    "RU": "Russia 🇷🇺",
    "RW": "Rwanda 🇷🇼",
    "KN": "Saint Kitts and Nevis 🇰🇳",
    "LC": "Saint Lucia 🇱🇨",
    "VC": "Saint Vincent and the Grenadines 🇻🇨",
    "WS": "Samoa 🇼🇸",
    "SM": "San Marino 🇸🇲",
    "ST": "Sao Tome and Principe 🇸🇹",
    "SA": "Saudi Arabia 🇸🇦",
    "SN": "Senegal 🇸🇳",
    "RS": "Serbia 🇷🇸",
    "SC": "Seychelles 🇸🇨",
    "SL": "Sierra Leone 🇸🇱",
    "SG": "Singapore 🇸🇬",
    "SK": "Slovakia 🇸🇰",
    "SI": "Slovenia 🇸🇮",
    "SB": "Solomon Islands 🇸🇧",
    "SO": "Somalia 🇸🇴",
    "ZA": "South Africa 🇿🇦",
    "SS": "South Sudan 🇸🇸",
    "ES": "Spain 🇪🇸",
    "LK": "Sri Lanka 🇱🇰",
    "SD": "Sudan 🇸🇩",
    "SR": "Suriname 🇸🇷",
    "SE": "Sweden 🇸🇪",
    "CH": "Switzerland 🇨🇭",
    "SY": "Syria 🇸🇾",
    "TJ": "Tajikistan 🇹🇯",
    "TZ": "Tanzania 🇹🇿",
    "TH": "Thailand 🇹🇭",
    "TL": "Timor-Leste 🇹🇱",
    "TG": "Togo 🇹🇬",
    "TO": "Tonga 🇹🇴",
    "TT": "Trinidad and Tobago 🇹🇹",
    "TN": "Tunisia 🇹🇳",
    "TR": "Turkey 🇹🇷",
    "TM": "Turkmenistan 🇹🇲",
    "TV": "Tuvalu 🇹🇻",
    "UG": "Uganda 🇺🇬",
    "UA": "Ukraine 🇺🇦",
    "AE": "United Arab Emirates 🇦🇪",
    "GB": "United Kingdom 🇬🇧",
    "US": "United States 🇺🇸",
    "UY": "Uruguay 🇺🇾",
    "UZ": "Uzbekistan 🇺🇿",
    "VU": "Vanuatu 🇻🇺",
    "VA": "Vatican City 🇻🇦",
    "VE": "Venezuela 🇻🇪",
    "VN": "Vietnam 🇻🇳",
    "YE": "Yemen 🇾🇪",
    "ZM": "Zambia 🇿🇲",
    "ZW": "Zimbabwe 🇿🇼"
}