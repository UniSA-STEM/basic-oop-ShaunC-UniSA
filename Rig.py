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
    def __init__(self, name):
        self.name = name
        self.condition = 2
        self.broken = False
        self.removable_drive = 1
        self.encrypted_storage = []
        self.unencrypted_storage = []
        self.upgrade_level = 0
        self.hardware_patch = 0
        self.data_spike = 1
        self.security_chip = 1

    def extract_unsecured_assets(self, hacker):
        """Unsecured assets are extracted from the rig."""
        if self.removable_drive > 0:
            self.removable_drive -= 1
            hacker.trace_level += 1
            print("Unsecured assets removed from rig.")
        else:
            print(f"There are no removable drives!")

    def repair_damage(self, hacker):
        """Use a CryptoToken to repair the rig."""
        if hacker.crypto_tokens > 0:
            hacker.crypto_tokens -= 1
            self.condition = 2
            self.broken = False
            print("rig repaired successfully!")
        else:
            print("You don't have enough crypto_tokens to repair the rig.")
        time.sleep(1)

    def take_damage(self):
        """Get hit with a data spike!"""
        if Rig:
            self.condition -= 1
            print(f"The rig was damaged by a spike!")
        else:
            print("Hacker doesn't have a rig! No damage.")
        self.check_damage()
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

    def give_random_asset(self):
        """Creates a random asset and adds to player rig inventory."""
        asset_classes = [CryptoToken, DataSpike, RemovableDrive, SecurityChip, HardwarePatch]
        asset = random.choice(asset_classes)()
        self.unencrypted_storage.append(asset)
        time.sleep(1)
        return asset

    def __str__(self):
        """Prints the details of the rig."""
        return (f"rig: {self.name}\n"
                f"Condition: {self.condition}\n"
                f"Upgrade: {self.upgrade_level}\n"
                f"Assets: {self.encrypted_storage}{self.unencrypted_storage}")