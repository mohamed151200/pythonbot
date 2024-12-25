from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes


# وظيفة الرد على أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # إنشاء زر
    keyboard = [
        [InlineKeyboardButton("عرض الكتب 📚", callback_data="books")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # إرسال الرسالة مع الزر
    await update.message.reply_text(
        "مرحبًا بك! اختر ما تريد:",
        reply_markup=reply_markup
    )


# وظيفة التعامل مع الضغط على الزر
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()  # تأكيد أن الطلب تم معالجته

    # التعامل مع الزر الذي تم الضغط عليه
    if query.data == "books":
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


# تشغيل البوت
def main():
    application = Application.builder().token("7564252375:AAFnPLQ4L89f46SyBlaYBuxA4961QVjeVX8").build()

    # أوامر
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # بدء التشغيل
    application.run_polling()


if __name__ == "__main__":
    main()
