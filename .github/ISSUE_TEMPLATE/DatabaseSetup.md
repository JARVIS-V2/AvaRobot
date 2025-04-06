# 📦 Setting Up a PostgreSQL Database for AvaRobot

If you're **not using Heroku or Railway**, you'll need to manually create a PostgreSQL database and provide the `DATABASE_URL` in your `.env` file.

This guide helps you get that setup on VPS or free hosting platforms.

---

## ✅ If You're Using a VPS

Install PostgreSQL and create a new database:

```bash
# Install PostgreSQL
sudo apt update
sudo apt install postgresql postgresql-contrib

# Create a new database user
sudo -u postgres createuser ava_user --pwprompt

# Create a new database owned by that user
sudo -u postgres createdb -O ava_user ava_db
```

Then use this format in your `.env`:

```
DATABASE_URL=postgresql://ava_user:your_password@localhost:5432/ava_db
```

---

## 🌐 Free Cloud PostgreSQL Options

You can also use a cloud database provider to get your `DATABASE_URL` for free.

### 1. Supabase
- 🔗 [https://supabase.com](https://supabase.com)
- Free tier with ~500MB PostgreSQL storage.
- After creating a project, go to **Project Settings → Database** to copy your connection string.

### 2. Railway
- 🔗 [https://railway.app](https://railway.app)
- Create a new project → Add Plugin → PostgreSQL
- Copy the auto-generated `DATABASE_URL` from the "Connect" tab.

### 3. ElephantSQL
- 🔗 [https://www.elephantsql.com](https://www.elephantsql.com)
- Free tier for testing (20MB).
- One-click setup and a connection URL is provided instantly.

---

## 🧪 Example `.env` Variable

```env
DATABASE_URL=postgresql://username:password@host:port/database
```

Paste this into your `.env` file and you're ready to go!

---

## 🛠️ Need Help?

If you're stuck, open an issue or reach out in our support group: [t.me/CertifiedCoders](https://t.me/CertifiedCoders)

---

