#!/usr/bin/env
import telebot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#Put bot api key
BOT_API = ""
bot = telebot.TeleBot(token=BOT_API)
english_bot = ChatBot("Steve", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")

@bot.message_handler(commands=['start'])
def start(message):
	print("User: {}".format(message.text))
	bot.reply_to(message, "Welcome, my name is Steve")
	
@bot.message_handler(func=lambda m: True)
def echo_message(message):
	print("User: {}".format(message.text))
	response = bot_respond(message.text)
	bot.reply_to(message, str(response))
	print("Steve: {}".format(response))


def bot_respond(message):
	return str(english_bot.get_response(message))

bot.polling()
