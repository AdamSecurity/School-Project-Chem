from utils import wait 
from utils import error
from utils import option
from utils import banner
from utils import success
from utils import exiting

from amounts import Amounts
from methods import get_element
from methods import formula_balance
from methods import get_compound_info
from methods import percentage_mass

while True:
    try:
        cmd = int(input(">> ")) 

        if cmd == 0:
            banner()

        if cmd == 69:
            exiting()
            exit()

        if cmd == 1:
            formula = input("Enter the formula: ")
            wait("balancing the formula... ")
            success("formula has been balanced\n")
            formula_balance(formula)
        
        if cmd == 2:
            symbol = input("Enter the symbol of Element: ")
            get_element(symbol)
        
        if cmd == 3:
            compound = input("Enter the Compound: ")
            get_compound_info(compound)

        if cmd == 4:
            mass       = input("Enter the Compund: ")
            percentage = input("Enter the Element: ")
            percentage_mass(mass, percentage)

        if cmd == 5:
            option()
            option = input("\nEnter the option: ")
            if option == "1":
                compounder = input("Enter the Compound: ")
                gram       = int(input("Enter the number of grams: "))
                amount     = Amounts(compounder, gram)
                amount.grams()
    
            if option == "2":
                compounder = input("Enter the Compound: ")
                mole       = int(input("Enter the number of moles: "))
                amount     = Amounts(compounder, mole)
                amount.moles()
    
            if option == "3":
                compounder = input("Enter the Compound: ")
                molecule   = int(input("Enter the number of molecule: "))
                amount     = Amounts(compounder, molecule)
                amount.molecules()
            
    except:
        error()
        exit()