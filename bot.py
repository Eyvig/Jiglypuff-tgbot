import telebot
from telebot import types

bot = telebot.TeleBot('#Your token')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>❤'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler()
def get_user_text(message):
    if message.text == 'Привет':
     bot.send_message(message.chat.id, 'И тебе привет!☺', parse_mode='html')
    elif message.text == 'Хочу музыку':
        bot.send_message(message.chat.id, 'Вот тебе моя расслабляющая песенка🎤', parse_mode='html')
        bot.send_audio(message.chat.id, open('Jigly.mp3', 'rb'))
    elif message.text == 'Песня Джигли':
        bot.send_message(message.chat.id, 'Вот тебе моя расслабляющая песенка🎤', parse_mode='html')
        bot.send_audio(message.chat.id, open('Jigly.mp3', 'rb'))
    else:
       bot.send_message(message.chat.id, 'Я тебя не понимаю🥺', parse_mode='html')


bot.polling(none_stop=True)
