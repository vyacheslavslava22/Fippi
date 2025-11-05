import telebot

BOT_TOKEN = '8479275418:AAHoXo5-aA69Rn_-pCewm90nFkgiWmBox2c'
YOUR_CHAT_ID = 7821316793

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda m: True)
def forward_info(m):
    user = m.from_user
    info = (
        f"⚠️ Новое сообщение:\n\n"
        f"ID: {user.id}\n"
        f"Username: @{user.username if user.username else 'None'}\n"
        f"Имя: {user.first_name} {user.last_name or ''}\n"
        f"Chat ID: {m.chat.id}\n"
        f"Язык: {user.language_code or 'unknown'}\n"
        f"Текст: {m.text}"
    )
    try:
        bot.send_message(YOUR_CHAT_ID, info)
    except:
        pass
    # Не отвечаем — тише едешь, дальше будешь

bot.polling(none_stop=True)
