import json
import logging
from http import HTTPStatus

from app.bot import TelegramBot
from app.config import Config
from app.readeck import ReadeckClient, ReadeckError
from app.validation import is_valid_url

logger = logging.getLogger()
logger.setLevel(logging.INFO)

config = Config()
bot = TelegramBot(config.telegram_bot_token, config.allowed_user_ids)
readeck = ReadeckClient(config.readeck_api_url, config.readeck_api_token)


def lambda_handler(event, context):
    try:
        body = event.get("body", "{}")
        if isinstance(body, str):
            body = json.loads(body)

        message = bot.extract_message(body)
        if not message:
            return {"statusCode": HTTPStatus.OK}

        chat_id = message["chat_id"]
        user_id = message["user_id"]
        text = message["text"].strip()

        if not bot.is_authorized(user_id):
            return {"statusCode": HTTPStatus.OK}

        if not is_valid_url(text):
            return {"statusCode": HTTPStatus.OK}

        try:
            readeck.create_bookmark(text)
            bot.reply(chat_id, "Saved!")
        except ReadeckError as e:
            logger.error("Readeck error: %s", e)
            bot.reply(chat_id, "Failed to save bookmark. Please try again later.")

    except Exception:
        logger.exception("Unexpected error processing update")

    return {"statusCode": HTTPStatus.OK}
