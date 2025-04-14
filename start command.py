from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Xush kelibsiz!")

def main():
    token = "7992036519:AAFnPWosBo36LloYytseuOLFWW7E22eHcBs"  # o‘zingizning bot tokeningizni yozing
    updater = Updater(token, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
