import pypokedex

def option2():
    start = int(input("start: "))
    while start <= 0:
        start = int(input("Try Again: "))
    end = int(input("end: "))
    while end < start:
        end = int(input("Try Again: "))
    print("\t\t\tList of Pokemon Numerically")
    counter = 0
    for i in range(start, end+1):
        counter += 1
        print(pypokedex.get(dex=i).name.ljust(15), end="")
        if counter % 10 == 0:
            print("")
    print("\n")
