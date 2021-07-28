# Telegram ChatBot
A telegram chatbot built with Chatterbot Python library. The bot trains itself with a pre-computed data set from [ChatterBot Corpus](https://chatterbot.readthedocs.io/en/stable/corpus.html) to engage in a converstaion. The bot stores the chat sqlite3 database named db.sqlite3 and uses this to train/imporve itself.

# Requirements
* chatterbot==1.0.0
* chatterbot-corpus
* pyTelegramBotApi

# Installation
**Step 1**
```console
root@pc:~# git clone https://github.com/Tropes-Ot/Telegram-ChatBot.git
```
* [Setup virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
```console
root@pc:~# pip3 install requirements.txt #listed above
```
**Step 2**
* Create [Telegram Bot](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
* [Disable Group Privacy](https://teleme.io/articles/group_privacy_mode_of_telegram_bots)
* Get the bot API key and set in the __init__.py

**Step 3**
```console
root@pc:~# python3 __init__.py
```
* Start converstion with bot
