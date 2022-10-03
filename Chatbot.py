name = input("What is your name?")
print("Hello" + name + "my name is Gary")


feeling = input("Are you feeling sad or happy today?")
if (feeling == "sad"):
    print("That is sad I hope you are  no not sad")
elif (feeling == "happy"):
    print("That is extravagant i am also happy")
else:
    print("That is a great feeling")


def rank():
    play = input("Do you play rainbow six siege")
    if (play == "yes"):
        ranks = input ("What is your highest rank  (G3,S5,C3)")
        print("Wow you are really good")
    elif (play == "no"):
        print("That is bad")
    else:
        print("Nice!")

rank()


fortnite = input("Do you play fortnite?")
if (fortnite == "yes"):
    print("wow thats amazing")
else:
    print("You are not cultured")



def freetime():
    freetime1=input("what do you do in your freetime?")
    if (freetime1 == "minecraft"):
        print("go play a real game like nickelodon all stars")
    elif (freetime1 == "football"):
        print("Sui")
    else:
        print("sussy")
        


freetime()

def outside():
    outsid3=input("Do you go outside?")
    if (outsid3  == "yes"):
        print("you musnt be harry peers")
    
posotive_feelings =["happy" , "excited","joy","hope"]
negative_feelings =["sad","angry","raging","disappointed"]

feel=input("Whar is your current feeling")
if feel in posotive_feelings or in negative_feelings:
    print("I understand why you feel that way")
else:
    print("thats cool")

