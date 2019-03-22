"""Kyle McInness, 23/03/19, Travel Tracker,
https://github.com/KyleMcInness/CP1404_2019_SP1_Assignment_1_-_Travel_Tracker"""

list_of_places = open("list_of_places.txt", 'r+')

MENU = """Menu:
L - List of places
A - Add a new place
M - Mark a place as visited
Q - Quit
> """

MENU_CHOICE = "LAMQ"
PLACES = list_of_places.read().split("\n")
print(PLACES)


def main():
    print("Welcome, my name is Kyle.")

    menu_choice = input(MENU)
    while menu_choice not in MENU_CHOICE:
        print("That was an invalid choice")
        menu_choice = input(MENU)

    while menu_choice != "Q":
        if menu_choice == "L" or menu_choice == "l":

            display_places()
            menu_choice = input(MENU)
        elif menu_choice == "A" or menu_choice == "a":
            add_new_place()
            menu_choice = input(MENU)
        elif menu_choice == "M" or menu_choice == "m":
            print('''tbc''')

    print("Bye")
    for position in PLACES:
        list_of_places.write("\n")
        list_of_places.write(position)
    list_of_places.close()


def display_places():
    unvisited = 0
    visited = 0
    for position in range(len(PLACES)):
        if PLACES[position].split(",")[-1] == "n":
            print("*{}. {} in {} priority {}".format(position + 1, PLACES[position].split(',')[0],
                                                     PLACES[position].split(',')[1], PLACES[position].split(',')[2]))
            unvisited += 1
        else:
            print("{}. {} in {} priority {}".format(position + 1, PLACES[position].split(',')[0],
                                                    PLACES[position].split(',')[1], PLACES[position].split(',')[2]))
            visited += 1
    print("{} place(s). You still want to visit {} place(s)".format(unvisited + visited, unvisited))


def add_new_place():
    new_place = ""
    place_name = input("Name: ")
    new_place += place_name + ","
    country_name = input("Country: ")
    new_place += country_name + ","
    priority_value = input("Priority: ")
    new_place += priority_value + ","
    new_place += "n"
    PLACES.append(new_place)
    print("{} in {} (priority {}) has been added to Travel Tracker".format(place_name, country_name, priority_value))


main()
