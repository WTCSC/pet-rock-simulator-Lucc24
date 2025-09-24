import sys
import time

def type_text(text, delay=0.4, pause=0):
    lines = text.split('\n')
    for line in lines:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print() 
        time.sleep(pause) 

rock_name = input("What is the name of your rock?: ").lower()

rage = 2
hunger = 3
health = 7
happiness = 7
mystery = 0

#ahahahaha dont worry about any of this just keep scrolling down haha

if rock_name =="chara":
    type_text("\n\n\n\n\nI wonder...?\n\n\n")
    rage = 8
    health = 5
    happiness = 5
    hunger = 8




if rock_name =="lucca":
    print("\n \n \n \n \ni dunno who that is but he seems like he is very cool and handsome\n \n \n")
    rage = 0
    health = 10
    happiness = 10
    hunger = 0
    


turns = 0
max_turns = 15



    
while True:
    if turns >= max_turns:
        print(f"\033[1mCongratulations! {rock_name} has survived for {max_turns} days! You win :)\033[0m")
        break
    if rock_name =="gaster":
        type_text("\n\n\n\n\nInteresting... very interesting\n\n\n")
        rage = '????'
        health = '????'
        happiness = '????'
        hunger = '????'
        print(f"\n{rock_name}'s stats:")
        print(f"Rage: {rage}")
        print(f"Hunger: {hunger}")
        print(f"Health: {health}")
        print(f"Happiness: {happiness}")
        type_text('try again')
        break
    print(f"\n{rock_name}'s stats:")
    print(f"Rage: {rage}")
    print(f"Hunger: {hunger}")
    print(f"Health: {health}")
    print(f"Happiness: {happiness}")
    
    action = input("\nWhat would you like to do? (feed, pet, throw, glue, quit): ").lower()
    
    if action == "feed":
        hunger -= 2
        happiness += 1
        print(f"You feed {rock_name}.")
    elif action == "pet":
        happiness += 2
        rage -= 1
        hunger += 2
        print(f"You pet {rock_name}. It seems happy.")
    elif action == "throw":
        rage += 3
        health -= 2
        happiness -= 1
        print(f"You throw {rock_name}. ouch.")
    elif action == "glue":
        health += 2
        rage += 3
        print(f"You glue {rock_name}. It seems to hold together better.")
    elif action == "soul":
        mystery += 2
        print(f"You examine {rock_name} closely. It ?????????????.")
    elif action == "quit":
        print("Thanks for playing!")
        break
    else:
        print("Invalid action. Please choose again.")

    hunger += 1
    health -= 1
    happiness -= 1
    rage -= 1
    turns += 1

    if hunger < 1:
        hunger = 0
        print(f"\n\n{rock_name} is full!")  
    if health < 1:
        health = 0
        print(f"\n\n{rock_name} has died of poor health. Game over.")
        break
    if happiness < 1:
        happiness = 0
        print(f"\n\n{rock_name} has died of sadness. Game over.")
        break
    if rage < 1:
        rage = 0
        print(f"\n\n{rock_name} is very calm.")
    if mystery < 1:
        mystery = 0
    if mystery > 5:
        print("\n\n\n\nhalfway there.\n\n\n\n")
    if hunger > 10:
        hunger = 10
        print(f"{rock_name} has died of starvation. Its \033[1msoul\033[0m seemed to leak from its body. \nGame over.")
        break

    if health > 10:
        health = 10
        print(f"\n\n{rock_name} is in perfect health!")

    if happiness > 10:
        happiness = 10
        print(f"\n\n{rock_name} is extremely happy!")

    if rage > 10:
        rage = 10
        print(f"\n\n{rock_name} is extremely angry. It has exploded. Game over.")
        break
    if mystery > 10:
        mystery = 10
        print("the rot consumes" * 500)
        break