from telebot import TeleBot, types

TELEGRAM_TOKEN = '6512871872:AAFhDjesvJ1CU4F8wkyBjOgdQQki4RqAW8o'

# Инициализация бота Telegram
bot = TeleBot(TELEGRAM_TOKEN)
andrtxt = 'Привет, это бот. Сейчас Андрей не может ответить на твое сообщение, но я ему передал, что ты заходил'
users = [763649163]
myid = 763649163


@bot.business_message_handler(func=lambda message: True, content_types=['text', 'photo', 'video'])
def handle_business_message(message):
    user_id = message.chat.id
    chel_id = message.from_user.id
    business_connection_id = message.business_connection_id
    print(message.text)
    print('chatid', user_id)
    print('user writing:', chel_id)

    if chel_id not in users and chel_id != myid:
        bot.send_message(message.chat.id, andrtxt, reply_to_message_id=message.id,
                         business_connection_id=business_connection_id)
    
        bot.send_message(myid, f"пишет чел такой tg://user?id={chel_id}: \n {message.text}")
        users.append(chel_id)
    else:
        pass
    
    print(f'in users now: {users}')


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Привет! Я ваш бот.")
    print(message.text)


@bot.message_handler(content_types=['text'])
def reply(message):
    bot.send_message(message, "Привет! Я ваш бот, информации не было!")
    print(message.text)


bot.polling(none_stop=True, interval=0)
