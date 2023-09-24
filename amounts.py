from utils import success
from chemlib import Compound

class Amounts:
    def __init__(self, compound, number):
        self.compound = compound
        self.number   = number

    def grams(self):
        compound = Compound(self.compound)
        result   = compound.get_amounts(grams = self.number)
        success(f"Grams     : {result['grams']}")
        success(f"moles     : {result['moles']}")
        success(f"Molecules : {result['molecules']}")

    def moles(self):
        compound = Compound(self.compound)
        result   = compound.get_amounts(moles = self.number)
        success(f"Grams     : {result['grams']}")
        success(f"moles     : {result['moles']}")
        success(f"Molecules : {result['molecules']}")

    def molecules(self):
        compound = Compound(self.compound)
        result   = compound.get_amounts(molecules = self.number)
        success(f"Grams     : {result['grams']}")
        success(f"moles     : {result['moles']}")
        success(f"Molecules : {result['molecules']}")