import telebot

from crypto.config import ConretionException, CryptConveret
from crypto.data import TOKEN, keys

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'To get started, enter the command for the bot in the following format  :\n ' \
        '<Name of currency>\ < What currency to transfer> \  <amount of transferred currency> ' \
        'see the currencies available for transfer /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Available currencies'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert( message: telebot.types.Message ):
    try:
        values = message.text.split(' ')
        quot, base, amount = values
        if len(values) != 3:
            raise ConretionException('Too many parameters')
        total_base = CryptConveret.convert(quot, base, amount)
        am = float(values[2])
        sum = total_base * am
        text = f'Цена {amount} {quot}, в {base} - {sum}'
        bot.send_message(message.chat.id, text)
    except ConretionException as e:
        bot.reply_to(message, f'User error\n {e}')
    except Exception as e:
        bot.reply_to(message, f'Failed to process command \n {e}')


bot.polling()
