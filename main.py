import math

def calc(x):
    if x < 30000:
        return 0  # Zwolniona z podatku
    elif x <= 120000:
        return math.ceil((x * 0.12) - 3600)
    elif x <= 1000000:
        return math.ceil(10800 + 0.32 * (x - 120000))
    else:
        return math.ceil(10800 + 0.32 * (x - 120000) + 0.04 * (x - 1000000))

def main():
    try:
        price = float(input("Wpisz kwotę do obliczenia (liczba dodatnia): "))
        if price < 0:
            print("Błąd: Wprowadzona kwota nie może być ujemna.")
        else:
            podatek = calc(price)
            if podatek == 0:
                print("Jest to kwota zwolniona z podatku.")
            else:
                print(f"Obliczony podatek: {podatek} zł")
    except ValueError:
        print("Błąd: Wprowadź prawidłową liczbę.")

if __name__ == "__main__":
    main()
