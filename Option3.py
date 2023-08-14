# global list to hold pokemon names entered by user
poke_list = [] * 10

def option3():
    """Creates a list of pokemon input by user"""
    print("")
    # block to check if input is valid, if invalid proceeds to print list
    try:
        save_pokemon = int(input("Would you like add more pokemon to your list of favorites? [1] Yes [0] No, just view list: "))
    except:
        save_pokemon = 0
        print("Invalid option selected. Printing current list.")
    # can choose to update list, adds input
    if save_pokemon == 1:
        enter_pokemon = str(input("Enter pokemon to add to list: "))
        poke_list.append(enter_pokemon)
    # prints list after adding pokemon
    print("\t\tMy List")
    print("--------------------")
    for i in range(len(poke_list)):
        if poke_list[i] == []:
            break
        else:
            print(poke_list[i])
    print("")
    # can continue to add pokemon until loop is broken
    while True:
        try:
            response = int(input("Add more pokemon? [1] yes or [0] no: "))
        # if input is invalid, loop is broken, list printed
        except:
            response = 0
            print("Invalid option selected. Returning to main menu")
        if response == 1:
            enter_pokemon = str(input("Enter pokemon to add to list: "))
            poke_list.append(enter_pokemon)
            continue
        elif response == 0:
            print("\t\tMy List")
            print("--------------------")
            for i in range(len(poke_list)):
                print(poke_list[i])
            break
    print("")
