"""
File: Hacker.py
Description: This represents a hacker. Hackers can perform a variety of tasks.
Author: Shaun Cantley
ID: cansy012@mymail.unisa.edu.au
Username: cansy012
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Hacker:
    """A hacker can hack rigs"""

    CryptoToken = 1
    Rig = 0
    TraceLevel = 0
    Exposed = False
    SecurityChip = 0
    HardwarePatch = 0
    Assets = []

    def __init__(self, name):
        self.name = name
        self.CryptoToken = Hacker.CryptoToken
        self.Rig = Hacker.Rig
        self.TraceLevel = Hacker.TraceLevel
        self.Exposed = Hacker.Exposed
        self.SecurityChip = Hacker.SecurityChip
        self.HardwarePatch = Hacker.HardwarePatch
        self.Assets = Hacker.Assets

    def _aquire_rig(self):
        """Finds a rig to hack"""
        if CryptoToken <= 1:

            CryptoToken -= 1
            Rig += 1

            print(f"{self.name} used a CryptoToken.")
            print("A rig has been aquired!")
        else:
            print("not enough cryptotokens")
    pass # TODO: Rig interactions

    def _launch_attack(self):
        """Launches an attack"""
        pass  # TODO: Rig interactions

    def _encrypt_assets(self):
        """Encrypts assets"""
        pass  # TODO: Rig interactions

    def _decrypt_assets(self):
        """Decrypts assets"""
        pass  # TODO: Rig interactions

    def _upgrade_rig(self):
        """Upgrades rig with a hardware patch"""
        if Rig > 0 and HardwarePatch > 0:
            UpgradeLevel += 1
        pass  # TODO: Rig interactions



