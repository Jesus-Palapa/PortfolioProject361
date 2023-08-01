import pypokedex

def option1():
    poke_name = str(input("Enter pokemon you want to search: "))
    try:
        pokemon = pypokedex.get(name = poke_name)
        print("\nPokeFax Sheet")
        print("-------------------------")
        print("Number: \t", pokemon.dex)
        print("Name: \t\t", pokemon.name.upper())
        print("Type(s): ")
        for i in range(len(pokemon.types)):
            print("\t\t\t", pokemon.types[i].upper())
        print("")
    except:
        print("\nError! Pokemon does not exist. Try checking your spelling.\n")
