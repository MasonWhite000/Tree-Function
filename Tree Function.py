import time
soil = True
soil_nutrients = True
oxygen = True 
sunlight = True 
tree_type = input("What type of tree is it?: ")
tree_height = 33.8
branch_ammount = 45
branch_type = "low"
season = "fall"
age = 45

def Can_Live(soil, soil_nutrients, oxygen, sunlight, season):
    if all([soil, oxygen, sunlight, soil_nutrients]) and season.lower() in ["summer", "spring",]:
        print ("The Tree can live! Prepare for photosynthesis!!")
    else: 
        print ("The Tree cannot live! Prepare for hibernation!!")

def have_leaves(season):   
    if season.lower() in ["spring",]:
        print("The Tree is growing leaves!")
    elif season.lower in ["summer"]:
        print("The Tree has leaves!")
    elif season.lower() in ["fall", "autumn"]:
        print ("The leaves are changing color and dying!")
    else:
        print("The Tree doesn't have any leaves!")

def OorY(age):
    if age > 10:
        print ("The Tree is fairly old!")
    else:
        print ("The Tree is young!")
        
def bigORsmol(tree_height, branch_ammount):
    if tree_height > 15 and branch_ammount > 25:
        print("The Tree is large!")
    else:
        print("The tree is small.")

def can_climb(branch_type, branch_ammount, tree_height):
    if branch_ammount > 0:
        if branch_type.lower() in ["low"] and tree_height >= 10 and tree_height <= 25:
            print("The Tree is safe to climb! Climb away!")
        elif branch_type.lower() in ["low"] and tree_height < 10:
            print("The Tree isn't tall enough to climb!")
        elif branch_type.lower() in ["low"] and tree_height >= 10 and tree_height > 25:
            print("Be careful! The Tree is very tall, don't fall out!")
        elif branch_type.lower() in ["high", "tall"]:
            print("The branches are too high to reach!")
    else:
        print("There are no branches to climb!")

print ("Analyzing Tree data!!")
time.sleep(2)
Can_Live(soil, soil_nutrients, oxygen, sunlight, season)
time.sleep(1)
have_leaves(season)
time.sleep(1)
OorY(age)
time.sleep(1)
bigORsmol(tree_height, branch_ammount)
time.sleep(1)
can_climb(branch_type, branch_ammount, tree_height)
