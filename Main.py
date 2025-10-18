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
                title = f"*** It's turn number {turn_number}, {player.name}. How should we proceed? ***"
                options = [
                    "1: Acquire Rig",
                    "2: Launch Data Spike",
                    "3: Encrypt Asset",
                    "4: Upgrade Rig",
                    "I: View Inventory",
                    "S: Show Status",
                    "Q: Exit Game"
                ]

                width = max(len(title), *(len(option) for option in options)) + 8
                print("+" + "-" * width + "+")
                print("|" + title.center(width) + "|")
                print("|" + "-" * width + "|")
                for option in options:
                    print("| " + option.ljust(width - 2) + " |")
                print("+" + "-" * width + "+")

                choice = input("Choose an action: ").lower()
                if choice == "1":
                    if player.crypto_tokens >= 1:
                        player.acquire_rig()
                        action_success = True
                    else:
                        print(f"{player.name} needs a CryptoToken to acquire a rig.")
                elif choice == "2":
                    if player.rig is not None:
                        print(f"{player.name} launched a Spike!")
                        player.trace_level += 1
                        print(f"{player.name}'s trace level is now {player.trace_level}.")
                        action_success = True
                    else:
                        print(f"{player.name} needs a rig to send a spike.")
                elif choice == "3":
                    if player.security_chip >= 1 and player.inventory:
                        print("Select an item to encrypt:", ", ".join(player.inventory))
                        player.encrypt_assets()
                        player.security_chip -= 1
                        print("Encryption complete!")
                        action_success = True
                    else:
                        print("Cannot encrypt. Either no SecurityChip or inventory is empty.")
                elif choice == "4":
                    player.upgrade_rig()
                    action_success = True
                elif choice == "i":
                    print("Inventory:", player.inventory)
                elif choice == "s":
                    print(f"Trace Level: {player.trace_level}")
                elif choice == "q":
                    print("Exiting game...")
                    running = False
                    break
                else:
                    print("Invalid choice. Try again.")

            else:
                # AI turn
                while not action_success:
                    actions = []
                    if player.crypto_tokens >= 1:
                        actions.append("acquire")
                    if player.rig is not None:
                        actions.append("spike")
                        if (hasattr(player.rig, # Only allow upgrade if player or rig has a hardware patch
                                    'HardwarePatch') and player.rig.HardwarePatch > 0) or player.hardware_patch > 0:
                            actions.append("upgrade")
                    if player.security_chip >= 1 and player.inventory:
                        actions.append("encrypt")

                    action = random.choice(actions)

                    if action == "acquire" and player.crypto_tokens >= 1:
                        player.acquire_rig()
                        action_success = True
                    elif action == "spike" and player.rig is not None:
                        player.trace_level += 1
                        action_success = True
                    elif action == "encrypt" and player.security_chip >= 1 and player.inventory:
                        player.encrypt_assets()
                        player.security_chip -= 1
                        action_success = True
                    elif action == "upgrade":
                        player.upgrade_rig()
                        action_success = True

                print(f"{player.name} successfully chose to {action}.")
                time.sleep(3)

        if running:  # End of turn logic
            turn_number += 1
            for player in [hacker] + other_players:
                give_random_asset(player, hacker)

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

    # Test menu formatting
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
        print(f"DOX protocols has confirmed the presence of {hacker2.name}, {hacker3.name} and {hacker4.name}")
        print(f"The system reads as network online and awaits your command.")
        play(hacker, other_players)

    elif choice == "t":
        test_mode()
    elif choice == "q":
        print("Thanks for playing!\nSee you next time.")
        quit()
    else:
        print("Invalid input.")
        time.sleep(3)
        main()

if __name__ == "__main__":
    main()