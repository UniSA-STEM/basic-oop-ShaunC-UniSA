"""
File: Asset.py
Description: An asset represents a computer object.
Author: Shaun Cantley
ID: cansy012@mymail.unisa.edu.au
Username: cansy012
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset():
    """This class represents a digital asset."""
    def __init__(self):
        self.name = name
        self.description = description
        self.encrypted = False

    def encrypt(self):
        self.encrypted = True
        print(f"{self.name} is now encrypted.")

    def decrypt(self):
        self.encrypted = False
        print(f"{self.name} is now decrypted.")

class CryptoToken(Asset):
    """A cryptographic token is used to acquire or repair rigs."""
    def __init__(self):
        name = CryptoToken
        description = "A cryptographic token is used to acquire or repair rigs."

class DataSpike(Asset):
    """A data spike is used in battle."""
    def __init__(self):
        name = DataSpike
        description = "A data spike is used in battle."

class RemoveableDrive(Asset):
    """A removeable drive is found in rigs and used for data extraction."""
    def __init__(self):
        name = RemoveableDrive
        description = "A removeable drive is used in battle."

class SecurityChip(Asset):
    """A security chip is used to encrypt or decrypt assets."""
    def __init__(self):
        name = SecurityChip
        description = "A security chip is used to encrypt or decrypt assets."

class HardwarePatch(Asset):
    """A hardware patch is used to upgrade rigs."""
    def __init__(self):
        name = HardwarePatch
        description = "A hardware patch is used to upgrade rigs."



