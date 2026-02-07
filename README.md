# Readeck Telegram Bot

A Telegram bot that saves URLs as bookmarks to a self-hosted [Readeck](https://readeck.org) instance. Runs on AWS Lambda via webhook.

## How it works

Send a URL to the bot on Telegram. If the message is a valid HTTP(S) URL from an authorized user, the bot saves it as a bookmark in Readeck and replies "Saved!". Non-URL messages, unauthorized users, and non-text updates are silently ignored.

## Setup

### Prerequisites

- [uv](https://docs.astral.sh/uv/) for dependency management
- AWS account with Lambda access
- A Telegram bot token (from [@BotFather](https://t.me/BotFather))
- A running Readeck instance with an API token

### Environment Variables

| Variable | Purpose |
|---|---|
| `TELEGRAM_BOT_TOKEN` | Telegram Bot API token |
| `READECK_API_URL` | Readeck instance base URL (e.g. `https://readeck.example.com`) |
| `READECK_API_TOKEN` | Readeck API bearer token |
| `ALLOWED_USER_IDS` | Comma-separated Telegram user IDs allowed to use the bot |

Copy `.env.example` and fill in the values:

```bash
cp .env.example .env
```

### Deploy to AWS Lambda

1. Build the deployment package:

```bash
bash scripts/package.sh
```

2. Upload `package.zip` to AWS Lambda:
   - Runtime: Python 3.12
   - Architecture: x86_64
   - Handler: `app.handler.lambda_handler`

3. Set the four environment variables in the Lambda configuration.

4. Create a Function URL for the Lambda function.

5. Register the Telegram webhook:

```bash
bash scripts/set_webhook.sh <TELEGRAM_BOT_TOKEN> <LAMBDA_FUNCTION_URL>
```

## Project Structure

```
readeck-telegram-bot/
├── pyproject.toml           # uv project config + dependencies
├── .env.example             # Template for required env vars
├── app/
│   ├── __init__.py
│   ├── handler.py           # Lambda entry point
│   ├── bot.py               # Telegram message parsing + replies
│   ├── readeck.py           # Readeck API client
│   ├── validation.py        # URL validation
│   └── config.py            # Env var loading + validation
└── scripts/
    ├── package.sh           # Build Lambda deployment zip
    └── set_webhook.sh       # Register Telegram webhook
```
