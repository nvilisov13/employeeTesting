from config import my_token
import telebot
from telebot import types
import requests
import json

bot = telebot.TeleBot(my_token, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def start_message(message):
    if message.text == '/start':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.KeyboardButton(text='Пройти тест!'))
        bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Пройти тест!')
def write_to_support(message):
    requests_test_info = requests.get('http://127.0.0.1:8000/drf_employees_test/1/')
    parsing_test_info = json.loads(requests_test_info.text)
    bot.send_message(message.chat.id,
                     f"<b><u>{parsing_test_info['NameTest']}\n{parsing_test_info['DescriptionTest']}</u></b>")
    requests_questions = requests.get('http://127.0.0.1:8000/drf_questions/1/questions_test/')
    parsing_questions = json.loads(requests_questions.text)
    for key_questions in parsing_questions:
        bot.send_message(message.chat.id, f'<b><i>{parsing_questions[key_questions][0]}</i></b>')
        requests_answers = requests.get(f'http://127.0.0.1:8000/drf_questions/{key_questions}/question_answers/')
        parsing_answers = json.loads(requests_answers.text)
        keyboard = telebot.types.InlineKeyboardMarkup()
        for key_answers in parsing_answers:
            name_button = parsing_answers[key_answers][0]
            button_save = telebot.types.InlineKeyboardButton(text=f'✅ {name_button}', callback_data=name_button[-34:])
            keyboard.add(button_save)
        bot.send_message(message.chat.id, 'Выберите правильный ответ?', reply_markup=keyboard)
    requests_questions_count = requests.get('http://127.0.0.1:8000/drf_questions/1/question_count/')
    parsing_questions_count = json.loads(requests_questions_count.text)
    bot.send_message(message.chat.id,
                     f"<i><u>Общее количество вопросов тесте - {parsing_questions_count['QuestionCount']}</u></i>")


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    selected_option = call.data
    bot.send_message(call.message.chat.id, f"Вы выбрали опцию: ✅ {selected_option}")
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)


if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling(none_stop=True)
