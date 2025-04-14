import random
from telegram import Update
from telegram.ext import Updater, CommandHandler

# Fayllarni o'qish funksiyasi
def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

# random tanlash funksiyasi
def random_choice():
    # Fayllardan so'zlarni o'qib olish
    file1_words = read_file('file1.txt')
    file2_words = read_file('file2.txt')
    file3_words = read_file('file3.txt')

    # Random tanlash
    word1 = random.choice(file1_words)
    word2 = random.choice(file2_words)
    word3 = random.choice(file3_words)

    return f"{word1} bilan {word2} {word3}"

# /play komandasini bajaruvchi funksiya
def play(update: Update, context):
    result = random_choice()  # Random tanlangan xabar
    update.message.reply_text(result)  # Bot orqali xabar yuborish

def main():
    # Botni o'rnatish
    updater = Updater("7992036519:AAFnPWosBo36LloYytseuOLFWW7E22eHcBs", use_context=True)
    dp = updater.dispatcher

    # /play komandasini qo'shish
    dp.add_handler(CommandHandler("play", play))

    # Botni ishga tushirish
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
