import time
import random
import subprocess
from termcolor import colored, cprint
from tabulate import tabulate
import sys

# ---------- Game State ----------
inventory = []
found_keys = False

# ---------- Utility Functions ----------
def clear_screen():
    subprocess.run("clear", shell=True, check=True)

def fancy_title(text):
    subprocess.run(f"figlet {text} | lolcat --force", shell=True, check=True)

def slow_print(text, color, delay=2):
    print(colored(text, color))
    time.sleep(delay)

def print_table(data, headers):
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

def neon_text(text, color="cyan", repeat=5, delay=0.1):#copiesd from gpt 3.5 do not make fun of it

    for i in range(repeat):
        sys.stdout.write("\r" + colored(text, color, attrs=["bold"]))
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write("\r" + " " * len(text))
        sys.stdout.flush()
        time.sleep(delay)
    print(colored(text, color, attrs=["bold"]))    

# ---------- Game Events ----------
def try_to_leave():
    gibberish = [
        "ThE dOorS wOn'T oPeN...",
        "YoU cAn'T lEaVe yEt...",
        "tHeY'rE cOmIng...",
        "sTaY wItH uS...",
        "(Strange Stares from back)"
    ]
    print(colored(random.choice(gibberish), "red"))

def call_employee():
    responses = [
        "Help is not available at the moment.",
        "Please remain calm.",
        "We're all out of exits today.",
        "Employee not found. Try again.",
        "Employee is missing"
    ]
    print(colored(random.choice(responses), "yellow"))

def keys_event():
    global found_keys
    found_keys = True
    print(colored("\n[You hear loud banging from the front door...]", "light_red"))
    time.sleep(2)
    print(colored("You rush towards it.", "light_blue"))
    time.sleep(2)
    print(colored("You hear someone crying...", "light_red"))
    print(colored("\nDo you want to try opening the door?", "yellow"))
    print("[1] Yes, open it!")
    print("[2] No, stay away.")

    choice = input("> ")
    if choice == "1":
        thedoor()
    else:
        print(colored("\nYou step back... maybe it's safer not to open it.", "light_yellow"))

def door_event():
    print(colored("\nYou approach the door again...", "light_cyan"))
    time.sleep(2)
    print(colored("\n Its locked.", "light_red"))
    time.sleep(2)
    print(colored("\nYou hear whispers from outside...", "magenta"))
    time.sleep(2)
    slow_print("\nDo you want to open it .", "yellow")
    print(colored("[1] Yes,open it!","light_magenta"))
    print(colored("[2] No, stay away.","light_yellow"))
    print()
    choice = input("> ")
    if choice == "1":
        thedoor()
    else:
        print(colored("\nYou step back... maybe it's safer not to open it.", "light_yellow"))



# ---------- Inventory ----------
def show_inventory():
    if inventory:
        table = [[item] for item in inventory]
        print("\n🛒 Your Inventory:")
        print_table(table, ["Items"])
    else:
        cprint("\nYour inventory is empty...", "blue")



# ---------- Item Handling ----------
def pick_item(items):
    # Filter out already collected items
    available_items = [item for item in items if item not in inventory]

    if not available_items:
        print(colored("\nYou've already collected everything here.", "light_yellow"))
        return

    print("\nYou see:")
    table = [[i + 1, available_items[i]] for i in range(len(available_items))]
    print_table(table, ["Option", "Item"])
    choice = input("> ")

    try:
        selected_item = available_items[int(choice) - 1]
        inventory.append(selected_item)
        print(f"\nYou picked up: {selected_item}")

        if selected_item.lower() == "keys":
            keys_event()

    except (ValueError, IndexError):
        print("You reach out... but there's nothing there...")

# ---------- Area Selection ----------
def choose_section():
    global found_keys
    sections = ["Electronics", "Food", "Toys"]
    if found_keys:
        sections.append("The Door")

    print("\nWhere do you want to go?")
    table = [[i+1, sections[i]] for i in range(len(sections))]
    print_table(table, ["Option", "Section"])
    choice = input("> ")

    if choice == "1":
        pick_item(["Old TV", "Broken Laptop", "Static Radio", "Ps5", "Keys"])
    elif choice == "2":
        pick_item(["Rotten Apple", "Stale Bread", "Creepy Candy"])
    elif choice == "3":
        pick_item(["Haunted Doll", "Broken Toy Car", "Torn Teddy Bear"])
    elif choice == "4" and found_keys:
        door_event()
    else:
        print("You wandered into darkness... Nothing here.")
def thedoor():

    slow_print("\n(You slowly unlock the door... A freezing wind blows in. You see a shadow move outside...)", "light_magenta")
    slow_print("\nNew area unlocked: The StoreRoom!", "cyan")
    slow_print("\nThere is a girl standing there covered in wires.", "blue")
    slow_print("\n Do you want to go ","blue")
    slow_print("[1] Yes","red")
    slow_print("[2] No","yellow")
    choice = input("> ")
    if choice == "1":
             slow_print("You were teleported outside and ran back to the car and drove aways","green")
             time.sleep(3)
             subprocess.run("clear",shell=True,check=True)
             subprocess.run("figlet THANKS FOR PLAYING | lolcat --force  ",shell=True,check=True)
             subprocess.run("exit",shell=True,check=True)
    elif choice == "2":
             neon_text("you are teleported it back room")
             time.sleep(3)
             subprocess.run("clear",shell=True,check=True)
             subprocess.run("figlet THANKS FOR PLAYING | lolcat --force  ",shell=True,check=True)
             subprocess.run("exit",shell=True,check=True)
    else:
            subprocess.run("exit",shell=True,check=True)

# ---------- Game Intro ----------
def game_intro():
    clear_screen()
    fancy_title("SERIAL EXPERIMENT LAIN")
    print()
    slow_print("It's raining outside and you're alone on the road.\n", "red")
    slow_print("You're hungry, and BAM!\n", "light_magenta")
    slow_print("You see a supermarket and go in.\n", "light_yellow")
    slow_print("It's pretty empty for a supermarket... but you don't care.\n", "light_blue")
    slow_print("Still... you get a strange feeling.", "red")

    clear_screen()
    fancy_title("Super Mart")
    slow_print('An employee standing by the door says:\n', "magenta")
    slow_print('"Welcome... why are you here? No one comes here anymore."\n', "yellow")
    player_response = input(colored("ANSWER: ", "light_blue"))
    slow_print(f'"{player_response}?" the employee mutters. "Strange..."', "yellow")
    print()
    slow_print('"Well, I don\'t care..." [Employee whispers] "Call me... if you dare."', "yellow")

# ---------- Game Loop ----------
def main():
    game_intro()
    while True:
        cprint("\nWhat do you want to do?", "light_blue")
        options = [
            ["1", "Wander to a section"],
            ["2", "Try to leave"],
            ["3", "Call the employee"],
            ["4", "Check your inventory"],
            ["5", "Quit"],
        ]
        print_table(options, ["Option", "Action"])

        choice = input("> ")

        if choice == "1":
            choose_section()
        elif choice == "2":
            try_to_leave()
        elif choice == "3":
            call_employee()
        elif choice == "4":
            show_inventory()
        elif choice == "5":
            print("\nThanks for playing... if you can ever leave... 🕷️")
            break
        else:
            print("\nConfused... you stand still...")

if __name__ == "__main__":
    main()
