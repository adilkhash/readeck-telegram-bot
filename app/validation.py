from urllib.parse import urlparse


def is_valid_url(text: str) -> bool:
    try:
        result = urlparse(text.strip())
        return result.scheme in ("http", "https") and bool(result.netloc)
    except Exception:
        return False
