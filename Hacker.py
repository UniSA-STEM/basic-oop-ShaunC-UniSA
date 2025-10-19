"""
File: Hacker.py
Description: This represents a hacker. Hackers can perform a variety of tasks.
Author: Shaun Cantley
ID: cansy012@mymail.unisa.edu.au
Username: cansy012
This is my own work as defined by the University's Academic Misconduct Policy.
"""
# Imports
from Asset import CryptoToken, DataSpike, RemovableDrive, SecurityChip, HardwarePatch
from Rig import Rig
import time

class Hacker:
    """A hacker can acquire rigs and hack others with them"""
    def __init__(self, name):
        self.name = name
        self.crypto_tokens = 1
        self.rig = None
        self.trace_level = 0
        self.exposed = False
        self.security_chip = 1
        self.hardware_patch = 1
        self.inventory = []
        self.upgrade_level = 0

    def acquire_rig(self):
        """Finds a rig to hack"""
        if self.crypto_tokens > 0:
            self.crypto_tokens -= 1
            self.rig = Rig(f"{self.name}'s Rig")
            time.sleep(1)
        else:
            print(f"Sorry {self.name}, you need a CryptoToken to do that.")

    def upgrade_rig(self):
        """Upgrades rig with a hardware patch"""
        if self.rig and self.hardware_patch > 0:  # self.rig is the Hacker's rig
            self.upgrade_level += 1
            self.hardware_patch -= 1
            print(f"{self.name} upgraded their rig to level {self.upgrade_level}!")
        else:
            print(f"{self.name}, you need a rig and a hardware patch to upgrade.")

    def launch_data_spike(self, target):
        """Launches an attack"""
        if self.rig and self.rig.data_spike > 0:
            self.rig.data_spike -= 1
            print(f"{self.name} launched a Data Spike at {target.name}!")
            self.trace_level += 1
            if target.rig:  # Only reduce condition if target has a rig
                target.rig.condition -= 1
                target.rig.check_damage(target)
            else:
                print(f"{target.name} has no rig! The attack has no effect.")
            time.sleep(1)
        else:
            print(f"{self.name} needs a DataSpike to do that.")

    def encrypt_assets(self):
        """Encrypts assets"""
        if not self.rig:
            print(f"{self.name} does not have a rig for encryption.")
        if not self.rig.unencrypted_storage:
            print(f"{self.name} has no assets that can be encrypted.")
        for item in self.rig.unencrypted_storage:
            self.rig.encrypted_storage.append(item)
            print(f"Encrypted: {item}")
        self.rig.unencrypted_storage.clear()

    def decrypt_assets(self):
        """Decrypts assets"""
        if not self.rig:
            print(f"{self.name} does not have a rig for decryption.")
        if not self.rig.encrypted_storage:
            print(f"{self.name} has no encrypted assets.")
        for item in self.rig.encrypted_storage:
            self.rig.unencrypted_storage.append(item)
            print(f"Decrypted: {item}")
        self.rig.unencrypted_storage.clear()