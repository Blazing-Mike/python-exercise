# Treasure hunter exercise
#
# Define an initial state for the inventory, containing any items you like. A dictionary works well, with the keys being items and the values being how many of that item we have.
# Define functions for: adding something to the inventory, finding something in the inventory, and printing everything in the inventory.
#
# Afterwards, check out our code to get more ideas!

# My solution

inventory = {
  "cars" : "2",
  "houses": "3"
}

print(f"This is the state of our inventory: {inventory}")
      
inventory_item = input('Enter name of the item you wan to add: ')

item_quantity = input('Enter quantity of item you add added: ')
def add_item_to_inventory():
  inventory.update({f"{inventory_item}": f"{item_quantity}"})
  print(inventory)

  

def find_item_in_inventory():
  return inventory[input('Enter waht you want to find in this inventory: ')]
  


print(inventory)


## Teclacode's solution


inventory = {
    "rope": 1,
    "coin": 10,
    "ruby": 2
}

def add_item(item = "coin", amount_found = 1):
    item = item.lower()

    if item in inventory:
        current_quantity = inventory[item]
        inventory[item] = current_quantity + amount_found
    else:
        inventory[item] = amount_found

def print_item(item):
    item = item.lower()

    if item not in inventory:
        print(f"The adventurer doesn't have a {item}")
    else:
        quantity = inventory[item]
        print(f"{item.capitalize()}: {quantity}")

def print_all_items():
    print("-- Items in inventory --")
    for item in inventory:
        item.lower()
        quantity = inventory[item]
        print(f"{item.capitalize()}: {quantity}")

print_all_items()
add_item("dagger")
print_item("coin")
print_all_items()

# https://python.tecladocode.com/4_treasure_hunters/8_treasure_hunter_solution.html
