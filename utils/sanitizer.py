import re

def sanitize_input(user_input: str) -> str:
    # Whitelist: allow alphanumeric and basic punctuation
    return re.sub(r"[^\w @\.,_-]", "", user_input)