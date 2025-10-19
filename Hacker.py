"""
File: Hacker.py
Description: This represents a hacker. Hackers can perform a variety of tasks.
Author: Shaun Cantley
ID: cansy012@mymail.unisa.edu.au
Username: cansy012
This is my own work as defined by the University's Academic Misconduct Policy.
"""
# Imports
from Asset import CryptoToken, DataSpike, SecurityChip, HardwarePatch, RemovableDrive
from Rig import Rig
import time

class Hacker:
    """A hacker can aquire rigs and hack others with them"""
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
        if self.crypto_tokens <= 1:
            self.crypto_tokens -= 1
            self.rig = Rig(f"{self.name}'s Rig")
            time.sleep(1)
        else:
            print(f"Sorry {self.name}, you need a CryptoToken to do that.")

    def launch_data_spike(self, target):
        """Launches an attack"""
        if self.rig and getattr(self.rig, 'data_spikes', 0) > 0:
            self.rig.data_spikes -= 1
            print(f"{self.name} launched a Data Spike at {target.name}!")
            self.trace_level += 1
            target.rig.Condition -= 1
            time.sleep(1)
        else:
            print(f"{self.name} needs a DataSpike to do that.")

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
            print(f"{self.name}'s rig has been upgraded!\n")
        else:
            print(f"You need a rig and a hardware patch to upgrade.")

    def deploy_honeypot(self):
        """Consumes a honeypot to stop any spikes directed at the player"""
        if self.crypto_tokens <= 1:

            self.crypto_tokens -= 1