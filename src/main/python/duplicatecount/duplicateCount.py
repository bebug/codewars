def duplicate_count(text: str):
    return len([c for c in set(text.lower()) if text.lower().count(c) > 1])
