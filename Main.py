from telebot import TeleBot, types

TELEGRAM_TOKEN = '6512871872:AAEpkj9ZhRUwIW85GfagOhbL05og8MQOioI'

# Инициализация бота Telegram
bot = TeleBot(TELEGRAM_TOKEN)
andrtxt = 'Привет, это бот. Сейчас Андрей не может ответить на твое сообщение, но я ему передал, что ты заходил'
users = [763649163]


@bot.business_message_handler(func=lambda message: True, content_types=['text', 'photo', 'video'])
def handle_business_message(message):
    user_id = message.chat.id
    chel_id = message.from_user.id
    business_connection_id = message.business_connection_id
    print(message.text)
    print('chatid', user_id)
    print('user writing:', chel_id)

    if chel_id not in users:
        bot.send_message(message.chat.id, andrtxt, reply_to_message_id=message.id,
                         business_connection_id=business_connection_id)
        users.append(chel_id)
    else:
        pass
    print(f'in users now: {users}')


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Привет! Я ваш бот.")
    print(message.text)


bot.polling(none_stop=True, interval=0)
