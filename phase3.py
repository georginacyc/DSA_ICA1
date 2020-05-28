# Name: Georgina Chew
# Admin No.: 180954W
# Tutorial Group: 2
# Phase 3:Stock Inventory – Additional features(5%)

import re

storeInv = []

def addItem():
    pass

def removeItem():
    pass

def displayItem():
    pass

def salesReport():
    pass

# menu
ans = True
while ans:
    print("""
Welcome to 1Mart Inventory System! Please select an option to continue.
1. Add New Item
2. Remove Item
3. Display Items
4. Display Sales Report
5. Exit/Quit
""")
    ans = input("Option: ")
    if ans == "1":
        addItem()
    elif ans == "2":
        removeItem()
    elif ans == "3":
        displayItem()
    elif ans == "4":
        salesReport()
    elif ans == "5" or ans.lower() == "q":
        print("This program has terminated.")
    else:
        print("Not a valid choice. Please try again.")
