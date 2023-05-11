import telebot
import psycopg2
from telebot import types
from decouple import config


connection = psycopg2.connect(user=config('DB_USER'),
                                password=config('DB_PASSWORD'),
                                host=config('DB_HOST'),
                                port=config('DB_PORT'),
                                database=config('DB_NAME'))
cursor = connection.cursor()
connection.commit();
# cursor.execute("SELECT * FROM election_citizens WHERE election_uchastka_id IS NULL AND election_status_id = 1  LIMIT 300 OFFSET 0;")

bot = telebot.TeleBot(config('TG_BOT_TOKEN'))

@bot.message_handler(commands=['start'])
def start_message(message):
    
    cursor.execute("SELECT * FROM users WHERE chat_id = %s;", [message.from_user.id])
    user = cursor.fetchall()
    if not user:
        cursor.execute("INSERT INTO users (chat_id, first_name, last_name, username) VALUES(%s, %s, %s, %s);", [message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username])
        connection.commit()
    bot.send_message(message.chat.id, 'Revision IT rasmiy botiga xush kelibsiz! \n'
                                       "Ko'proq ma'lumot olish uchun /help buyrug'ini kiriting.")
    bot.send_message(message.chat.id, '/start - boshlash\n'
                                      "/help - buyruqlar ro'yxati\n"
                                      "/main - menyular ro'yxati"
                                      )


#################################                                      

    keyboard = types.ReplyKeyboardMarkup (row_width = 1, resize_keyboard = True)
    button_phone = types.KeyboardButton (text = "Telefon raqamni yuborish", request_contact = True)
    keyboard.add (button_phone)
    bot.send_message (message.chat.id, 'Telefon raqamingizni yuboring', reply_markup = keyboard)

@bot.message_handler (content_types = ['contact']) # Announced a branch in which we prescribe logic in case the user decides to send a phone number :)
def contact (message):
    if message.contact is not None: # If the sent object <strong> contact </strong> is not zero
        cursor.execute("UPDATE users SET phone = %s WHERE chat_id = %s;", [message.contact.phone_number, message.from_user.id])
        connection.commit()

#################################    
    
@bot.message_handler(commands=['help'])
def help_message(message):

    bot.send_message(message.chat.id, '/start - boshlash\n'
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
        bot.send_message(message.chat.id, "Iltimos, kerakli bo'limni tanlang 👇🏼:", reply_markup=markup) #bot javobi

    elif message.text == 'Biz taklif etadigan xizmatlar':
        # bot.send_message(message.chat.id, 'Вы пишете первый пост, его проверяют модераторы, и, если всё хорошо, отправляют в основную ленту Хабра, где он набирает просмотры, комментарии и рейтинг. В дальнейшем премодерация уже не понадобится. Если с постом что-то не так, вас попросят его доработать.\n \nПолный текст можно прочитать по ' + '[ссылке](https://habr.com/ru/sandbox/start/)', parse_mode='Markdown')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Mobil ilova")
        btn2 = types.KeyboardButton("Veb sayt")
        btn3 = types.KeyboardButton("Telegram bot")
        btn4 = types.KeyboardButton("Bosh menyu")
        

        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, "Tanlang:", reply_markup=markup)

     
    elif message.text == "Mobil ilova":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Bosh menyu")
        markup.add(btn1)
        bot.send_message(message.chat.id, "Mobil ilova nomini kiriting:", reply_markup=markup)

        cursor.execute("INSERT INTO orders (chat_id, service) VALUES(%s, %s) RETURNING id;", [message.from_user.id, message.text])
        order_id = cursor.fetchone()[0]

        cursor.execute("UPDATE users SET current_order_id = %s, current_action = 'waiting_order_name' WHERE chat_id = %s;", [order_id, message.from_user.id])
        connection.commit()

    elif message.text == 'Biz haqimizda':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # bot.send_message(message.chat.id, 'Прочитать правила сайта вы можете по ' + '[ссылке](https://habr.com/ru/docs/help/rules/)', parse_mode='Markdown')
        btn1 = types.KeyboardButton("Bosh menyu")
        markup.add(btn1)
        bot.send_message(message.chat.id, "Mobil ilova nomini kiriting:", reply_markup=markup)

    elif message.text == 'Aloqa':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # bot.send_message(message.chat.id, 'Подробно про советы по оформлению публикаций прочитать по ' + '[ссылке](https://habr.com/ru/docs/companies/design/)', parse_mode='Markdown')
        btn1 = types.KeyboardButton("Bosh menyu")
        markup.add(btn1)
        bot.send_message(message.chat.id, "Mobil ilova nomini kiriting:", reply_markup=markup)
    
    else:
        cursor.execute("SELECT * FROM users WHERE chat_id = %s;", [message.from_user.id])
        user = cursor.fetchone()
        if user[7] == 'waiting_order_name':
            cursor.execute("UPDATE orders SET name = %s WHERE id = %s;", [message.text, user[6]])
            connection.commit()
            cursor.execute("UPDATE users SET current_action = 'waiting_order_sphere' WHERE chat_id = %s;", [message.from_user.id])
            connection.commit()

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Bosh menyu")
            markup.add(btn1)
            bot.send_message(message.chat.id, "Mobil ilova yo'nalishini kiriting:", reply_markup=markup)

        elif user[7] == 'waiting_order_sphere':
            cursor.execute("UPDATE orders SET sphere = %s WHERE id = %s;", [message.text, user[6]])
            connection.commit()
            cursor.execute("SELECT * FROM orders WHERE id = %s;", [user[6]])
            order = cursor.fetchone()
            cursor.execute("UPDATE users SET current_action = 'waiting_order_confirmation' WHERE chat_id = %s;", [message.from_user.id])
            connection.commit()

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Tasdiqlash")
            markup.add(btn1)
            bot.send_message(message.chat.id, "Buyurtmangizni tasdiqlang!\nBuyurtma turi: " + order[2] + "\nNomi: " + order[3] + "\nYo‘nalishi: " + order[4], reply_markup=markup)

        elif user[7] == 'waiting_order_confirmation':
            cursor.execute("SELECT * FROM orders WHERE id = %s;", [user[6]])
            order = cursor.fetchone()
            cursor.execute("UPDATE users SET current_action = null, current_order_id = null WHERE chat_id = %s;", [message.from_user.id])
            connection.commit()

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Bosh menyuga qaytish")
            markup.add(btn1)
            bot.send_message(message.chat.id, "Buyurtmangiz qabul qilindi!", reply_markup=markup)
            bot.send_message(-939668063, "Yangi buyurtma qabul qilindi!\nBuyurtma turi: " + order[2] + "\nNomi: " + order[3] + "\nYo‘nalishi: " + order[4], reply_markup=markup)
        else:
            bot.send_message(message.chat.id, message.chat.id, reply_markup=markup)

bot.infinity_polling()