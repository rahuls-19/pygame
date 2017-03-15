import os
import random
import time
for i in range(1,4):
    a = random.choice(("hi","hey","sup"))
    print(a)
    os.system("say '"+a+" ' ")
    resp1 = input("")
    if resp1 in ("hi","hey","sup","hello"):
        GE = random.choice(("ok what would you like to do","k whats up what are we going to do","what are we gonna do sir"))
        print (GE)
        os.system("say ' " + GE + " ' ")
        break
    while 1 :
        lis = ("joke","email","note")
        resp2 = input("")
        esa = ""
        for word in lis :
            if word in resp2 :
                esa = word
            if esa == "email":
                e = random.choice(("ok what would you like to do","k whats up what are we going to do","what are we gonna do sir"))
                print (e)
                os.system("say ' " + e + " ' ")
                break
            if esa in ("grounded" , "detention" , "in trouble"):
                ef = random.choice(("ok what would you like to do","k whats up what are we going to do","what are we gonna do sir"))
                print (ef)
                os.system("say ' " + ef + " ' ")
                break
