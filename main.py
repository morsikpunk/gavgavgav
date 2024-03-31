from config import token
import telebot

API_TOKEN = token
bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'мяу')

@bot.message_handler(commands=['sos'])
def send_sos(message):
    bot.send_message(message.chat.id, 'огооо огооо гогоо огоооооо')

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, message.text)

bot.infinity_polling()