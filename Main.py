"""
File: main.py
Description: This contains the main program logic for 'Into the Grid'.
Author: Shaun Cantley
ID: cansy012@mymail.unisa.edu.au
Username: cansy012
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# Imports
from Asset import CryptoToken, DataSpike, SecurityChip, HardwarePatch
from Hacker import Hacker
from Rig import Rig
import random

def play(hacker):
    """Starts a new game of Into the Grid."""
    running = True

    while running:
        # Player actions menu
        print("\n\n--- Main Menu ---\n")
        print("1. Acquire Rig")
        print("2. Launch Data Spike")
        print("3. Encrypt Asset")
        print("4. Upgrade Rig")
        print("5. View Inventory")
        print("6. Show Status")
        print("0. Exit Game\n")
        choice = input("Choose an action: ")

        if choice == "1":
            # Aquire a rig
            if hacker.crypto_tokens >= 1:
                hacker.acquire_rig()
            else:
                print("You need a CryptoToken to acquire a rig.")

        elif choice == "2":
            # Launch an attack
            if hacker.rig != None:
                print("You launch a Data Spike!")
                hacker.trace_level += 1
                print(f"Your spike is being traced!\n{hacker.name}'s trace level is now {hacker.trace_level}.")
            else:
                print("You need a rig before you can send a spike.")

        elif choice == "3":
            # Encrypt assets
            if hacker.security_chip >=1:
                hacker.encrypt_assets()
                if hacker.inventory != None:
                    print("Select an item from your inventory to encrypt:")
                    print(", ".join(hacker.inventory))
                    hacker.security_chip -= 1
                    print(f"Encryption complete!")
                else:
                    print("Your inventory is empty!")
            else:
                print("A security chip is needed to encrypt an You need a SecurityChip to encrypt an asset.")

        elif choice == "4":
            # Upgrade hacker rig
            if hacker.hardware_patch >= 1:
                hacker.upgrade_rig()
                print(f"Your rig has been upgraded!")
            else:
                print("You need a hardware patch to upgrade a rig.")

        elif choice == "5":
            # Views current inventory
            print("Inventory:", hacker.inventory)

        elif choice == "6":
            # Show player status
            print(f"Hacker: {hacker.name}")
            print(f"Trace Level: {hacker.trace_level}")

        elif choice == "0":
            print("Exiting game...")
            running = False

        else:
            print("Invalid choice. Try again.")

    else:
        print("Grid offline!")
        print("Thanks for playing the game")


def main():
    """Into the Grid Main Menu"""
    title = " *** Into the Grid *** "
    options = ["P: Play", "Q: Quit", "H: Help"]
    width = max(len(title), *(len(option) for option in options)) + 4
    names_list = ["Neo", "Boris", "Ghost", "Shadow", "Trinity"]


    print("+" + "-" * width + "+")
    print("|" + title.center(width) + "|")
    print("|" + "-" * width + "|")

    for option in options:
        print("| " + option.ljust(width - 2) + " |")

    print("+" + "-" * width + "+")

    choice = input("Select an option: ").lower()

    if choice == "p":
        # ask the user for a name, strip whitespace
        name = input("Enter the player name (or press Enter to pick randomly): ").strip()
        if not name:
            name = random.choice(names_list)

        # create the Hacker with the chosen name
        hacker = Hacker(name)
        print("\nGrid online!\nYou are now in the Grid.\n")
        print(f"Welcome, {hacker.name}. You are now in a digital realm where code shapes reality"
              f" and every connection pulses with possibility.\nHere, the lines between the virtual and the real blur,"
              f" and only those who can navigate its layers survive.\nThis isn't only a network- it is a living system,"
              f"a constantly shifting matrix where data is power and hackers are kings.\n"
              f"Remember, all your choices ripple across the grid- so step carefully- your journey begins now...\n")
        input("Press Enter to continue...\n")
        play(hacker)
    elif choice == "h":
        help() # TODO function
    elif choice == "q":
        quit()
    else:
        print("Invalid input.")

if __name__ == "__main__":
    main()