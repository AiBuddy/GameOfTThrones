
import time
import sys
import random


def loading():
    for i in range(101):
        time.sleep(.01)
        sys.stdout.write(f"\r{i}%")
        sys.stdout.flush()
    time.sleep(1)

def placeOfDanny():
    kidnapPlaceOfDanny = ['westeros', 'essos' , 'sothoryos']
    placeOfDanny.selectPlace = random.choice(kidnapPlaceOfDanny)
    return placeOfDanny.selectPlace


def westeros():
    print("Lets go Westeros.")
    print("We are in Westeros")
    if "westeros" in placeOfDanny.selectPlace:
        print("Dany is in westeros")
        playAgain = input("Want to Play Again? ")
        if "yes" in playAgain:
            start()
        else:
            stop()
    else:
        print("Dany is not here")
        print("Go to another place")
        selectContinents()


def essos():
    print("Lets go Essos.")
    if "essos"  in placeOfDanny.selectPlace:
        print("Dany is in essos")
        playAgain = input("Want to Play Again? ")
        if "yes" in playAgain:
            start()
        else:
            stop()
    else:
        print("Dany is not here")
        print("Go to another place")
        selectContinents()


def sothoryos():
    print("Lets go Sothoryos")

    if "sothoryos" in placeOfDanny.selectPlace:
        print("Dany is in sothoryos")
        playAgain = input("Want to Play Again? ")
        if "yes" in playAgain:
            start()
        else:
            stop()
    else:
        print("Dany is not here")
        print("Go to another place")
        selectContinents()

def selectContinents():
    print("1.\tWesteros")
    print("2.\tEssos")
    print("3.\tSothoryos")
    select = input()
    if "1" in select:
        westeros()
    elif "2" in select:
        essos()
    elif "3" in select:
        sothoryos()
    else:
        print("No choice matched, try again! ")
        selectContinents()

def stop():
    print("Ok, No problem. I will find someone else")
    exit(0)

def start():
    placeOfDanny()
    print("\tLoading Game", end="")
    loading()
    print("\nALERT!!!")
    time.sleep(.5)
    print("\nALERT!!!")
    time.sleep(.4)
    print("\nALERT!!!")
    time.sleep(.3)
    print("\nOh no, Dany is KIDNAPPED!!!")
    print("\nI am Jorah. Would you like to help me in finding of Dany?")

    answer = input("> ")
    if "yes" in answer:
        print("Great, what is your name?")
        nameOfPlayer = input("> ")
        print(f"{nameOfPlayer} Thank you for your kindness. Lets Find Her.")
        print("Where should we go first?")
        selectContinents()
    else:
        stop()

def playAgain():
    againPlay = input("Want to play again? ")
    if "yes" in againPlay:
        start()
    else:
        stop()

start()
