def escape_characters(original: str) -> str:
    return original.replace("&", "\&").replace("%", "\%")
