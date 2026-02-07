import telepot


class TelegramBot:
    def __init__(self, token: str, allowed_user_ids: set[int]):
        self.bot = telepot.Bot(token)
        self.allowed_user_ids = allowed_user_ids

    def extract_message(self, update: dict) -> dict | None:
        message = update.get("message")
        if not message:
            return None
        text = message.get("text")
        if not text:
            return None
        chat_id = message["chat"]["id"]
        user_id = message["from"]["id"]
        return {"chat_id": chat_id, "user_id": user_id, "text": text}

    def is_authorized(self, user_id: int) -> bool:
        return user_id in self.allowed_user_ids

    def reply(self, chat_id: int, text: str) -> None:
        self.bot.sendMessage(chat_id, text)
