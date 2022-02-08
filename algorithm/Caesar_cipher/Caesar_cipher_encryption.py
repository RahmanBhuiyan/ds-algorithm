def Caesar_cipher(text,key):
    cipher = ''
    #store data
    for char in text:
        if not char.isalpha():
        #check data is alphabetic or not
            pass
        char = char.upper()
        #convert data into capital latter
        code = ord(char) + key
        #convert latter into  number
        cipher += chr(code)
        #store data and convert it again latter
    return cipher
print(Caesar_cipher("abc",3))
