from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8755823773:AAFxZ2J3wRjHa4j0XNUMuK2lnM7HNqgVmVw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📲 WhatsApp-қа жазылу", url="https://wa.me/77784894483")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Сәлем! Мен ботпын.\n\nКурс туралы толық ақпарат алу үшін төмендегі батырманы басыңыз 👇",
        reply_markup=reply_markup
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
