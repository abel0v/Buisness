import logging

from telebot import TeleBot, types

TELEGRAM_TOKEN = '6512871872:AAEpkj9ZhRUwIW85GfagOhbL05og8MQOioI'

# Инициализация бота Telegram
bot = TeleBot(TELEGRAM_TOKEN)


@bot.business_message_handler(func=lambda message: True, content_types=['text', 'photo', 'video'])
def handle_business_message(message):
    user_id = message.chat.id
    business_connection_id = message.business_connection_id
    print(message.text)
    bot.send_message(message.chat.id, 'ddd', reply_to_message_id=message.id,
                     business_connection_id=business_connection_id)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Привет! Я ваш бот.")
    print(message.text)


bot.polling(none_stop=True, interval=0)
