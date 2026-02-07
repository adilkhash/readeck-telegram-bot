import os


class Config:
    def __init__(self):
        self.telegram_bot_token = self._require("TELEGRAM_BOT_TOKEN")
        self.readeck_api_url = self._require("READECK_API_URL").rstrip("/")
        self.readeck_api_token = self._require("READECK_API_TOKEN")
        self.allowed_user_ids = self._parse_user_ids(self._require("ALLOWED_USER_IDS"))

    def _require(self, name: str) -> str:
        value = os.environ.get(name)
        if not value:
            raise RuntimeError(f"Missing required environment variable: {name}")
        return value

    def _parse_user_ids(self, raw: str) -> set[int]:
        return {int(uid.strip()) for uid in raw.split(",") if uid.strip()}
