import telebot
import config
bot = telebot.TeleBot(config.TOKEN)
def f(message):
 return message.text == '.dlmod bfg'
def premium_sticks(message):
    return message.text== '.dlmod premium_sticks'
@bot.message_handler(func=premium_sticks)
def premium_stik(message):
 bot.reply_to(message, '<a href="https://t.me/userbotik/5">Чтобы скачать модуль вам надо сделать юзер бота💫   Нажмите на это сообщение чтобы сделать юзер бота🐸(легче всего сделать бота на гугл клауд и термуксе)</a>', disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(func=f)
def bfg(message):
 bot.reply_to(message, '<a href="https://t.me/userbotik/5">Чтобы скачать модуль вам надо сделать юзер бота💫   Нажмите на это сообщение чтобы сделать юзер бота🐸(легче всего сделать бота на гугл клауд и термуксе)</a>', disable_web_page_preview=True, parse_mode='HTML')

def wini(message):
 return message.text == 'wini'

@bot.message_handler(regexp='wini')
def start(message):
 bot.reply_to(message, '<a href="https://t.me/WiniChat">👾ссылка на чат</a>', disable_web_page_preview=True, parse_mode='HTML')


@bot.message_handler(regexp='бампи')
def bampi(message):
    bot.reply_to(message,'💫На месте')


@bot.message_handler(regexp='bampi')
def bampi2(message):
    bot.reply_to(message,'💫На месте')


@bot.message_handler(regexp='шлюха')
def ock(message):
    bot.reply_to(message,'Понятно')


@bot.message_handler(regexp='!report')
def rep(message):
    bot.reply_to(message,'Ваш репорт отправлен.')

bot.polling(none_stop=True)