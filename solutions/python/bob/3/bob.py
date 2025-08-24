def response(hey_bob: str) -> str:
    hey_bob = hey_bob.strip()  # remove leading/trailing whitespace first

    if not hey_bob:  
        # Empty or only whitespace
        return "Fine. Be that way!"

    is_question = hey_bob.endswith("?")
    is_yelling = hey_bob.isupper()

    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    elif is_question:
        return "Sure."
    elif is_yelling:
        return "Whoa, chill out!"
    else:
        return "Whatever."
