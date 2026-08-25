import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ========== 1. 配置区：定义按钮和回复内容 ==========
REPLY_CONTENT = {
    "💳 vcc services": "💳 VCC Services\n\nUL PAY solutions are designed for simple, secure, flexible, and seamless online payments.\n\n• Visa & Mastercard\n• Multi-Currency Top-Ups\n• Instant Card Issuance\n• 24/7 Smart CRM\n• Free API Access",
    "🎫 sign up": "Ready to dive in?\n\nHit us up for your invite code and the best rates. We'll get you started in no time!\n\nExplore the platform: https://dev.ul-card.com/\n\n💬 Contact us: @Jayee_uL @Lenkahu999 @Zoe_0831\n@TONNNY321 @Christine_1030 @Elvis_uldigital",
    "📗 supported payment scenarios": "📗 Supported Payment Scenarios\n\n• Advertising payments (Facebook, Tiktok, Google, etc.)\n• AI Subscriptions (ChatGPT, Claude, Cursor, etc.)\n• Online Shopping\n• Travel Bookings\n\nMore features coming soon — Stay tuned!",
    "🌐 website": "UL PAY Official Website: https://ul-pay.com/",
    "🗳 contact": "🗳 Contact Us\n\nLenka\nTelegram: @Lenkahu999\nEmail: lenkahu723@gmail.com\n\nZoe\nTelegram: @Zoe_0831\nEmail: kh_01@uldigital.net\n\nJayee\nTelegram: @Jayee_uL\nEmail: kh_09@uldigital.net\n\nTony\nTelegram: @TONNNY321\nEmail: kh_14@uldigital.net\n\nChristine\nTelegram: @Christine_1030\nEmail: kh_20@uldigital.net\n\nElvis\nTelegram: @Elvis_uldigital\nEmail: kh_33@uldigital.net",
    "💶 pricing": "💶 Pricing\n\n• No monthly fees\n• Ultra-low issuance fees & commissions\n\nCustom solutions? Let's chat!",
    "🧚🏻 about": "🧚🏻 About UL PAY\n\nPowered by UL Digital, UL PAY is committed to delivering secure, convenient, and reliable virtual payment solutions to users worldwide."
}

# ========== 2. 处理 /start 命令 ==========
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 创建按钮布局（一行两个，共四行）
    keyboard = [
        ["💳 vcc services", "🎫 sign up"],
        ["📗 supported payment scenarios"],
        ["🌐 website", "🗳 contact"],
        ["💶 pricing", "🧚🏻 about"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        "Hello! 👋🏻\n\nWelcome to UL PAY Support Bot! How can I help you today?\n\n"
        "Click the button below to learn more!",
        reply_markup=reply_markup
    )

# ========== 3. 处理用户点击按钮/发送消息 ==========
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    

    if text in REPLY_CONTENT:
        await update.message.reply_text(REPLY_CONTENT[text])
    else:
        await update.message.reply_text(
            "Please select a service using the menu buttons below, or send /start to reopen the main menu."
        )

# ========== 4. 主程序 ==========
def main():
    TOKEN = os.environ.get("TELEGRAM_TOKEN")
    
    if not TOKEN:
        print("错误：请在环境变量中设置 TELEGRAM_TOKEN")
        return
    
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
