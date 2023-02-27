# A program to create, monitor, and edit a shoe inventory

#========The beginning of the class==========
# Create a class definition for Shoe
class Shoe:
#  Constructor for Shoe class to initiate variables:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

# Get cost function to return the code and cost of a shoe object.
    def get_cost(self):
        return f"Cost of {self.code} = {self.cost}"
        '''
        Add the code to return the cost of the shoe in this method.
        '''
# Get quantity function to return the code and quantity of a shoe object.
    def get_quantity(self):
        return f"Quantity of {self.code} = {self.quantity}"
        '''
        Add the code to return the quantity of the shoes.
        '''

# The main string method that returns a readable format for the data contained in the class.
    def __str__(self):
        return f"""
Country: {self.country.capitalize()}
Code: {self.code}
Product: {self.product.capitalize()}
Cost: {self.cost}
Quantity: {self.quantity}"""
        '''
        Add a code to returns a string representation of a class.
        '''

#==========Global Variables=============
# This is the main shoe inventory list that stores all the shoe objects
# This can be read and edited throughout the program
inventory = []

# This shoe list stores the initial data when reading the inventory text file
# shoe_list supports creating the inventory list that includes shoe objects  
shoe_list = []

#==========Functions outside the class==============
# Function to read and copy data from the inventory.txt file to the shoe list
def read_shoes_data():
    # Tries to open the inventory file. If the file doesn't exist gives a warning message and closes program
    try:
        file = open("inventory.txt", "r", encoding = "utf-8-sig")
    except FileNotFoundError:
        print("Inventory.txt file does not exist. This program can not run. Please create the file! No data saved.")
        exit()
    # skip first line of inventory.txt file (header line)
    next(file)
    # Sorts the information from the inventory.txt file so that it populates shoe list correctly
    for shoe in file:
        shoe = shoe.replace("\n", "")
        shoe = shoe.split(",")
        shoe_list.append(shoe)
    file.close()
    # Loop to run through a position at a time in the shoe list and send to the capture shoes function 
    # This will populate the inventory list with shoe objects
    for i in shoe_list:
        country, code, product, cost, quantity = i[0], i[1], i[2], i[3], i[4]
        capture_shoes(country, code, product, cost, quantity)
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
# A function to capture shoes data in the correct order for the Shoe class
# This adds the data to the end of the main inventory list as an object
def capture_shoes(country, code, product, cost, quantity):
    shoe = Shoe(country, code, product, cost, quantity)
    inventory.append(shoe)

# A function to add a new shoe type to the inventory
def add_shoe():
    # This function will not allow any commas in the user input
    # A comma will corrupt the inventory and text file, so advises the user to try again
    # Collects all the information about each attribute in the Shoe class from the user
    # It will prompt the user if they are sure the information is correct before saving to the inventory 
    while True:
        code = input("What is the shoe code: ")
        # If there is a space or comma it will ask for the user input again
        if code.find(" ") != -1 or code.find(",") != -1:
            print("You can not have a code with a space or a comma in, please try again!")
            continue
        break
    while True:
        country = input ("What is the shoe country: ")
        # If there is a comma in the country input it will ask the user to try again.
        if country.find(",") != -1:
            print("You can not have a country with a comma in, please try again!")
            continue
        break
    while True:
        product = input("What is the shoe product name: ")
        # If there is a comma in the product input it will ask the user to try again.
        if product.find(",") != -1:
            print("You can not have a product with a comma in, please try again!")
            continue
        break
    while True:
        cost = input("what is the cost of the shoe (integer): ")
        # This will check to see if the cost is a positive integer.
        # An integer is assumed from the data in the text file.
        # It can be changed to a float if required 
        try:
            cost = int(cost)
        except:
            print("This needs to be a whole number, please try again!")
            continue
        if cost <= 0:
            print("The cost cannot be less than zero, please try again!")
            continue
        break
    while True:
        # This will check that the quantity is a positive integer and not too large to fit in the warehouse
        quantity = input("What is the quantity of shoes (integer): ")
        try:
            quantity = int(quantity)
        except:
            print("This needs to be a whole number, please try again!")
            continue
        if quantity <= 0:
            print("The quantity cannot be less than zero, please try again!")
            continue
        if quantity > 1000:
            # A limit on the number of shoes based on the inventory data has been assumed.
            # This can be changed if required
            print("There is not enough room in the warehouse for this many shoes, please try again!")
            continue
        break
    # Final check before adding the data to the inventory
    check = input("Are you sure you want to add this information to the shoe database (Y/N): ").upper()
    if check == "Y" or check == "YES":
        # If yes, it will send the user data to capture shoes and wriet objects to the inventory file
        capture_shoes(country, code, product, cost, quantity)
        write_objects_file()
        print("Shoe information added to the database, thank you!")
    else:
        # If anything else is typed, it will display the message and go back to the main menu
        print("No information added, please re-try if you want to add a new shoe to the inventory!")
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

# Function to show all the inventory items on screen in the format defined in the main string method
def view_all():
    for i in inventory:
        print(f"{i}")
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python's tabulate module.
    '''
# Function re_stock to check the shoes with the lowest inventory
# Then ask the user if they want to increse the inventory
# The amount is ambigious in the task document, so I assumed the user was inputting an amount to increase
# The new amount is checked with the user to confirm
# If yes, it will write the new quantity to both the inventory object list and the inventory.txt file
def re_stock():
    min_quantity = int(inventory[0].quantity) + 1
    # This loops through the inventory list to see which has the lowest quantity
    for i in range (0, len(inventory)):
        current_quantity = int(inventory[i].quantity)
        if current_quantity < min_quantity:
            min_quantity = current_quantity
            # the position is recorded to know which object to edit if confirmed
            position = i
    print("Shoe with the current lowest stock")
    print(str(inventory[position]))
    while True:
        # Asks the user for an amount to increase it by and makes sure it is a positive integer less than 1000
        increase_quantity = input("How many shoes do you want to add to this stock: ")
        try:
            increase_quantity = int(increase_quantity)
        except:
            print("This is not a valid number, please try again!")
            continue
        if increase_quantity < 1:
            print("This is less than one, please try again!")
            continue
        elif increase_quantity > 1000:
            print("There is not enough room in the warehouse to increase by this many shoes, please try again!")
            continue
        break
    # Adds the user input with the current quantity to get the new quantity
    new_quantity = min_quantity + increase_quantity
    check = input(f"Are you sure you want to increase the stock from {min_quantity} to {new_quantity} Y/N: ").upper()
    # Check to make sure all is okay and to confirm writing the info to inventory list and inventory.txt
    if check == "Y" or check == "YES":
        print(f"\nThank you, The stock will be increased to {new_quantity}")
        change_quantity(new_quantity, position) 
    else:
        print("\nThe quantity has not been increased and nothing has been changed!")
    print(inventory[position])
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

# Function to write the new quantity to the correct position in the inventory list
# Then sends the data to write objects file that will save the new information to inventory.txt
def change_quantity(new_quantity, position):
    inventory[position].quantity = new_quantity
    write_objects_file()

# A write function that will take the objects from the current inventory list
# Then overwrite it all as new data in the correct format in the inventory.txt file 
def write_objects_file():
    file = open("inventory.txt", "w+", encoding = "utf-8-sig")
    # This is to create the header in the inventory text file and start the file fresh
    file.write("Country,Code,Product,Cost,Quantity")
    # This loop writes one object at a time in the inventory list to the new inventory.txt file
    # It uses the format defines in the line file format function
    for i in range (0, len(inventory)):
        file.write(f"\n{line_file_format(i)}")
    file.close

# This function returns the correct format for any information being written to the inventory.txt file
def line_file_format(i):
    return f"{inventory[i].country},{inventory[i].code},{inventory[i].product},{inventory[i].cost},{inventory[i].quantity}"

# Function to ask user for a shoe code to search the inventory
# If found it will display the information defined in the main string function  
def search_shoe():
    user_code = input("What is the code of the shoe you want to find: ").upper()
    # Keeps a tally, if above 1 then it will know that a code has been found
    tally = 0
    # Loop to compare the user code, with the shoe object codes in the inventory
    for i in range (0, len(inventory)):
        # If the code is found it will print out the result in the main string format
        if user_code == str(inventory[i].code):
            print(f"{inventory[i]}")
            tally += 1
    # if nothing found it will prompt the user that their inputted code was not found 
    if tally == 0:
        print("Sorry code not found!")
    '''
    This function will search for a shoe from the list
    using the shoe code and return this object so that it will be printed.
    '''

# This function will go through the inventory list an object at a time
# Work out the cost and quantity of each shoe, then print out the total value (cost x quantity)of each item
# It will also work out the cumulative value of all the shoes in the inventory and display at the end 
def value_per_item():
    # Variable to keep the cumulative total of all the shoes in stock
    cumulative_value = 0
    print()
    # Loop to go through each item in the inventory
    for i in range (0, len(inventory)):
        # Works out the quantity x cost for product value
        product_value = int(inventory[i].quantity) * int(inventory[i].cost)
        # Returns format from the get cost class function, to make sure it is displayed correctly
        print(inventory[i].get_cost())
        # Returns format from the get quantity class function, to make sure it is displayed correctly
        print(inventory[i].get_quantity())
        # Prints out the code, product name, and total value of each item in the inventory
        print(f"""Total value of {inventory[i].code} {inventory[i].product} = {product_value}\n""")
        # Every loop it adds the product value to the cumulative value to keep a total tally
        cumulative_value += product_value
    # After the loop is finished, it will print out the cumulative total of all items in stock
    print(f"\nTotal value of all items in stock = {cumulative_value}")
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

# A function to get the highest quantity object in the inventory and offer to put it on sale
def highest_qty():
    # Variable to store the highest quantity total to compare it to the next item in the loop 
    max_quantity = 0
    # Loop to go through the inventory one item at a time and compare the quantity in stock
    for i in range (0, len(inventory)):
        current_quantity = int(inventory[i].quantity)
        # If the current objects quantity is larger that the max quantity found
        # it will record this as the new max quantity
        if current_quantity > max_quantity:
            max_quantity = current_quantity
            # It will also record the position of the item with the max quantity
            position = i
    # At the end of the loop, it will print out the shoe with the highest quantity in the main string format
    print("Shoe with the current heighest stock")
    print(str(inventory[position]))
    # Once displayed it will ask the user if they want to put it on sale or not
    sale = input("Do you want to put this show on sale (Y/N): ").upper()
    if sale == "Y" or sale == "YES":
        print("\nThis shoe is now on sale!")
    else:
        print("\nThe shoe is not on sale and has not been changed!")
# The task was a bit ambigiuous here, so I assumed that it would let shops know to put it on sale.
# However, it could be used to change the price of the stock in the inventory list / text file if required 
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

# This function diplays the main menu items to the user, and returns a choice from 0-6
def main_menu():
    while True:
        # Format of main menu
        menu_number = input("""
Please select a value (1 to 6) for the shoe inventory, or \'0\' to quit: 
1 - View all inventory items
2 - Re-stock lowest show quantity
3 - Search for a particular shoe by code
4 - Calculate total value for each shoe in stock
5 - Find shoe with the highest quantity and put on sale
6 - Add a new shoe to the inventory
0 - Quit
Select your option: """)
# Gets an input from the user for a choice and makes sure it is an integer between 0-6
# If not it will ask the user to try again.
        try:
            menu_number = int(menu_number)
        except:
            print("This is not a number, please try again!")
            continue
        if menu_number > 6 or menu_number < 0:
            print("Number is not in range (0-6), please try again!")
            continue
        return menu_number

#==========Main Menu=============

# First thing is to run the read shoes data function and read the data from the inventory.txt file 
# Then store the data as shoe objects in the inventory list
read_shoes_data()

# The main program is minimal and consists mainly of menu selection
# This controls which function to send the program to depending on user input
# This is all contained in a nice and simple while loop
while True:
    choice = main_menu()
    if choice == 1:
        view_all()
    if choice == 2:
        re_stock()
    if choice == 3:
        search_shoe()
    if choice == 4:
        value_per_item()
    if choice == 5:
        highest_qty()
    if choice == 6:
        add_shoe()
    if choice == 0:
        print("The program will now exit! Thank you.")
        break
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''