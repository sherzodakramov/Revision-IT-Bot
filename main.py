# import sqlite3
import telebot

from telebot import types

token = '61075890_nFq26IIpyxFDLLqVWdxmdZsI1bI'

bot = telebot.TeleBot(token)


# conn = sqlite3.connect('C:/Users/Sherzod/db/revision_it.db', check_same_thread=False)
# cursor = conn.cursor()



        



@bot.message_handler(commands=['start'])
def start_message(message):

    bot.send_message(message.from_user.id, 'Revision IT rasmiy botiga xush kelibsiz! \n'
                                       "Ko'proq ma'lumot olish uchun /help buyrug'ini kiriting.")
    

@bot.message_handler(commands=['help'])
def help_message(message):

    bot.send_message(message.from_user.id, '/start - boshlash\n'
                                      "/help - buyruqlar ro'yxati\n"
                                      "/main - menyular ro'yxati"
                                      )

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/main':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #yangi knopkalar qo'shish
        btn1 = types.KeyboardButton('Biz taklif etadigan xizmatlar')
        btn2 = types.KeyboardButton('Biz haqimizda')
        btn3 = types.KeyboardButton('Aloqa')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "Iltimos, kerakli bo'limni tanlang 👇🏼:", reply_markup=markup) #bot javobi

    elif message.text == 'Biz taklif etadigan xizmatlar':
        # bot.send_message(message.from_user.id, 'Вы пишете первый пост, его проверяют модераторы, и, если всё хорошо, отправляют в основную ленту Хабра, где он набирает просмотры, комментарии и рейтинг. В дальнейшем премодерация уже не понадобится. Если с постом что-то не так, вас попросят его доработать.\n \nПолный текст можно прочитать по ' + '[ссылке](https://habr.com/ru/sandbox/start/)', parse_mode='Markdown')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Mobil ilova")
        btn2 = types.KeyboardButton("Veb sayt")
        btn3 = types.KeyboardButton("Telegram bot")
        btn4 = types.KeyboardButton("Bosh menyu")
        

        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, "Tanlang:", reply_markup=markup)

     
    elif message.text == "Mobil ilova":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Bosh menyu")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Mobil ilova nomini kiriting:", reply_markup=markup)


    elif message.text == 'Biz haqimizda':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # bot.send_message(message.from_user.id, 'Прочитать правила сайта вы можете по ' + '[ссылке](https://habr.com/ru/docs/help/rules/)', parse_mode='Markdown')
        btn1 = types.KeyboardButton("Bosh menyu")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Mobil ilova nomini kiriting:", reply_markup=markup)

    elif message.text == 'Aloqa':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # bot.send_message(message.from_user.id, 'Подробно про советы по оформлению публикаций прочитать по ' + '[ссылке](https://habr.com/ru/docs/companies/design/)', parse_mode='Markdown')
        btn1 = types.KeyboardButton("Bosh menyu")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Mobil ilova nomini kiriting:", reply_markup=markup)

bot.infinity_polling()