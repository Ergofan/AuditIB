import asyncio, requests, json, base64, hashlib, datetime, re, aiohttp, io, logging, sys
thissite = 'https://creator.nightcafe.studio/u/Hag'
hashsite = base64.urlsafe_b64encode(thissite.encode()).decode().strip("=")
print(hashsite)