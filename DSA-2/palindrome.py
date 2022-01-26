def palindrome(data):
    data=data.lower()
    stor=""
    #remove space in string
    for char in data:
        if char !=" ":
            stor+=char
    #reverse string 
    palindrome=stor[::-1]
    if stor == palindrome:
        return ("It's a palindrome")
    else:
        return ("It's not a palindrome")
        
print(palindrome("Ten animals I slam in a net"))
