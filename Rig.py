"""
File: Rig.py
Description: A rig represents a computer object.
Author: Shaun Cantley
ID: cansy012@mymail.unisa.edu.au
Username: cansy012
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# imports
from Asset import CryptoToken, DataSpike, RemovableDrive, SecurityChip, HardwarePatch
import random

class Rig:
    """A rig is a computer with various properties that a hacker may interact with."""
    def __init__(self, name):
        self.Name = name
        self.Condition = 2
        self.Broken = False
        self.RemovableDrive = 1
        self.EncryptedStorage = []
        self.UnencryptedStorage = []
        self.UpgradeLevel = 0
        self.HardwarePatch = 0
        self.DataSpike = 1

    def extract_unsecured_assets(self, hacker):
        """Unsecured assets are extracted from the rig."""
        if self.RemoveableDrive > 0:
            self.RemoveableDrive -= 1
            hacker.trace_level += 1
            print("Unsecured assets removed from rig.")
        else:
            print(f"There are no removable drives!")

    def repair_damage(self, hacker):
        """Use a CryptoToken to repair the rig."""
        if hacker.crypto_tokens > 0:
            hacker.crypto_tokens -= 1
            self.Condition = 2
            self.Broken = False
            print("Rig repaired successfully!")
        else:
            print("You don't have enough CryptoTokens to repair the rig.")

    def take_damage(self):
        """Get hit with a data spike!"""
        self.Condition -= 1
        print(f"The rig was damaged by a spike!")
        self.check_damage()

    def check_damage(self):
        """Checks the damage level of the rig"""
        if self.Condition == 2:
            print(f"Pristine: Rig is not damaged")
        elif self.Condition == 1:
            print(f"Warning: Rig has taken damage")
        elif self.Condition == 0:
            print(f"ALERT: Rig is Broken. Assets are exposed!")
            self.Broken = True

    def upgrade_rig(self, player):
        """Consumes a hardware patch from rig or player inventory to increase the rig level."""
        if hasattr(self, 'HardwarePatch') and self.HardwarePatch > 0:
            self.HardwarePatch -= 1
            self.UpgradeLevel += 1
            print(f"The hardware patch was successful!\nThe rig level is now {self.UpgradeLevel}.")
        elif hasattr(player, 'hardware_patch') and player.hardware_patch > 0:
            player.hardware_patch -= 1
            self.UpgradeLevel += 1
            print(f"The hardware patch was successful!\nThe rig level is now {self.UpgradeLevel}.")
        else:
            print("There are no hardware patches available to upgrade the rig!")

    def give_random_asset(player, hacker):
        """Creates a random asset and adds to player rig inventory."""
        asset_classes = [CryptoToken, DataSpike, RemovableDrive, SecurityChip, HardwarePatch]
        chosen_asset_class = random.choice(asset_classes)  # Allocate random asset to player
        asset = chosen_asset_class()
        player.rig.UnencryptedStorage.append(asset)
        if player is hacker:
            print(f"\n{player.name} received a {asset.name}!")
        else:
            print(f"{player.name} received a {asset.name}")

    def __str__(self):
        """Prints the details of the rig."""
        return (f"Rig: {self.Name}\n"
                f"Condition: {self.Condition}\n"
                f"Upgrade: {self.UpgradeLevel}\n"
                f"Assets: {self.EncryptedStorage}{self.UnencryptedStorage}")