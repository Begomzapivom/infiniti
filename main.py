
import telebot
bot = telebot.TeleBot('1865729104:AAG-aM4Xs9xmK8zsxTrVnDOU9GrMEmjeHc8')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')
    
bot.polling(none_stop=True)