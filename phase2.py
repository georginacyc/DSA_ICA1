# Name: Georgina Chew
# Admin No.: 180954W
# Tutorial Group: 2
# Phase 2: Stock Inventory – Search and Sort Algorithms(10%)

# Lesson(s) learnt:
#   - i should immediately convert values of attributes like buyprice/sellprice/stock so as to be able to sort them properly. previously, i had all of them as strings and that caused issues with comparisons -- "100" was seen to be smaller than "90"

import re

storeInv = [{'type': 'Fruit', 'description': 'Red Apple', 'supplier': 'Ringo Farms', 'buyPrice': 1, 'sellPrice': 1.65, 'stock': 100},
{'type': 'Fruit', 'description': 'Orange', 'supplier': 'Orenji Farms', 'buyPrice': 1.20, 'sellPrice': 1.70, 'stock': 50},
{'type': 'Fruit', 'description': 'Pear', 'supplier': 'Nashi Farms', 'buyPrice': 1, 'sellPrice': 1.50, 'stock': 30},
{'type': 'Fruit', 'description': 'Dragonfruit', 'supplier': 'Tangy Farms', 'buyPrice': 2, 'sellPrice': 2.95, 'stock': 100},
{'type': 'Fruit', 'description': 'Mangosteen', 'supplier': 'Hallelujah Acres', 'buyPrice': 1, 'sellPrice': 1.50, 'stock': 80},
{'type': 'Fruit', 'description': 'Starfruit', 'supplier': 'Old Loon Farm', 'buyPrice': 0.90, 'sellPrice': 1.40, 'stock': 120},
{'type': 'Vegetable', 'description': 'Bok Choy', 'supplier': 'Victory Farms', 'buyPrice': 1.80, 'sellPrice': 2.80, 'stock': 40},
{'type': 'Vegetable', 'description': 'Celery', 'supplier': 'Sea View Farm', 'buyPrice': 0.70, 'sellPrice': 1.10, 'stock': 60},
{'type': 'Vegetable', 'description': 'Tomato', 'supplier': 'EarthDance', 'buyPrice': 1, 'sellPrice': 1.40, 'stock': 100},
{'type': 'Vegetable', 'description': 'Lettuce', 'supplier': 'Serenity Farm', 'buyPrice': 0.70, 'sellPrice': 1.10, 'stock': 20},
{'type': 'Fruit', 'description': 'Mango', 'supplier': 'Full Hand Farm', 'buyPrice': 1.50, 'sellPrice': 2.30, 'stock': 50},
{'type': 'Fruit', 'description': 'Strawberries', 'supplier': 'Strawberry Valley Fields', 'buyPrice': 1.20, 'sellPrice': 1.80, 'stock': 94},
{'type': 'Fruit', 'description': 'Cherries', 'supplier': 'Heart and Soil Farm', 'buyPrice': 1.10, 'sellPrice': 1.80, 'stock': 100},
{'type': 'Vegetable', 'description': 'Cucumber', 'supplier': 'Diamond Ring Farm', 'buyPrice': 0.80, 'sellPrice': 1.20, 'stock': 80},
{'type': 'Vegetable', 'description': 'Red Bell Pepper', 'supplier': 'Good Turn Farm', 'buyPrice': 0.90, 'sellPrice': 1.20, 'stock': 90},
{'type': 'Vegetable', 'description': 'Yellow Bell Pepper', 'supplier': 'Black Cat Farmstead', 'buyPrice': 1, 'sellPrice': 1.20, 'stock': 38},
{'type': 'Vegetable', 'description': 'Brussel Sprouts', 'supplier': 'North Outback', 'buyPrice': 1.20, 'sellPrice': 1.60, 'stock': 84},
{'type': 'Vegetable', 'description': 'Carrot', 'supplier': 'Dorothys Range', 'buyPrice': 0.80, 'sellPrice': 1.20, 'stock': 85},
{'type': 'Fruit', 'description': 'Blueberries', 'supplier': 'Blueberry Basket Grange', 'buyPrice': 1, 'sellPrice': 1.40, 'stock': 27},
{'type': 'Fruit', 'description': 'Raspberry', 'supplier': 'Broken Arrow Farms', 'buyPrice': 0.70, 'sellPrice': 1.30, 'stock': 54},
{'type': 'Fruit', 'description': 'Red Grapes', 'supplier': 'Eagle Hill Vineyard', 'buyPrice': 0.90, 'sellPrice': 1.25, 'stock': 93},
{'type': 'Fruit', 'description': 'Green Grapes', 'supplier': 'Northwind Vineyard', 'buyPrice': 1, 'sellPrice': 1.25, 'stock': 45},
{'type': 'Fruit', 'description': 'Green Apple', 'supplier': 'Virgin Valley Farms', 'buyPrice': 0.90, 'sellPrice': 1.70, 'stock': 77},
{'type': 'Vegetable', 'description': 'Cabbage', 'supplier': 'Blue Dasher Farm', 'buyPrice': 0.70, 'sellPrice': 1, 'stock': 93},
{'type': 'Fruit', 'description': 'Rambutan', 'supplier': 'Blackmeadow Farmstead', 'buyPrice': 1.15, 'sellPrice': 1.60, 'stock': 25},
{'type': 'Vegetable', 'description': 'Bird Eye Chili', 'supplier': 'Hollow Point Farm', 'buyPrice': 0.40, 'sellPrice': 0.90, 'stock': 85},
{'type': 'Vegetable', 'description': 'Asparagus', 'supplier': 'Old Stone Farms', 'buyPrice': 1.20, 'sellPrice': 1.60, 'stock': 94},
{'type': 'Vegetable', 'description': 'Soy Beans', 'supplier': 'Fresh Fountain Acres', 'buyPrice': 1.80, 'sellPrice': 2.25, 'stock': 63},
{'type': 'Vegetable', 'description': 'Broccoli', 'supplier': 'Mossy Boulder Gardens', 'buyPrice': 0.70, 'sellPrice': 1.10, 'stock': 6},
{'type': 'Vegetable', 'description': 'Cauliflower', 'supplier': 'Red Robin Meadow', 'buyPrice': 0.80, 'sellPrice': 1.30, 'stock': 38},
{'type': 'Vegetable', 'description': 'Spinach', 'supplier': 'Straight Arrow Range', 'buyPrice': 0.90, 'sellPrice': 1.40, 'stock': 83},
{'type': 'Fruit', 'description': 'Kiwi', 'supplier': 'Misty River Grange', 'buyPrice': 0.80, 'sellPrice': 1.40, 'stock': 57},
{'type': 'Fruit', 'description': 'Peach', 'supplier': 'Peach Tree Farm', 'buyPrice': 0.80, 'sellPrice': 1.40, 'stock': 18},
{'type': 'Fruit', 'description': 'Plum', 'supplier': 'Lone Wolf Gardens', 'buyPrice': 0.90, 'sellPrice': 1.30, 'stock': 100},
{'type': 'Fruit', 'description': 'Watermelon', 'supplier': 'Blackmeadow Farms', 'buyPrice': 1.25, 'sellPrice': 2.40, 'stock': 20},
{'type': 'Fruit', 'description': 'Honeydew Melon', 'supplier': 'Weeping Willow Lands', 'buyPrice': 1.25, 'sellPrice': 2.50, 'stock': 93},
{'type': 'Fruit', 'description': 'Avocado', 'supplier': 'River Hallow Pastures', 'buyPrice': 3.20, 'sellPrice': 3.90, 'stock': 75},
{'type': 'Fruit', 'description': 'Pumpkin', 'supplier': 'Muddy Pumpkin Farms', 'buyPrice': 6, 'sellPrice': 7, 'stock': 36},
{'type': 'Vegetable', 'description': 'Potato', 'supplier': 'Grassway Organics', 'buyPrice': 0.60, 'sellPrice': 1, 'stock': 100},
{'type': 'Vegetable', 'description': 'Zucchini', 'supplier': 'Mossy Rock Farms', 'buyPrice': 4, 'sellPrice': 5.20, 'stock': 63},
{'type': 'Vegetable', 'description': 'Onion', 'supplier': 'Crescent Moon Gardens', 'buyPrice': 1, 'sellPrice': 1.30, 'stock': 26},
{'type': 'Vegetable', 'description': 'Garlic', 'supplier': 'Moonshadow Acres', 'buyPrice': 1, 'sellPrice': 1.35, 'stock': 100},
{'type': 'Vegetable', 'description': 'Eggplant', 'supplier': 'Patchwork Farms', 'buyPrice': 3, 'sellPrice': 3.90, 'stock': 69},
{'type': 'Vegetable', 'description': 'Kale', 'supplier': 'Sunset Farms', 'buyPrice': 3, 'sellPrice': 3.90, 'stock': 94},
{'type': 'Fruit', 'description': 'Grapefruit', 'supplier': 'Stone Valley Farm', 'buyPrice': 1.20, 'sellPrice': 2.10, 'stock': 96},
{'type': 'Fruit', 'description': 'Passionfruit', 'supplier': 'Diamond Creek Meadow', 'buyPrice': 1.20, 'sellPrice': 1.80, 'stock': 23},
{'type': 'Vegetable', 'description': 'Yam', 'supplier': 'Windy Willows Acres', 'buyPrice': 1.30, 'sellPrice': 2, 'stock': 50},
{'type': 'Vegetable', 'description': 'Ginger', 'supplier': 'Yew Valley Farms', 'buyPrice': 0.80, 'sellPrice': 1.20, 'stock': 40},
{'type': 'Vegetable', 'description': 'Parsley', 'supplier': 'Rebirth Fields', 'buyPrice': 0.70, 'sellPrice': 1.20, 'stock': 100},
{'type': 'Vegetable', 'description': 'Bean Sprouts', 'supplier': 'Broken Cart Gardens', 'buyPrice': 0.50, 'sellPrice': 1, 'stock': 26}]


def addItem(): # item desc, selling price, stock level (quantity), supplier, buying price, popularity(?)
    print("""
Please select the option that best fits the item:
1. Vegetable
2. Fruit
    """)
    typechoice = input("Option: ")
    while True:
        if typechoice == "1":
            itemType = "Vegetable"
            break
        elif typechoice == "2":
            itemType = "Fruit"
            break
        else:
            print("Please enter a valid choice")
        typechoice = input("Option: ")
    desc = input("Please enter item description: ")
    supplier = input("Please enter item supplier: ")
    bprice = input("Please enter item buy price ($): ")
    while True:
        if not re.match("^\d*[.]?\d*$", bprice):
            bprice = input("Please enter a valid item buy price ($): ")
        else:
            bprice = float(bprice)
            break
    price = input("Please enter item selling price ($): ")
    while True:
        if not re.match("^\d*[.]?\d*$", price):
            price = input("Please enter a valid item sell price ($): ")
        elif float(bprice) >= float(price):
            while True:
                choice = input("Item's selling price is less than or equal to its buying price. Are you sure you want to continue? (Y/N): ")
                if choice.lower() == "n":
                    print("Please re-enter the item information again carefully.")
                    addItem()
                elif choice.lower() == "y":
                    price = float(price)
                    break
                else:
                    print("Invalid input. Please try again.")
        price = float(price)
        break


    stock = input("Please enter quantity of items: ")
    while True:
        if stock.isdigit() == False or int(stock) <= 0:
            stock = input("Please enter a valid quantity: ")
        else:
            stock = int(stock)
            break
    
    x = ""
    isMatch = False
    for item in storeInv:
        if desc.lower() == item["description"].lower() and supplier.lower() == item["supplier"].lower():
            item["stock"] = int(item["stock"]) + int(stock)
            isMatch = True
            x = item
    if isMatch == False:
        x = {"type": itemType, "description": desc, "supplier": supplier, "buyPrice": bprice, "sellPrice": price, "stock": stock}
        storeInv.append(x)
    print("Type: " + itemType)
    print("Item Description: " + desc)
    print("Supplier: " + supplier)
    print("Buy Price: " + str(bprice))
    print("Sell Price: " + str(price))
    print("Stock: " + str(x["stock"]))
    if isMatch == False:
        print("Item successfully added.")
    else:
        print("Item stock successfully updated")


def itemReduce(x, item):
    if x == 1:
        num = input("Please input how much you would like to decrease the quantity by: ")
        if num.isdigit() and int(num) <= int(item["stock"]):
            item["stock"] = int(item["stock"]) - int(num)
            print("Item quantity is now", item["stock"])
        else:
            print("Please enter a valid quantity.")
            itemReduce(1, item)
    if x == 2:
        storeInv.remove(item)
        print("Item successfully removed.")


def rowCheck():
    row = input("Please enter the row number containing the item you would like to edit: ")
    print(row)
    if row.isdigit() and int(row) <= len(storeInv):
        row = int(row) - 1
        return row
    else:
        print("Please enter a valid row number.")
        rowCheck()


def removeItem():
    count = 1
    for item in storeInv:
        print(str(count) + ":", item)
        count = int(count) + 1
    
    while True:
        row = rowCheck()
        item = storeInv[row]
        print(item)
        print("Item Description: " + item["description"])
        print("Supplier:", item["supplier"])
        print("Buy Price:", item["buyPrice"])
        print("Sell Price:", item["sellPrice"])
        print("Stock:", item["stock"])
        print("""
Please select an option to continue:
    1. Decrease Stocks
    2. Delete Item Completely
    3. Back
""")
        choice = input("Option: ")
        if choice == "1":
            itemReduce(1, item)
            break
        elif choice == "2":
            itemReduce(2, item)
            break
        elif choice == "3":
            removeItem()
            break
        else:
            print("Please enter a valid option.")


def searchKey():
    while True:
        print("""
Please select an option to sort the display by:
    1. Order Added (Default)
    2. Type
    3. Description
    4. Supplier
    5. Buy Price
    6. Sell Price
    7. Stock
        """)
        choice = input("Option: ")
        if choice == "1":
            return "Default"
        elif choice == "2":
            return "type"
        elif choice =="3":
            return "description"
        elif choice == "4":
            return "supplier"
        elif choice == "5":
            return "buyPrice"
        elif choice == "6":
            return "sellPrice"
        elif choice == "7":
            return "stock"
        else:
            print("Not a valid choice. Please try again.")


def displayOrder():
    while True:
        print("""
Please select the order to sort the display:
    1. Ascending
    2. Descending
        """)
        choice = input("Option: ")
        if choice == "1":
            return "Ascending"
        elif choice == "2":
            return "Descending"
        else:
            print("Not a valid choice. Please try again.")


def sortMethod():
    while True:
        print("""
Please select a method to sort the display with:
    1. Bubble Sort
    2. Insertion Sort
        """)
        choice = input("Option: ")
        if choice == "1":
            return "Bubble"
        elif choice == "2":
            return "Insertion"
        else:
            print("Not a valid choice. Please try again.")


def bubbleSort(seq, key, order):
    n = len(seq)

    for i in range(n-1, 0, -1):
        for j in range(i):
            x = seq[j]
            y = seq[j+1]
            if order == "Ascending": # try except
                if x[key] > y[key]:
                    tmp = seq[j]
                    seq[j] = seq[j+1]
                    seq[j+1] = tmp
            else:
                if x[key] < y[key]:
                    tmp = seq[j+1]
                    seq[j+1] = seq[j]
                    seq[j] = tmp
    return seq


def insertionSort(seq, key, order):
    n = len(seq)

    for i in range(1, n):
        pos = i

        value = seq[i]

        x = seq[i]
        y = seq[pos-1]

        z = y[key]
        w = x[key]
        if order == "Ascending":
            while pos > 0 and w < z:
                seq[pos] = seq[pos-1]
                pos -= 1
        else:
            while pos > 0 and w > z:
                seq[pos] = seq[pos-1]
                pos -= 1

        seq[pos] = value
    return seq


def displayItems():
    if storeInv == []:
        print("No items in inventory")
    else:
        searchkey = searchKey()
        if searchkey == "Default":
            count = 1
            for item in storeInv:
                print(str(count) + ":", item)
                count = int(count) + 1
            return
        order = displayOrder()
        method = sortMethod()
        if method == "Bubble":
            sortedInv = bubbleSort(storeInv, searchkey, order)
            count = 1
            for item in sortedInv:
                print(str(count) + ":", item)
                count = int(count) + 1
        else:
            sortedInv = insertionSort(storeInv, searchkey, order)
            count = 1
            for item in sortedInv:
                print(str(count) + ":", item)
                count = int(count) + 1
        
    
    

# menu
ans = True
while ans:
    print("""
Welcome to 1Mart Inventory System! Please select an option to continue.
    1. Add New Item
    2. Remove Item
    3. Display Items
    4. Exit/Quit
""")
    ans = input("Option: ")
    if ans == "1":
        addItem()
    elif ans == "2":
        removeItem()
    elif ans == "3":
        displayItems()
    elif ans == "4" or ans.lower() == "q":
        print("This program has terminated.")
        exit()
    else:
        print("Not a valid choice. Please try again.")
