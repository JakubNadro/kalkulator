def dodawanie(x, y):
    return (x + y)

def odejmowanie(x, y):
    return (x-y)

def mnożenie(x, y):
    return (x * y)

def dzielenie(x, y):
    return (x / y)

def potęgowanie(x, y):
    return (x ** y)

print("Witaj w kalkulatorze!")
print("Wybierz operacje:")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnożenie")
print("4.Dzielenie")
print("5.Potęgowanie")

while True:

    wybór = input("Wybór: ")

    if wybór in ('1', '2', '3', '4'):
        x = float(input("Wybierz pierwszą cyfrę: "))
        y = float(input("Wybierz drugą cyfrę: "))

        if wybór == '1':
            print(x, "+", y, "=", dodawanie(x, y))
        elif wybór == '2':
            print(x, "-", y, "=", odejmowanie(x, y))
        elif wybór == '3':
            print(x, "*", y, "=", mnożenie(x,y))
        elif wybór == '4':
            print(x, "/", y, "=", dzielenie(x,y))
        elif wybór == '5':
            print(x, "**", y, "=", potęgowanie(x,y))
        break
    else:
        print("Zły wybór")






