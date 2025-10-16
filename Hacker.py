"""
File: Hacker.py
Description: This represents a hacker. Hackers can perform a variety of tasks.
Author: Shaun Cantley
ID: cansy012@mymail.unisa.edu.au
Username: cansy012
This is my own work as defined by the University's Academic Misconduct Policy.
"""
# Imports
from Asset import CryptoToken, DataSpike, SecurityChip, HardwarePatch, RemoveableDrive
import Rig


class Hacker:
    """A hacker can hack rigs"""

    def __init__(self, name):
        self.name = name
        self.crypto_tokens = 1
        self.rig = False
        self.trace_level = 0
        self.exposed = False
        self.security_chip = 1
        self.hardware_patch = 1
        self.inventory = []
        self.upgrade_level = 0


    def acquire_rig(self):
        """Finds a rig to hack"""
        if self.crypto_tokens <= 1:
            self.crypto_tokens -= 1
            print(f"{self.name} used a CryptoToken.")
            self.rig = Rig.Rig("Normal Rig")
            print("A rig has been acquired!")
        else:
            print("Not enough CryptoTokens!")

    def launch_attack(self):
        """Launches an attack"""
        pass  # TODO: Rig interactions

    def encrypt_assets(self):
        """Encrypts assets"""
        for item in self.inventory:
            print(item)

    def decrypt_assets(self):
        """Decrypts assets"""
        pass  # TODO: Rig interactions

    def upgrade_rig(self):
        """Upgrades rig with a hardware patch"""
        if self.rig != 0 and self.hardware_patch != 0: # Upgrades rig if the required items are available
            self.upgrade_level += 1
            print(f"Your rig has been upgraded!")
        else:
            print(f"You need a rig and a hardware patch to upgrade.")