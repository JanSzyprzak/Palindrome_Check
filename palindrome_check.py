


pal = "Ile roman ładny dyndał na moreli."

def is_palindrome(text):
    
    alnum_signs = [x for x in text.lower() if x.isalnum()]
    if alnum_signs == alnum_signs[::-1]:
        return "To jest palindrom."
    else:
        return "To nie jest palindrom"

print(is_palindrome(pal))