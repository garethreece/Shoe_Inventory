# Shoe Inventory using OOP
A program (inventory.py) that uses object orienatated programming to control the information stored in a shoe inventory file (inventory.txt)
This program creates, monitor, and edit a shoe inventory and allows the user these options:

Please select a value (1 to 6) for the shoe inventory, or '0' to quit: 
1 - View all inventory items
2 - Re-stock lowest show quantity
3 - Search for a particular shoe by code
4 - Calculate total value for each shoe in stock
5 - Find shoe with the highest quantity and put on sale
6 - Add a new shoe to the inventory
0 - Quit
Select your option: 

Every time the program is opened, it reads the inventory.txt file and turns all the information into shoe objects using the shoe class:
Shoes added / edited in the shoe inventory will be saved as shoe objects.
When the file is closed it is saved in the inventory.txt file. Therefore, it can be opened as shoe class objects in future.

This program has been tested so that the user cannot enter incorrect information and damage the inventory.txt file.
