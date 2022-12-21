import time as t
import random as r
import turtle as tr

pcardnum = 0
dcardnum = 0

def game():
    global pcardnum
    print("\n\n\n\n\n\n\nThe dealer is shuffling")
    dealdraw()
    firstdraw()
    firstdraw()
    print('your hand is')
    print (pcardnum)
    userdraw()

def dealdraw():
    global dcardnum
    dcardnum = dcardnum + r.randint(2,11)
    dcardnum = dcardnum + r.randint(2,10)
    print('the dealers hand is:')
    print(dcardnum)
    if dcardnum == 21:
        print('you lose')
        exit()

def firstdraw():
    global pcardnum
    pcardnum = pcardnum + r.randint(2,11)

def userdraw():
    global pcardnum
    if pcardnum > 21:
        print('you lose')
        exit()
    if pcardnum == 21:
        print('you win')
        exit()
    draw = input("Draw card?\ny or n\n")
    if draw == "y":
        firstdraw()
        print('\nyour new hand is')
        print (pcardnum)
        userdraw()
    if draw == "n":
        finhand()
    else:
      print('please type y or n\n')
      userdraw()

def findeal():
    global dcardnum
    if dcardnum <= pcardnum:
        dcardnum = dcardnum + r.randint(2,10)
        findeal()
    if dcardnum > 21:
        print('\nthe dealer is drawing')
        t.sleep(2)
        print('\nthe dealers hand is:')
        print(dcardnum)
        print('\nyou win!')
        exit()
    else:
        return

def finhand():
    global pcardnum
    global dcardnum
    findeal()
    print('\nthe dealer is drawing')
    t.sleep(2)
    print('\nthe dealers hand is:')
    print(dcardnum)
    print('\n')
    if pcardnum > 21:
        print('you lose\n')
        exit()
    if pcardnum > dcardnum:
        print('you win\n')
        exit()
    if pcardnum < dcardnum:
        print('you lose\n')
        exit()
    if pcardnum == dcardnum:
        print('its a draw')
        exit()

game()
