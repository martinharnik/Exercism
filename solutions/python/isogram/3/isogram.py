def is_isogram(string):
    cleaned = string.replace("-", "").replace(" ", "").lower()
    return len(cleaned) == len(set(cleaned))