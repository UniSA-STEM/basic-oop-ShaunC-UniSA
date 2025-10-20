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
    """A hacker can acquire rigs and hack others with them"""
    def __init__(self, name):
        self.name = name
        self.upgrade_level = 0
        self.rig = None
        self.trace_level = 0
        self.damage_taken = 0
        self.damage_dealt = 0
        self.exposed = False
        self.alive = True
        self.inventory = []
        self.inventory.append(CryptoToken())
        self.inventory.append(HardwarePatch())
        self.inventory.append(SecurityChip())

    def acquire_rig(self):
        """Finds a rig to hack"""
        token = next((a for a in self.inventory if isinstance(a, CryptoToken)), None)
        if token:
            self.inventory.remove(token)
            self.rig = Rig(f"{self.name}'s Rig", self)  # pass self as owner
            time.sleep(1)
            print(f"{self.name} acquired a rig.")
        else:
            print(f"Sorry {self.name}, you need a CryptoToken to do that.")

    def upgrade_rig(self):
        """Upgrades rig with a hardware patch"""
        if self.rig:
            patch = next((a for a in self.inventory if isinstance(a, HardwarePatch)), None)
            if patch:
                self.inventory.remove(patch)
                self.upgrade_level += 1
                print(f"{self.name} upgraded their rig to level {self.upgrade_level}!")
            else:
                print(f"{self.name}, you need a hardware patch to upgrade.")
        else:
            print(f"{self.name}, you need a rig to upgrade.")

    def launch_data_spike(self, target):
        """Launches an attack"""
        if not self.rig:
            print(f"{self.name} needs a rig to launch a Data Spike.")
            return
        token = next((a for a in self.rig.unencrypted_storage if isinstance(a, DataSpike)), None)
        if token is None:
            print(f"{self.name} needs a DataSpike to do that.")
            return
        self.rig.unencrypted_storage.remove(token)
        print(f"{self.name} launched a Data Spike at {target.name}!")
        self.trace_level += 1
        if target.exposed:
            print(f"{target.name} was exposed and is TERMINATED!")
            target.alive = False
            return
        if target.rig: # Calls damage function to calculate actual damage with multipliers
            target.rig.take_damage(1, attacker=self)
            target.rig.check_damage(target)
        else:
            print(f"{target.name} has no Rig! The attack has no effect.")
        time.sleep(1)

    def encrypt_assets(self):
        """Encrypts assets using a SecurityChip from inventory"""
        token = next((a for a in self.inventory if isinstance(a, SecurityChip)), None)
        if not self.rig:
            print(f"{self.name} does not have a rig for encryption.")
            return
        if not self.rig.unencrypted_storage:
            print(f"{self.name} has no assets that can be encrypted.")
            return
        if token is None:
            print(f"{self.name} has no SecurityChip to encrypt assets.")
            return
        self.inventory.remove(token)
        for item in self.rig.unencrypted_storage:
            self.rig.encrypted_storage.append(item)
            print(f"Encrypted: {item.name}")
        self.rig.unencrypted_storage.clear()

    def decrypt_assets(self):
        """Decrypts assets using a SecurityChip from inventory"""
        chip = next((a for a in self.inventory if isinstance(a, SecurityChip)), None)
        if not self.rig:
            print(f"{self.name} does not have a rig for decryption.")
            return
        if not self.rig.encrypted_storage:
            print(f"{self.name} has no encrypted assets.")
            return
        if chip is None:
            print(f"{self.name} has no SecurityChip to decrypt assets.")
            return
        self.inventory.remove(chip)
        for item in self.rig.encrypted_storage:
            self.rig.unencrypted_storage.append(item)
            print(f"Decrypted: {item.name}")
        self.rig.encrypted_storage.clear()

    def __str__(self):
        """Prints the details of the hacker."""
        rig_name = self.rig.name if self.rig else "No Rig"
        inventory_items = ", ".join([item.name for item in self.inventory]) if self.inventory else "Empty"
        return f"Hacker: {self.name} | Rig: {rig_name} | Trace Level: {self.trace_level} | Inventory: {inventory_items}"