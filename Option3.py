poke_list = [] * 10
def option3():
    print("")
    save_pokemon = int(input("Would you like add more pokemon to your list of favorites? [1] Yes [0] No, just view list: "))
    if save_pokemon == 1:
        enter_pokemon = str(input("Enter pokemon to add to list: "))
        poke_list.append(enter_pokemon)

    print("\t\tMy List")
    print("--------------------")
    for i in range(len(poke_list)):
        if poke_list[i] == []:
            break
        else:
            print(poke_list[i])
    print("")
    while True:
        response = int(input("Add more pokemon? [1] yes or [0] no: "))
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
