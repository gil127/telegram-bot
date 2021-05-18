import telebot

API_TOKEN = ''

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
	disagree_message = "Dear {0} {1} \n No, you are {2} !!!".format(message.from_user.first_name, message.from_user.last_name, message.text)
	bot.reply_to(message, disagree_message)


bot.polling()