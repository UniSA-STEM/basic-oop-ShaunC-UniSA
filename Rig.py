"""
File: Rig.py
Description: A rig represents a computer object.
Author: Shaun Cantley
ID: cansy012@mymail.unisa.edu.au
Username: cansy012
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Rig:
    """A rig is a computer with various properties that a hacker may interact with."""

    Name = ""
    DataSpike = 2
    Damage = 0
    Broken = False
    RemoveableDrives = 1
    EncryptedStorage = []
    UnencryptedStorage = []
    UpgradeLevel = 0

    def __init__(self, name):
        self.Name = name
        self.DataSpike = 2
        self.Damage = 0
        self.Broken = False
        self.RemoveableDrive = 1
        self.EncryptedStorage = []
        self.UnencryptedStorage = []

    def extract_unsecured_assets(self):
        """Unsecured assets are extracted from the rig."""
        if RemoveableDrive > 0:
            RemoveableDrive -= 1
        else:
            print(f"There are no removable drives!")

    def repair(self):
        """Uses a CryptoToken to repair the rig."""
        if CryptoToken >= 0:
            if self.Damage > 0:
                Damage = 0
                Broken = False
            else:
                print(f"No repair is needed.")
        else:
            print("You don't have enough CryptoTokens to repair!")

    def upgrade(self):
        """Consumes a hardware patch to increase the rig level."""
        if HardwarePatch > 0:
            HardwarePatch -= 1
            UpgradeLevel += 1
            print(f"The hardware patch was successful!\nThe rig level is now {level}.")
        else:
            print(f"There are no hardware patches!")

    def take_damage(self, damage):
        """Get hit with a data spike!"""


    def __str__(self):
        """Prints the details of the rig."""
        return (f"Rig: {self.Name}\n"
                f"Damage: {self.Damage}\n"
                f"Upgrade: {self.UpgradeLevel}\n"
                f"Assets: {self.EncryptedStorage}{self.UnencryptedStorage}")