import random  # Biblioteka losowania
import time  # Biblioteka sluzaca do pomiaru czasu

############# Algorytmy #############

def sortowanieGrzebieniowe(tabA):
    n = len(tabA)
    gap = n # przypisanie przerwy pomiedzy grzebieniami sortowania
    swapped = True
    while gap != 1 or swapped == 1:
        # oblicza przerwe pomiedzy zamienianymi elementami
        gap = (gap * 10) // 13
        if gap < 1:
            return 1
        swapped = False
        # porównywanie elementu itego z itym + przerwa i zamiana
        for i in range(0, n - gap):
            if tabA[i] > tabA[i + gap]:
                tabA[i], tabA[i + gap] = tabA[i + gap], tabA[i]
                swapped = True

def sortowaniePoprzezWybieranie(tabB):
    for i in range(len(tabB)):
        # Znalezienie najmniejszego elementu
        min_idx = i
        for j in range(i + 1, len(tabB)):
            if tabB[min_idx] > tabB[j]:
                min_idx = j
        # zamiana najmniejszego elementu z pierwszym elementem
        tabB[i], tabB[min_idx] = tabB[min_idx], tabB[i]

##################################################################

def sortowanie(poczatkowa):
    tabA = poczatkowa
    tabB = poczatkowa

    with open('WynikTablicaPoczatkowa.txt', 'w') as plik:
        plik.write("Tablica poczatkowa:\n")
        for poczatkowa_el in poczatkowa:
            plik.write(str(poczatkowa_el) + '\n')

    startA = time.time()
    sortowanieGrzebieniowe(tabA)
    czasA = str(round(((time.time() - startA) * 1000), 8)) + " ms"
    # Wyswietlanie danych w konsoli
    print("Sortowanie grzebieniowe\nCzas: ", czasA, "\n", tabA)
    startB = time.time()
    sortowaniePoprzezWybieranie(tabB)
    czasB = str(round(((time.time() - startB) * 1000), 8)) + " ms"
    # Wyswietlanie danych w konsoli
    print("\nSortowanie poprzez wybieranie\nCzas: ", czasB, "\n", tabB)
    zapis(tabA, tabB, czasA, czasB)

def zapis(tabA, tabB, czasA, czasB):
    with open("Wynik.txt", 'w') as plik:
        # Dla każdego elementu w tablicach
        i = 0
        plik.write("Tablica początkowa, Sortowanie Grzebieniowe,  Sortowanie poprzez wybór\n" +
                   "czas sortowania: " + czasA + "| czas sortowania: " + czasB + "\n")

        for tabA_el, tabB_el in zip(tabA, tabB):
            i = i + 1
            # Konwertujemy elementy na ciągi znaków i zapisujemy 
            # je do pliku w formacie "tabA[i] | tabB[i]"
            plik.write("   Element nr " + str(i) + ": "
                       + str(tabA_el) + ' | ' + str(tabB_el) + '\n')
        plik.write("\n\nProgram napisany z wykorzystaniem wersji:" +
                   "\n Python 3.10.6 (Linux)")


def samodzielneWprowadzanieDanych():
    poczatkowa = []
    min = int(input("\nPodaj wartosc minimalna losowanej liczby\n"))
    max = int(input("\nPodaj wartosc maksymalna\n"))
    elementy = int(input("Podaj ilosc elementow\n"))
    # losowanie elementow tablicy
    for i in range(elementy):
        poczatkowa.append(random.randint(min, max))
    print("Tablica poczatkowa:\n", poczatkowa, "\n")
    sortowanie(poczatkowa)


def losowanieNiecalkowitychElementow():
    poczatkowa = []
    min = float(input("\nPodaj wartosc minimalna losowanej liczby\n"))
    max = float(input("Podaj wartosc maksymalna\n"))
    elementy = int(input("Podaj ilosc elementow\n"))
    # losowanie elementow tablicy
    for i in range(elementy):
        poczatkowa.append(random.uniform(min, max))
    # wypisywanie tablicy poczatkowej
    print("Tablica poczatkowa", poczatkowa, "\n")
    sortowanie(poczatkowa)


def daneZpliku():
    poczatkowa = []
    with open('tablica.txt', 'r') as plik:
        for i, line in enumerate(plik):
            poczatkowa.append(line)
            poczatkowa[i] = int(poczatkowa[i])
    print("Tablica początkowa\n", poczatkowa, "\n")
    sortowanie(poczatkowa)


def wprowadzanieDanych(metoda_wprowadzania):
    metoda_wprowadzania = input(
        "Podaj metode wprowadzania danych\n " +
        "1: Wprowadzanie wartosci dla losowanych " +
        "liczb calkowitych \n 2: " +
        "Wprowadzanie danych niecalkowitych \n " +
        "3: Wprowadzanie danych z pliku\n\n")
    slicz(metoda_wprowadzania)


def slicz(metoda_wprowadzania):
    match metoda_wprowadzania:
        case "1":
            samodzielneWprowadzanieDanych()
        case "2":
            losowanieNiecalkowitychElementow()
        case "3":
            daneZpliku()
        case _:
            print("Poprawnie wprowadz dane")
            wprowadzanieDanych(metoda_wprowadzania)


##################################################################
########################## MAIN ##################################


metoda_wprowadzania = 0
print("Sortowanie poprzez wybor, oraz grzebieniowe\n")
wprowadzanieDanych(metoda_wprowadzania)
