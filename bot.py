import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

if __name__ == '__main__':
     bot.infinity_polling()