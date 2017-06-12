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


def decrypt(ui):

    x = 0
    uo = ""
    while x < len(ui):
        char = chr(ord(ui[x])-3)
        uo = uo + char
        x += 1
    return(uo)
