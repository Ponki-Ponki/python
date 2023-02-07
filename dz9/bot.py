import telebot
from telebot import types
import random

# bot name    @py_32_bot (https://t.me/py_32_bot)
bot = telebot.TeleBot("5851996036:AAES5jL097Lq30krvr6r8npoh1dBy4GcBoI")

sweets = 200
max_sweet = 28
a = 0
name1 = 'User'
name2 = "bot"
flag = name1


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Узнать правила игры")
    but2 = types.KeyboardButton("Играть")
    but3 = types.KeyboardButton("Рестарт")
    markup.add(but1)
    markup.add(but2)
    markup.add(but3)
    bot.send_message(message.chat.id, "Выбери ниже", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def controller(message):
    global flag,max_sweet,sweets
    if message.text == "Узнать правила игры":
        bot.send_message(message.chat.id, f"На столе лежит {sweets} конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем {max_sweet} конфет. Все конфеты оппонента достаются сделавшему последний ход.")
    elif message.text == "Играть":
        bot.send_message(message.chat.id, "Давай начнем")
        first_turn = random.choice([name1, name2])
        flag = name1 if first_turn == name1 else name2
        bot.send_message(message.chat.id, f"Первым ходит {flag}, нажмите 'играть' ")
        bot.register_next_step_handler(message, play)
    elif message.text == "Рестарт":
        restart(message)


def user_turn(message):
    global a, sweets, flag, max_sweet
    a = int(message.text)
    if a > max_sweet or a < 1:
        bot.send_message(
            message.chat.id, "Вы ввели не правильное количество конфет")
        play(message)
    else:
        sweets -= a
        if sweets < 1:
            play(message)
        else:
            flag = name2
            play(message)


def bot_turn(message):
    global a, max_sweet, sweets, flag
    if max_sweet > sweets:
        max_sweet = sweets
    turn = random.randint(1, max_sweet)
    bot.send_message(message.chat.id, f"bot взял {turn} конфет.")
    sweets -= turn
    if sweets == 0 and sweets < 0:
        bot.send_message(message.chat.id, f'Конфет осталось - 0')
    else:
        flag = name1
    play(message)


def play(message):
    global a, sweets, flag
    if sweets > 0:
        bot.send_message(
            message.chat.id, f"конфет осталось - {sweets}, ходит {flag}")
        if flag == name1:
            bot.send_message(
                message.chat.id, "Введите кол-во конфет от 1 до 28")
            bot.register_next_step_handler(message, user_turn)
        else:
            bot_turn(message)
    else:
        bot.send_message(
            message.chat.id, f"Поздравляем победил игрок {flag}")


def restart(message):
    global a, sweets
    a = 0
    sweets = 200
    bot.send_message(message.chat.id, "Игра сброшена, можно начать новую игру")


bot.infinity_polling()
