"""
File: main.py
Description: This contains the main program logic for "Into the Grid".
Author: Shaun Cantley
ID: cansy012@mymail.unisa.edu.au
Username: cansy012
This is my own work as defined by the University"s Academic Misconduct Policy.
"""

# Imports
from Asset import CryptoToken, DataSpike, SecurityChip, HardwarePatch, RemovableDrive
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
        all_players = [p for p in all_players if p.alive]  # End the game when only one hacker remains
        if len(all_players) <= 1:
            print(f"\n{all_players[0].name} is the last hacker alive! Game over.")
            running = False
        print(f"\n--- Turn {turn_number} ---\n")
        for player in all_players:
            turn_taken = False
            while not turn_taken:
                if player == hacker:
                    title = f"*** Okay {player.name}, how should we proceed? ***"
                    options = [
                        "1: Acquire Rig",
                        "2: Upgrade Rig",
                        "3: Repair Rig",
                        "4: Spike Opponent",
                        "5: Extract Opponents Asset",
                        "6: Decrypt Asset",
                        "7: Encrypt Asset",
                        "8: Move Asset",
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

                    if choice == "1":  # Acquire Rig
                        if player.rig is None:
                            print("You have activated a rig! Commencing network scan...")
                            player.acquire_rig()
                            turn_taken = True
                        else:
                            print("Rig and CryptoToken needed to do that.\n")
                        input("\nPress Enter to continue...")

                    elif choice == "2":  # Upgrade Rig
                        if player.rig:
                            player.upgrade_rig()
                            turn_taken = True
                        else:
                            print("Rig and Hardware Patch needed to do that.\n")
                        input("\nPress Enter to continue...")

                    elif choice == "3":  # Repair Rig
                        if player.rig:
                            player.rig.repair_damage(player)
                            turn_taken = True
                        else:
                            print("Rig and CryptoToken needed to do that.\n")
                        input("\nPress Enter to continue...")

                    elif choice == "4":  # Spike attack
                        if player.rig:
                            print("Valid targets:")
                            for i, p in enumerate(other_players, start=1):  # Prevents AI from targeting itself
                                print(f"{i}) {p.name}")
                            target_index = int(input("Choose target (number): ")) - 1
                            target = other_players[target_index]
                            player.launch_data_spike(target)
                            turn_taken = True
                        else:
                            print(f"{player.name} needs a rig to send a spike.\n")
                        input("\nPress Enter to continue...")

                    elif choice == "5":  # Extract assets
                        if not player.rig:
                            print(f"{player.name} needs a rig to attempt extraction.\n")
                            input("\nPress Enter to continue...")
                            continue
                        print("Valid targets:")
                        for i, p in enumerate(other_players, start=1):  # Prevents AI from targeting itself
                            print(f"{i}) {p.name} {"No Rig" if not p.rig else "Broken Rig)" if p.rig.broken else ""}")
                        try:
                            target_index = int(input("Choose target (number): ")) - 1
                            target = other_players[target_index]
                        except (ValueError, IndexError):
                            print("Invalid selection.")
                            input("\nPress Enter to continue...")
                            continue
                        token = next((a for a in player.inventory if isinstance(a, CryptoToken)), None)
                        if not token:
                            print(f"{player.name} needs a CryptoToken to do that.\n")
                            input("\nPress Enter to continue...")
                            continue
                        player.inventory.remove(token)
                        if not target.rig:
                            print(f"{target.name} has no rig — nothing to extract.")
                            input("\nPress Enter to continue...")
                            continue
                        success = target.rig.extract_unsecured_assets(player)
                        if success:
                            turn_taken = True
                        else:
                            print("Extraction failed.")
                        input("\nPress Enter to continue...")

                    elif choice == "6":  # Decrypt asset
                        if player.rig:
                            player.decrypt_assets()
                            turn_taken = True
                        else:
                            print("Cannot decrypt. No rig available.\n")
                        input("\nPress Enter to continue...")

                    elif choice == "7":  # Encrypt asset
                        if player.rig:
                            player.encrypt_assets()
                            turn_taken = True
                        else:
                            print("Cannot encrypt. No rig available.\n")
                        input("\nPress Enter to continue...")

                    elif choice == "8":  # Transfer unencrypted assets from Rig
                        if player.rig:
                            player.rig.move_item()
                            turn_taken = True
                        else:
                            print("Cannot transfer assets. No rig available.\n")
                        input("\nPress Enter to continue...")

                    elif choice == "i":  # View player inventory
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
                            for item in player.rig.encrypted_storage:
                                print(item)
                        else:
                            print("Empty")
                        input("\nPress Enter to continue...")

                    elif choice == "s":  # Show player status
                        print(f"\n{player.name}'s Status:")
                        print(f"Turn: {turn_number}")
                        print(f"Trace Level: {player.trace_level}")
                        if player.rig:
                            player.rig.check_damage(player)
                        input("\nPress Enter to continue...")

                    elif choice == "q":  # Finish turn and exit game
                        print("Exiting game...")
                        turn_taken = True
                        running = False

                    else:
                        print("Invalid choice. Try again.")
                        input("\nPress Enter to continue...")

                else:  # AI's turns
                    while not turn_taken:
                        actions = []  # Uses validation to build a list of valid AI actions this turn
                        target = None  # Spike target must be initalised for game loop
                        token = any(isinstance(a, CryptoToken) for a in player.inventory)
                        if token and player.rig is None:
                            actions.append("acquires a rig")
                        if player.rig:
                            actions.append("spikes")
                            actions.append("encrypts an asset")
                            actions.append("upgrades their rig")
                        action = random.choice(actions)  # Simulates AI choice by picking a random valid action
                        if action == "acquires a rig":
                            player.acquire_rig()
                        elif action == "spikes":  # Spike target list that excludes current player
                            valid_targets = [p for p in all_players if p is not player and p.alive]
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
            turn_number += 1  # Increment turn
            action = None  # Initialise variable
            for player in other_players + [hacker]:  # All players get a new random asset at end of turn
                player.trace_level = max(0, player.trace_level - 0.25)  # Decay trace level each turn
                if player.trace_level > 5.0:
                    player.exposed = True
                else:
                    player.exposed = False
                damage_summary = f"Damage dealt: {player.damage_dealt:.2f}, Damage taken: {player.damage_taken:.2f}"
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
                print(f"| {player.name} adds a {asset_name} to inventory".ljust(width) + " |")  # Show new player asset
                print(f"| {player.name}'s trace level: {player.trace_level:.2f}".ljust(width) + " |")  # Display trace
                print(f"| {damage_summary}".ljust(width) + " |")  # Display damage counters
                if player.exposed:
                    print(f"| DANGER! {player.name} is EXPOSED!".ljust(width) + " |")
                print("+" + "-" * width + "+")
                time.sleep(1)

    print("\nGrid offline! Thanks for playing.")


def test_mode():
    """A variety of tests to show how various elements work"""
    running = True
    while running:
        title = "*** Into the Grid: Test Mode ***"
        options = [
            "1: Test encryption/decryption",
            "2: View player inventories",
            "3: Encrypt without Security Chip",
            "4: Rig upgrade modifiers",
            "5: Call strings",
            "6: High Trace Level Attack (Death Simulator™)",
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
            player1 = Hacker("Tester")
            player1.acquire_rig()
            player1.inventory.append(SecurityChip())
            print("\nRig items:")
            for item in player1.rig.unencrypted_storage:
                print(item.name)
            player1.encrypt_assets()
            print("\nRig items after decryption:")
            for item in player1.rig.encrypted_storage:
                print(item.name)
            player1.inventory.append(SecurityChip())
            player1.decrypt_assets()
            print("\nUnencrypted storage after encryption:")
            for item in player1.rig.unencrypted_storage:
                print(item.name)
            input("\nTest Successful! Press Enter to continue...")

        elif choice == "2":  # Test: Encryption
            player1 = Hacker("Player1")
            player1.acquire_rig()
            player1.rig.give_random_asset()
            player2 = Hacker("Player2")
            player2.acquire_rig()
            player2.rig.give_random_asset()
            for player in [player1, player2]:
                print(f"\n--- {player.name}'s inventory ---")
                for item in player.inventory:
                    print(item)
                if player.rig:
                    print(f"\n--- {player.name}'s Rig inventory ---")
                    for item in player.rig.unencrypted_storage + player.rig.encrypted_storage:
                        print(item)
            input("\nTest Successful! Press Enter to continue...")

        elif choice == "3":  # Test: Encrypt without SecurityChip
            player1 = Hacker("Player1")
            player1.acquire_rig()
            player1.inventory = [asset for asset in player1.inventory if not isinstance(asset, SecurityChip)]
            player1.rig.unencrypted_storage = [DataSpike(), RemovableDrive()]
            print(f"{player1.name} inventory: {[asset.name for asset in player1.inventory]}")
            print(f"{player1.name} rig unencrypted: {[asset.name for asset in player1.rig.unencrypted_storage]}")
            print("\nAttempting encryption without SecurityChip:")
            player1.encrypt_assets()
            print(f"Encrypted storage after attempt: {[asset.name for asset in player1.rig.encrypted_storage]}")
            input("\nTest Completed! Press Enter to continue...")

        elif choice == "4":  # Test: Upgrading rigs
            player1 = Hacker("Player1")  # Attacker
            player2 = Hacker("Player2")  # Defender
            player1.acquire_rig()
            player2.acquire_rig()
            print("=== Rig Upgrade Damage Reduction Test ===")
            for upgrade in range(3):
                player2.rig.condition = 2
                player2.rig.upgrade_level = upgrade
                player1.rig.unencrypted_storage.append(DataSpike())
                before = player2.rig.condition
                player1.launch_data_spike(player2)
                after = player2.rig.condition
                damage = before - after
                print(
                    f"Defender {player2.name} upgrade level {upgrade}: Damage taken={damage:.2f}\n"
                    f"Condition before={before:.2f}, after={after:.2f} (attacked by {player1.name})\n")
            input("\nTest Successful! Press Enter to continue...")

        elif choice == "5":  # Test: String methods
            print("\nTest Hacker:")  # Test hacker
            hacker = Hacker("Neo")
            hacker.acquire_rig()
            hacker.inventory.append(DataSpike())
            hacker.inventory.append(SecurityChip())
            print(hacker)
            input("\nTest Successful! Press Enter to continue...")
            print("\nTest Assets:")  # Test all asset types
            asset_classes = [CryptoToken, DataSpike, RemovableDrive, SecurityChip, HardwarePatch]
            for AssetClass in asset_classes:
                asset = AssetClass()
                print(asset)
            input("\nTest Successful! Press Enter to continue...")
            print("\nTest Rig:")  # Tests rig
            rig = Rig("TestRig", Hacker("Tester"))
            rig.unencrypted_storage.append(DataSpike())
            rig.encrypted_storage.append(SecurityChip())
            rig.unencrypted_storage.append(RemovableDrive())
            print(rig)
            input("\nTest Successful! Press Enter to continue...")

        elif choice == "6":  # Test: High trace level attack logic (death simulator)
            player1 = Hacker("Player1")
            player2 = Hacker("Player2")
            player1.acquire_rig()
            player2.acquire_rig()
            player1.rig.unencrypted_storage.append(DataSpike())
            player2.trace_level = 6.0
            player2.exposed = True
            print(f"\nBefore: {player2.name} alive={player2.alive}, exposed={player2.exposed}\n")
            player1.launch_data_spike(player2)
            print(f"\nAfter: {player2.name} alive={player2.alive}\n")
            input("\nDeath Successful! Press Enter to continue...")

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
        hacker = Hacker(name)  # Create the player hacker with the chosen name
        print("\nGrid online!\nYou are now in the Grid.\n")  # Opening sequence
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

    elif choice == "t":  # Test mode to check game functions and shows output
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