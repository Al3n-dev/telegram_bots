import telebot

"""Сюда пишем токен созданный в BotFather"""
token = 'сюда токен вставляем'
"""Создаем экземпляр бота"""
bot = telebot.TeleBot(token)
"""Получаем id чата по его имени"""
GROUP_ID = bot.get_chat('Сюда пишем айди').id
"""Список слов которые нужно удалять"""
blacklist = ['Ауе', 'Хуй', 'Пизда', 'суки', 'etc']

"""Перехват чужих сообщений в чате"""


@bot.message_handler(content_types=["text"])
def handle_text(message):
    """По очереди ищем слова из списка в сообщении """
    for x in blacklist:
        if (x in message.text):
            """Если найдены слова удаляем сообщение с ними"""
            bot.delete_message(message.chat.id, message.messege_id)
        else:
            return


if __name__ == "__main__":
    bot.infinity_polling()
