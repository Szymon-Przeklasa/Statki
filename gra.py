# Importowanie bibliotek
import os
from colorama import Fore, Back, Style
import time

# Menu Sterujące
def Menu():
    print(Style.BRIGHT + Fore.WHITE + "                         [" + Style.BRIGHT + Fore.BLUE  + "+" +Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE  +"["+ Style.BRIGHT + Fore.BLUE  + "+" + Style.BRIGHT + Fore.WHITE +"]")
    print(Style.BRIGHT + Fore.WHITE + "                                                   " + Fore.WHITE + "Statki\n")
    print(Style.BRIGHT + Fore.WHITE + "                                         [1] " + Fore.YELLOW + "Zagraj w Statki!")
    print(Style.BRIGHT + Fore.WHITE + "                                         [2] " + Fore.YELLOW + "Autorzy")
    print(Style.BRIGHT + Fore.WHITE + "                         [" + Style.BRIGHT + Fore.BLUE  + "+" +Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE  +"["+ Style.BRIGHT + Fore.BLUE  + "+" + Style.BRIGHT + Fore.WHITE +"]")

# Funkcje tworzące, wyświetlające i aktualizujące planszę
def Stworz_plansze(Rozmiar):
    Plansza = []
    for i in range(Rozmiar):
        Plansza.append(["O"] * Rozmiar)
    return Plansza
def Wyswietl_plansze(Plansza):
    for Rzad in Plansza:
        print("                                                " + " ".join(Rzad))
def Aktualizuj_plansze(Plansza, Kolumna_gracza, Wiersz_gracza):
    Plansza[Wiersz_gracza][Kolumna_gracza] = Style.BRIGHT + Fore.BLACK + "S" + Fore.WHITE
    os.system('cls')
    print(Style.BRIGHT + Fore.WHITE + "                         [" + Style.BRIGHT + Fore.BLUE + "+" +Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE + "[" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]")
    print(Style.BRIGHT + Fore.GREEN + "                                                 Twój ruch")
    print(Style.BRIGHT + Fore.WHITE + "                                                                                      O - puste pole")
    print(Style.BRIGHT + Fore.BLACK + "                                                                                      S" + Fore.WHITE + " - pole ze statkiem")
    print(Style.BRIGHT + Fore.WHITE + "                                                  Plansza:                            " + Fore.GREEN + "X" + Fore.WHITE + " - trafione pole")
    print(Style.BRIGHT + Fore.WHITE + "                                                                                      " + Fore.RED + "X" + Fore.WHITE + " - nietrafione pole")
    Wyswietl_plansze(Plansza)

# Losowanie pozycji statków komputera
def Losuj_pozycje(Plansza):
    Pozycja = random.randint(0, len(plansza) - 1)
    return Pozycja

# Rozstawianie statków na planszy (gracza)
def Rozstawianie_statkow_gracza(Plansza, Ilosc_statkow):
    for i in range(Ilosc_statkow):
        print("Pozycja Statku #%s" % (i+1))
        while True:
            Kolumna_gracza = int(input("Podaj kolumnę statku: ")) - 1
            Wiersz_gracza = int(input("Podaj wiersz statku: ")) - 1
            if Plansza[Kolumna_gracza][Wiersz_gracza] != "S":
                Aktualizuj_plansze(Plansza, Kolumna_gracza, Wiersz_gracza)
                break
            else:
                print("Na tym polu jest już statek!")
      
# Rozstawianie statków na planszy (komputera)
def Rozstawianie_statkow_komputera(Plansza, Ilosc_statkow):
    for i in range(Ilosc_statkow):
        while True:
            Kolumna_komputera = Losuj_pozycje(Plansza)
            Wiersz_komputera = Losuj_pozycje(Plansza)
            if Plansza[Kolumna_komputera][Wiersz_komputera] != "S":
                Plansza[Kolumna_komputera][Wiersz_komputera] = "S"
                break

while True:
    os.system('cls') # Wyczyszczenie konsoli
    Menu() # Wywołanie Menu Głównego
    opcja = int(input("Opcja: "))

    # Sprawdzanie, czy podana opcja jest prawidłowa
    while opcja != 1 and opcja != 2:
        print(Style.BRIGHT + Fore.RED  + "Podana opcja nie istnieje. " + Fore.WHITE + "Spróbuj ponownie.")
        time.sleep(0.5) # Opóźnienie 0.5 sekundy
        opcja = int(input("Opcja: "))
    
    # Gra
    if opcja == 1:
        time.sleep(0.35)
        os.system('cls') # Wyczyszczenie konsoli

        # Dane potrzebne do gry
        Rozmiar_planszy = 7
        Ilosc_statkow = 3

        Plansza = Stworz_plansze(Rozmiar_planszy)
        
        Ruch = "gracz"

        print(Style.BRIGHT + Fore.WHITE + "                         [" + Style.BRIGHT + Fore.BLUE + "+" +Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE + "[" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]")
        if Ruch == "gracz":
            print(Style.BRIGHT + Fore.GREEN + "                                                 Twój ruch")
            print(Style.BRIGHT + Fore.WHITE + "                                                                                      O - puste pole")
            print(Style.BRIGHT + Fore.BLACK + "                                                                                      S" + Fore.WHITE + " - pole ze statkiem")
            print(Style.BRIGHT + Fore.WHITE + "                                                  Plansza:                            " + Fore.GREEN + "X" + Fore.WHITE + " - trafione pole")
            print(Style.BRIGHT + Fore.WHITE + "                                                                                      " + Fore.RED + "X" + Fore.WHITE + " - nietrafione pole")
            Wyswietl_plansze(Plansza)
            Rozstawianie_statkow_gracza(Plansza, Ilosc_statkow)

        elif Ruch == "komputer":
            print(Style.BRIGHT + Fore.RED + "                                               Ruch komputera")
            print(Style.BRIGHT + Fore.WHITE + "                                                                                      O - puste pole")
            print(Style.BRIGHT + Fore.BLACK + "                                                                                      S" + Fore.WHITE + " - pole ze statkiem")
            print(Style.BRIGHT + Fore.WHITE + "                                                  Plansza:                            " + Fore.GREEN + "X" + Fore.WHITE + " - trafione pole")
            print(Style.BRIGHT + Fore.WHITE + "                                                                                      " + Fore.RED + "X" + Fore.WHITE + " - nietrafione pole")
            Wyswietl_plansze(Plansza)
            Rozstawianie_statkow_komputera(Plansza, Ilosc_statkow)
        print(Style.BRIGHT + Fore.WHITE +"                         [" + Style.BRIGHT + Fore.BLUE + "+" +Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE + "[" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]")
        
        input()

    # Autorzy
    elif opcja == 2:
        os.system("cls") # Wyczyszczenie konsoli
        
        print(Style.BRIGHT + Fore.WHITE + "                         [" + Style.BRIGHT + Fore.BLUE + "+" +Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE + "[" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]")
        print(Style.BRIGHT + Fore.WHITE + "                                               Statki - Autorzy"+Fore.WHITE)
        print(Style.BRIGHT + Fore.YELLOW + "\n                                       Szymon Stelmach, Szymon Przeklasa")
        print(Style.BRIGHT + Fore.WHITE + "                         [" + Style.BRIGHT + Fore.BLUE + "+" +Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE + "[" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]")
        
        powrot = input(Style.BRIGHT + Fore.WHITE + Back.BLACK + "Powrót (" + Fore.GREEN + "T" + Fore.WHITE + "/" + Fore.RED + "N" + Fore.WHITE + "): ")
        if powrot.lower() == "t" or powrot.lower() == "ta" or powrot.lower() == "tak":
            True
        elif powrot.lower() == "n" or powrot.lower() == "ni" or powrot.lower() == "nie":
            time.sleep(10000)
        else:
            pass 