import random
import dp as dp
import telebot
from telebot import types
import config
from DB_for_PSS_Game import db
bot = telebot.TeleBot(token='5540090670:AAEb8EKPXB1lyq6OGY3ODMtrGB01fcGAEqg')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Начать играть")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я Бот для игры в камень-ножницы-бумага"
                     .format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    moves = ["Камень 🗿", "Бумага 📄", "Ножницы ✂"]
    comp = random.choice(moves)
    if message.text == "Играть 🕹" or message.text == "Начать играть":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Камень 🗿")
        btn2 = types.KeyboardButton("Ножницы ✂")
        btn3 = types.KeyboardButton("Бумага 📄")
        btn4 = types.KeyboardButton("Помощь ❓")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text="Выберите свой ход для начала игры, или Помощь ❓ "
                                               "для помощи", reply_markup=markup)
    elif message.text == "Камень 🗿" or message.text == "Бумага 📄" or message.text == "Ножницы ✂":
        bot.send_message(message.from_user.id, f"Ход 🤖 Бота {comp}")
        if message.text == "Камень 🗿":
            if comp == message.text:
                bot.send_message(message.from_user.id, f"🧑‍💻 Игрок и 🤖 Бот выбрали одинаковый ход. Ничья! 🤝")
            elif comp == "Бумага 📄":
                bot.send_message(message.from_user.id, f"🧑‍💻 Игрок проиграл... 😱")
                db['bot_win'] = db['bot_win'] + 1
            else:
                bot.send_message(message.from_user.id, f"🧑‍💻 Игрок выиграл! ✌")
                db['player_win'] = db['player_win'] + 1
            bot.send_message(message.from_user.id,
                             "Выберите свой ход для продолжения игры или Помощь ❓ для помощи")
        elif message.text == "Ножницы ✂":
            if comp == message.text:
                bot.send_message(message.from_user.id, f"🧑‍💻 Игрок и 🤖 Бот выбрали одинаковый ход. Ничья! 🤝")
            elif comp == "Камень 🗿":
                bot.send_message(message.from_user.id, f"🧑‍💻 Игрок проиграл... 😱")
                db['bot_win'] = db['bot_win'] + 1
            else:
                bot.send_message(message.from_user.id, f"🧑‍💻 Игрок выиграл! ✌")
                db['player_win'] = db['player_win'] + 1
            bot.send_message(message.from_user.id,
                             "Выберите свой ход для продолжения игры или Помощь ❓ для помощи")
        elif message.text == "Бумага 📄":
            if comp == message.text:
                bot.send_message(message.from_user.id, f"🧑‍💻 Игрок и 🤖 Бот выбрали одинаковый ход. Ничья! 🤝")
            elif comp == "Ножницы ✂":
                bot.send_message(message.from_user.id, f"🧑‍💻 Игрок проиграл... 😱")
                db['bot_win'] = db['bot_win'] + 1
            else:
                bot.send_message(message.from_user.id, f"🧑‍💻 Игрок выиграл! ✌")
                db['player_win'] = db['player_win'] + 1
            bot.send_message(message.from_user.id,
                             "Выберите свой ход для продолжения игры или Помощь ❓ для помощи")
    elif message.text == "Очистить 🧽":
        bot.send_message(message.from_user.id,
                         f"Игра окончена со счетом 🧑‍💻 Игрок {db['player_win']} - 🤖 Бот {db['bot_win']}, счет обнулен")
        bot.send_message(message.from_user.id, f"Напишите Играть 🕹 для начала новой игры")
        db['bot_win'] = 0
        db['player_win'] = 0
    elif message.text == "Счет 🧮":
        bot.send_message(message.from_user.id, f"🧑‍💻 Игрок {db['player_win']} - 🤖 Бот {db['bot_win']}")
        bot.send_message(message.from_user.id,
                         "Нажмите Играть 🕹 для продолжения игры")
    elif message.text == "Серия побед 🏆":
        if db['player_win'] > db['bot_win']:
            bot.send_message(message.from_user.id, f"Серия побед 🧑‍💻 Игрока  - {db['player_win']} 🏆")
        elif db['player_win'] < db['bot_win']:
            bot.send_message(message.from_user.id, f"Серия побед 🤖 Бота - {db['bot_win']} 🏆")
        else:
            bot.send_message(message.from_user.id,
                             f"У Вас и Бота одинаковое число побед 🧑‍💻 Игрок {db['player_win']} - "
                             f"🤖 Бот {db['bot_win']}")
        bot.send_message(message.from_user.id,
                         "Выберите Камень 🗿, Бумага 📄, Ножницы ✂ продолжения игры, Помощь ❓ для помощи")
    elif message.text == "Помощь ❓":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Играть 🕹")
        btn2 = types.KeyboardButton("Счет 🧮")
        btn3 = types.KeyboardButton("Серия побед 🏆")
        btn4 = types.KeyboardButton("Очистить 🧽")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text="Выберите Играть 🕹 для начала игры, Счет 🧮 для таблицы, Серия побед "
                                               "🏆 для "
                                               "серии побед, Очистить 🧽 для сброса счета", reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Помощь ❓")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Выберите Помощь ❓", reply_markup=markup)


bot.polling(none_stop=True, interval=0)
