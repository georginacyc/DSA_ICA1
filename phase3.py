# Name: Georgina Chew
# Admin No.: 180954W
# Tutorial Group: 2
# Phase 3: Stock Inventory – Additional features(5%)

# Lesson(s) learnt:
#   - 

import re
import math

storeInv = [{'type': 'Fruit', 'description': 'Apple', 'supplier': 'Ringo Farms', 'buyPrice': 1, 'sellPrice': 1.65, 'stock': 14},
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
{'type': 'Vegetable', 'description': 'Cucumber', 'supplier': 'Diamond Ring Farm', 'buyPrice': 0.80, 'sellPrice': 1.20, 'stock': 3},
{'type': 'Vegetable', 'description': 'Red Bell Pepper', 'supplier': 'Good Turn Farm', 'buyPrice': 0.90, 'sellPrice': 1.20, 'stock': 90},
{'type': 'Vegetable', 'description': 'Yellow Bell Pepper', 'supplier': 'Black Cat Farmstead', 'buyPrice': 1, 'sellPrice': 1.20, 'stock': 38},
{'type': 'Vegetable', 'description': 'Brussel Sprouts', 'supplier': 'North Outback', 'buyPrice': 1.20, 'sellPrice': 1.60, 'stock': 84},
{'type': 'Vegetable', 'description': 'Carrot', 'supplier': 'Dorothys Range', 'buyPrice': 0.80, 'sellPrice': 1.20, 'stock': 85},
{'type': 'Fruit', 'description': 'Blueberries', 'supplier': 'Blueberry Basket Grange', 'buyPrice': 1, 'sellPrice': 1.40, 'stock': 27},
{'type': 'Fruit', 'description': 'Raspberry', 'supplier': 'Broken Arrow Farms', 'buyPrice': 0.70, 'sellPrice': 0.80, 'stock': 54},
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
{'type': 'Vegetable', 'description': 'Spinach', 'supplier': 'Straight Arrow Range', 'buyPrice': 0.90, 'sellPrice': 1.40, 'stock': 15},
{'type': 'Fruit', 'description': 'Kiwi', 'supplier': 'Misty River Grange', 'buyPrice': 0.80, 'sellPrice': 1.40, 'stock': 57},
{'type': 'Fruit', 'description': 'Peach', 'supplier': 'Peach Tree Farm', 'buyPrice': 0.80, 'sellPrice': 1.40, 'stock': 18},
{'type': 'Fruit', 'description': 'Plum', 'supplier': 'Lone Wolf Gardens', 'buyPrice': 0.90, 'sellPrice': 1.30, 'stock': 12},
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
{'type': 'Vegetable', 'description': 'Bean Sprouts', 'supplier': 'Broken Cart Gardens', 'buyPrice': 0.50, 'sellPrice': 1, 'stock': 26},
{'type': 'Fruit', 'description': 'Apple', 'supplier': 'PingGuo Farms', 'buyPrice': 0.50, 'sellPrice': 1.35, 'stock': 100},
{'type': 'Vegetable', 'description': 'Garlic', 'supplier': 'GG Acres', 'buyPrice': 0.80, 'sellPrice': 1.15, 'stock': 27},
{'type': 'Vegetable', 'description': 'Potato', 'supplier': 'Fresh Farms', 'buyPrice': 0.70, 'sellPrice': 1, 'stock': 100},
{'type': 'Vegetable', 'description': 'Potato', 'supplier': 'ABC Acres', 'buyPrice': 0.60, 'sellPrice': 1.20, 'stock': 23}]


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
    1. No Preference
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

        w = x[key]
        z = y[key]
        if order == "Ascending":
            while pos > 0 and w < z:
                seq[pos] = seq[pos-1]
                pos -= 1

                y = seq[pos-1]

                z = y[key]
        else:
            while pos > 0 and w > z:
                seq[pos] = seq[pos-1]
                pos -= 1

                y = seq[pos-1]

                z = y[key]
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


def binarySearch(key, cat):
    if cat == "description":
        sortedInv = bubbleSort(storeInv, "description", "Ascending")
    else:
        sortedInv = insertionSort(storeInv, "supplier", "Ascending")

    first = 0
    last = len(sortedInv)-1
    found = False
    while first<=last and not found:

        mid = (first+last) // 2
        
        x = storeInv[mid]
        if x[cat].lower() == key.lower():
            item = x
            found = True
        else:
            if key.lower() < x[cat].lower():
                last = mid - 1
            else:
                first = mid + 1
    if found == True:
        print("The following item was found: ")
        print("Type:", item["type"])
        print("Description:", item["description"])
        print("Supplier:", item["supplier"])
        print("Buy Price:", item["buyPrice"])
        print("Sell Price:", item["sellPrice"])
        print("Stock:", item["stock"])
    else:
        print("Item was not found.")


def searchItems():
    key = input("Search: ")
    binarySearch(key)


def retreiveItems(t):
    x = storeInv
    y = []

    for i in x:
        if i["type"] == t:
            y.append(i)

    return y


def totalStock():
    while True:
        print("""
Please select what types of items you would like to include:
    1. All
    2. Fruit
    3. Vegetable
        """)
        choice = input("Option: ")
        if choice == "1":
            items = storeInv
            break
        elif choice == "2":
            items = retreiveItems("Fruit")
            break
        elif choice == "3":
            items = retreiveItems("Vegetable")
            break
        else:
            print("Invalid choice. Please try again.")
    total = 0
    for i in items:
        total += i["stock"]
    
    print("The total stock is", total)

def averageStock():
    while True:
        print("""
Please select what types of items you would like to include:
    1. All
    2. Fruit
    3. Vegetable
        """)
        choice = input("Option: ")
        if choice == "1":
            items = storeInv
            break
        elif choice == "2":
            items = retreiveItems("Fruit")
            break
        elif choice == "3":
            items = retreiveItems("Vegetable")
            break
        else:
            print("Invalid choice. Please try again.")
    total = 0
    for i in items:
        total += i["stock"]
    
    avg = total/len(items)
    
    print("The average stock is", avg)


def retreiveLow():
    x = storeInv
    y = []

    for i in x:
        if i["stock"] <= 15:
            y.append(i)

    return y


def supplierCompare():
    a = {}

    for x in storeInv:
        desc = x["description"]
        if desc in a:
            l = a[desc]
            l.append(x)
            a[desc] = l
        else:
            l = []
            l.append(x)
            a[desc] = l
    for y in a.values():
        eq = False
        if len(y) > 1:
            first = y[0]
            cheapest = first
            lowest = first["buyPrice"]
            for i in y:
                if i["buyPrice"] < lowest:
                    cheapest = i
                    lowest = cheapest["buyPrice"]
            for m in y:
                if m != cheapest:
                    if m["buyPrice"] == lowest and eq == False:
                        eq = True
            if eq == False:
                print("For {}, {} sells the cheapest at ${}. Consider using them as the main supplier of {}.".format(cheapest["description"], cheapest["supplier"], cheapest["buyPrice"], cheapest["description"]))
                


def truncate(num, digits):
    stepper = 10 ** digits
    return math.trunc(stepper * num) / stepper


def priceCompare():
    for x in storeInv:
        y = x["buyPrice"]
        z = x["sellPrice"]

        ideal = truncate((y * 0.2), 2)
        actual = truncate((z - y), 2)

        if actual < ideal:
            print("The profit margin of {} from {} is only ${}. The ideal profit margin would be ${}.".format(x["description"], x["supplier"], actual, ideal))


def displayReports():
    low = retreiveLow()
    if low != []:
        count = 1
        print("The following items' stocks are low. It it recommended that they are restocked soon.")
        for i in low:
            print("\t {}: {} from {} has {} left".format(count, i["description"], i["supplier"], i["stock"]))
            count += 1
    supplierCompare()
    priceCompare()


# menu
ans = True
while ans:
    print("""
Welcome to 1Mart Inventory System! Please select an option to continue.
    1. Add New Item
    2. Remove Item
    3. Display Items
    4. Display Total Stock Level
    5. Display Average Stock Level
    6. Display Reports
    7. Search 
    8. Exit/Quit
""")
    ans = input("Option: ")
    if ans == "1":
        addItem()
    elif ans == "2":
        removeItem()
    elif ans == "3":
        displayItems()
    elif ans == "4":
        totalStock()
    elif ans == "5":
        averageStock()
    elif ans == "6":
        displayReports()
    elif ans == "7":
        searchItems()
    elif ans == "8" or ans.lower() == "q":
        print("This program has terminated.")
        exit()
    else:
        print("Not a valid choice. Please try again.")
