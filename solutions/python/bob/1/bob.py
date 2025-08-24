def response(hey_bob):
    if hey_bob == "" or hey_bob.isspace():
        return "Fine. Be that way!"
    elif hey_bob.strip().endswith("?") and not hey_bob.isupper():
        return "Sure."
    elif hey_bob.isupper() and hey_bob.strip().endswith("!"):
        return "Whoa, chill out!"
    elif hey_bob.isupper() and hey_bob.strip().endswith("?"):
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif "!" in hey_bob and hey_bob.title():
        return "Whatever."
    elif hey_bob.title():
        return "Whatever."