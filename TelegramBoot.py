import config
import telebot
from telebot import types
import requests
import json

bot = telebot.TeleBot(config.my_token, parse_mode='HTML')


@bot.message_handler(commands=['start', 'button'])
def start_message(message):
	if message.text == '/start':
		bot.send_message(message.chat.id, 'Привет ✌️')
	elif message.text == '/button':
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton(text='HTTP_Request')
		keyboard.add(item1)
		bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'HTTP_Request')
def write_to_support(message):
	# http_requests = requests.get('http://127.0.0.1:8000/drf_employees_test/1/')
	http_requests = requests.get('http://127.0.0.1:8000/drf_questions/1/questions_test/')
	parsing_json = json.loads(http_requests.text)
	bot.send_message(message.chat.id, parsing_json)


bot.infinity_polling()
