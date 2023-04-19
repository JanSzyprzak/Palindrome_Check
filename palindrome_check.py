



def is_palindrome(text):
    
    alnum_signs = [x for x in text.lower() if x.isalnum()]
    if alnum_signs == alnum_signs[::-1]:
        return f"'{word}' jest palindromem"
    else:
        return f"'{word}' nie jest palindromem"


test_cases = ['sos', 'soso', 'Sos', 'Soso', '', '111', 's,o,s!!!!!!', "Ile roman ładny dyndał na moreli."]

for word in test_cases:
    print(is_palindrome(word))