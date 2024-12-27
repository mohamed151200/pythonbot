from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, Dispatcher
import os

# Flask application
app = Flask(__name__)

# Telegram bot token
TOKEN = "7564252375:AAFnPLQ4L89f46SyBlaYBuxA4961QVjeVX8"
WEBHOOK_URL = "https://your-domain.com/webhook"  # Replace with your domain

# Create the application
application = Application.builder().token(TOKEN).build()

# Function to handle /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Create a button
    keyboard = [
        [InlineKeyboardButton("عرض الكتب 📚", callback_data="books")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the message with the button
    await update.message.reply_text(
        "مرحبًا بك! اختر ما تريد:",
        reply_markup=reply_markup
    )

# Function to handle button clicks
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()  # Confirm that the request has been processed

    # Handle the button pressed
    if query.data == "books":
        books_list = """
        📚 *قائمة الكتب :*

        1. [الأذكار للنووي](https://drive.google.com/file/d/1jUdMJohjMhKmtaMdIr0PMrt43qI6OuTi/view?usp=drive_link)
        2. [الفصول في سيرة الرسول صلي الله عليه وسلم](https://drive.google.com/file/d/1-RRDDEGDOpg_wUTIzdfjwp6KgaeorkIv/view?usp=drive_link)
        3. [المنتقى من أخبار المصطفى صلي الله عليه وسلم](https://drive.google.com/file/d/12B4WWqlUDt25PX6tQYHbipRecXxFXWVs/view?usp=drive_link)
        4. [الأدب المفرد للإمام البخاري](https://drive.google.com/file/d/1HW2v5rdMUtxCMkB3dhvRhH_bxCN5VfSw/view?usp=drive_link)
        5. [رياض الصالحين](https://drive.google.com/file/d/16oboNwQflVGTtZN7REzrezhB2VPAdy3c/view?usp=drive_link)
        6. [الفقه الميسر في ضوء الكتاب والسنة](https://drive.google.com/file/d/1ZzVEQ1_ply5qwzUWelstt2ln1zakVpDf/view?usp=drive_link)
        7. [صحيح البخاري](https://drive.google.com/file/d/1H1vnvcu4ysi2X57sSXn1WYgtcqZPKj6a/view?usp=drive_link)
        """
        await query.message.reply_text(
            text=books_list,
            parse_mode="Markdown"
        )

# Add handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(CallbackQueryHandler(button_handler))

# Flask route for the webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    update = Update.de_json(data, application.bot)
    application.update_queue.put_nowait(update)
    return "OK", 200

# Set webhook when the script starts
@app.before_first_request
def set_webhook():
    application.bot.set_webhook(url=WEBHOOK_URL)

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
