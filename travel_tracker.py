"""Kyle McInness, 23/03/19, Travel Tracker, https://github.com/KyleMcInness/CP1404_2019_SP1_Assignment_1_-_Travel_Tracker"""

list_of_places = open(("list_of_places.txt", 'r'))

MENU = """Menu:
L - List of places
A - Add a new place
M - Mark a place as visited
Q - Quit
> """


def main():
    print("Welcome, my name is Kyle.")

    menu_choice = input(MENU)
    print(menu_choice)
    while menu_choice != "L" or menu_choice != "A" or menu_choice != "M" or menu_choice != "Q":
        print("That was an invalid choice")
        menu_choice = input(MENU)


main()
