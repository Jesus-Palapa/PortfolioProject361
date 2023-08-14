# Name: Jesus Palapa
# OSU Email: palapacj@oregonstate.edu
# Course: CS361- Software Engineering I
# Portfolio Project
# Description: This program will allow a user to navigate Pokemon API database by generating pokemon names, generating
# pokemon information, creating pokemon lists, and viewing pokemon lists. This program also uses a microservice to
# gather pokemon facts from the API.

from Option1 import option1
from Option2 import option2
from Option3 import option3
from Option4 import option4

def menu():
    """ Main menu displayed on CLI"""
    print("\t\t\t\t\t\t\t\tMain Menu")
    print("-" * 85)
    print("[1] Pokemon Fact Sheet - search for Pokemon facts by name.")
    print("[2] List of Pokemon - generate a list of Pokemon (Intermediate).")
    print("[3] My Favorites - create and save a list of your favorite pokemon (Intermediate).")
    print("[4] Random Pokemon Generator - a random Pokemon name will appear!\n\t\t*** Great for New Fans or to be SURPRISED ***")
    print("[0] Exit")

def poke_program():
    """Runs program and calls different options on menu"""
    print("Welcome to PokeFax! Use our menu to navigate the following options to gather your pokemon facts.")
    print("To make a selection at any time, enter the number (#) corresponding to your [#] choice.\n")
    option = ""
    # loops menu/program as long as user does not choose to [0] exit
    while option != 0:
        # call menu options to print
        menu()
        # block to check if input is valid, returns to main menu if invalid
        try:
            option = int(input("\nPlease enter your option: "))
        except:
            option = 5
        # calls option 1, microservice must be run before continuing to program
        if option == 1:
            print("\nAre you sure we want to continue to Pokemon Fact Sheet?\n[1] yes (Make sure to run microservice)/ [0] return")
            # block to check if input is valid and user wishes to proceed, returns to main menu if invalid
            try:
                confirm_choice = int(input("Please enter your option: "))
            except:
                confirm_choice = 2
            print("")
            # returns to menu
            if confirm_choice == 0:
                option = 1
            # starts option 1 program
            elif confirm_choice == 1:
                option1()
                print("Return to main menu?\n[1] yes / [0] exit")
                cont_prog = int(input("Please enter your option: "))
                print("")
                if cont_prog == 1:
                    option = 1
                elif cont_prog == 0:
                    option = 0
            # if input not [0] or [1] returns to menu
            else:
                print("")
                print("Invalid option. Returning to main menu.\n")
                continue
        # calls option 2, generates a list
        elif option == 2:
            print("\nAre you sure we want to continue to List of Pokemon?\n[1] yes / [0] return")
            # block to check if input is valid and user wishes to proceed, returns to main menu if invalid
            try:
                confirm_choice = int(input("Please enter your option: "))
                print("")
            except:
                confirm_choice = 2
            # returns to menu
            if confirm_choice == 0:
                option = 2
            # starts option 2 program
            elif confirm_choice == 1:
                option2()
                print("Return to main menu?\n[1] yes / [0] exit")
                cont_prog = int(input("Please enter your option: "))
                print("")
                if cont_prog == 1:
                    option = 2
                elif cont_prog == 0:
                    option = 0
            # if input not [0] or [1] returns to menu
            else:
                print("")
                print("Invalid option. Returning to main menu.\n")
                continue
        # calls options 3, generates list of favorites, can only add list, list saved while program running
        elif option == 3:
            print("\nAre you sure we want to continue to My Favorites?\n[1] yes / [0] return")
            # block to check if input is valid and user wishes to proceed, returns to main menu if invalid
            try:
                confirm_choice = int(input("Please enter your option: "))
            except:
                confirm_choice = 2
            # returns to menu
            if confirm_choice == 0:
                option = 3
            # starts option 3 program
            elif confirm_choice ==1:
                option3()
                print("Return to main menu?\n[1] yes / [0] exit")
                cont_prog = int(input("Please enter your option: "))
                print("")
                if cont_prog == 1:
                    option = 3
                elif cont_prog == 0:
                    option = 0
            # if input not [0] or [1] returns to menu
            else:
                print("")
                print("Invalid option. Returning to main menu.\n")
                continue
        # calls option 4, random generator name
        elif option == 4:
            print("\nAre you sure we want to continue to Random Pokemon Generator?\n[1] yes / [0] return")
            # block to check if input is valid and user wishes to proceed, returns to main menu if invalid
            try:
                confirm_choice = int(input("Please enter your option: "))
            except:
                confirm_choice = 2
            # returns to menu
            if confirm_choice == 0:
                option = 4
            # starts option 4 program
            elif confirm_choice == 1:
                option4()
                print("Return to main menu?\n[1] yes / [0] exit")
                cont_prog = int(input("Please enter your option: "))
                print("")
                if cont_prog == 1:
                    option = 4
                elif cont_prog == 0:
                    option = 0
            # if input not [0] or [1] returns to menu
            else:
                print("")
                print("Invalid option. Returning to main menu.\n")
                continue
        elif option > 4 or option < 0:
            print("")
            print("Invalid option. Please choose a number 1-4 or 0 to exit.\n")
    # if chosen [0] to end program, display end message
    print("Thank you for using PokeFax for your PokeData. Goodbye!")


# run entire program
poke_program()

# MIT License
#
# Copyright (c) 2018-2023 Arnav Borborah
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.