import json
from telegram import Update
from telegram.ext import ApplicationBuilder, TypeHandler, CallbackContext


async def echo(update: Update, context: CallbackContext) -> None:
    text = json.dumps(update.to_dict(), indent=2)
    print(text)
    await update.message.reply_text(text)


def main() -> None:
    app = ApplicationBuilder().token('2312321452151').build()

    app.add_handler(TypeHandler(Update, echo))

    print('Started')

    app.run_polling()


if __name__ == "__main__":
    main()