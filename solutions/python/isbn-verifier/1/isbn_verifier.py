def is_valid(isbn: str) -> bool:
 
    isbn = isbn.replace("-", "")

    if isbn == "":
        return False
    
    if len(isbn) != 10:
        return False
    
    numbers = []
    for i, ch in enumerate(isbn):
        if ch.isdigit():
            numbers.append(int(ch))
        elif ch == "X" and i == 9:
            numbers.append(10)
        else:
            return False
    
    total = sum((10 - i) * num for i, num in enumerate(numbers))
    
    return total % 11 == 0