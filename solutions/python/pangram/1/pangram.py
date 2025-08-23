import string
import re

def is_pangram(sentence):
    cleaned = re.sub(r'[^a-zA-Z]', '', sentence).lower()
    return set(cleaned) >= set(string.ascii_lowercase)
