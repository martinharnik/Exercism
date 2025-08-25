def translate(text):
    vowels = ["a", "e", "i", "o", "u"]
    suffix = "ay"

    # check if it's a sentence
    if " " in text:
        words = text.split()
        return " ".join([translate(word) for word in words])

    # now text is a single word
    # special cases: starts with vowel, xr, yt
    if text.startswith(("xr", "yt")) or text[0] in vowels:
        return text + suffix

    # collect initial consonant cluster
    i = 0
    while i < len(text):
        ch = text[i]
        # stop at vowel or 'y' not at start
        if ch in vowels or (ch == 'y' and i != 0):
            break
        # include 'u' if it follows 'q'
        if ch == 'q' and i+1 < len(text) and text[i+1] == 'u':
            i += 1
        i += 1

    return text[i:] + text[:i] + suffix
