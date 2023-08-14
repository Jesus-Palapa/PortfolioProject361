import random
import pypokedex

def option4():
    """Generates a random pokemon name"""
    poke_rand = random.randint(0, 1008)
    pokemon = pypokedex.get(dex = poke_rand)
    poke_name = pokemon.name
    print("\nGenerator Completed")
    print("--------------------")
    print("Pokemon Name:", poke_name)
    print(f'Try entering {poke_name} in the [1] Pokemon Fact Sheet.\n')
