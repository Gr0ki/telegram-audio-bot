import telebot
from secret import TOKEN


bot = telebot.TeleBot(TOKEN, parse_mode=None)


audio_commands = '''
        /amongus
        /virus
        /FBI
        /scream
        /boiii
        /wow
        /bullshit
        /money'''


@bot.message_handler(commands=['start'])
def handle_start_help(message):
    bot.send_message(message.chat.id, 'Привет, я создан для аудио мемов ^_^')
    bot.send_message(message.chat.id, 
        'Вот список того что вы можете использовать: ' + audio_commands)


@bot.message_handler(commands=['help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, 'Список команд: ' + audio_commands)


@bot.message_handler(commands=['amongus'])
def among_us_command_handler(message):
    audio = open('./audio/amogus.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['virus'])
def among_us_command_handler(message):
    audio = open('./audio/virus.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['FBI'])
def among_us_command_handler(message):
    audio = open('./audio/fbi.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['scream'])
def among_us_command_handler(message):
    audio = open('./audio/help.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['boiii'])
def among_us_command_handler(message):
    audio = open('./audio/hehe-boiii.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['wow'])
def among_us_command_handler(message):
    audio = open('./audio/wow.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['bullshit'])
def among_us_command_handler(message):
    audio = open('./audio/всё-хуйня.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['money'])
def among_us_command_handler(message):
    audio = open('./audio/денег-не-даст.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


bot.infinity_polling()
