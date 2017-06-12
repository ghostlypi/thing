def encrypt(user_input):
    myname = user_input
    bigstring = ""
    for x in range (len(myname)):
        bigstring = bigstring + str(ord(myname[x])+3).zfill(3)

    x = 0
    encrypted = ""
    while x < len(bigstring):
        charnumber = bigstring[x:x+3]
        x = x + 3
        charnumber = int(charnumber)
        encrypted = encrypted + chr(charnumber)


    return encrypted
