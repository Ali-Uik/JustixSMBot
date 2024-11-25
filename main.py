from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Ваш токен от BotFather
TOKEN = "8079933122:AAGoj-YbKvrREKFSKgmZB3CA3O_1C0mIk7I"
YOUR_TELEGRAM_ID = 86199576  # Ваш Telegram ID


# Функция обработки входящих сообщений
def forward_message(update: Update, context: CallbackContext):
    # Получаем текст сообщения от пользователя
    message = update.message.text
    user = update.message.from_user

    # Формируем текст для пересылки
    forward_text = f"Сообщение от {user.first_name} {user.last_name or ''} (@{user.username or 'нет ника'}):\n{message}"

    # Пересылаем сообщение на ваш аккаунт
    context.bot.send_message(chat_id=YOUR_TELEGRAM_ID, text=forward_text)


# Настройка и запуск бота
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Обработчик текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_message))

    # Запуск бота
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
