import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def start(message):
     markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
     item1=types.KeyboardButton("text1")
     item2=types.KeyboardButton("text2")
     item3=types.KeyboardButton("text3")
     item4=types.KeyboardButton("text4")
     markup.add(item1)	
     markup.add(item2)
     markup.add(item3)
     markup.add(item4)
     bot.send_message(message.chat.id, "Start message", reply_markup=markup)	

if __name__ == '__main__':
     bot.infinity_polling()