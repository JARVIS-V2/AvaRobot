<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

<h1 align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=F778A1&width=350&lines=🧳+AVA+THE+ROBOT🖤+🦍">
</h1>

<p align="center">
  <a href="https://t.me/Ava_The_Robot">
    <img src="https://telegra.ph/file/6a58ec930e5c45d78464d.jpg" width="600">
  </a>
</p>

# 🤖 AvaRobot

AvaRobot is a fast, modular, and fully-featured Telegram group management bot written in Python. It uses `python-telegram-bot`, `Telethon`, and `Pyrogram` for maximum flexibility and power.

---

## ✨ Features

- Group administration (bans, mutes, warns, filters)
- Custom welcomes & rules
- Global bans & SpamWatch integration
- Fun modules (quotes, jokes, ARQ API, deepAI)
- Telegraph integration
- Dual Telegram client support
- Optional PostgreSQL + MongoDB backend

---

## 📦 Requirements

- Python 3.8+
- MongoDB connection URI (MongoDB Atlas or VPS)
- PostgreSQL URI (if using SQL features)
- A Telegram bot token from [@BotFather](https://t.me/BotFather)

---

## 🛠️ VPS Deployment (Ubuntu 20.04+ or 22.04)

### 📁 Step-by-step guide

```bash
# 1. Install system dependencies
sudo apt update && sudo apt install git curl python3 python3-pip ffmpeg tmux -y

# 2. Clone the repository
git clone https://github.com/JARVIS-V2/AvaRobot
cd AvaRobot

# 3. Install Python requirements
pip3 install -U pip
pip3 install -U -r requirements.txt

# 4. Run the setup script
chmod +x setup
./setup
# Fill all required values when prompted (skip optional ones)

# 5. Start tmux session (optional for persistent run)
tmux new -s avarobot

# 6. Launch the bot
chmod +x start
./start
```

To detach from tmux:
```bash
Ctrl + B then press D
```

To stop:
```bash
tmux kill-session -t avarobot
```

---

## ☕ Deploy to Heroku

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/JARVIS-V2/AvaRobot)

> Make sure to fill all required environment variables during deployment.

## 🚀 Deploy to Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/JARVIS-V2/AvaRobot)

> After deploy, open the Railway Dashboard → Environment tab → Add your secrets (.env values)

---

## 📂 Environment Variables Reference

| Variable         | Required | Description                                  |
|------------------|----------|----------------------------------------------|
| `API_ID`         | ✅       | From [my.telegram.org](https://my.telegram.org) |
| `API_HASH`       | ✅       | Same as above                                |
| `TOKEN`          | ✅       | From [@BotFather](https://t.me/BotFather)     |
| `OWNER_ID`       | ✅       | Your user ID (use @userinfobot to get it)     |
| `LOGGER_ID`      | ✅       | Telegram log group/channel ID                |
| `MONGO_DB_URI`   | ✅       | MongoDB connection string                    |
| `DATABASE_URL`   | ✅       | PostgreSQL connection string (if using SQL)  |
| `ARQ_API_KEY`    | ✅       | From [ARQ](https://t.me/ARQRobot) |
| `SPAMWATCH_API`  | ✅       | From [Spam Watchers](https://t.me/SpamWatchBot)   |
| `OWNER_USERNAME` | 🔹       | Your @username (used in UI, optional)        |
| `SUPPORT_CHAT`   | 🔹       | Support chat link (used in /help)            |
| `DEEP_API`       | 🔹       | From [deepai.org](https://deepai.org)        |
| `DB_NAME`        | 🔹       | MongoDB DB name (default: AvaRobot)          |

---

## 🤝 Credits

- [Python Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [Telethon](https://github.com/LonamiWebs/Telethon)
- [Pyrogram](https://github.com/pyrogram/pyrogram)
- [ARQ API](https://github.com/thehamkercat/ARQ)
- [SpamWatch](https://spamwatch.org/)

---

## 💎 License

Licensed under the [GNU General Public License v3.0](LICENSE)
