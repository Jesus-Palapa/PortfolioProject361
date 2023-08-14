import pypokedex


def option2():
    """Creates a list of range(x, y) of pokemon in database"""
    print("Please enter the range of pokemon you would like to see (#1-1008)")
    # block to verify input is valid integer
    try:
        start = int(input("Start: "))
    except:
        start = 0
    # if integer is not in range of available pokemon, user will have to enter input until correct
    while start <= 0:
        try:
            start = int(input("Invalid starting range, try Again: "))
        except:
            start = 0
    try:
        end = int(input("End: "))
    except:
        end = 0
    # if integer is less than start, user will have to enter input until correct
    while end < start:
        try:
            end = int(input("Invalid ending range, try Again: "))
        except:
            end = 0
    # print title and list for all pokemon in range
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tList of Pokemon Numerically")
    print("-"*180)
    counter = 0
    for i in range(start, end+1):
        counter += 1
        print(f'{i}. {pypokedex.get(dex=i).name.ljust(15)}', end="")
        if counter % 10 == 0:
            print("")
    print("\n")
