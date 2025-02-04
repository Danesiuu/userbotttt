import json

import requests
from pyrogram import filters

from PyroUbot import *
from PyroUbot.config import *
from PyroUbot import eor

__MODULE__ = "adzan"
__HELP__ = f"""
 Document for Adzan

• Command: <code>{cmd[0]}adzan</code> [nama kota]
• Function: Untuk mengetahui jadwal adzan di lokasi anda.
"""


@PY.UBOT("adzan")
async def _(client, message):
    LOKASI = message.text.split(None, 1)[1]
    if len(message.command) < 2:
        return await eor(message, "<b>Silahkan Masukkan Nama Kota Anda</b>")
    url = f"http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    request = requests.get(url)
    if request.status_code != 200:
        await eor(message, f"<b>Maaf Tidak Menemukan Kota <code>{LOKASI}</code>")
    result = json.loads(request.text)
    catresult = f"""
Jadwal Shalat Hari Ini

<b>Tanggal</b> <code>{result['items'][0]['date_for']}</code>
<b>Kota</b> <code>{result['query']} | {result['country']}</code>

<b>Terbit:</b> <code>{result['items'][0]['shurooq']}</code>
<b>Subuh:</b> <code>{result['items'][0]['fajr']}</code>
<b>Zuhur:</b> <code>{result['items'][0]['dhuhr']}</code>
<b>Ashar:</b> <code>{result['items'][0]['asr']}</code>
<b>Maghrib:</b> <code>{result['items'][0]['maghrib']}</code>
<b>Isya:</b> <code>{result['items'][0]['isha']}</code>
"""
    await eor(message, catresult)
