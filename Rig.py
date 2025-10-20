"""
File: rig.py
Description: A rig represents a computer object.
Author: Shaun Cantley
ID: cansy012@mymail.unisa.edu.au
Username: cansy012
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# imports
from Asset import CryptoToken, DataSpike, RemovableDrive, SecurityChip, HardwarePatch
import random
import time

class Rig:
    """A rig is a computer with various properties that a hacker may interact with."""
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.damage = 0
        self.condition = 2
        self.broken = False
        self.upgrade_level = 0
        self.encrypted_storage = []
        self.unencrypted_storage = []
        self.unencrypted_storage.append(DataSpike()) # Start with 2 DataSpikes and 1 RemovableDrive
        self.unencrypted_storage.append(DataSpike())
        self.unencrypted_storage.append(RemovableDrive())

    def extract_unsecured_assets(self, hacker):
        """Unsecured assets are extracted from the rig."""
        removable_drive = next((asset for asset in self.unencrypted_storage if asset.name == "Removable Drive"),None)
        if removable_drive:
            self.unencrypted_storage.remove(removable_drive)
            hacker.trace_level += 1
            print("Unsecured assets removed from rig.")
        else:
            print(f"There are no removable drives!")

    def repair_damage(self, hacker):
        """Use a CryptoToken to repair the rig if damaged"""
        if self.condition == 2 and not self.broken:
            print(f"{self.name}'s Rig is Pristine. No repair needed.")
            return
        token = next((a for a in hacker.inventory if isinstance(a, CryptoToken)), None)
        if token:
            hacker.inventory.remove(token)
            self.condition = 2
            self.broken = False
            print(f"{self.name} has been repaired successfully!")
        else:
            print(f"{hacker.name} does not have a CryptoToken to repair {self.name}.")
        time.sleep(1)

    def check_damage(self, hacker):
        """Checks the damage level of the rig"""
        if self.condition == 2:
            print(f"{hacker.name}'s rig is Pristine- No current damage.\n")
        elif self.condition == 1:
            print(f"Warning: {hacker.name} your rig has taken damage\n")
        elif self.condition == 0:
            print(f"ALERT: {hacker.name}'s rig is broken. Assets are exposed!\n")
            self.broken = True
        time.sleep(1)

    def move_item(self): # Moves an item from rig to personal inventory
        choice = -1
        player = self.owner
        while self.unencrypted_storage and choice != 0:
            print("--- Transfer Assets from Rig ---")
            for index, asset in enumerate(self.unencrypted_storage, 1): # Lists assets that can be moved
                print(f"{index}. {asset.name} - {asset.description}")
            print("0. Exit")
            choice = input("Select an asset to transfer to inventory: ")
            if not choice.isdigit():
                print("Invalid choice. Enter a number.")
                choice = -1
                continue
            choice = int(choice)
            if 1 <= choice <= len(self.unencrypted_storage):
                asset = self.unencrypted_storage.pop(choice - 1) # Gets the item and deletes it from Rig storage
                player.inventory.append(asset)
                player.trace_level += 1
                print(f"{asset.name} moved to inventory. Your Trace level increased by 1!")
            elif choice != 0:
                print("Invalid selection. Try again.")

    def damage_multiplier(self):
        """Damage multiplier based on upgrade level. Each upgrade halves the damage."""
        return 0.5 ** max(0, int(self.upgrade_level))

    def take_damage(self, base_damage, attacker=None):
        """Apply damage to the rig, reduced by upgrades."""
        if self.broken: # If the Rig is already broken no need to continue
            return
        multiplier = self.damage_multiplier() # Deal actual damage with multipliers
        actual_damage = base_damage * multiplier
        self.damage += actual_damage
        self.condition -= actual_damage
        if attacker:
            attacker.damage_dealt += actual_damage  # track damage dealt
            self.owner.damage_taken += actual_damage  # track damage received
        if self.condition <= 0: # Prevents condition from being negative
            self.broken = True
            self.condition = 0

    def give_random_asset(self):
        """Creates a random asset and adds to player rig inventory."""
        asset_classes = [CryptoToken, DataSpike, RemovableDrive, SecurityChip, HardwarePatch]
        asset = random.choice(asset_classes)()
        self.unencrypted_storage.append(asset)
        time.sleep(1)
        return asset

    def __str__(self):
        """Prints the details of the rig."""
        encrypted_names = [asset.name for asset in self.encrypted_storage]
        unencrypted_names = [asset.name for asset in self.unencrypted_storage]
        return (f"Rig: {self.name}\n"
                f"Condition: {self.condition}\n"
                f"Upgrade: {self.upgrade_level}\n"
                f"Encrypted Assets: {encrypted_names}\n"
                f"Unencrypted Assets: {unencrypted_names}")