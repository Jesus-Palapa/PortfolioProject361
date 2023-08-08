from Option1 import option1
from Option2 import option2
from Option3 import option3
from Option4 import option4
def menu():
    #main menu
    print("\t\t\t\t\t\t\tMain Menu")
    print("------------------------------------------------------------------------")
    print("[1] Pokemon Fact Sheet - search for Pokemon facts by name.")
    print("[2] List of Pokemon - generate a list of Pokemon (Intermediate).")
    print("[3] My Favorites - create and save a list of your favorite pokemon (Intermediate).")
    print("[4] Random Pokemon Generator - a random Pokemon name will appear!\n\t\t*** Great for New Fans or to be SURPRISED ***")
    print("[0] Exit")

def poke_program():
    print("Welcome to PokeFax! Use our menu to navigate the following options to gather your pokemon facts.")
    print("To make a selection at any time, enter the number (#) corresponding to your [#] choice.\n")
    option = ""
    while option != 0:
        menu()
        option = int(input("\nPlease enter your option: "))
        if option == 1:
            print("\nAre you sure we want to continue to Pokemon Fact Sheet?\n[1] yes (Make sure to run microservice)/ [0] return")
            confirm_choice = int(input("Please enter your option: "))
            print("")
            if confirm_choice == 0:
                option = 1
            else:
                option1()
                print("Return to main menu?\n[1] yes / [0] exit")
                cont_prog = int(input("Please enter your option: "))
                print("")
                if cont_prog == 1:
                    option = 1
                elif cont_prog == 0:
                    option = 0
        elif option == 2:
            print("\nAre you sure we want to continue to List of Pokemon?\n[1] yes / [0] return")
            confirm_choice = int(input("Please enter your option: "))
            print("")
            if confirm_choice == 0:
                option = 2
            else:
                option2()
                print("Return to main menu?\n[1] yes / [0] exit")
                cont_prog = int(input("Please enter your option: "))
                print("")
                if cont_prog == 1:
                    option = 2
                elif cont_prog == 0:
                    option = 0
        elif option == 3:
            print("\nAre you sure we want to continue to My Favorites?\n[1] yes / [0] return")
            confirm_choice = int(input("Please enter your option: "))
            if confirm_choice == 0:
                option = 3
            else:
                option3()
                print("Return to main menu?\n[1] yes / [0] exit")
                cont_prog = int(input("Please enter your option: "))
                print("")
                if cont_prog == 1:
                    option = 3
                elif cont_prog == 0:
                    option = 0
        elif option == 4:
            print("\nAre you sure we want to continue to Random Pokemon Generator?\n[1] yes / [0] return")
            confirm_choice = int(input("Please enter your option: "))
            if confirm_choice == 0:
                option = 4
            else:
                option4()
                print("Return to main menu?\n[1] yes / [0] exit")
                cont_prog = int(input("Please enter your option: "))
                print("")
                if cont_prog == 1:
                    option = 4
                elif cont_prog == 0:
                    option = 0
        elif option > 4:
            print("")
            print("Invalid option. Please choose a number 1-4 or 0 to exit.\n")
    print("Thank you for using PokeFax for your PokeData. Goodbye!")

poke_program()
