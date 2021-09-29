from random import choice 
from random import randint
import time
import sys
import pyfiglet
from speech import print_speech
from clear import clear_screen
from tabulate import tabulate

## Classes ##

# The Character Class has 6 attributes: name, age, shape, tries, coins and result. 
# The shape determins which bonus the player gets at the start of the game 
# The tries refer to how many attempts they have to answer a question during a battle. If they get it wrong they use up a try 
# The coins are used to buy the help of the calculator 
# The result is changed to win or lose at the end of a battle.

# The class has 3 functions: pick up, die and win 
# Pick up adds an item to their list of items 
# Die is for when they run out of tries during a battle 
# Win is for when they win a battle. It adds water to the fountain and tells the player how many coins and tries they ended the battle with 

class Character:
    def __init__(self,tries, coins): 
        self.name= ""             
        self.age= "" 
        self.shape= ""
        self.tries= tries
        self.coins= coins
        self.result= ""
        
    
    def pick_up(self,item):                 
        items.append(item)
        print(f"You picked up the {item}!")

    def die(self, enemy):                   
        print(f"Oh no! You ran out of tries and the {enemy.name} didn't lose its knowledge!")

    def win(self, enemy):                   
        global fountain_water                
        print(f"You defeated the {enemy.name}!\n")
        time.sleep(2)
        print(f"You gained {enemy.water} litres of water for the fountain!\n")
        time.sleep(2)
        fountain_water += enemy.water 
        print(f"Now the fointain has {fountain_water} litres of water. You need {100-fountain_water} more litres to win!\n")
        print(f"You have {user.coins} coins and {user.tries} tries left.\n")
        


# An Org has 4 attributes: name, knowledge, coins and water 
# Name defines their name 
# Knowledge defines how difficult they are to beat in a battle. A correct regular question knocks off two knowledge points while 
#  a correct calculator question knocks off only 1 knowledge point. 
# Coins defines how many coins a player needs to be able to use the calculator against them 
# Water defines how many litres of water the player wins for the fountain when they beat them. 

# They have two functions: attack and describe.
# Attack is used when a player is attacked by them and a battle starts 
# Describe is used to bring up their stats 

class Org:

    def __init__(self, name, knowledge, coins, water): 
        self.name = name                               
        self.knowledge = knowledge                     
        self.coins = coins 
        self.water = water 

    def attack(self,user):                              # An Org attacks the player at the start of the battle.
        print(f"You have been attacked by a {self.name}! They have a knowledge of {self.knowledge}.\n")
        time.sleep(2)
        print("I'm going to ask you a really tricky question, you better be ready!\n")
    

    def describe(self):                                 # A user can get the Org's stats 
        print_speech(f"The {self.name} has knowledge of {self.knowledge}.\n"
        f"You will need {self.coins} coins to use the Calculator and if you win you will gain {self.water} litres of water for the fountain.\n") 


# The Owl Question class has three attributes: quesiton, answer, and coins. 
# If a player gets the question right, they win 5 coins. 

class Owl_question:                                    
                                                        
    def __init__(self, question, answer):
        self.question = question 
        self.answer = answer
        self.coins = 5 


## Functions ##


# The owl asks the user a question for them to try and win 5 coins  

def owl(): 
    print("./\_/\.")
    print("((@v@))")
    print("():::()")
    print(" VV-VV\n")
    print_speech(f"Welcome {user.name.title()}, I'm the Wise-Owl and I am here to help you gain gold coins!\n"
            "To win coins you must answer a question!\n")
    time.sleep(2)
    print("Here it comes!")
    time.sleep(2)
    num1 = randint(20,100)                                               # Two random numbers between 20 and 100 are chosen
    num2 = randint(20, 100)
    o_question = Owl_question(f"What is {num1} + {num2}?: ",num1 + num2) # A quesiton is created using the Owl question class 
    answer = input(o_question.question)                                  # Player enters their answer 
    if answer.isdecimal() == False:                                      # Answer is checked to make sure it is a number 
        while answer.isdecimal() == False:
            print("Sorry, you must enter a number.")
            answer = input(o_question.question)
    else:
        pass
    answer = int(answer)                     # The player is asked a question and their inputted answer is turned from a string to an int
    if answer == o_question.answer:          # If they get it correct they win the coins. 
        print(f"That's right! You have won {o_question.coins} gold coins!")
        user.coins += o_question.coins 
        user.result= "win"
        time.sleep(2)
        clear_screen()
    else:                                      # If they get it wrong they don't win anything. 
        print("Sorry, thats not right. Better luck next time!")
        user.result= "lose"
        clear_screen()


# The bonus function gives the player a bonus at the start of the game, depending on whicih shape they choose. 

def bonus(shape): 
    if user.shape.lower() == "star":
        user.coins += 5             # if star is chosen, the player will start with 5 extra coins 
        print("As you chose a star, you start with 5 extra gold coins!\n")
        time.sleep(2)
    elif user.shape.lower() == "circle":
        items.append("spade")       # if the circle is chosen, the player starts with a spade in their bag
        print("As you chose a circle, you get to start the game with a spade!\nThat means we can get going straight away\n")
        time.sleep(2)
    elif user.shape.lower() == "triangle":
        user.tries += 1             # if the triangle is chosen, they will start with an extra free go 
        print("As you chose a triangle , you get to start the game with an extra free go!\n")
        time.sleep(2)
    else:
        user.coins +=10             # if a square is chosen they start with 10 extra coins 
        print("As you chose a square, you start with 10 extra gold coins!\n")
        time.sleep(2)
    

##Add-land starts here##

# The Eazorgs are in Add-land. 

def add_land():
    print("You landed safely in Add-land, which has been taken over by the Eazorgs.\n")
    time.sleep(2)
    stats= input("Do you want to look at their stats? Enter 'y' or 'n' to carry on ") # player can choose to look at an Eazorg's stats 
    answers = ["y", "n"]
    while stats not in answers:
        stats = input("You must enter 'y' or 'n': ")
    if stats.lower() == 'y':
        eazorg.describe()
    else:
        pass
    print("\nYou carry on into the land and past some strange looking trees.\n")
    time.sleep(2)
    print("Oh no! An Eazorg has crept up behind you!\n")
    time.sleep(2)
    clear_screen()
    eazorg.attack(user)  
    time.sleep(2)                                        # Player is attacked by an Eazorg  
    addquestion, addquestion_cal= battle.add_question()  # Addition quesitons are created using the add_question function 
    battle.battle(user, eazorg, addquestion, addquestion_cal,items) # they are passed into the battle function. 
    if user.result== "win":                        # If they win the first round, it continues. 
        user.tries += 1                            # They get an extra try to help them through 
        while eazorg.knowledge >= 1:               # While the Org still has knowledge points left they continue to battle, unless they 
            if user.result == "win":               # lose, in which case the 'else' option is chosen and the game ends. 
                user.tries += 1
                battle.next_round(eazorg,user)
                time.sleep(2)
                clear_screen()
                addquestion, addquestion_cal= battle.add_question() 
                battle.battle(user, eazorg, addquestion, addquestion_cal,items) 
            else: 
                print("You ran out of tries, so that's the end of your visit to Digiland. Better luck next time!")
                break
        if user.result == "win":               # If the player wins, Add-land gets appended to places so that if they save and quit
            user.win(eazorg)                   # the game will then start at Sub-land.
            places.append("add-land")
            time.sleep(2)
            print("Your next stop is Sub-Land.\n")
            quit= input("Do you want to save and quit or continue? Enter 'q' or 'c': ")
            answers = ["q", "c"]
            while quit not in answers:
                quit= input( "Please enter 'q' or 'c': ")
            if quit.lower() == "q":                                                  # If they quit, the game saves and exits.
                print("Ok, thanks for playing! See you again soon.")                    # The game is also saved if they continue. 
                save_load.save(user.name,places, items, user.coins, user.tries,fountain_water)
                sys.exit()
            else:
                save_load.save(user.name, places, items, user.coins, user.tries,fountain_water)
                time.sleep(2)
                clear_screen()
                sub_land()
        else:
            print("We're sorry you ran out of tries. Please come and help us again soon.")
    else:     
        print("You ran out of tries, so that's the end of your visit to Digiland. Better luck next time!")   


## Sub-land starts here ##

# Demi-zorgs are in subland 
# The player starts with the option to pick up some coins that the see on the floor. In they do, pick_up() is called.
# If they don't, they continue on to go past a cafe which they can enter or pass by. 
# Either enter_cafe() or not_cafe() is called. 
        
def sub_land():
    print("You arrive in Sub-land. The talk on the town is that the Demi-zorgs have landed here.\n")
    time.sleep(2)
    stats= input("Do you want to look at their stats? Enter 'y' or 'n' to carry on ")
    answers = ["y", "n"]
    while stats not in answers:
        stats = input("You must enter 'y' or 'n': ")
    if stats.lower() == 'y':
        demizorg.describe()
    else:
        pass
    time.sleep(2)
    print("You walk on and see some gold coins on the floor\n") 
    time.sleep(2)   
    coins = input("Do you want to pick them up? Enter 'pick up' if you do or 'leave' to leave them: ")
    options = ["pick up", "leave"]    #There are some gold coins on the floor. If the player picks up the coins pick_up() is called 
    while coins.lower() not in options:
        coins= input("You must choose 'pick up' or 'leave': ")
    if coins.lower() == "pick up":                                      
        pick_up()
    else: 
        print("You decide to leave them there- someone might be coming back for them!\n")
        time.sleep(2)
        cafe = input("You carry on and notice a sign for a cafe, do you want to go in? Type 'enter' or 'continue': ")
        answers = ['enter', 'continue']                  # If the player doesn't pick up the coins, they find a cafe 
        while cafe.lower() not in answers:
            cafe = input("You need to type 'enter' or 'continue': ")
        if cafe == "enter": 
            time.sleep(2)
            clear_screen()                                # If they go into the cafe, enter_cafe() is called 
            enter_cafe()
        else:  
            time.sleep(2)
            clear_screen()                                 # If they dont go into the cafe not_cafe() is called 
            not_cafe()
            

##Functions used within Sub-Land##

# If the player picked up the coins, they win 5 coins, but then they are attacked by a Demi-Zorg. 
# At the end of the battle if they win they are approached by an old man who they can choose to speak with or ignore. 
# If they speak with him, man() is called, if not, they continue and div_land() is called, unless they save and quit. 

def pick_up():                                                      
    print("You found 5 coins! You add them to your collection.\n")    
    user.coins += 5                                                 
    time.sleep(2)                                                    
    print("Uh-oh, it looks like those coins may have belonged to a Demi-zorg\n")
    time.sleep(2) 
    print("He's come to investigate and now he's attacked you!\n")
    time.sleep(2)
    demizorg.attack(user)
    time.sleep(2)
    clear_screen()
    subquestion, subquestion_cal= battle.sub_question()   # subtraction questions are created using the sub_question() function 
    battle.battle(user, demizorg, subquestion, subquestion_cal,items)
    if user.result== "win":                  #if they win the first round it continues while the Demizorg knowledge is higher than 1
        user.tries += 1
        while demizorg.knowledge >= 1:
            if user.result == "win":
                user.tries += 1
                battle.next_round(demizorg,user)
                time.sleep(2)
                clear_screen()
                subquestion, subquestion_cal= battle.sub_question()
                battle.battle(user, demizorg, subquestion, subquestion_cal,items)
            else: 
                print("You ran out of tries, so that's the end of your visit to Digiland. Better luck next time!")
                break
        if user.result == "win":                                         # if they win, the old man approaches. 
            user.win(demizorg)
            time.sleep(2)
            clear_screen()
            print("As you are about to leave to tunnel over to Div-land, an old man approaches you.\n"
            "It looks like he's got something in his hand but you can't be sure.\n")
            time.sleep(2)
            talk = input("Do you want to stop and speak with him? Enter 'speak' or 'ignore': ")
            answers = ['speak', 'ignore']
            while talk.lower() not in answers:                          # Player chooses to speak to or ignore old man 
                talk = input("You need to type 'speak' or 'ignore': ")
            if talk == "speak":   
                time.sleep(2)
                clear_screen()                                        # If they speak to him, man() is called, if not they can save and exit, 
                man()                                                   # or carry on. 
            else:
                print("You avoid the old man as you aren't sure which side he's on.\n")
                time.sleep(2)
                places.append("sub-land")
                time.sleep(2)
                quit= input("Do you want to save and quit or continue? Enter 'q' or 'c': ")
                answers = ["q", "c"]
                while quit not in answers:
                    quit= input( "Please enter 'q' or 'c': ")
                if quit.lower() == "q": 
                    print("Ok, thanks for playing! See you again soon.")
                    save_load.save(user.name,places, items, user.coins, user.tries,fountain_water)
                    sys.exit()
                else:
                    save_load.save(user.name,places, items, user.coins, user.tries,fountain_water)
                    time.sleep(2)
                    clear_screen()
                    div_land()
        else: 
            print("We're sorry you ran out of tries. Please come and help us again soon.")
    else:     
        print("We're sorry you ran out of tries. Please come and help us again soon.")   


# If they speak to the man, he gives them a golden calculator which is appended to their items. 
# The golden calculator is there to be used if they run out of coins during a battle and get stuck on a question. 
# It can only be used once and once it's been used they won't be offered it again. 
# Div-land() funciton is called at the end, unless they save and quit. 

def man():
    print("You stop and speak to him\n")
    time.sleep(2)
    print_speech(f"Hi {user.name.title()}, thank you so much for helping us defeat the Orgs!\n"
    "I can see you're doing a wonderful job, so I'd like to give you my golden calculator to use if you get stuck and have no coins left.\n"
    "It's very old and will only work once! So use it wisely.\n"
    "Good luck with the rest of your adventure!\n")
    items.append("Golden Calculator") 
    time.sleep(2)
    print("You thank the man and put the golden calculator in your bag, ready to use when you need it.\n")
    time.sleep(2)
    print("You decide to move on from Sub-land and tunnel over to Div-land\n")
    places.append("sub-land")
    time.sleep(2)
    quit= input("Do you want to save and quit or continue? Enter 'q' or 'c': ")
    answers = ["q", "c"]
    while quit not in answers:
        quit= input( "Please enter 'q' or 'c': ")
    if quit.lower() == "q": 
        print("Ok, thanks for playing! See you again soon.")
        save_load.save(user.name,places, items, user.coins, user.tries,fountain_water)
        sys.exit()
    else:
        save_load.save(user.name,places, items, user.coins, user.tries,fountain_water)
        time.sleep(2)
        clear_screen()
        div_land()


# If they dont go into the cafe they get attacked. If they win the battle, they get given 10 gold coins by the bartender of the cafe. 
# Div-land is called at the end, unless they save and quit. 

def not_cafe():
    print("You continue on past the cafe, but all of a sudden the door swings open and a Demi-zorg appears!\n")
    time.sleep(2)
    print("You stop in your tracks and get ready to take him on!\n")
    time.sleep(2)
    demizorg.attack(user)
    subquestion, subquestion_cal= battle.sub_question()
    battle.battle(user, demizorg, subquestion, subquestion_cal,items)
    if user.result== "win":
        user.tries += 1
        while demizorg.knowledge >= 1:
            if user.result == "win":
                user.tries += 1
                battle.next_round(demizorg,user)
                clear_screen()
                subquestion, subquestion_cal= battle.sub_question()
                battle.battle(user, demizorg, subquestion, subquestion_cal,items)
            else: 
                print("You ran out of tries, so that's the end of your visit to Digiland. Better luck next time!")
                break
        if user.result == "win":
            user.win(demizorg)
            time.sleep(2)
            print("You dust yourself down and the owner of the cafe comes running out\n")
            time.sleep(2)
            print("He thanks you for saving Sub-land and hands you 10 gold coins!\n")  #They are given 10 coins. 
            time.sleep(2)
            user.coins += 10
            print("You put the coins in your bag, thank him, and head to Div-land.\n") 
            places.append("sub-land")
            quit= input("Do you want to save and quit or continue? Enter 'q' or 'c': ")
            answers = ["q", "c"]
            while quit not in answers:
                quit= input( "Please enter 'q' or 'c': ")
            if quit.lower() == "q":
                print("Ok, thanks for playing! See you again soon.") 
                save_load.save(user.name,places, items, user.coins, user.tries,fountain_water)
                sys.exit()
            else:
                save_load.save(user.name,places, items, user.coins, user.tries,fountain_water)
                time.sleep(2)
                clear_screen()
                div_land()
        else: 
            print("We're sorry you ran out of tries. Please come and help us again soon.")
    else:     
        print("We're sorry you ran out of tries. Please come and help us again soon.") 


# If they go into the cafe, they can choose to sit or stand. 
# If they stand, bar_stand is called and a demi-zorg enters and they fight. 
# If they sit, they get the option to talk to the barman or ignore him.
# If they ignore him, bar_ignore is called and a demi-zorg comes in and they fight. 
# If they speak to him, bar_speak is called and they are given 5 gold coins. Then a demi-zorg enters and they fight. 

def enter_cafe():
    print("You open the door to the cafe and step inside."
    " There are a few scared looking locals huddled round small tables.\n")
    time.sleep(2)
    sit = input("There's a seat free at the bar, do you want to take it? Enter 'sit' or 'stand'")
    answers = ['sit', 'stand']
    while sit.lower() not in answers:
        sit = input("You need to type 'sit' or 'stand': ")
    if sit == 'sit': #if they sit down at the bar 
        print("You take a seat at the bar and order a drink.\n")
        time.sleep(2)
        print("The barman looks like he wants to say something\n")
        talk = input("Do you want to talk to him? Enter 'talk' or 'ignore': ")
        answers = ['talk', 'ignore']
        while talk.lower() not in answers:
            talk = input("You need to type 'talk' or 'ignore': ")
        if talk == 'talk': #if they talk to the barman
            time.sleep(2)
            clear_screen()  
            bar_talk()
        else: 
            time.sleep(2)
            clear_screen()  
            bar_ignore()
    else: 
        time.sleep(2)
        clear_screen()  
        bar_stand()

# If they don't sit at the bar, this function is called and they fight a demi-zorg. 

def bar_stand(): 
    print("You decide to stay where you are, but hear a huge crash behind you!")
    time.sleep(2) #if they dont sit down 
    print("A Demi-Zorg has entered and it's time for you to fight!")
    time.sleep(2)
    demizorg.attack(user)
    subquestion, subquestion_cal= battle.sub_question()
    battle.battle(user, demizorg, subquestion, subquestion_cal,items)
    if user.result== "win":
        user.tries += 1
        while demizorg.knowledge >= 1:
            if user.result == "win":
                user.tries += 1
                battle.next_round(demizorg,user)
                clear_screen()
                subquestion, subquestion_cal= battle.sub_question()
                battle.battle(user, demizorg, subquestion, subquestion_cal,items)
            else: 
                print("You ran out of tries, so that's the end of your visit to Digiland. Better luck next time!")
                break
        if user.result == "win":
            user.win(demizorg)
            print("There is a round of applause in the cafe and it looks like your work here is done")
            print("You leave the cafe and head to Div-land.") 
            places.append("sub-land")
            quit= input("Do you want to save and quit or continue? Enter 'q' or 'c': ")
            answers = ["q", "c"]
            while quit not in answers:
                quit= input( "Please enter 'q' or 'c': ")
            if quit.lower() == "q": 
                print("Ok, thanks for playing! See you again soon.")
                save_load.save(user.name,places, items, user.coins, user.tries,fountain_water)
                sys.exit()
            else:
                save_load.save(user.name,places, items, user.coins, user.tries,fountain_water)
                time.sleep(2)
                clear_screen()
                div_land()
        else: 
            print("We're sorry you ran out of tries. Please come and help us again soon.")
    else:     
        print("We're sorry you ran out of tries. Please come and help us again soon.")        



# if they sit down and then speak to the bar man, this functiton is called. They are given 5 coins and then they fight a demi-zorg. 

def bar_talk():
    print("The barman comes over and says:\n")
    print_speech(f"Hi, {user.name.title()}, I heard you were here to help,\n"
        "and I hear you defeated the Eazorgs over in Add-land.\n"
    "I want to give you this to say thanks (and the milkshake is on the house!)\n")
    time.sleep(2)
    print("The barman hands you a pouch with 5 gold coins inside!")
    user.coins += 5              
    save_load.save(user.name,places, items, user.coins, user.tries,fountain_water)
    print(f"You say thank you and count your coins. You now have {user.coins} coins in total.")
    time.sleep(2)
    print("Just as you put the coins away there's huge crash behind you!\n")
    time.sleep(2)
    print("A Demi-zorg has entered and it's time for you to fight!\n")     
    demizorg.attack(user)
    time.sleep(2)
    subquestion, subquestion_cal= battle.sub_question()
    battle.battle(user, demizorg, subquestion, subquestion_cal,items)
    if user.result== "win": 
        while demizorg.knowledge >= 1: #continues with rounds until enemy has 0 knowledge 
            if user.result == "win":
                user.tries += 1
                battle.next_round(demizorg,user)
                clear_screen()
                subquestion, subquestion_cal= battle.sub_question()
                battle.battle(user, demizorg, subquestion, subquestion_cal,items)
            else: 
                print("You ran out of tries, so that's the end of your visit to Digiland. Better luck next time!")
                break
        if user.result == "win": #if they win the next rounds 
            user.win(demizorg)
            print("There is a round of applause in the cafe and it looks like your work here is done")
            time.sleep(2)
            print("The bartender tells you good luck as you leave and head off to Div-land") #they go to the next land 
            places.append("sub-land")
            quit= input("Do you want to save and quit or continue? Enter 'q' or 'c': ")
            answers = ["q","c"]
            while quit not in answers:
                quit= input( "Please enter 'q' or 'c': ")
            if quit.lower() == "q": 
                print("Ok, thanks for playing! See you again soon.")
                save_load.save(user.name,places, items, user.coins, user.tries,fountain_water)
                sys.exit()
            else:
                save_load.save(user.name,places, items, user.coins, user.tries,fountain_water)
                time.sleep(2)
                clear_screen()
                div_land()
        else: 
            print("We're sorry you ran out of tries. Please come and help us again soon.")
    else:     
        print("We're sorry you ran out of tries. Please come and help us again soon.")  


# If they ignore the barman this funciton is called and they fight a demi-zorg. 

def bar_ignore(): 
    print("You look away, but then hear a huge crash.\n")
    time.sleep(2)
    print("A Demi-zorg enters the bar and and it's time for you to fight!") 
    demizorg.attack(user)
    time.sleep(2)
    subquestion, subquestion_cal= battle.sub_question()
    battle.battle(user, demizorg, subquestion, subquestion_cal,items)
    if user.result== "win":
        user.tries += 1
        while demizorg.knowledge >= 1:
            if user.result == "win":
                user.tries += 1
                battle.next_round(demizorg, user)
                clear_screen()
                subquestion, subquestion_cal= battle.sub_question()
                battle.battle(user, demizorg, subquestion, subquestion_cal,items)
            else: 
                print("You ran out of tries, so that's the end of your visit to Digiland. Better luck next time!")
                break
        if user.result == "win":
            user.win(demizorg)
            print("There is a round of applause in the cafe and it looks like your work here is done.\n")
            time.sleep(2)
            print("The bartender tells you good luck as you leave and head off to Div-land.\n")
            places.append("sub-land")
            quit= input("Do you want to save and quit or continue? Enter 'q' or 'c': ")
            answers = ["q", "c"]
            while quit not in answers:
                quit= input( "Please enter 'q' or 'c': ")
            if quit.lower() == "q": 
                print("Ok, thanks for playing! See you again soon.") 
                save_load.save(user.name,places, items, user.coins, user.tries,fountain_water)
                sys.exit()
            else:
                save_load.save(user.name,places, items, user.coins, user.tries,fountain_water)
                time.sleep(2)
                clear_screen()
                div_land()
        else: 
            print("We're sorry you ran out of tries. Please come and help us again soon.")
    else:
        print("We're sorry you ran out of tries. Please come and help us again soon.") 




## Div-land starts here ##

# When they arrive in Div-land, they are given the option to see the wise owl. 
# If they weren't given the calculator by the old man, tree()is called where they are then given the option to climb a tree, where they are given a golden calculator 
# If they already have a calculator, this function is skipped. 
# They see a key by the lake and can choose whether to pick it up or leave it where it is. 
# After this, they are attacked by a Centorg 
# If they win the battle, they swim in the lake and find a chest. 
# if they have the key, they open the chest to find 10 coins. 
# If they dont have the key, they keep the chest for later. 

def div_land():
    print("You arrive in Div-land to be surrounded by huge redwood trees. Be careful, the Centorgs are roaming here.\n")
    time.sleep(2)
    stats= input("Do you want to look at their stats? Enter 'y' or 'n' to carry on: ")
    answers = ["y", "n"]
    while stats not in answers:
        stats = input("You must enter 'y' or 'n': ")
    if stats.lower() == 'y':
        time.sleep(2)
        centorg.describe()
    else:
        pass
    time.sleep(2)
    print("You look up and see the Wise-Owl purched on the top branch!\n")
    answers= ['c', 'o']
    visit = input("Do you want to visit the owl and try to win more coins? Enter 'o' to visit or 'c' continue: ")
    while visit.lower() not in answers:
        visit = input("Sorry, you need to enter 'o' or 'c': ")
    if visit.lower() == 'o':
        time.sleep(2)
        clear_screen()
        owl()
        save_load.save(user.name,places, items, user.coins, user.tries,fountain_water) 
    else: 
        print("Ok, he looks a little tetchy anyway, maybe best to stay away!")
    time.sleep(2)
    print("You carry on through the shadowy trees")
    time.sleep(2)
    if "Golden Calculator" not in items:   # If they don't have the golden calculator, tree() is called. 
        time.sleep(2)
        clear_screen()
        tree()
        save_load.save(user.name,places, items, user.coins, user.tries,fountain_water)
    else:                                  # If they have the golden calculator, nothing happens. 
        pass
    print("You come to a clearing and see a huge lake. It looks like there is something beside it at the shore.\n")
    time.sleep(2)
    print("You walk down to the side of the lake and find a silver key.\n")
    time.sleep(2)
    take_key= input(f"Do you want to pick it up {user.name.title()}? Enter 'y' or 'n': ")
    answers = ['y','n']
    while take_key.lower() not in answers:
        take_key= input(f"Please enter 'y' or 'n': ")
    if take_key.lower() == 'y':
        user.pick_up("key")                                                         # if they pick up the key, it is added to items.
    else:
        print("You decide to leave the key where it is.\n")                         # if they don't, it isn't. 
    print("Just as you stand up from examining the key, a Centorg knocks you down!\n")
    time.sleep(3)
    clear_screen()
    centorg.attack(user)                                                            # They are attacked by a Centorg.
    divquestion, divquestion_cal= battle.div_question()
    battle.battle(user, centorg, divquestion, divquestion_cal,items)
    if user.result== "win":
        user.tries += 1
        while centorg.knowledge >= 1:
            if user.result == "win":
                user.tries += 1
                battle.next_round(centorg,user)
                clear_screen()
                time.sleep(2)
                divquestion, divquestion_cal= battle.div_question()
                battle.battle(user, centorg, divquestion, divquestion_cal,items)
            else: 
                print("You ran out of tries, so that's the end of your visit to Digiland. Better luck next time!")
                break
        if user.result == "win":
            user.win(centorg)
            places.append("div-land")
            time.sleep(2)
            print("That was a tough battle, but you made it! \n"
                    "You decide to have a swim in the lake to cool down. ")
            time.sleep(3)
            clear_screen()  
            lake()                                          # if they win, lake() is called 
    else: 
        print("You ran out of tries, so that's the end of your visit to Digiland. Better luck next time!")

##functions used in div-land##

# If they don't have a golden calculator, this function is called.
# They are given the option to climb a tree. 
# If they climb it, they speak to a bird at the top who gives them a golden calculator. 
# If they don't climb it, nothing happens. 

def tree():
    print("You see something glittering up in one of the trees.\n")
    time.sleep(2)
    answers = ['climb', 'continue']
    climb = input("Do you want to climb up and investigate? Enter 'climb' or 'continue': ")
    while climb.lower() not in answers:
        climb = input("Sorry, you need to enter 'climb' or 'continue: ")
    if climb.lower() == 'climb':
        print("You decide to climb up the tree\n")
        time.sleep(2)
        i = 3
        while i > 0:             #repeats 3 times 
            print("higher...")
            time.sleep(2)    
            i -= 1
        print("You finally reach the top and find a golden calculator sitting in a nest.\n")
        time.sleep(2)
        print(f"A bird hops over to you and says:")
        time.sleep(2)
        print_speech(f"Hi {user.name.title()}! It's great to meet you.\n"
        "I've heard so much about what you've acheived so far and I'd love to give you my golden calculator.\n"
        "It's very old so will only work once, but if you're stuck you can use it to make the question easier!\n")
        items.append("Golden Calculator")    # golden calculator is added to items. 
        time.sleep(2)
        print("You thank the bird, put the calculator in your bag, ready for if you need it, and climb back down the tree.\n")
        time.sleep(2)
        clear_screen()
    else:
            print("You carry on past the tree ")
    return items 



# This funciton is called after their battle with the Centorg. 
# They swim down and find a chest at the bottom of the lake. 
# If they have a key, yes_key() is called. 
# If they didn't pick up the key, no_key() is called. 

def lake():
    print("You jump into the lake and swim around.\n")
    time.sleep(3)
    print("After a few minutes you notice something glinting right at the bottom of the lake.\n")
    time.sleep(3)
    print("You swim down and see that it's a chest! You pull it up with you with all your strentgh.\n")
    if "key" not in items:
        time.sleep(2)
        clear_screen()
        no_key()
    else:
        time.sleep(2)
        clear_screen()
        yes_key()

# If they didn't pick up the key, they have to take the chest with them. 
# Mult-land is called at the end of this function, unless they save and quit. 

def no_key():
    print("Once you're out of the water you run over to where you saw that silver key, but it's gone!!\n"
        "If only you had picked it up, you're sure it would open the chest.\n"
        "luckily the chest fits in your bag, so you take it with you.\n")
    time.sleep(2)
    print("You decide it's time to tunnel over to Mult-land and finished what you came here to do!")
    time.sleep(2)
    quit= input("Do you want to save and quit or continue? Enter 'q' or 'c': ")
    answers = ["q", "c"]
    while quit not in answers:
        quit= input( "Please enter 'q' or 'c': ")
    if quit.lower() == "q": 
        print("Ok, thanks for playing! See you again soon.")
        save_load.save(user.name,places, items, user.coins, user.tries,fountain_water)
        sys.exit()
    else:
        save_load.save(user.name,places, items, user.coins, user.tries,fountain_water)
        time.sleep(2)
        clear_screen()
        mult_land()


# If they picked up the key, they can open the chest and find 10 gold coins. 
# Mult-land is then called, unless they save and quit. 

def yes_key():
    print("You're so happy you picked up that key earlier! You take the key from you bag and try it in the lock...")
    time.sleep(3)
    print("...")
    time.sleep(3)
    print("...")
    time.sleep(3)
    print("It fits! You open the chest to find 10 gold coins")
    user.coins += 10
    time.sleep(2)
    print("You put the coins in your bag, you'll be needing them in Mult-land!")
    time.sleep(2)
    print("It's time to get going!")
    quit= input("Do you want to save and quit or continue? Enter 'q' or 'c': ")
    answers = ["q", "c"]
    while quit not in answers:
        quit= input( "Please enter 'q' or 'c': ")
    if quit.lower() == "q": 
        print("Ok, thanks for playing! See you again soon.")
        save_load.save(user.name,places, items, user.coins, user.tries,fountain_water)
        sys.exit()
    else:
        save_load.save(user.name,places, items, user.coins, user.tries,fountain_water)
        time.sleep(2)
        clear_screen()
        mult_land()


##Mult-land starts##

# When they arrive in Mult-land they speak with the Mayor. 
# If they dont have a golden calculator or an empty calculator case, max_cal() is called.
# If they do have the calculator or the empty case, max_coins() is called. 
# Then they are given the option to visit the owl to try and win more coins. 
# If they don't have the key, give_key() is called. 
# They then have their final battle with Zorgatron, who is waiting for them in the town square. 

def mult_land():
    print("You arrive in Mult-land to a crowd of excited people who have been waiting for your arrival!\n")
    time.sleep(2)
    print("As you walk through the crowd you see the Mayor of Digiland Max-A-Million up ahead, and he's coming your way.\n")
    time.sleep(3)
    if "Golden Calculator" not in items:
        if "Empty Calculator Case" not in items:
            clear_screen()
            max_cal() 
            save_load.save(user.name,places, items, user.coins, user.tries,fountain_water)
        else:
            clear_screen()
            max_coin()
            save_load.save(user.name,places, items, user.coins, user.tries,fountain_water)
    else:
        clear_screen()
        max_coin()
    print("After speaking with Max-A-Million, you start to feel nervous about your impending battle with Zorgatron.\n")
    time.sleep(2)
    print(f"You have {user.coins} coins at the moment. You will need coins to be able to use the calculator against Zorgatron.\n")
    time.sleep(2)
    visit = input("Do you want to visit the owl and try to win more coins? Enter 'o' to visit or 'c' to continue: ")
    answers= ["o", "c"]
    while visit.lower() not in answers:
        visit = input("Sorry, you need to enter 'o' or 'c': ")
    if visit.lower() == 'o':
        time.sleep(2)
        clear_screen()  
        owl()
        save_load.save(user.name,places, items, user.coins, user.tries,fountain_water)
    else: 
        print("Ok, let's carry on.")
        time.sleep(2)
    if "key" not in items:
        time.sleep(2)
        clear_screen()  
        give_key()
        save_load.save(user.name,places, items, user.coins, user.tries,fountain_water)
    else:
        pass 
    print("You carry on walking and finally make it to the town square.\n")
    print("You see the fountain of knowledge in the centre.\n")   
    time.sleep(2)
    print("There are crowds of people around, and suddenly Zorgatron appears!\n")
    time.sleep(3)
    print("You take a deep breath, this is it- time to fight the final battle!\n")
    time.sleep(2)
    clear_screen()
    print_speech(f"Hello {user.name.title()}, I am Zorgatron. I hear you have managed to beat the Orgs and take back knowledge for the people here, but not any more!!\n")
    print_speech("It's time to fight me, I hope you're ready!\n")
    time.sleep(2)
    clear_screen()
    multquestion, multquestion_cal= battle.mult_question()
    battle.battle(user, zorgatron, multquestion, multquestion_cal,items)
    if user.result== "win":
        user.tries += 1
        while zorgatron.knowledge >= 1:
            if user.result == "win":
                user.tries += 1
                battle.next_round(zorgatron, user)
                time.sleep(2)
                clear_screen()
                multquestion, multquestion_cal= battle.mult_question()
                battle.battle(user, zorgatron, multquestion, multquestion_cal,items)
            else: 
                print("You ran out of tries, so that's the end of your visit to Digiland. Better luck next time!")
                break
        if user.result == "win":
            time.sleep(2)
            clear_screen()
            congratulations = pyfiglet.figlet_format(f"Congratulations {user.name.title()}!!")
            print(congratulations)
            print_speech("\nZorgatron lost all his knowledge and the battle is won!\n")
            print_speech(f"Cogratulations {user.name.title()}, you defeated the Orgs and now the fountain of knowledge if full again!!\n"
            "There is a huge cheer as the townspeople rush around you, lifting you into the air\n"
            f"Max-A-Million comes over to say thank you, Digiland is returned to peace once more and it's all thanks to you {user.name.title()}\n"
            "Who knows what the future brings, but Digiland is safe, for now!")
            sys.exit()
        else:
            print("You ran out of tries, and Zorgatron won this battle. Thank you for everything you've done and better luck next time!")
            
    else:
        print("You ran out of tries, and Zorgatron won this battle. Thank you for everything you've done and better luck next time!")
       



##functions used in Mult-land##

# If they don't have the golden calculator and they've never had it, they are given it by the mayor, Max-A-Million. 

def max_cal():
    print_speech(f"'Hi {user.name.title()}, I'm Max-A-Million, the mayor of Digiland. It's such an honor to finally meet you!\n"
    "I can't thank you enough for everything you've done so far to help save our land, but I know it's not finished yet.\n"
    "Here in Mult-land the leader of the Zorgs has taken over.\n"
    "It isn't until you've beaten him that the Fountain of Knowledge will be completely replenished.\n"
    "He knows that you're here and is waiting to battle you, so you will need to meet him in the town square to finish this off.\n"
    "This isn't going to be easy, so I'd like to give you my golden calculator to use if you run out of coins and get stuck.\n"
    "It's very old so you'll only be able to use it once, so choose yout timing wisely!\n")
    items.append("Golden Calculator\n")
    print("You thank Max-A-Million and put the calculator in your bag, ready for when you might need it.")
    time.sleep(2)
    clear_screen()


# If they have had the golden calculator or still have it, Max- A- Million gives them 10 gold coins. 

def max_coin():
    print_speech(f"Hi {user.name.title()}, I'm Max-A-Million, the mayor of Digiland. It's such an honor to finally meet you!\n"
    "I can't thank you enough for everything you've done so far to help save our land, but I know it's not finished yet.\n"
    "Here in Mult-land Zorgatron, the leader of the Zorgs, has taken over.\n"
   "It isn't until you've beaten him that the Fountain of Knowledge will be completely replenished.\n"
    "He knows that you're here and is waiting to battle you, so you will need to meet him in the town square to finish this off.\n"
    "As a thank you, I'd like to give you this...\n")
    time.sleep(3)
    print("He hands you a bag of 10 gold coins! You thank him and put the coins away.\n")
    user.coins += 10 
    time.sleep(2)
    clear_screen()


# If they didnt pick up the key in Div-land, a little girl finds them and give it to them.
# They open the chest to find the coins. They give the girl 1 coin to say thank you.

def give_key():
    print("You start to make your way to the town square to meet Zorgatron, when a little girl runs up to you.")
    time.sleep(2)
    print_speech(f"Hi, {user.name.title()}, I'm so glad I found you!\n"
    "I saw you with that chest by the river, but you left before I had time to give you this...")
    time.sleep(2)
    print("She reaches into her pocket and takes out the silver key you left behind!\n")
    print("You try the key in the lock of the chest...")
    time.sleep(3)
    print("...")
    time.sleep(3)
    print("...")
    time.sleep(3)
    print("It fits! You open the chest to find 10 gold coins.\n")
    user.coins += 10
    time.sleep(2)
    print("You thank the girl, and give her a coin as an extra thank you.\n")
    user.coins -= 1 
    time.sleep(2)
    clear_screen()
    



## game starts here ##

import save_load 
import battle 

# The orgs are created.

eazorg= Org("Eazorg", 4, 8, 10)
demizorg= Org("Demi-zorg", 6, 6, 20)
centorg= Org("Centorg", 8, 4, 30)
zorgatron= Org("Zorgatron", 10, 2, 40)
welcome = pyfiglet.figlet_format("Digiland")
print(welcome)

#user can choose to reload a previous game 
new_game= input("Do you want to start a new game, or load a saved one? Enter 'new' or 'load': ") 
responses =["new", "load"]
while new_game not in responses:
    new_game= input("Sorry, please enter 'new' or 'load: ")

# If it's a new game, places, items and fountain water are set to 0 and a character is created, assigned to the variable 'user'. 
# They are assigned 3 tries and 5 coins to start off with.
# The player is given the option to load the intro

if new_game== 'new': 
    places = []
    items= []
    fountain_water = 0 
    user= Character(3, 5)
    show_intro = input("Great! Let's start a new game. Would you like to find out about what's been going on in Digiland, and how you can help? Enter 'y' or 'n': ")
    responses = ['y', 'n']
    while show_intro.lower() not in responses:
        show_intro = input("Please enter 'y' or 'n': ")
    if show_intro.lower() == 'y':
        time.sleep(2)
        clear_screen()
        orgs = [["Eazorg", 4, 8, 10], ["Demi-zorg", 6, 6, 20],["Centorg", 8, 4,30],["Zorgatron", 10, 2, 40]] #in the intro, a table is made to describe the Orgs
        labels = ["Org", "Knowledge Level", "Gold Coins Needed for Calculator", "Water reward"]
        print(tabulate(orgs, labels, tablefmt= "pretty"))
        import intro
        time.sleep(2)
        clear_screen()
    else:
        pass # if they choose not to see the into, it passes on. 
    shapes= ["star", "circle", "square", "triangle"] #player must choose one of these 4 options for 'shape'
    flag = True 
    while flag: # Name age and shape are assigned. 
        user.name = input("Before we start, what's your name? ")  
        user.age = input(f"\nGreat to see you {user.name.title()}. How old are you? ")
        user.shape = input("\nPerfect! Now you can choose your shape; either star, triangle, circle or square: ")
        while user.shape.lower() not in shapes:
                print("Sorry, you need to choose star, circle, square or triangle.")
                user.shape = input("Choose your shape: ")
        flag = False 
    clear_screen()
    table = [["Player name", user.name.title()],["Player age", user.age],["Player shape", user.shape]] # a table is made to show their details 
    print(tabulate(table, tablefmt= "pretty"))
    bonus(user.shape) #passes shape through bonus to see what bonus they get depending on which shape they chose 

    # Checks if user has a spade already or not, as the circle option lets them start with one. 
    # If so, they get the option of visiting the owl or going to add-land. 
    if "spade" in items:  
        print("As you already have a spade you can go straight to Add-Land\n")
        time.sleep(2)
        print("Before you go, if you want to you can visit the Wise-Owl and try and win some extra coins along the way?\n")
        time.sleep(2)
        visit = input(f"You have {user.coins} at the moment, enter 'visit to visit the owl or 'n' to go straight to Add-land: ")
        answers = ["visit", "n"]
        while visit not in answers: 
            visit= input("Sorry, you need ot enter 'visit' or 'n': ")
        if visit == "visit":
            print(f"You decide to visit the owl first.")
            time.sleep(2)
            clear_screen()
            owl()
            time.sleep(2)
            print("You finish with the owl and head straight to Add-land.")
            time.sleep(2)
            clear_screen()
            add_land() 
        else:
            print(f"You decide to leave the owl for now and go straght over to Add-land") 
            time.sleep(2)
            clear_screen()
            add_land()
    # if they dodn't start with a spade, they can use their coins to buy one or go to the owl to win more coins first. 
    else:           
        answers = ["c", "o"] 
        print(f"You need a spade before you can get anywhere.\n")
        time.sleep(2)
        print(f"You have {user.coins} gold coins. A spade will cost you 2 coins.\n")
        time.sleep(2)
        print("You can use your coins or visit the Wise-Owl to try and win some more.")
        time.sleep(2)
        choice_1= input("Enter 'c' if you want to use your coins or 'o' to visit the Wise-Owl: ")
        while choice_1 not in answers:
            print("Sorry you need to enter 'c' to use your coins or 'o' to visit the owl.")
            choice_1= input("Enter 'c' to use your coins or 'o' to visit the Wise-Owl: ")
        if choice_1.lower() == "c":
            user.coins -= 2 #if they choose 'c' they use two coins to purchase a spade 
            items.append("spade") #they now have a spade
            print(f"You used your coins to buy a spade! You have {user.coins} coins left. Lets go to Add_land!\n")
            time.sleep(2)
            clear_screen()
            add_land()
        else:           #if they don't choose option 'c' it defaults to option 'o' and they visit the owl. 
            print("Great, let's go see the owl!\n")
            time.sleep(2)
            clear_screen()
            owl()
            # if they win at the owl, it says well done they automatically buy the spade for two coins. Then add_land() is called 
            if user.result == "win":
                print("Well done for winning! You can buy a spade!\n")
                user.coins -= 2 
                items.append("spade")
                time.sleep(2)
                print (f"You spent 2 coins on a spade, you have {user.coins} coins left\n")
                time.sleep(2)
                print("Lets get going to Add-Land!\n")
                time.sleep(2)
                clear_screen()
                add_land() 
            # if they don't win at the owl, it says sorry and they automatically buy the spade for two coins. The add_land is called 
            else: 
                print("Sorry you didn't win. As you know you need to buy a spade to getet going, so that will cost you 2 gold coins\n")
                user.coins -= 2 
                items.append("spade") 
                time.sleep(2)
                print(f"You bought a spade and have {user.coins} left! Now you  can tunnel to Add-Land!\n")
                time.sleep(2)
                clear_screen()
                add_land()  

# If they choose to load a previous game, the name, places, items, coins and tries are loaded from the last game. 
# Places is looked at to see where they have already been and based on that they start at the next place. 
# If they choose to load a game but have never previously played, they start at add-land and are asked to enter their name 
# They are given 5 coins and 3 tries to start with.
else: 
    name= save_load.load_name()
    places = save_load.load_places()
    items = save_load.load_items()
    coins = save_load.load_coins()
    tries = save_load.load_tries()
    fountain_water = save_load.load_fountain()
    #If they have never played 
    if "add-land" not in places:
        if name =="":
            user_name = input("Hi! Please enter your name: ")
        else:
            user_name = name
        if tries == "":
            print("You get to start again with 3 trys!")
            user_tries = 3
        else:
            user_tries = int(tries) 
        if coins == "":
            print("You get to start with 5 gold coins to get going.")
            user_coins = 5 
        else: 
            user_coins = int(coins)
        if fountain_water =="":
            fountain_water= 0 
        else:
            fountain_water = int(fountain_water)
        user= Character(user_tries, user_coins)
        user.name = name 
        table = [["Player name", user.name.title()],["Coins", user.coins],["Tries", user.tries]]
        print(tabulate(table, tablefmt= "pretty"))
        print(f"Welcome {user.name.title()}! Your next destination is Add-land. You will start this game with{user.coins} coins and {user.tries} tries.\n")
        time.sleep(5)
        print("Let's get going!\n")
        time.sleep(3)
        clear_screen()
        add_land()
    # If they saved and quit after Add-land, they will start at sub-land. 
    elif "sub-land" not in places:
        if name =="":
            user_name = input("Hi! Please enter your name: ")
        else:
            user_name = name
        if tries == "":
            print("You get to start again with 3 trys!")
            user_tries = 3
        else:
            user_tries = int(tries) 
        if coins == "":
            print("You get to start with 5 gold coins to get going.")
            user_coins = 5 
        else: 
            user_coins = int(coins)
        if fountain_water =="":
            fountain_water= 0 
        else:
            fountain_water = int(fountain_water)
        user= Character(user_tries, user_coins)
        user.name = name 
        table = [["Player name", user.name.title()],["Coins", user.coins],["Tries", user.tries]]
        print(tabulate(table, tablefmt= "pretty"))
        print(f"Welcome back {user.name.title()}! Your next destination is Sub-land. From your previous game you have {user.coins} coins and {user.tries} tries.\n")
        time.sleep(5)
        print("Let's get going!\n")
        time.sleep(3)
        clear_screen()
        sub_land()
    # If they saved and quit after sub-land, they start at Div-land 
    elif "div-land" not in places:
        if name =="":
            user_name = input("Hi! Please enter your name: ")
        else:
            user_name = name
        if tries == "":
            print("You get to start again with 3 trys!")
            user_tries = 3
        else:
            user_tries = int(tries) 
        if coins == "":
            print("You get to start with 5 gold coins to get going.")
            user_coins = 5 
        else: 
            user_coins = int(coins)
        if fountain_water =="":
            fountain_water= 0 
        else:
            fountain_water = int(fountain_water)
        user= Character (user_tries, user_coins)
        user.name = name
        table = [["Player name", user.name.title()],["Coins", user.coins],["Tries", user.tries]]
        print(tabulate(table, tablefmt= "pretty"))
        print(f"Welcome back {user.name.title()}! Your next destination is Div-land. From your previous game you have {user.coins} coins and {user.tries} tries.\n")
        time.sleep(5)
        print("Let's get going!\n")
        time.sleep(3)
        clear_screen()
        div_land()
    #If they saved and quit after Div-land, they sart at Mult-land. 
    else:
        if name =="":
            user_name = input("Hi! Please enter your name: ")
        else:
            user_name = name
        if tries == "":
            print("You get to start again with 3 trys!")
            user_tries = 3
        else:
            user_tries = int(tries) 
        if coins == "":
            print("You get to start with 5 gold coins to get going.")
            user_coins = 5 
        else: 
            user_coins = int(coins)
        if fountain_water =="":
            fountain_water= 0 
        else:
            fountain_water = int(fountain_water)
        user= Character(user_tries, user_coins)
        user.name = name
        table = [["Player name", user.name.title()],["Coins", user.coins],["Tries", user.tries]]
        print(tabulate(table, tablefmt= "pretty"))
        print(f"Welcome back {user.name.title()}! Your next destination is Mult-land. From your previous game you have {user.coins} coins and {user.tries} tries.\n")
        time.sleep(5)
        print("Let's get going!\n")
        time.sleep(3)
        clear_screen()
        mult_land()
