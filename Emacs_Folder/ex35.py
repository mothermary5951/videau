from sys import exit

def gold_room():
    print "This room is full of gold.  How much do you take?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:    # I think this makes the program recognize an integer, OR a
        how_much = int(choice)          #  string.
    else:
        dead("Man, learn to type a number.") # If a non-integer is typed, this returns & ends the game.

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)  # This is the end of the game
    else:
        dead("You greedy bastard!")  #or this is, depending on your greed.

def bear_room():   # This is the door on the left.
    print "There's a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        choice = raw_input("> ")
        
        if choice == "take honey":
            dead ("The bear looks at you and slaps your face off.") # end game
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door.  You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.") # output if you reenter "taunt
        elif choice == "open door" and bear_moved:   # bear" instead of open door. ends game.  
            gold_room()
        else:
            print "I have no idea what that means." # output if you hit return or enter gibberish.

def cthulhu_room():    #This is the door on the right.
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start() #Takes you back to the beginning, so you can choose "left" instead.
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):  
    print why, "Good job!"  # Tells you why you died and congratulates you.
    exit(0)    # CLEAN EXIT FROM SCRIPT

def start():   # Beginnning of game
    print "You are in a dark room."
    print "There is a door to your right and a door to your left."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
start()

