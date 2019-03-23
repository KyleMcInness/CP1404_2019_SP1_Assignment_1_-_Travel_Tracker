"""Kyle McInness, 23/03/19, Travel Tracker,
https://github.com/KyleMcInness/CP1404_2019_SP1_Assignment_1_-_Travel_Tracker"""

input_file = open("list_of_places.txt", 'r')

MENU = """Menu:
L - List of places
A - Add a new place
M - Mark a place as visited
Q - Quit
> """

MENU_CHOICE = "LAMQ"
PLACES = input_file.read().split("\n")
new_places = []
for pos in PLACES:
    new_places.append(pos)
print(new_places)


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
            display_places()
            mark_visited()
            menu_choice = input(MENU)
    print("Bye")
    output_file = open("list_of_places.txt", "w")
    for position in new_places:
        output_file.write(position + "\n")
    input_file.close()
    output_file.close()


def mark_visited():
    number_of_place = int(input("Enter the number of a place to mark as visited "
                             "> "))
    print("{} in {} visited.".format(PLACES[number_of_place - 1].split(",")[0], PLACES[number_of_place - 1].split(",")[1]))
    visited_place = new_places[number_of_place - 1]
    visited_places = visited_place.split(",")
    new_entry = ""
    for i in range(len(visited_places) -1):
        new_entry += visited_places[i]
        new_entry += ","
    new_entry += "v"
    new_places[number_of_place - 1] = new_entry


def display_places():
    unvisited = 0
    visited = 0
    try:
        for position in range(len(new_places)):
            if new_places[position].split(",")[-1] == "n":
                print("*{}. {} in {} priority {}".format(position + 1, new_places[position].split(',')[0],
                                                         new_places[position].split(',')[1], new_places[position].split(',')[2]))
                unvisited += 1
            else:
                print("{}. {} in {} priority {}".format(position + 1, new_places[position].split(',')[0],
                                                        new_places[position].split(',')[1], new_places[position].split(',')[2]))
                visited += 1
        print("{} place(s). You still want to visit {} place(s)".format(unvisited + visited, unvisited))
    except IndexError:
        pass


def add_new_place():
    new_place = ""
    place_name = input("Name: ")
    new_place += place_name + ","
    country_name = input("Country: ")
    new_place += country_name + ","
    priority_value = input("Priority: ")
    new_place += priority_value + ","
    new_place += "n"
    new_places.append(new_place)
    print("{} in {} (priority {}) has been added to Travel Tracker".format(place_name, country_name, priority_value))


main()
