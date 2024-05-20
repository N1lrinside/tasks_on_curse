import re
from telegram import Update
from telegram.ext import (filters, MessageHandler, ApplicationBuilder,
                          ContextTypes, CommandHandler)
import json
from datetime import datetime

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('''
    Бот может здороваться на разных языках.
    Список поддерживаемых приветствий:
    - привет - русский
    - hello - английский
    - hola - испанский
    ''')

async def ru(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = json.dumps(update.to_dict(), indent=2)
    print(text)
    h=json.loads(text)
    print(datetime.fromtimestamp(h['message']['date']))
    await update.message.reply_text(f'привет, {h["message"]["chat"]["first_name"]}, хорошего тебе дня!) \nТвой username: @{h["message"]["chat"]["username"]}')


async def en(update: Update, context: ContextTypes.DEFAULT_TYPE):
    h = json.loads(json.dumps(update.to_dict(), indent=2))
    await update.message.reply_text(f'hello, {h["message"]["chat"]["first_name"]}, have a good day!)')

async def es(update: Update, context: ContextTypes.DEFAULT_TYPE):
    h = json.loads(json.dumps(update.to_dict(), indent=2))
    await update.message.reply_text(f'hola, {h["message"]["chat"]["first_name"]}, que tengas un buen día!)')


async def not_supported(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Приветствие "{update.message.text}" не поддерживается.')
async def not_supported_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Приветствие "{update.message.text}" не поддерживается.')

async def timer(update: Update,context: ContextTypes.DEFAULT_TYPE):
    h = json.loads(json.dumps(update.to_dict(), indent=2))
    data=h["message"]["date"]
    print(data)

def get_greeting_filter(greeting: str):
    return filters.Regex(re.compile(f'^{greeting}$', re.IGNORECASE))
async def started_message(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Приветствую в чате!, напиши help для работы с роботом')

if __name__ == '__main__':
    application = ApplicationBuilder().token('6166029768:AAFOWtWdfMak0SUC5wtJIr9LGGZPwimePyg').build()
    application.add_handler(MessageHandler(get_greeting_filter('привет'), ru))
    application.add_handler(MessageHandler(get_greeting_filter('hello'), en))
    application.add_handler(MessageHandler(get_greeting_filter('hola'), es))
    application.add_handler(MessageHandler(get_greeting_filter('/help'),help_command))
    application.add_handler(MessageHandler(get_greeting_filter('/start'), started_message))
    application.add_handler(MessageHandler(get_greeting_filter('17:40'), timer))
    application.add_handler(MessageHandler(filters.TEXT, not_supported))
    print('STARTED')
    application.run_polling()