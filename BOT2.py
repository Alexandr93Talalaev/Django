import telebot
bot = telebot.TeleBot('1653643163:AAEQyL8XTpfAemYoBXWzoarlONcr16UL2m4')
@bot.message_handler(content_types=["text","document","audio"])
if message.text() == "Привет":
    bot.send_message(message.from_user.id,"Привет,чем я могу тебе помочь?")
elif message.text() == "/help":
    bot.send_message(message.from_user.id,"Напиши Привет")
else:
    bot.send_message(message.from_user.id, "Я тебя не понимаю, напиши /help")
bot.polling(none_stop=True, interval=0)