import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import requests

BOT_TOKEN = "8028110075:AAEF5EctyqFimN4v3YwO8lG7cNHv6LFsg1Y"
RENDER_API = "https://sarkar-md-free.onrender.com/"
ADMIN_ID = 7216826752

logging.basicConfig(level=logging.INFO)
user_states = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalamualaikum! Apna forked GitHub repo ka link dein:")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text.strip()

    if user_id not in user_states:
        if "github.com" in text:
            if text.startswith("https://github.com/") and len(text.split("/")) >= 5:
                user_states[user_id] = {"repo": text}
                await update.message.reply_text("✅ Repository link sahi hai\nAb apna session ID dein:")
            else:
                await update.message.reply_text("❌ Invalid GitHub repo link.")
        else:
            await update.message.reply_text("⚠️ Pehle apna forked GitHub repo ka link dein.")
    elif "session" not in user_states[user_id]:
        user_states[user_id]["session"] = text
        repo = user_states[user_id]["repo"]
        session = user_states[user_id]["session"]
        await update.message.reply_text("🔄 Deploy ho raha hai, please wait...")

        try:
            res = requests.post(RENDER_API + "deploy", json={"repo": repo, "session": session})
            if res.status_code == 200:
                await update.message.reply_text("✅ Bot successfully deployed!")
                await context.bot.send_message(chat_id=ADMIN_ID, text=f"📢 New Deployment:\n👤 User: {user_id}\n🔗 Repo: {repo}")
            else:
                await update.message.reply_text("❌ Deployment failed. Check repo/session.")
        except Exception as e:
            await update.message.reply_text("🚫 Error during deployment.")
        del user_states[user_id]

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
