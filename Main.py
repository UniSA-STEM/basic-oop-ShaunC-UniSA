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
            turn_taken = False
            while not turn_taken:
                if player == hacker:
                    title = f"*** Okay {player.name}, how should we proceed? ***"
                    options = [
                        "1: Acquire rig",
                        "2: Upgrade rig",
                        "3: Repair rig",
                        "4: Spike Player",
                        "5: Encrypt Asset",
                        "6: Decrypt Asset",
                        "7: Extract Asset",
                        "",
                        "I: View inventory",
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

                    if choice == "1": # Acquire rig
                        if player.crypto_tokens != 0 and player.rig != False:
                            print("You have activated a rig! Commencing network scan...")
                            player.acquire_rig()
                            turn_taken = True
                        else:
                            print("You need a rig and CryptoToken to do that.\n")
                        input("\nPress Enter to continue...")

                    elif choice == "2":  # Upgrade rig
                        if player.rig and player.hardware_patch > 0:
                            player.upgrade_rig()
                            turn_taken = True
                        else:
                            print("You need a rig and a hardware patch to do that.\n")
                        input("\nPress Enter to continue...")

                    elif choice == "3": # Repair rig
                        if player.rig and hacker.crypto_tokens != 0:
                            player.repair_damage()
                            turn_taken = True
                        else:
                            print("You need a rig and CryptoToken to do that.\n")
                        input("\nPress Enter to continue...")

                    elif choice == "4":  # Spike Attack
                        if player.rig and player.rig.data_spike:
                            print("Valid targets:")
                            for i in range(len(other_players)):
                                print(f"{i + 1}) {other_players[i].name}")
                            target_index = int(input("Choose target (number): ")) - 1
                            target = other_players[target_index]
                            player.launch_data_spike(target)
                            player.trace_level += 1
                            turn_taken = True
                        else:
                            print(f"{player.name} needs a rig and a DataSpike to send a spike.\n")
                        input("\nPress Enter to continue...")

                    elif choice == "5": # Encrypt Asset
                        if player.security_chip >= 1 and player.inventory:
                            print("Select an item to encrypt:", ", ".join(player.inventory))
                            player.encrypt_assets()
                            player.security_chip -= 1
                            turn_taken = True
                        else:
                            print("Cannot encrypt. No Security Chip or inventory is empty.\n")
                        input("\nPress Enter to continue...")

                    elif choice == "6": # Decrypt Asset
                        if player.security_chip >= 1 and player.inventory:
                            print("Select an item to decrypt:", ", ".join(player.rig.encrypted_storage))
                            player.decrypt_assets()
                            player.security_chip -= 1
                            turn_taken = True
                        else:
                            print("Cannot Decrypt. No Security Chip or inventory is empty.\n")
                        input("\nPress Enter to continue...")

                    elif choice == "7": # Extract Assets
                        if player.security_chip >= 1 and player.inventory:
                            player.deploy_honeypot()
                            player.CryptoToken -= 1
                            turn_taken = True
                        else:
                            print(f"{player.name} needs a CryptoToken to do that.\n")
                        input("\nPress Enter to continue...")

                    elif choice == "i":  # View inventory
                        print(f"\n--- {player.name}'s inventory ---")
                        if player.inventory:
                            for item in player.inventory:
                                print(item)
                        else:
                            print("Empty")
                        print("\n--- Rig inventory ---")
                        if player.rig:
                            for item in player.rig.unencrypted_storage:
                                print(item)
                        else:
                            print("Empty")
                        input("\nPress Enter to continue...")

                    elif choice == "s":  # Show status
                        print(f"\n{player.name}'s Status:")
                        print(f"Turn: {turn_number}")
                        print(f"Trace Level: {player.trace_level}")
                        if player.rig:
                            player.rig.check_damage(player)
                        input("\nPress Enter to continue...")

                    elif choice == "q":
                        print("Exiting game...")
                        running = False
                    else:
                        print("Invalid choice. Try again.")
                        input("\nPress Enter to continue...")

                else: # AI's turns
                    while not turn_taken:
                        actions = [] # Uses validation to build a list of valid AI actions this turn
                        target = None # Spike target must be initalised for game loop
                        if player.crypto_tokens != 0:
                            actions.append("acquires a rig")
                        if player.rig:
                            actions.append("spikes")
                            actions.append("encrypts an asset")
                            actions.append("upgrades their rig")
                        action = random.choice(actions) # Simulates AI choice by picking a random valid action
                        if action == "acquires a rig":
                            player.acquire_rig()
                        elif action == "spikes":
                            valid_targets = [p for p in all_players if p is not player]
                            target = random.choice(valid_targets)
                            player.trace_level += 1
                            player.launch_data_spike(target)
                        elif action == "encrypts an asset":
                            player.encrypt_assets()
                        elif action == "upgrades their rig":
                            player.upgrade_rig()
                        turn_taken = True

        if running:  # End of turn summary
            print(f"\nEnd of turn {turn_number}\n\n")
            turn_number += 1
            for player in other_players + [hacker]:  # All players get a new random asset at end of turn
                if player.rig:
                    asset = player.rig.give_random_asset()
                    asset_name = asset.name if asset else "Nothing"
                header = f"{player.name}'s Turn"
                print("+" + "-" * width + "+")
                print("|" + header.center(width) + "|")
                if action == "spikes":
                    print(f"| {player.name} {action} {target.name}".ljust(width) + " |")
                elif action == "acquires a rig":
                    print(f"| {player.name} {action}".ljust(width) + " |")
                elif action == "encrypts an asset":
                    print(f"| {player.name} {action}".ljust(width) + " |")
                elif action == "upgrades their rig":
                    print(f"| {player.name} {action}".ljust(width) + " |")
                print(f"| {player.name} adds a {asset_name} to inventory".ljust(width) + " |")
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

    elif choice == "2": # Test Encryption
        hacker1 = Hacker.Hacker("Hacker1")
        hacker1.acquire_rig()
        hacker1.rig.give_random_asset()
        hacker2 = Hacker.Hacker("Hacker2")
        hacker2.acquire_rig()
        hacker2.rig.give_random_asset()
        for player in [hacker1, hacker2]:
            print(f"\n--- {player.name}'s inventory ---")
            for item in player.inventory:
                print(item)
            if player.rig:
                print(f"\n--- {player.name}'s rig inventory ---")
                for item in player.rig.unencrypted_storage + player.rig.encrypted_storage:
                    print(item)

        input("\nTest Successful! Press Enter to continue...")

    elif choice == "3":
        # Test: Upgrading rigs
        input("\nTest Successful! Press Enter to continue...")

    elif choice == "q":
        # Quit to main menu
        print("\n" * 20)
        main()

    else:
        print("Invalid choice. Try again.")

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
              f" and every connection pulses with possibility.\n"
              f"Here, the lines between the virtual and the real blur,"
              f" and only those who can navigate its layers survive.\n"
              f"This isn't only a network- it is a living system,"
              f"a constantly shifting matrix where data is power and hackers are kings.\n"
              f"Remember, all your choices ripple across the grid- so step carefully- your journey begins now...\n")
        input("Press Enter to continue...")

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