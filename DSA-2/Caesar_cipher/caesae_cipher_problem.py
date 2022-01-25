def Caesar_cipher(data):
    store=''
    for char in data:
        if not char.isnumeric():
            # code=ord(char)
            if char=="": 
               store+=" "
            
            elif char < 'x' or char < 'X':
                char=ord(char)+3
                # code = ord('Z')
                store+=chr(char)
               
            elif char >= 'x' or char >= 'X':
                nw_code=ord(char)
                store+=chr(nw_code-23)
                
        else:
            store+=char
    return store
print(Caesar_cipher("Sgd chd hr bzrs"))
