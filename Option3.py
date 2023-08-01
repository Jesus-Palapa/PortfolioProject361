poke_list = [] * 10
def option3():
    print("")
    save_pokemon = int(input("add pokemon?"))
    if save_pokemon == 1:
        enter_pokemon = str(input("enter pokemon"))
        poke_list.append(enter_pokemon)

    print("\t\tMy List")
    print("--------------------")
    for i in range(len(poke_list)):
        if poke_list[i] == []:
            break
        else:
            print(poke_list[i])
