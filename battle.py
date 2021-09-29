from random import choice 
from random import randint
import time 
from clear import clear_screen

# The question class has three attributes, question, answer and damage. 
# The damage indicates how many knowledge points it will know off the enemy is the player gets it correct. 

class Question:

    def __init__(self, question, answer, damage):
        self.question= question 
        self.answer = answer
        self.damage = damage 


# This is the framwork of a battle. It leads to the normal_battle function, the cal_battle function or the goldcal_battle 
# function, depending on the player's choices. 

def battle (user, enemy, question, calquestion, items):
    answer1 = input(question.question)
    if answer1.isdecimal() == False:                 # This if statement ensures the player enters a number as an answer. 
        while answer1.isdecimal() == False:
            print("Sorry, you must enter a number.")
            answer1 = input(question.question)
    else:
        pass
    answer1 = int(answer1)                          # The str digit is converted to an int so that it can be compared with the answer
    if user.tries > 0:                              # If they haven't run out of tries 
        if answer1 != question.answer:              # If they get the quesiton wrong
            user.tries -= 1                         # They have one try less 
            print(f"That was wrong!! You have {user.tries} tries left\n")
            if user.coins >= enemy.coins:           # If they have enough coins, they can choose to use the calculator 
                print(f"You have {user.coins} coins and can use the calculator if you need.\n")
                print(f"It will cost {enemy.coins} coins to use it.\n")
                help = input("Enter y to use the calculator on n to continue: ")
                options = ["y", "n"]
                while help.lower() not in options:
                    print("You must choose 'n' or 'y'")
                    help= input("Enter 'y' to user the calculator or 'n' to continue: ")
                if help == 'y':                     # If they choose yes they go to the calculator 
                    time.sleep(2)
                    clear_screen()
                    cal_battle(user, enemy, calquestion)
                else:
                    print("Ok, we'll carry on")     # If they pick 'n' they continue without help and normal_battle is called 
                    time.sleep(2)
                    normal_battle(user, question, enemy)
            elif "Golden Calculator" in items :     # If they dont have any coins but they get a question wrong, then  
                print(f"You can use the golden calculator if you need!\n")  # if they have the gold cal they get the chance to use it 
                help = input("Enter y to use the golden calculator on n to continue: ")
                options = ["y", "n"]
                while help.lower() not in options:
                    print("You must choose 'n' or 'y'")
                    help= input("Enter 'y' to user the calculator or 'n' to continue: ")
                if help == 'y':                      # If they choose yes the gold_cal funciton is called 
                    time.sleep(2)
                    clear_screen()
                    goldcal_battle(user, enemy, calquestion,items)
                else:
                    print("Ok, we'll carry on") # If they pick no they continue without help
                    time.sleep(2)
                    normal_battle(user, question, enemy)
            else:
                normal_battle(user, question, enemy)
        else:
            print("That's right!")
            enemy.knowledge -= question.damage
            user.result ="win"    
    else:
        user.die(enemy) #if they get it wrong the program ends 
        user.result = "lose"



# this battle function is called if they don't use the calculator or the gold calculator, so is a 'normal battle'

def normal_battle(user, question, enemy):
    answer1 = input(question.question)
    if answer1.isdecimal() == False:
        while answer1.isdecimal() == False:
            print("Sorry, you must enter a number.")
            answer1 = input(question.question)
    else:
        pass
    answer1 = int(answer1)
    if user.tries > 0:
        while answer1 != question.answer:   # This loop runs every time they enter a wrong answer, unless they run out of tries. 
            user.tries -= 1                 # They have one try less 
            print(f"That was wrong!! You have {user.tries} tries left\n") 
            if user.tries == 0:
                user.die(enemy)             # If they run out of tries, the program ends 
                user.result = "lose"
                return
            else:
                answer1 = input(question.question)
                if answer1.isdecimal() == False:
                    while answer1.isdecimal() == False:
                        print("Sorry, you must enter a number.")
                        answer1 = input(question.question)
                else:
                    pass
                answer1 = int(answer1)
        print("That's right!")
        enemy.knowledge -= question.damage
        user.result ="win"
    else:
        user.die(enemy) #if they get it wrong the program ends 
        user.result = "lose"



# If they use the caculator, this function is called. The player coins are reduced by the price it costs to use the calculator against the 
# Org they are fighting 

def cal_battle(user, enemy, calquestion):
    user.coins -= enemy.coins
    print(f"You have {user.coins} coins remaining!\n")
    time.sleep(2)
    all_cal_battle(user,  enemy, calquestion)



 # If they use the gold calculator, this function is called. The calculator is removed from their item list and an empty case is added, 
 # This means they wont get the chance to be given it again.    

def goldcal_battle(user, enemy, calquestion,items):
    items.remove("Golden Calculator")
    items.append("Empty Calculator Case")
    all_cal_battle(user, enemy, calquestion)


    
# This function is used for both calculator battles. An easier question is generated and used. 

def all_cal_battle(user, enemy, calquestion):
    print("Here's an easier question\n")
    answer2 = input(calquestion.question)
    if answer2.isdecimal() == False:
        while answer2.isdecimal() == False:
            print("Sorry, you must enter a number.")
            answer2 = input(calquestion.question)
    else:
        pass
    answer2 = int(answer2)
    if user.tries > 0:
        while answer2 != calquestion.answer:
            user.tries -= 1                     # They have one try less 
            print(f"That was wrong!! You have {user.tries} tries left\n") 
            if user.tries == 0:
                user.die(enemy)                 # If they get it wrong the program ends 
                user.result = "lose"
                return
            else:
                answer2 = input(calquestion.question)
                if answer2.isdecimal() == False:
                    while answer2.isdecimal() == False:
                        print("Sorry, you must enter a number.")
                        answer2 = input(calquestion.question)
                else:
                    pass
                answer2 = int(answer2)
        print("That's right!")
        enemy.knowledge -= calquestion.damage
        user.result ="win"
    else:
        user.die(enemy) #if they get it wrong the program ends 
        user.result = "lose"


# This function is called between each round until the Org loses all its knowledge points 

def next_round(enemy,user):
    print(f"You got through that round, but the {enemy.name} isn't defeated yet. They have {enemy.knowledge} knowledge points left.\n")
    time.sleep(2)
    print(f"You get an extra free try! Now you have {user.tries} tries and {user.coins} coins left.\n")
    time.sleep(2)
    print("Next round!\n")
    


# This generates an addition question, using the random integer generator 
# For a normal uestion, it generates a random number between 20 and 100. 
# For a calculator question, it generates a random number betwween  1 and 30 
# The numbers are passed into the Question class which creates a question and an answer. 

def add_question(): 
    num1 = randint(20,100)
    num2 = randint(20, 100)
    num3= randint(1,30)
    num4= randint(1,30)
    addquestion= Question(f"What is {num1} + {num2}?: ",num1 + num2, 2)
    addquestion_cal= Question(f"What is {num3} + {num4}?: ",num3 + num4, 1)
    time.sleep(2)
    return addquestion, addquestion_cal

# This does the same as the above funciton, but generates a subtraction question. 

def sub_question(): 
    num1 = randint(80,120)
    num2= randint(20,79)
    num3= randint(20,50)
    num4= randint(1,19)
    subquestion= Question(f"What is {num1} - {num2}?: ",num1-num2, 2)
    subquestion_cal= Question(f"What is {num3} - {num4}?: ",num3-num4, 1)
    time.sleep(2)
    return subquestion, subquestion_cal

# This generates a division question 
# It used the 'choice' function from random to choose a number from a list
# This is to avoid giving the player a question that doesnt result in a whole number

def div_question(): 
    numbers0 = [80,96,128,144,160,176]
    numbers1 = [4,8,16]
    num1 = choice(numbers0)
    num2= choice(numbers1)
    numbers2 = [4,8,12,16,20, 24,28,32]
    numbers3= [2,4]
    num3= choice(numbers2)
    num4= choice(numbers3)
    divquestion= Question(f"What is {num1} / {num2}?: ",num1/num2, 2)
    divquestion_cal= Question(f"What is {num3} / {num4}?: ",num3/num4, 1)
    time.sleep(2)
    return divquestion, divquestion_cal

#This generates a multiplication question 

def mult_question(): 
    num1 = randint(5, 20)
    num2= randint(5,20)
    num3= randint(1,10)
    num4= randint(1,10)
    multquestion= Question(f"What is {num1} x {num2}?: ",num1*num2, 2)
    multquestion_cal= Question(f"What is {num3} x {num4}?: ",num3*num4, 1)
    time.sleep(2)
    return multquestion, multquestion_cal


