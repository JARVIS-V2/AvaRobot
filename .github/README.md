
<p align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
</p>

<h1 align="center">
  <img src="https://telegra.ph/file/fbd55ee956abef2a74e15.jpg" width="60px">
  Ava The Telegram Bot 🖤
</h1>

<p align="center">
  <a href="https://t.me/Ava_The_Robot">
    <img src="https://telegra.ph/file/6a58ec930e5c45d78464d.jpg" width="600">
  </a>
</p>

---

## ✨ Features

- Multi-language support
- Admin tools, AFK, anti-spam, AI tools, and more
- MongoDB and PostgreSQL support
- Docker, Okteto, and VPS deployment ready
- Fast performance with modular architecture

---

## 🚀 Deployment Options

### 🐳 Deploy with Docker

```bash
git clone https://github.com/doraemo890/AvaRobot
cd AvaRobot
cp sample.env .env
docker-compose up --build -d
```

---

### ☁️ Deploy to Okteto

1. Make sure you have [Okteto CLI](https://www.okteto.com/docs/getting-started/) installed.
2. Run:

```bash
okteto pipeline deploy --name AvaRobot
```

> Make sure your `okteto-pipeline.yml` and `.env` are set correctly.

---

### 💻 Deploy on VPS (Ubuntu/Debian)

```bash
# 1. Update & install dependencies
sudo apt update && sudo apt install -y git python3 python3-venv python3-pip

# 2. Clone the repo
git clone https://github.com/doraemo890/AvaRobot.git
cd AvaRobot

# 3. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 4. Install requirements
pip install -U pip
pip install -r requirements.txt

# 5. Set up environment
cp sample.env .env
nano .env  # Fill in your credentials

# 6. Run the bot
bash start
```

✅ Want to run it in background? Use `screen` or set up a `systemd` service.

---

## 📁 Project Structure

```
Ava/
├── modules/         # Feature modules
├── langs/           # Language files
├── utils/           # Helper utilities
├── events.py        # Event handling
├── __main__.py      # Entrypoint
```

---

## 🧪 Code Quality & Automation

- [`black`](https://github.com/psf/black), `isort`, `ruff`
- `.deepsource.toml` and GitHub Actions integrated
- `pyproject.toml` for consistent formatting

---

## 📜 License

This project is licensed under the MIT License.

---

## 🧑‍💻 Credits

Made with ❤️ by [@doraemo890](https://github.com/doraemo890) and contributors.

