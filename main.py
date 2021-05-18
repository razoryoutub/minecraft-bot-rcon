from mcrcon import MCRcon
import telebot
import random


mcr = MCRcon(ip, pass)
mcr.disconnect()
mcr.connect()


#resp = mcr.command("/say hi")


from telebot import apihelper

apihelper.proxy = {'https':'http://80.187.140.26:8080'}

bot = telebot.TeleBot("1225831912:AAG60sUGFoeRVePSufgLFM0Xaat176T2t1o")


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
 r = random.randint(0,2)
 if r == 0:
     bot.send_message(message.chat.id, '1')
 elif r == 1:
     bot.send_message(message.chat.id, '2')
 elif r == 2:
     bot.send_message(message.chat.id, '3')




@bot.message_handler(content_types=['text'])
def echo_msg(message):
  bot.send_message(message.chat.id, message.text)
  resp = mcr.command(message.text)





bot.polling(none_stop=True)
