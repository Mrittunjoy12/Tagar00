import json
import random
import smtplib
from email.mime.text import MIMEText
from telegram.ext import Updater, CommandHandler
import os

BOT_TOKEN = os.getenv("769'9490123:AAE7jD59d0jYgfbLa0ixP3EfXEXtjPuhbGQ")
GMAIL_ADDRESS = os.getenv("Freelancingzone.office@gmail.com")
GMAIL_APP_PASSWORD = os.getenv("apes mcdm wxhl xvbe")
ADMIN_PANEL_URL = "https://tagar.onrender.com"  # আপনার লাইভ এডমিন প্যানেল লিংক

DATABASE_FILE = "database.json"

# ইউজার ডেটাবেজ লোড
def load_users():
    try:
        with open(DATABASE_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

# ইউজার ডেটাবেজ সেভ
def save_users(users):
    with open(DATABASE_FILE, "w") as f:
        json.dump(users, f)

# ভেরিফিকেশন কোড পাঠানো
def send_verification_code(email, code):
    msg = MIMEText(f"Your verification code is: {code}")
    msg["Subject"] = "Verification Code"
    msg["From"] = GMAIL_ADDRESS
    msg["To"] = email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        server.send_message(msg)

# /start command
def start(update, context):
    update.message.reply_text("👋 Welcome! Use /register <your email> to register.")

# /register command
def register(update, context):
    users = load_users()
    user_id = str(update.message.from_user.id)

    if len(context.args) != 1:
        update.message.reply_text("Usage: /register your_email@example.com")
        return

    email = context.args[0]
    code = str(random.randint(100000, 999999))
    users[user_id] = {"email": email, "verified": False, "code": code}
    save_users(users)

    try:
        send_verification_code(email, code)
        update.message.reply_text(f"📧 Verification code sent to {email}. Use /verify <code>")
    except:
        update.message.reply_text("❌ Failed to send email. Please check email or try again later.")

# /verify command
def verify(update, context):
    users = load_users()
    user_id = str(update.message.from_user.id)

    if user_id not in users:
        update.message.reply_text("❌ Please register first using /register")
        return

    if len(context.args) != 1:
        update.message.reply_text("Usage: /verify 123456")
        return

    code = context.args[0]
    if users[user_id]["code"] == code:
        users[user_id]["verified"] = True
        save_users(users)
        update.message.reply_text("✅ You are successfully verified!")
    else:
        update.message.reply_text("❌ Invalid verification code.")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("register", register))
    dp.add_handler(CommandHandler("verify", verify))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()import json
import random
import smtplib
from email.mime.text import MIMEText
from telegram.ext import Updater, CommandHandler
import os

BOT_TOKEN = os.getenv("769'9490123:AAE7jD59d0jYgfbLa0ixP3EfXEXtjPuhbGQ")
GMAIL_ADDRESS = os.getenv("Freelancingzone.office@gmail.com")
GMAIL_APP_PASSWORD = os.getenv("apes mcdm wxhl xvbe")
ADMIN_PANEL_URL = "https://tagar.onrender.com"  # আপনার লাইভ এডমিন প্যানেল লিংক

DATABASE_FILE = "database.json"

# ইউজার ডেটাবেজ লোড
def load_users():
    try:
        with open(DATABASE_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

# ইউজার ডেটাবেজ সেভ
def save_users(users):
    with open(DATABASE_FILE, "w") as f:
        json.dump(users, f)

# ভেরিফিকেশন কোড পাঠানো
def send_verification_code(email, code):
    msg = MIMEText(f"Your verification code is: {code}")
    msg["Subject"] = "Verification Code"
    msg["From"] = GMAIL_ADDRESS
    msg["To"] = email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        server.send_message(msg)

# /start command
def start(update, context):
    update.message.reply_text("👋 Welcome! Use /register <your email> to register.")

# /register command
def register(update, context):
    users = load_users()
    user_id = str(update.message.from_user.id)

    if len(context.args) != 1:
        update.message.reply_text("Usage: /register your_email@example.com")
        return

    email = context.args[0]
    code = str(random.randint(100000, 999999))
    users[user_id] = {"email": email, "verified": False, "code": code}
    save_users(users)

    try:
        send_verification_code(email, code)
        update.message.reply_text(f"📧 Verification code sent to {email}. Use /verify <code>")
    except:
        update.message.reply_text("❌ Failed to send email. Please check email or try again later.")

# /verify command
def verify(update, context):
    users = load_users()
    user_id = str(update.message.from_user.id)

    if user_id not in users:
        update.message.reply_text("❌ Please register first using /register")
        return

    if len(context.args) != 1:
        update.message.reply_text("Usage: /verify 123456")
        return

    code = context.args[0]
    if users[user_id]["code"] == code:
        users[user_id]["verified"] = True
        save_users(users)
        update.message.reply_text("✅ You are successfully verified!")
    else:
        update.message.reply_text("❌ Invalid verification code.")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("register", register))
    dp.add_handler(CommandHandler("verify", verify))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
