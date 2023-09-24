from utils import *
from chemlib import Element 
from chemlib import Compound
from chemlib import Reaction

def get_element(element):
    item = Element(element)
    success(f"Name of element  : {item.Element}")
    success(f"Type of element  : {item.Type}")
    success(f"Phase            : {item.Phase}")
    success(f"Config           : {item.Config}")
    success(f"Atomic Mass      : {item.AtomicMass}") 
    success(f"Atomic Number    : {item.AtomicNumber}")
    success(f"Neutrons         : {item.Neutrons}")
    success(f"Protons          : {item.Protons}")
    success(f"Electrons        : {item.Electrons}")
    success(f"Group            : {item.Group}")
    success(f"Density          : {item.Density}")
    success(f"Valence          : {item.Valence}")
    success(f"First ionization : {item.FirstIonization}")
    success(f"Melting Point    : {item.MeltingPoint}")
    success(f"Boiling Point    : {item.BoilingPoint}")
    success(f"Atomic Radius    : {item.AtomicRadius}")
    success(f"Electronegativity: {item.Electronegativity}")
    success(f"Discoverer       : {item.Discoverer}")

def formula_balance(balance):
    reaction = Reaction.by_formula(balance)
    reaction.balance()
    success(f"Calculating the Equilibrium constant -=[ {reaction.formula} ]=-")

def get_compound_info(compound):
    compounded = Compound(compound)
    success(f"Compound   : {compounded}")
    success(f"Molar mass : {compounded.molar_mass()}")

def percentage_mass(compounder, mass):
    compounders = Compound(compounder)
    result      = compounders.percentage_by_mass(mass)
    success(f"percentage: {result}")