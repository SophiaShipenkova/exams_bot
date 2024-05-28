from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
import datetime


TOKEN = "6339137859:AAFZrdrS-GCOEPSWpvhB4TsvP930AidsKfQ"

# Создаем словарь с соответствующими значениями для каждой кнопки
button_texts = {
    'subbutton1.1': 'Экзамен состоится 21 июня 13:00 - 14:30',
    'subbutton1.2': 'Экзамен состоится 15 июня 12:20 - 13:20',
    'subbutton1.3': 'Экзамен состоится 25 июня 11:00 - 12:30',
    'subbutton1.4': 'Экзамен состоится 3 июля 11:00 - 17:00',
    'subbutton1.5': 'Экзамен состоится:\n1.1 13 июня 11:20 - 14:35; \n1.2 5 июня 13:30 - 16:45',
    'subbutton1.6': 'Экзамен состоится 29 июня 10:00 - 16:00',
    'subbutton1.7': 'Экзамен состоится 4 июня 11:20 - 14:35',
    'subbutton1.8': 'Экзамен состоится 28 мая 11:00 - 12:00',
    'subbutton1.9': 'Экзамен состоится:\n 25 мая 8:00 - 11:15 ; \n 1 июня 8:00 - 11:15',
    'subbutton2.1': 'Экзамен состоится 21 июня 13:00 - 14:00',
    'subbutton2.2': 'Экзамен состоится 15 июня 11:20 - 12:20',
    'subbutton2.3': 'Экзамен состоится 25 июня 11:00 - 12:30',
    'subbutton2.4': 'Экзамен состоится 29 июня 11:00 - 17:00',
    'subbutton2.5': 'Экзамен состоится:\n2.1 20 июня 11:20 - 14:35; \n2.2 5 июня 8:00 - 11:15',
    'subbutton2.6': 'Экзамен состоится 3 июля 10:00 - 16:00',
    'subbutton2.7': 'Экзамен состоится 11 июня 11:20 - 14:35',
    'subbutton2.8': 'Экзамен состоится 28 мая 9:40 - 11:20',
    'subbutton2.9': 'Экзамен состоится:\n 8 июня 8:00 - 11:15; \n 15 июня 8:00 - 11:15',
}

# Обработчик команды /start
async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("ИТвД 1", callback_data='button1')],
        [InlineKeyboardButton("ИТвД 2", callback_data='button2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Выберите группу:', reply_markup=reply_markup)

# Обработчик нажатия на кнопку
async def button_click(update, context):
    query = update.callback_query
    if query.data == 'button1':
        keyboard = [
            [InlineKeyboardButton("Иностанный язык", callback_data='subbutton1.1')],
            [InlineKeyboardButton("Архитектура информационных систем", callback_data='subbutton1.2')],
            [InlineKeyboardButton("Моделирование систем", callback_data='subbutton1.3')],
            [InlineKeyboardButton("Технологии программирования", callback_data='subbutton1.4')],
            [InlineKeyboardButton("Инструментальные средства информационных систем", callback_data='subbutton1.5')],
            
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text('Выберите дисциплину:', reply_markup=reply_markup)
    elif query.data == 'button2':
        keyboard = [
            [InlineKeyboardButton("Иностанный язык", callback_data='subbutton2.1')],
            [InlineKeyboardButton("Архитектура информационных систем", callback_data='subbutton2.2')],
            [InlineKeyboardButton("Моделирование систем", callback_data='subbutton2.3')],
            [InlineKeyboardButton("Технологии программирования", callback_data='subbutton2.4')],
            [InlineKeyboardButton("Инструментальные средства информационных систем", callback_data='subbutton2.5')],
           
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text('Выберите дисциплину:', reply_markup=reply_markup)
    elif query.data.startswith("subbutton"):
        content = button_texts[query.data]
        await query.message.reply_text(content)
        

async def subbutton_click(update, context):
    query = update.callback_query
    text = button_texts.get(query.data, 'Нет текста для этой кнопки')
    await query.message.reply_text(text)

# Функция для отправки уведомления в выбранный день
async def send_notification(context):
    context.bot.send_message(chat_id=context.job.context['chat_id'], text="Напоминание: сегодня важное событие!")

# Основная функция
def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_click))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
