"""
File: main.py
Description: This contains the main program logic for 'Into the Grid'.
Author: Shaun Cantley
ID: cansy012@mymail.unisa.edu.au
Username: cansy012
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# Imports
from Asset import Asset, CryptoToken, DataSpike, SecurityChip, HardwarePatch, RemovableDrive
from Hacker import Hacker
from Rig import Rig
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
                    "2: Spike Player",
                    "3: Deploy HoneyPot",
                    "4: Upgrade Rig",
                    "5: Encrypt Asset"
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
                if choice == "1": # Aquire Rig
                    if player.crypto_tokens != 0:
                        print("You have aquired a rig! Commencing network scan...")
                        player.acquire_rig()
                        action_success = True
                    else:
                        print(f"{player.name} needs a CryptoToken to acquire a rig.")
                elif choice == "2": # Attack
                    if player.rig is not None:
                        print(f"Select target:")
                        spike_player(self, target)
                        player.trace_level += 1
                        action_success = True
                    else:
                        print(f"{player.name} needs a rig to send a spike.")
                elif choice == "3": # Defend
                    if player.security_chip >= 1 and player.inventory:
                        player.deploy_honeypot()
                        player.CryptoToken -= 1
                        action_success = True
                    else:
                        print("You need a CryptoToken to deploy a HoneyPot!")
                elif choice == "4": # Encrypt Asset
                    if player.security_chip >= 1 and player.inventory:
                        print("Select an item to encrypt:", ", ".join(player.inventory))
                        player.upgrade_rig()
                        player.security_chip -= 1
                        action_success = True
                    else:
                        print("Cannot encrypt. Either no SecurityChip or inventory is empty.")
                elif choice == "5": # Upgrade Rig
                    player.upgrade_rig()
                    action_success = True

                elif choice == "i": # Shows player inventory and also rig inventory if player has a rig.
                    print(f"--- {player.name}'s Inventory ---")
                    if player.inventory:
                        for item in player.inventory:
                            print(item)
                    else:
                        print("There's nothing in your inventory right now")
                    if player.rig:
                        if player.rig.UnencryptedStorage:
                            print(item)
                        else:
                            print("There's nothing in rig storage")
                        print(f"--- {player.name}'s Rig Inventory ---")
                        for item in player.rig.UnencryptedStorage:
                            print(item)

                    play(hacker, other_players)

                elif choice == "s":
                    print(f"\n\n{player.name}'s Status:")
                    print(f"\nYour current trace Level is: {player.trace_level}")
                    if player.rig == True:
                        print(f"You have a rig in your posession")
                    else:
                        print(f"You don't have a Rig at the moment")
                    play(hacker, other_players)

                elif choice == "q":
                    print("Exiting game...")
                    running = False
                else:
                    print("Invalid choice. Try again.")
                    play(hacker, other_players)

            else: # AI's turns
                while not action_success:
                    actions = [] # Uses validation to build a list of valid AI actions this turn
                    if player.crypto_tokens != 0:
                        actions.append("acquire a rig")
                    if player.rig == True:
                        actions.append("spikes player")
                        actions.append("encrypts an asset")
                        actions.append("deploys a honeypot")
                        actions.append("upgrades their rig")
                    action = random.choice(actions) # Simulates AI player choice by picking a random valid action
                    if action == "acquire a rig":
                        player.acquire_rig()
                        action_success = True
                    elif action == "spikes player":
                        spike_player(target)
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
            turn_number += 1
            for player in other_players:  # All players get a new random asset at end of turn
                give_random_asset(player, hacker)
                header = f"{player.name}'s End of Turn"
                print("+" + "-" * width + "+")
                print("|" + header.center(width) + "|")
                print("|" + "-" * width + "|")
                print((f"| {player.name} chose to {action}").ljust(width) + " |")
                print((f"| {player.name} added an item to their inventory").ljust(width) + " |")
                print("+" + "-" * width + "+")
                time.sleep(1)

    print("\nGrid offline! Thanks for playing.")

def give_random_asset(player, hacker):
    """Creates a random asset and adds to player inventory."""
    asset_classes = [CryptoToken, DataSpike, RemovableDrive, SecurityChip, HardwarePatch]
    chosen_asset_class = random.choice(asset_classes)
    asset = chosen_asset_class()
    player.inventory.append(asset)
    if player is hacker:
        print(f"\n{player.name} received a {asset.name}!")
    else:
        print(f"{player.name} received a new inventory item")

def test_mode():
    """A variety of tests to show how various elements work"""
    title = "*** Into the Grid: Test Mode ***"
    options = [
        "1: Asset encrypt/decrypt validator",
        "2: Attack scenario simulation",
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
        # Test: Attack scenarios
        pass # TODO - Test
        input("\nTest Successful! Press Enter to continue...")
        test_mode()

    elif choice == "3":
        # Test: Upgrading rigs
        pass # TODO - Test
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
        hacker = Hacker(name) # Create the player hacker with the chosen name
        print("\nGrid online!\nYou are now in the Grid.\n") # Opening sequence
        print(f"Welcome, {hacker.name}. You are now in a digital realm where code shapes reality"
              f" and every connection pulses with possibility.\nHere, the lines between the virtual and the real blur,"
              f" and only those who can navigate its layers survive.\nThis isn't only a network- it is a living system,"
              f"a constantly shifting matrix where data is power and hackers are kings.\n"
              f"Remember, all your choices ripple across the grid- so step carefully- your journey begins now...\n")
        input("Press Enter to continue...\n")

        # Create three other unique players
        remaining_names = [n for n in names_list if n != name]
        hacker2 = Hacker(random.choice(remaining_names))
        remaining_names.remove(hacker2.name)
        hacker3 = Hacker(random.choice(remaining_names))
        remaining_names.remove(hacker3.name)
        hacker4 = Hacker(random.choice(remaining_names))
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