
# Telegram Bot for WhatsApp Bot Deployment

This Telegram bot allows users to deploy their own WhatsApp bot by submitting their forked GitHub repo and session ID.

## Features
- GitHub repo validation
- Session ID input
- Auto deployment via Render API
- Admin notification on each deployment

## How to Use
1. Start the bot with `/start`
2. Provide your **forked GitHub repository** link
3. Provide your **WhatsApp session ID**
4. Bot will handle the deployment and notify the admin

## Deployment

### Render
1. Upload this code to GitHub.
2. Create new service on [Render.com](https://render.com/)
3. Use this repo and deploy a **background worker** with:
   ```
   Procfile: worker: python3 main.py
   ```

### Railway / Termux / VPS
Make sure Python 3.10+ is installed, then:

```bash
pip install -r requirements.txt
python3 main.py
```

### Docker

```bash
docker build -t telegram-deploy-bot .
docker run -d telegram-deploy-bot
```

## Configuration
Edit `main.py` and set your:
- Telegram `BOT_TOKEN`
- `RENDER_API` endpoint
- `ADMIN_ID` for deployment notifications

---
Developed by [ArslanMDofficial](https://github.com/ArslanMDofficial)
