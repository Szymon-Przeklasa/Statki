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

# Funkcje tworzące i wyświetlające planszę
def Stworz_plansze(Wielkosc):
    Plansza = []
    for i in range(Wielkosc):
        Plansza.append(["O"] * Wielkosc)
    return Plansza

def Wyswietl_plansze(Plansza):
    for Rzad in Plansza:
        print("                                                " + " ".join(Rzad))


while True:
    os.system('cls') # Wyczyszczenie konsoli
    Menu() # Wywołanie Menu Głównego
    opcja = int(input("Opcja: "))

    # Sprawdzanie, czy podana opcja jest prawidłowa
    while opcja != 1 and opcja != 2:
        print(Style.BRIGHT + Fore.RED  + "Podana opcja nie istnieje. " + Fore.WHITE + "Spróbuj ponownie.")
        time.sleep(0.5)
        opcja = int(input("Opcja: "))
    
    # Gra
    if opcja == 1:
        os.system('cls') # Wyczyszczenie konsoli
        Wielkosc_planszy = 7
        Plansza = Stworz_plansze(Wielkosc_planszy)
        print(Style.BRIGHT + Fore.WHITE + "                         [" + Style.BRIGHT + Fore.BLUE + "+" +Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE + "[" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]")
        print(Style.BRIGHT + Fore.WHITE + "                                                  Twój ruch" + Fore.WHITE)
        print(Style.BRIGHT + Fore.WHITE + "                                                                                      O - puste pole")
        print(Style.BRIGHT + Fore.WHITE + "                                                  Plansza:                            " + Fore.GREEN + "X" + Fore.WHITE + " - trafione pole")
        print(Style.BRIGHT + Fore.WHITE + "                                                                                      " + Fore.RED + "X" + Fore.WHITE + " - nietrafione pole")
        Wyswietl_plansze(Plansza)
        Podaj_kolumna = input("Podaj kolumnę: ")
        time.sleep(0.5)
        Podaj_wiersz = input("Podaj wiersz: ")
        print(Style.BRIGHT + Fore.WHITE +"                         [" + Style.BRIGHT + Fore.BLUE + "+" +Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE + "[" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]")
        
        input()

    # Autorzy
    elif opcja == 2:
        os.system("cls") # Wyczyszczenie konsoli
        
        print(Style.BRIGHT + Fore.WHITE + "                         [" + Style.BRIGHT + Fore.BLUE + "+" +Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE + "[" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]")
        print(Style.BRIGHT + Fore.WHITE + "                                                  Statki"+Fore.WHITE)
        print(Style.BRIGHT + Fore.WHITE + "\n                                                  Autorzy: \n" + Fore.YELLOW + "                                       Szymon Stelmach, Szymon Przeklasa")
        print(Style.BRIGHT + Fore.WHITE + "                         [" + Style.BRIGHT + Fore.BLUE + "+" +Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE + "[" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]")
        input()