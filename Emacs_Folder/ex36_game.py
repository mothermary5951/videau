from sys import exit

def attack():
    print "Attacked by gesturing mudskippers!"
    print "But you have no weapons!"
    print "Will you scream or give them chewing gum?"

    choice = raw_input("> ")

    if choice == "scream":
        dead ("They hate noise and smother it.")
    elif choice == "chewing gum":
        print "No teeth, but they love the taste!  Now, onward!"
        ahead()
    else:
        print "Already confused?"
        flying()

def surprise():
    print "Up to your waist in underbrush ... but what's that?"
    print "On the ground, there.  Shiny!  Pick up or leave it?"

    choice = raw_input("> ")
    if choice == "pick up":
        water_world()
    elif choice == "leave it":
        dead ("Well, would have saved your life!")
    else:
        print "Adventure!"
        print "Now do some arithmetic to see what happens."
        print "What's the answer to this problem? 3 + 2 + 1 - 5 + 4 % 2 - 1 /4 + 6"

        choice = raw_input("> ")

        if choice == "7":
            print "You win a prize!  The mental sword of math excellence!"
            tree_climb()
        else:
            print "What happens to bad mathematicians?"
            attack()

def tree_climb():
    print "You climb a tree to see how close you're getting to The Light."
    print "You're up high, but what next?  Stay in the tree or climb down?"

    choice = raw_input("> ")

    if choice == "stay":
        print "Good choice!  Here's an eagle to take you to The Light!"
        water_world()
    elif choice == "climb down":
        print "Oops.  You climbed down into a pit of fire ants."
        dead ("Bad way to go, too.")

        
def flying():
    print "The choice is made for you, and you're airborne!"
    print "Wait. You're flying too fast, and The Light is already behind you now!"
    print "What now?  Land or fly?"
    
    choice = raw_input("> ")
    if choice == "land":
        ahead()
    elif choice == "fly":
        dead ("So, away you go!")
    else:
        print "Want another shot at this?"
        print "Here's a riddle:   How many kinds of people are there?"

        choice = raw_input("> ")
        x = "10"
        y = "Those who know binary and those who don't."
        if choice == x:
            print "Good job, you big nerd!"
            flying()
        elif choice == y:
            print "Good job, you big nerd!"
            flying()
        else:
            dead ("You oughta know that one.")

def ahead():
    print "More battles! Go fast, or grab a log or a boulder! Run or fight?"
    battle_ends = False
    
    while True:
        choice = raw_input("> ")
        if choice == "run" and not battle_ends:
            water_world()
        elif choice == "fight" and not battle_ends:
            print "This will be bloody. Prepare for pain, given and received!"
            bloody()
        elif choice == "fight" and battle_ends:
            print "You've won! Take a quick aspirin and bury the dead."
            battle_ends = True
            water_world()
        else:
            dead ("No decision is a decision, you know.")

def water_world():
    print "Surprise! Welcome to Crater Lake, underwater home of The Light!"
    print "You're very close now. In the mood to swim or sail?"

    choice = raw_input()
    if choice == "swim":
        print "You've arrived at the Light. Bask and enjoy! You win!"
    elif choice == "sail":
        dead ("Bounce out of the damn boat!")
    else:
        print "How would you like to travel?"
        flying()

def bloody():
    print "You are bleeding and bruised."
    print "You have battled bravely and done more damage than has been done to you."
    print "Do you give up or fight on?"

    choice = raw_input()
    if choice == "give up":
        dead ("RIP.")
    elif choice == "fight on":
        water_world()
    else:
        volunteers = 25
        enemies = 50
        horses = 25
        horses_ridden  = volunteers
        
        print "There are", horses, "horses and", volunteers, "volunteers giving us", horses_ridden, "mounted fighters."
        print "Our", horses_ridden, "mounted fighters against", enemies, "enemies on foot means we can win this!"
        water_world()

                          
def dead(why):
    print why, "The Light will wait for you. Bye!"
    exit(0)

def start():
    print "Welcome! Ready?"
    print "Go to The Light. See it in distance? But how to reach it?"
    print "At least two ways:  the path or dead reckoning.  Which for you?"

    choice = raw_input("> ")

    if choice == "path":
        print "It's a beautiful trap! Uh oh! An attack!"
        attack()   
    elif choice == "dead reckoning":
        surprise()
    else:
        print "You're flying!  You're flying!"
        flying()
start()
