from ast import main


def greet(name):
    print(f"Good Morning, {name}")

print(__name__)
if __name__ == "__main__" :
    n = input("Enter a name\n")
    greet(n)