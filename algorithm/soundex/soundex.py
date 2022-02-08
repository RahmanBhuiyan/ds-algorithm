def soundex(name, len=4):
    # digits holds the soundex values for the alphabet
    digits = '01230120022455012623010202'
    sndx = ''
    fc = ''
    # translate alpha chars in name to soundex digits
    for c in name.upper():
        if c.isalpha():
            if not fc:#store first letter
                fc = c
            d = digits[ord(c)-ord('A')]#convert letter in asii number 
            if not sndx or (d != sndx[-1]):# duplicate  soundex digits are skipped
                sndx += d
    sndx = fc + sndx[1:]#store first letter and digit 
    sndx = sndx.replace('0','')# remove all 0s from the soundex code
    return (sndx + "0")[:len]#if the soundex code geter len less than 4 then add 0 at last

print(soundex("Raihan", len=4))

    