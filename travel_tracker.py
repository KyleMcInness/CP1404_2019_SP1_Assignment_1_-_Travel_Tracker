"""Kyle McInness, 23/03/19, Travel Tracker,
https://github.com/KyleMcInness/CP1404_2019_SP1_Assignment_1_-_Travel_Tracker"""

list_of_places = open("list_of_places.txt", 'r+')

MENU = """Menu:
L - List of places
A - Add a new place
M - Mark a place as visited
Q - Quit
> """

MENU_CHOICE = "LAMlam"
PLACES = list_of_places.read().split("\n")
additions = []

def main():
    print("Welcome, my name is Kyle.")

    menu_choice = input(MENU)
    while menu_choice not in MENU_CHOICE:
        print("That was an invalid choice")
        menu_choice = input(MENU)

    while menu_choice != "Q" or menu_choice != "q":
        if menu_choice == "L" or menu_choice == "l":
            for position in range(len(PLACES)):
                if PLACES[position].split(",")[-1] == "n":
                    print("*{}. {} in {} priority {}".format(position + 1, PLACES[position].split(',')[0], PLACES[position].split(',')[1], PLACES[position].split(',')[2]))
                else:
                    print("{}. {} in {} priority {}".format(position + 1, PLACES[position].split(',')[0],
                                                             PLACES[position].split(',')[1],
                                                             PLACES[position].split(',')[2]))
            menu_choice = input(MENU)
        elif menu_choice == "A" or menu_choice == "a":
            place_name = input("Name: ")
            additions.append(place_name)
            country_name = input("Country: ")
            additions.append(country_name)
            priority_value = input("Priority: ")
            additions.append(priority_value)
            additions.append("n")
            print("{} in {} (priority {}) has been added to Travel Tracker".format(place_name, country_name, priority_value))
            print(additions)
            menu_choice = input(MENU)
        else:
            '''tbc'''

    print("Bye")
    for position in additions:
        list_of_places.write(position)


list_of_places.close()


main()
