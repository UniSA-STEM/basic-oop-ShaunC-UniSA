"""
File: Asset.py
Description: An asset represents a computer object.
Author: Shaun Cantley
ID: cansy012@mymail.unisa.edu.au
Username: cansy012
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    """This class represents a digital asset."""
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.encrypted = False

    def __str__(self):
        """Return a representation of the asset."""
        if self.encrypted:
            return f"{self.name}: {self.description} [Encrypted]"
        else:
            return f"{self.name}: {self.description}"

# Subclasses
class CryptoToken(Asset):
    """A cryptographic token is used to acquire or repair rigs."""
    def __init__(self):
        Asset.__init__(self, "crypto_token", "Used to acquire or repair rigs.")

class DataSpike(Asset):
    """A data spike is used in battle."""
    def __init__(self):
        Asset.__init__(self, "data_spike", "Used to attack players.")

class RemovableDrive(Asset):
    """A removable drive is found in rigs and used for data extraction."""
    def __init__(self):
        Asset.__init__(self, "removable_drive", "Used for data exfiltration.")

class SecurityChip(Asset):
    """A security chip is used to encrypt or decrypt assets."""
    def __init__(self):
        Asset.__init__(self, "security_chip", "Used to encrypt or decrypt assets.")

class HardwarePatch(Asset):
    """A hardware patch is used to upgrade rigs."""
    def __init__(self):
        Asset.__init__(self, "hardware_patch", "Used to upgrade rigs.")



