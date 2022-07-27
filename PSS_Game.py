import random

import telebot
from telebot import types

from DB_for_PSS_Game import id_lst, db

bot = telebot.TeleBot(token='5540090670:AAEb8EKPXB1lyq6OGY3ODMtrGB01fcGAEqg')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Привет, Бот!")
    markup.add(btn1)
    bot.send_message(message.from_user.id, text="Привет! Я Бот для игры в камень-ножницы-бумага!"
                     .format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    comp = random.randint(1, 9999)
    if 1 <= comp <= 3333:
        comp = "Камень 🗿"
    elif 3333 < comp <= 6666:
        comp = "Бумага 📄"
    elif 6666 < comp <= 9999:
        comp = "Ножницы ✂"
    if db['player_win'] < 5 and db['bot_win'] < 5:
        if message.text == "Играть 🕹" or message.text == "Играть без авторизации 🕹":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Камень 🗿")
            btn2 = types.KeyboardButton("Ножницы ✂")
            btn3 = types.KeyboardButton("Бумага 📄")
            btn4 = types.KeyboardButton("Помощь ❓")
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.from_user.id, text="Выберите свой ход или Помощь ❓",
                             reply_markup=markup)
        elif message.text == "Камень 🗿" or message.text == "Бумага 📄" or message.text == "Ножницы ✂":
            bot.send_message(message.from_user.id, f"Ход Бота - {comp}")
            if message.text == "Камень 🗿":
                if comp == message.text:
                    bot.send_message(message.from_user.id,
                                     f"Игрок и Бот выбрали одинаковый ход. Ничья! 🤝")
                elif comp == "Бумага 📄":
                    bot.send_message(message.from_user.id, f"Игрок проиграл... 😱")
                    db['bot_win'] = db['bot_win'] + 1
                else:
                    bot.send_message(message.from_user.id, f"Игрок выиграл! ✌")
                    db['player_win'] = db['player_win'] + 1
            elif message.text == "Ножницы ✂":
                if comp == message.text:
                    bot.send_message(message.from_user.id,
                                     f"Игрок и Бот выбрали одинаковый ход. Ничья! 🤝")
                elif comp == "Камень 🗿":
                    bot.send_message(message.from_user.id, f"Игрок проиграл... 😱")
                    db['bot_win'] = db['bot_win'] + 1
                else:
                    bot.send_message(message.from_user.id, f"Игрок выиграл! ✌")
                    db['player_win'] = db['player_win'] + 1
            elif message.text == "Бумага 📄":
                if comp == message.text:
                    bot.send_message(message.from_user.id,
                                     f"Игрок и Бот выбрали одинаковый ход. Ничья! 🤝")
                elif comp == "Ножницы ✂":
                    bot.send_message(message.from_user.id, f"Игрок проиграл... 😱")
                    db['bot_win'] = db['bot_win'] + 1
                else:
                    bot.send_message(message.from_user.id, f"Игрок выиграл! ✌")
                    db['player_win'] = db['player_win'] + 1
        elif message.text == "Войти в свой аккаунт 🚪":
            if message.from_user.id not in id_lst:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Играть без авторизации 🕹")
                markup.add(btn1)
                bot.send_message(message.from_user.id, f"Вас нет в базе данных...Просто играйте без авторизации!")
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Играть 🕹")
                markup.add(btn1)
                bot.send_message(message.from_user.id, f"Вы в базе данных! Привет! "
                                                       f"Жми Играть 🕹", reply_markup=markup)
        elif message.text == "Очистить 🧽":
            bot.send_message(message.from_user.id,
                             f"Игра окончена со счетом Игрок {db['player_win']} - Бот {db['bot_win']}, "
                             f"счет обнулен")
            bot.send_message(message.from_user.id, f"Напишите Играть 🕹 для начала новой игры")
            db['bot_win'] = 0
            db['player_win'] = 0
        elif message.text == "Счет 🧮":
            bot.send_message(message.from_user.id, f"Игрок {db['player_win']} - Бот {db['bot_win']}")
            bot.send_message(message.from_user.id,
                             "Нажмите Играть 🕹 для продолжения игры")
        elif message.text == "Серия побед 🏆":
            if db['player_win'] > db['bot_win']:
                bot.send_message(message.from_user.id, f"Серия побед Игрока  - {db['player_win']} 🏆")
            elif db['player_win'] < db['bot_win']:
                bot.send_message(message.from_user.id, f"Серия побед Бота - {db['bot_win']} 🏆")
            else:
                bot.send_message(message.from_user.id,
                                 f"У Вас и Бота одинаковое число побед Игрок - {db['player_win']}   "
                                 f"Бот - {db['bot_win']}")
            bot.send_message(message.from_user.id,
                             "Нажмите Играть 🕹 для продолжения игры")
        elif message.text == "Помощь ❓":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Играть 🕹")
            btn2 = types.KeyboardButton("Счет 🧮")
            btn3 = types.KeyboardButton("Серия побед 🏆")
            btn4 = types.KeyboardButton("Очистить 🧽")
            btn5 = types.KeyboardButton("Войти в свой аккаунт 🚪")
            markup.add(btn1, btn2, btn3, btn4, btn5)
            bot.send_message(message.from_user.id, text="Выберите Играть 🕹 для начала игры, Счет 🧮, Серия побед "
                                                        "🏆 или Очистить 🧽 для сброса счета", reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Камень 🗿")
            btn2 = types.KeyboardButton("Ножницы ✂")
            btn3 = types.KeyboardButton("Бумага 📄")
            btn4 = types.KeyboardButton("Помощь ❓")
            btn5 = types.KeyboardButton("Войти в свой аккаунт 🚪")
            markup.add(btn1, btn2, btn3, btn4, btn5)
            bot.send_message(message.from_user.id, text="Выберите свой ход для начала игры, Помощь ❓ "
                                                        "или Войдите в свой аккаунт",
                             reply_markup=markup)
    elif db['player_win'] == 5:
        bot.send_message(message.from_user.id, f"Игрок выиграл матч, одержав {db['player_win']} побед! 🏆")
        bot.send_message(message.from_user.id, f"Бот набрал {db['bot_win']}")
        db['bot_win'] = 0
        db['player_win'] = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Играть 🕹")
        markup.add(btn1)
        bot.send_message(message.from_user.id, f"Нажмите Играть 🕹 для нового матча!", reply_markup=markup)
    elif db['bot_win'] == 5:
        bot.send_message(message.from_user.id, f"Бот выиграл матч, одержав {db['bot_win']} побед!...😱")
        bot.send_message(message.from_user.id, f"Игрок набрал {db['player_win']}")
        db['bot_win'] = 0
        db['player_win'] = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Играть 🕹")
        markup.add(btn1)
        bot.send_message(message.from_user.id, f"Нажмите Играть 🕹 для нового матча!", reply_markup=markup)


bot.polling(none_stop=True, interval=0)
