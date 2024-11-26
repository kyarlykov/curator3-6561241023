from telebot import TeleBot

vasiabot = TeleBot ("7676467696:AAHExW-P923Gm0O5Q0kpOemr10-vDegaAYM")

@vasiabot.message_handler(commands=["start"])
def start(message):
    vasiabot.send_message(message.chat.id, 'Привет, напиши /привет или /1+1 что бы узнать чему равен 1+1')

@vasiabot.message_handler(commands=["привет"])
def hi(message):
    vasiabot.send_message(message.chat.id, "Приветствую, есть ли у тебя еда? Если еды нет, я не буду считать.")

@vasiabot.message_handler(commands=["1+1"])
def ch(message):
    vasiabot.send_message(message.chat.id, 'Нет еды, нет счета (я не умею считать)')

@vasiabot.message_handler(commands=["еда"])
def eat(message):
    vasiabot.send_message(message.chat.id, 'Спасибо. Покушаль. Считать от этого я все равно не научусь')

vasiabot.infinity_polling()