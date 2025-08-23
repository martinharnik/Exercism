def is_isogram(string):

    string = string.replace("-","")
    string = string.replace(" ","")
    
    string_length = len(string.lower())
    string_set = len(set(string.lower()))
   
    if string_length == string_set:
        return True
    return False
