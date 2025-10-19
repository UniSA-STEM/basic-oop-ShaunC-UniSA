"""
File: main.py
Description: This contains the main program logic for 'Into the Grid'.
Author: Shaun Cantley
ID: cansy012@mymail.unisa.edu.au
Username: cansy012
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# Imports
from Asset import CryptoToken, DataSpike, SecurityChip, HardwarePatch, RemovableDrive
from Rig import Rig
import Hacker
import random
import time

def play(hacker, other_players):
    """Starts a new game of Into the Grid."""
    running = True
    turn_number = 1
    all_players = [hacker] + other_players  # List to manage turns

    while running:
        print(f"\n--- Turn {turn_number} ---\n")
        for player in all_players:
            action_success = False  # Reset for each player's turn
            if player == hacker:
                title = f"*** Okay {player.name}, how should we proceed? ***"
                options = [
                    "1: Acquire Rig",
                    "2: Upgrade Rig",
                    "3: Repair Rig",
                    "4: Spike Player",
                    "5: Deploy HoneyPot",
                    "6: Attempt Asset Extraction",
                    "7: Encrypt Asset",
                    "",
                    "I: View Inventory",
                    "S: Show Status",
                    "Q: Exit Game"
                ]

                # Player menu formatting
                width = max(len(title), *(len(option) for option in options)) + 8
                print("+" + "-" * width + "+")
                print("|" + title.center(width) + "|")
                print("|" + "-" * width + "|")
                for option in options:
                    print("| " + option.ljust(width - 2) + " |")
                print("+" + "-" * width + "+")

                choice = input("Choose an action: ").lower()

                if choice == "1" and hacker.rig != True: # Acquire Rig
                    if player.crypto_tokens != 0:
                        print("You have activated a rig! Commencing network scan...")
                        player.acquire_rig()
                        action_success = True
                    else:
                        print("You need a Rig and CryptoToken to do that.")

                elif choice == "2": # Upgrade Rig
                    if player.rig == True and hacker.hardware_patch != 0:
                        player.upgrade_rig()
                        action_success = True
                    else:
                        print("You need a Rig and HardwarePatch to do that.")

                elif choice == "3": # Repair Rig
                    if player.rig and hacker.hardware_patch != 0:
                        player.upgrade_rig()
                        action_success = True
                    else:
                        print("You need a Rig and CryptoToken to do that.")

                elif choice == "4": # Spike Attack
                    if player.rig:
                        print("Valid targets:")
                        for i in range(len(other_players)):
                            print(f"{i + 1}) {other_players[i].name}")
                        target_index = int(input("Choose target (number): ")) - 1
                        target = other_players[target_index]
                        player.launch_data_spike(target)
                        player.trace_level += 1
                        action_success = True
                    else:
                        print(f"{player.name} needs a Rig to send a spike.")

                elif choice == "5": # Honeypot Defence
                    if player.security_chip >= 1 and player.inventory:
                        player.deploy_honeypot()
                        player.CryptoToken -= 1
                        action_success = True
                    else:
                        print(f"{player.name} needs a CryptoToken to do that.")

                elif choice == "4": # Encrypt Asset
                    if player.security_chip >= 1 and player.inventory:
                        print("Select an item to encrypt:", ", ".join(player.inventory))
                        player.upgrade_rig()
                        player.security_chip -= 1
                        action_success = True
                    else:
                        print("Cannot encrypt. Either no SecurityChip or inventory is empty.")


                elif choice == "i":
                    if player.inventory:
                        print(f"--- {player.name}'s Inventory ---")
                        for item in player.inventory:
                            print(item)
                    else:
                        print("\n\nThere's nothing in your inventory right now")
                    if player.rig:
                        if player.rig.UnencryptedStorage:
                            print(f"--- {player.name}'s Rig Inventory ---")
                            for item in player.rig.UnencryptedStorage:
                                print(item)
                        else:
                            print("There's nothing in rig storage\n\n")

                elif choice == "s":
                    print(f"\n\n{player.name}'s Status:")
                    print(f"\nYour current trace Level is: {player.trace_level}")
                    if player.rig:
                        print(f"You have a rig in your possession")
                    else:
                        print(f"You don't have a Rig at the moment")


                elif choice == "q":
                    print("Exiting game...")
                    action_success = True
                    running = False
                else:
                    print("Invalid choice. Try again.")

            else: # AI's turns
                while not action_success:
                    actions = [] # Uses validation to build a list of valid AI actions this turn
                    if player.crypto_tokens != 0:
                        actions.append("acquire a rig")
                    if player.rig:
                        actions.append("spikes player")
                        actions.append("encrypts an asset")
                        actions.append("deploys a honeypot")
                        actions.append("upgrades their rig")
                    action = random.choice(actions) # Simulates AI player choice by picking a random valid action
                    if action == "acquire a rig":
                        player.acquire_rig()
                        action_success = True
                    elif action == "spikes player":
                        valid_targets = [p for p in all_players if p is not player]
                        target = random.choice(valid_targets)
                        player.trace_level += 1
                        player.launch_data_spike(target)
                        action_success = True
                    elif action == "encrypts an asset":
                        player.encrypt_assets()
                        action_success = True
                    elif action == "upgrades their rig":
                        player.upgrade_rig()
                        action_success = True
                    elif action == "deploys a honeypot":
                        player.deploy_honeypot()
                        action_success = True

        if running and action_success:  # End of turn summary
            print(f"\nEnd of turn {turn_number}\n\n")
            turn_number += 1
            for player in other_players:  # All players get a new random asset at end of turn
                Rig.give_random_asset(player, hacker)
                header = f"{player.name}'s Actions"
                print("+" + "-" * width + "+")
                print("|" + header.center(width) + "|")
                print("|" + "-" * width + "|")
                print(f"| {player.name} chooses to {action}".ljust(width) + " |")
                print(f"| {player.name} added an item to their inventory".ljust(width) + " |")
                print("+" + "-" * width + "+")
                time.sleep(1)

    print("\nGrid offline! Thanks for playing.")

def test_mode():
    """A variety of tests to show how various elements work"""
    title = "*** Into the Grid: Test Mode ***"
    options = [
        "1: Asset encrypt/decrypt validator",
        "2: View player inventories",
        "3: Encrypt without Security Chip",
        "4: Upgrading rigs",
        "Q: Return to Main Menu"]

    # Test menu format
    print("\n" * 20)
    width = max(len(title), *(len(option) for option in options)) + 47
    print("+" + "-" * width + "+")
    print("|" + title.center(width) + "|")
    print("|" + "-" * width + "|")
    for option in options:
        print("| " + option.ljust(width - 2) + " |")
    print("+" + "-" * width + "+")
    choice = input("Select an option: ").lower()

    if choice == "1":
        # Test: Asset encryption/decryption
        asset_classes = [CryptoToken, DataSpike, RemovableDrive, SecurityChip, HardwarePatch]
        random_asset_class = random.choice(asset_classes)
        # Instantiate random asset
        test = random_asset_class()
        print("\nCreated Asset:")
        print(test)
        print("\nEncrypt Asset:")
        test.encrypt()
        print(test)
        print("\nDecrypt Asset:")
        test.decrypt()
        print(test)
        input("\nTest Successful! Press Enter to continue...")
        test_mode()

    elif choice == "2":
        # Test: View simulated inventory
        hacker1 = Hacker.Hacker("Hacker1")
        hacker1.acquire_rig()
        Rig.give_random_asset(hacker1, hacker1)  # give hacker1 a random asset
        hacker2 = Hacker.Hacker("Hacker2")
        hacker2.acquire_rig()
        Rig.give_random_asset(hacker2, hacker2)  # give hacker2 a random asset
        all_players = [hacker1, hacker2]
        for player in all_players:
            print(f"\n--- {player.name}'s Inventory ---")
            for item in player.inventory:
                print(item)
            if player.rig:
                print(f"\n--- {player.name}'s Rig Inventory ---")
                for item in player.rig.UnencryptedStorage:
                    print(item)
                for item in player.rig.EncryptedStorage:
                    print(item)
        input("\nTest Successful! Press Enter to continue...")
        test_mode()

    elif choice == "3":
        # Test: Upgrading rigs

        input("\nTest Successful! Press Enter to continue...")
        test_mode()

    elif choice == "q":
        # Quit to main menu
        print("\n" * 20)
        main()

    else:
        print("Invalid choice. Try again.")
        test_mode()

def main():
    """Into the Grid Main Menu"""
    title = "*** Into the Grid ***"
    options = ["P: Play", "T: Test Mode", "Q: Quit"]
    names_list = ["Neo", "Boris", "Ghost", "Shadow", "Trinity", "Stanley", "Angela", "Gabriel", "ZeroCool", "AcidBurn"]

    # Game menu formatting
    width = max(len(title), *(len(option) for option in options)) + 50
    print("\n" * 20)
    print("+" + "-" * width + "+")
    print("|" + title.center(width) + "|")
    print("|" + "-" * width + "|")
    for option in options:
        print("| " + option.ljust(width - 2) + " |")
    print("+" + "-" * width + "+")
    choice = input("Select an option: ").lower()

    # Start game
    if choice == "p":
        name = input("Enter the player name (or press Enter to pick randomly): ").strip()
        if not name:
            name = random.choice(names_list)
        hacker = Hacker.Hacker(name) # Create the player hacker with the chosen name
        print("\nGrid online!\nYou are now in the Grid.\n") # Opening sequence
        print(f"Welcome, {hacker.name}. You are now in a digital realm where code shapes reality"
              f" and every connection pulses with possibility.\nHere, the lines between the virtual and the real blur,"
              f" and only those who can navigate its layers survive.\nThis isn't only a network- it is a living system,"
              f"a constantly shifting matrix where data is power and hackers are kings.\n"
              f"Remember, all your choices ripple across the grid- so step carefully- your journey begins now...\n")
        input("Press Enter to continue...\n")

        # Create three other unique players
        remaining_names = [n for n in names_list if n != name]
        hacker2 = Hacker.Hacker(random.choice(remaining_names))
        remaining_names.remove(hacker2.name)
        hacker3 = Hacker.Hacker(random.choice(remaining_names))
        remaining_names.remove(hacker3.name)
        hacker4 = Hacker.Hacker(random.choice(remaining_names))
        remaining_names.remove(hacker4.name)
        other_players = [hacker2, hacker3, hacker4]

        # Game starting dialogue
        print(f"*** ALERT ***")
        print(f"We have detected other hackers in the network!")
        print(f"NetDOX protocols have confirmed the presence of {hacker2.name}, {hacker3.name} and {hacker4.name}")
        print(f"The system is online and awaits your command.")
        input("\nPress Enter to continue...")
        play(hacker, other_players)

    # Test mode checks game functions and shows output
    elif choice == "t":
        test_mode()
    elif choice == "q":
        print("Thanks for playing!\nSee you next time.")
        quit()
    else:
        print("Invalid input.")
        time.sleep(1)
        main()

if __name__ == "__main__":
    main()