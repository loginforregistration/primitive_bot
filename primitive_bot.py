# -*- coding: utf-8 -*-
from telegram.ext import Updater         # пакет называется python-telegram-bot, но Python-
from telegram.ext import CommandHandler  # модуль почему-то просто telegram ¯\_(ツ)_/¯
from telegram.ext import MessageHandler
from telegram.ext import RegexHandler
import sqlite3

# C:\Users\user\Documents\DB_001
def start(bot, update):
    # подробнее об объекте update: https://core.telegram.org/bots/api#update
    bot.sendMessage(chat_id=update.message.chat_id, text="Введите вопрос")
    print(update.message.chat.username)
    con = sqlite3.connect('db_001.db')
    cur = con.cursor()
    results = search(cur, update, "About_military", "Question")
    bot.sendMessage(chat_id=update.message.chat_id, text=str(results))
    con.close()

def search(cur, update, table, column):
    cur.execute("SELECT * "
                "FROM " + table + " "
                "WHERE " + column + " LIKE '%" + str(update.message.text) + "%'")
    return str(cur.fetchone()).split("'")[3]

updater = Updater(token='499411892:AAEUsC0XtVTP-TEn3zFW7yovccDvC4LmJg8')  # тут токен, который выдал вам Ботский Отец!

start_handler = CommandHandler('', start)  # этот обработчик реагирует
                                                # только на команду /start
start_handler = RegexHandler('.+', start)

#updater.dispatcher.
updater.dispatcher.add_handler(start_handler)   # регистрируем в госреестре обработчиков
updater.start_polling()  # поехали!
