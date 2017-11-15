# -*- coding: utf-8 -*-
from telegram.ext import Updater         # пакет называется python-telegram-bot, но Python-
from telegram.ext import CommandHandler  # модуль почему-то просто telegram ¯\_(ツ)_/¯
from telegram.ext import MessageHandler
from telegram.ext import RegexHandler
import sqlite3

DB_FAQ_KAI = "db_001.db"

needed_column = 2

column_index = (needed_column*2)-1

# C:\Users\user\Documents\DB_001
def start(bot, update):
    # подробнее об объекте update: https://core.telegram.org/bots/api#update
    print(update.message.chat.username)
    con = sqlite3.connect(DB_FAQ_KAI)
    cur = con.cursor()
    results = search(cur, update, "Reply", "About_military", "Question")
    bot_message(bot, update, str(results))
    con.close()
    bot_message(bot, update, "Введите вопрос")

def search(cur, update, column_reply, table, column):
    cur.execute("SELECT " + column_reply + " "
                "FROM " + table + " "
                "WHERE " + column + " LIKE '%" + str(update.message.text) + "%'")
    return fetch1(cur)

def bot_message(bot, update, question):
    bot.sendMessage(chat_id=update.message.chat_id, text=question)

def fetch1(cur):
    return str(cur.fetchone())
    # str(cur.fetchone()).split("'")[column_index]

updater = Updater(token='499411892:AAEUsC0XtVTP-TEn3zFW7yovccDvC4LmJg8')  # тут токен, который выдал вам Ботский Отец!

start_handler = CommandHandler('', start)  # этот обработчик реагирует
                                                # только на команду /start
start_handler = RegexHandler('.+', start)

#updater.dispatcher.
updater.dispatcher.add_handler(start_handler)   # регистрируем в госреестре обработчиков
updater.start_polling()  # поехали!
