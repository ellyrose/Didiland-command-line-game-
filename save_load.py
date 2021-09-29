# The funciton below saves the data. 
# It takes the argumenets 'username', 'places', 'items', 'coins', 'tries' and 'water'
# As places and items are lists, they are saved by joining the elements in each list separated by a comma. 
# As coins, tries and water are ints, they are converted into and saved as strings. 
# As user name is a string, it is written directly as a string 
# Each element has a title, and is saved underneath the relevent title so that when the load function is called, it can use the title 
# to identify the relevent information to be loaded. 



def save(username, places, items, coins, tries, water):
    with open("save_please.txt", "w") as file_object:
        file_object.write("name\n")
        file_object.write(username + "\n")
        file_object.write("visited\n")
        join_place = ",".join(places)
        join_place += "\n"
        file_object.write(join_place)
        file_object.write("items\n")
        join_it = ",".join(items)
        join_it += "\n"
        file_object.write(join_it)
        file_object.write("coins\n")
        num_coins = str(coins)
        num_coins += "\n"
        file_object.write(num_coins)
        file_object.write("tries\n")
        num_trys = str(tries)
        num_trys += "\n"
        file_object.write(num_trys)
        file_object.write("fountain\n")
        amount_water = str(water)
        amount_water += "\n"
        file_object.write(amount_water)
    file_object.close()



# The functions below load previous data from the save_please.txt file. 
# For 'name'it saves it as a string. 
#'items' and 'places' are loaded as lists
# Tries coins, and fountain water are saved as a string. 
# For each function, the title is found and then the next line of information is selected and assigned to the variable to be manipulated. 


def load_name():
    with open(f"save_please.txt") as file_object:
        lines = file_object.readlines()
    lines = list(lines)
    name = ""
    read_name = False
    for line in lines: 
        line = line.strip()
        if read_name:
            name = line                            
            read_name= False    

        if line == "name":
            read_name = True
    return name  


def load_items():
    with open(f"save_please.txt") as file_object:
        lines = file_object.readlines()
    lines = list(lines)
    items= []
    read_items = False
    for line in lines:
        line = line.strip()
        if read_items:
            items = line.split(",")
            read_items = False 
        
        if line == "items":
            read_items = True

    return  items 

def load_places():
    with open(f"save_please.txt") as file_object:
        lines = file_object.readlines()
    lines = list(lines)
    places = []
    read_place = False
    for line in lines:
        line = line.strip()
        if read_place:
            places = line.split(",")
            read_place = False

        if line == "visited":
            read_place = True

    return places 

def load_coins():
    with open(f"save_please.txt") as file_object:
        lines = file_object.readlines()
    lines = list(lines)
    coins = ""
    read_coins = False
    for line in lines: 
        line = line.strip()
        if read_coins:
            coins = line                            
            read_coins= False    

        if line == "coins":
            read_coins = True
    return coins     

def load_tries():
    with open(f"save_please.txt") as file_object:
        lines = file_object.readlines()
    lines = list(lines)
    tries = ""
    read_tries = False
    for line in lines:
        line = line.strip()
        if read_tries:
            tries = line 
            read_tries = False

        if line == "tries":
            read_tries = True
    return tries  

def load_fountain():
    with open(f"save_please.txt") as file_object:
        lines = file_object.readlines()
    lines = list(lines)
    fountain = ""
    read_fount = False
    for line in lines:
        line = line.strip()
        if read_fount:
            fountain = line
            read_fount = False

        if line == "fountain":
            read_fount = True
    return fountain    

