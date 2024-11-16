import math

def calc(x):
    if x < 30000:
        return print("Jest to kwota zwolniona z podatku.")
    elif x <= 120000:
        return math.ceil((x * 0.12) - 3600)
    elif x > 120000 and x <= 1000000:
        return math.ceil(10800 + 0.32 * (x - 120000))
    elif x > 1000000:
        return math.ceil(10800 + 0.32 * (x - 120000) + 0.04 * (x - 1000000))
    else:
        return 0  

def main():
    try:
        price = float(input("Wpisz kwotę do obliczenia (liczba dodatnia): "))
        if price < 0:
            print("Błąd: Wprowadzona kwota nie może być ujemna.")
        else:
            podatek = calc(price)
            print(f"Obliczony podatek: {podatek} zł")
    except ValueError:
        print("Błąd: Wprowadź prawidłową liczbę.")

if __name__ == "__main__":
    main()
