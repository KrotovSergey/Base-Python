import requests
import random
from bs4 import BeautifulSoup as bs
import telebot

URL = 'https://www.anekdot.ru/last/good'

TOKEN = '5988543394:AAH2GbufnTsIfxxRJqPZA2Ru4MA_8DhwC7A'


def parsing(url):
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    anekdot = soup.find_all('div', class_='text')
    return [c.text for c in anekdot]

clear_anekdots = parsing(URL)
random.shuffle(clear_anekdots)


bot = telebot.TeleBot(TOKEN)
@bot.message_handler(command=["начать"])

def hello(message):
    bot.send_message(message.chat.id, 'чтобы получить анекдот нажми любую цифру')

@bot.message_handler(content_types=['text'])

def jokes(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, clear_anekdots[0])
        del clear_anekdots[0]
    else:
        bot.send_message(message.chat.id, 'нужно ввести цифру')

bot.polling()

