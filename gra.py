# Importowanie bibliotek
import os
from colorama import init, Fore, Back, Style
import time
import sys
import random

init()

# Menu Sterujące
def Menu():
    print(Style.BRIGHT + Fore.WHITE + "                         [" + Style.BRIGHT + Fore.BLUE  + "+" +Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE  +"["+ Style.BRIGHT + Fore.BLUE  + "+" + Style.BRIGHT + Fore.WHITE + "]" + Fore.RESET)
    print(Style.BRIGHT + Fore.WHITE + "                                                   " + Fore.WHITE + "Statki\n" + Fore.RESET)
    print(Style.BRIGHT + Fore.WHITE + "                                         [1] " + Fore.YELLOW + "Zagraj w Statki!" + Fore.RESET)
    print(Style.BRIGHT + Fore.WHITE + "                                         [2] " + Fore.YELLOW + "Autorzy" + Fore.RESET)
    print(Style.BRIGHT + Fore.WHITE + "                         [" + Style.BRIGHT + Fore.BLUE  + "+" +Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE  +"["+ Style.BRIGHT + Fore.BLUE  + "+" + Style.BRIGHT + Fore.WHITE + "]" + Fore.RESET)

# Funkcje tworzące, wyświetlające i aktualizujące planszę
def Stworz_plansze(Rozmiar):
    Plansza = []
    for i in range(Rozmiar):
        Plansza.append(["O"] * Rozmiar)
    return Plansza

Plansza_gracza = Stworz_plansze(7)
Plansza_komputera = Stworz_plansze(7)

Wiersze = ["¹", "²", "³", "⁴", "⁵", "⁶", "⁷"]


def Wyswietl_obie_plansze(Plansza_gracza, Plansza_komputera):
    for i in range(0, len(Plansza)):
        print("                            " + Fore.BLUE + Wiersze[i] + " " + Fore.RESET + " ".join(Plansza_gracza[i]) + "                    " + Fore.BLUE + Wiersze[i] + " " + Fore.RESET + " ".join(Plansza_komputera[i]), sep="")

def Aktualizuj_plansze_gracza(Plansza, Kolumna_gracza, Wiersz_gracza):
    Plansza_gracza[Wiersz_gracza][Kolumna_gracza] = Style.BRIGHT + Fore.BLACK + "S" + Fore.WHITE
    os.system("cls")
    print(Style.BRIGHT + Fore.WHITE + "                         [" + Style.BRIGHT + Fore.BLUE + "+" +Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE + "[" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]" + Fore.RESET)
    print(Style.BRIGHT + Fore.GREEN + "                                                   Twój ruch" + Fore.RESET)
    print(Style.BRIGHT + Fore.WHITE + "                                                                                          O - puste pole" + Fore.RESET)
    print(Style.BRIGHT + Fore.BLACK + "                                                                                          S" + Fore.WHITE + " - pole ze statkiem" + Fore.RESET)
    print(Style.BRIGHT + Fore.WHITE + "                              Twoja Plansza:                   Plansza Komputera:         " + Fore.GREEN + "X" + Fore.WHITE + " - trafione pole" + Fore.RESET)
    print(Style.BRIGHT + Fore.BLUE + "                              ₁ ₂ ₃ ₄ ₅ ₆ ₇                      ₁ ₂ ₃ ₄ ₅ ₆ ₇            " + Fore.RED + "X" + Fore.WHITE + " - nietrafione pole" + Fore.RESET)
    
    Wyswietl_obie_plansze(Plansza_gracza, Plansza_komputera)

def Aktualizuj_plansze_komputera(Plansza, Kolumna_komputera, Wiersz_komputera):
    Plansza_komputera[Wiersz_komputera][Kolumna_komputera] = Style.BRIGHT + Fore.BLACK + "S" + Fore.WHITE
    os.system("cls")
    print(Style.BRIGHT + Fore.WHITE + "                         [" + Style.BRIGHT + Fore.BLUE + "+" +Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE + "[" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]" + Fore.RESET)
    print(Style.BRIGHT + Fore.RED + "                                                   Ruch komputera")
    print(Style.BRIGHT + Fore.WHITE + "                                                                                          O - puste pole" + Fore.RESET)
    print(Style.BRIGHT + Fore.BLACK + "                                                                                          S" + Fore.WHITE + " - pole ze statkiem" + Fore.RESET)
    print(Style.BRIGHT + Fore.WHITE + "                              Twoja Plansza:                   Plansza Komputera:         " + Fore.GREEN + "X" + Fore.WHITE + " - trafione pole" + Fore.RESET)
    print(Style.BRIGHT + Fore.BLUE + "                              ₁ ₂ ₃ ₄ ₅ ₆ ₇                      ₁ ₂ ₃ ₄ ₅ ₆ ₇            " + Fore.RED + "X" + Fore.WHITE + " - nietrafione pole" + Fore.RESET)
    
    Wyswietl_obie_plansze(Plansza_gracza, Plansza_komputera)

# Losowanie pozycji statków komputera
def Losuj_pozycje(Plansza):
    Pozycja = random.randint(0, len(Plansza) - 1)
    return Pozycja

# Rozstawianie statków na planszy (gracza)
def Rozstawianie_statkow_gracza(Plansza, Ilosc_statkow):
    for i in range(Ilosc_statkow):
        print(Style.BRIGHT + Fore.WHITE +"\n                         [" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE + "[" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]" + Fore.RESET)
        print("Pozycja Statku #%s" % (i+1))
        while True:
            try:
                Kolumna_gracza = int(input("Podaj kolumnę statku: ")) - 1
                time.sleep(0.2)
                Wiersz_gracza = int(input("Podaj wiersz statku: ")) - 1
                if Plansza_gracza[Wiersz_gracza][Kolumna_gracza] != Style.BRIGHT + Fore.BLACK + "S" + Fore.WHITE:
                    Aktualizuj_plansze_gracza(Plansza, Kolumna_gracza, Wiersz_gracza)
                    break
                else:
                    print(Style.BRIGHT + Fore.RED + "Na tym polu jest już statek!\n" + Fore.RESET)
            except IndexError:
                print(Style.BRIGHT + Fore.RED + "Koordynaty poza planszą! " + Fore.WHITE + "Wybierz inne pola.\n" + Fore.RESET)
            except ValueError:
                print(Style.BRIGHT + Fore.RED + "Podana wartość musi być liczbą! " + Fore.WHITE + "Wprowadź poprawną wartość.\n" + Fore.RESET)
   
# Rozstawianie statków na planszy (komputera)
def Rozstawianie_statkow_komputera(Plansza, Ilosc_statkow):
    for i in range(Ilosc_statkow):
        while True:
            Kolumna_komputera = Losuj_pozycje(Plansza)
            Wiersz_komputera = Losuj_pozycje(Plansza)
            if Plansza_komputera[Wiersz_komputera][Kolumna_komputera] != Style.BRIGHT + Fore.BLACK + "S" + Fore.WHITE:
                StatkiKomputera.append([Wiersz_komputera, Kolumna_komputera])
                break

StatkiKomputera = []

def StrzelanieGracza():
    global StrzalGracza_W_Kolumne
    global StrzalGracza_W_Wiersz
    print(Style.BRIGHT + Fore.WHITE +"\n                         [" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE + "[" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]" + Fore.RESET)
    while True:
        try: 
            StrzalGracza_W_Kolumne = int(input("Podaj kolumnę strzału: ")) - 1
            StrzalGracza_W_Wiersz = int(input("Podaj wiersz strzału: ")) - 1
            if Plansza_komputera[StrzalGracza_W_Wiersz][StrzalGracza_W_Kolumne] == Style.BRIGHT + Fore.GREEN + "X" + Fore.WHITE or Plansza_komputera[StrzalGracza_W_Wiersz][StrzalGracza_W_Kolumne] == Style.BRIGHT + Fore.RED + "X" + Fore.WHITE:
                print(Style.BRIGHT + Fore.RED + "Już strzelałeś w to miejsce! " + Fore.WHITE + "Wybierz inne pole.\n" + Fore.RESET)
            else:
                break
        except IndexError:
            print(Style.BRIGHT + Fore.RED + "Koordynaty poza planszą! " + Fore.WHITE + "Wybierz inne pola.\n" + Fore.RESET)
        except ValueError:
            print(Style.BRIGHT + Fore.RED + "Podana wartość musi być liczbą! " + Fore.WHITE + "Wprowadź poprawną wartość.\n" + Fore.RESET)

def StrzelanieKomputera():
    global StrzalKomputera_W_Kolumne
    global StrzalKomputera_W_Wiersz
    print(Style.BRIGHT + Fore.WHITE +"\n                         [" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE + "[" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]" + Fore.RESET)
    while True:
        StrzalKomputera_W_Kolumne = Losuj_pozycje(Plansza)
        StrzalKomputera_W_Wiersz = Losuj_pozycje(Plansza)
        if Plansza_gracza[StrzalKomputera_W_Wiersz][StrzalKomputera_W_Kolumne] == Style.BRIGHT + Fore.GREEN + "X" + Fore.WHITE or Plansza_gracza[StrzalKomputera_W_Wiersz][StrzalKomputera_W_Kolumne] == Style.BRIGHT + Fore.RED + "X" + Fore.WHITE:
            pass
        else:
            break

def TrafienieGracza(Kolumna, Wiersz):
    for statek in StatkiKomputera:
        if statek[0] == Wiersz and statek[1] == Kolumna:
            Plansza_komputera[Wiersz][Kolumna] = Style.BRIGHT + Fore.GREEN + "X" + Fore.WHITE
            return
    Plansza_komputera[Wiersz][Kolumna] = Style.BRIGHT + Fore.RED + "X" + Fore.WHITE

def TrafienieKomputera(Kolumna, Wiersz):
    if Plansza_gracza[Wiersz][Kolumna] == Style.BRIGHT + Fore.BLACK + "S" + Fore.WHITE:
        Plansza_gracza[Wiersz][Kolumna] = Style.BRIGHT + Fore.GREEN + "X" + Fore.WHITE
    else:
        Plansza_gracza[Wiersz][Kolumna] = Style.BRIGHT + Fore.RED + "X" + Fore.WHITE

def WygranaGracza():
    TrafionychStatkowGracz = 0
    for x in range(0, Rozmiar_planszy):
        for y in range(0, Rozmiar_planszy):
            if Plansza_komputera[x][y] == Style.BRIGHT + Fore.GREEN + "X" + Fore.WHITE:
                TrafionychStatkowGracz += 1
    if TrafionychStatkowGracz == 3:
        return True
    else:
        return False

def WygranaKomputera():
    TrafionychStatkowKomp = 0
    for x in range(0, Rozmiar_planszy):
        for y in range(0, Rozmiar_planszy):
            if Plansza_gracza[x][y] == Style.BRIGHT + Fore.GREEN + "X" + Fore.WHITE:
                TrafionychStatkowKomp += 1
    if TrafionychStatkowKomp == 3:
        return True
    else:
        return False

Ruch = 0 # 0 - gracz, 1 - komputer
Rozstawiono_statki_gracza = False
Rozstawiono_statki_komputera = False
temp = 0

Menu() # Wywołanie Menu Głównego
opcja = int(input("Opcja: "))
while True:
    os.system("cls") # Wyczyszczenie konsoli
    # Sprawdzanie, czy podana opcja jest prawidłowa
    while opcja != 1 and opcja != 2:
        Menu()
        print(Style.BRIGHT + Fore.RED  + "Podana opcja nie istnieje. " + Fore.WHITE + "Spróbuj ponownie." + Fore.RESET)
        opcja = int(input("Opcja: "))
        os.system("cls")
    # Gra
    if opcja == 1:
        os.system("cls") # Wyczyszczenie konsoli

        # Dane potrzebne do gry
        Rozmiar_planszy = 7
        Ilosc_statkow = 3

        Plansza = Stworz_plansze(Rozmiar_planszy)
         
        print(Style.BRIGHT + Fore.WHITE + "                         [" + Style.BRIGHT + Fore.BLUE + "+" +Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE + "[" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]" + Fore.RESET)
        if Ruch == 0: #Ruch gracza
            print(Style.BRIGHT + Fore.GREEN + "                                                   Twój ruch" + Fore.RESET)
            print(Style.BRIGHT + Fore.WHITE + "                                                                                          O - puste pole" + Fore.RESET)
            print(Style.BRIGHT + Fore.BLACK + "                                                                                          S" + Fore.WHITE + " - pole ze statkiem" + Fore.RESET)
            print(Style.BRIGHT + Fore.WHITE + "                              Twoja Plansza:                   Plansza Komputera:         " + Fore.GREEN + "X" + Fore.WHITE + " - trafione pole" + Fore.RESET)
            print(Style.BRIGHT + Fore.BLUE + "                              ₁ ₂ ₃ ₄ ₅ ₆ ₇                      ₁ ₂ ₃ ₄ ₅ ₆ ₇            " + Fore.RED + "X" + Fore.WHITE + " - nietrafione pole" + Fore.RESET)
            Wyswietl_obie_plansze(Plansza_gracza, Plansza_komputera)
            if Rozstawiono_statki_gracza == False:
                Rozstawianie_statkow_gracza(Plansza, Ilosc_statkow)
                Rozstawiono_statki_gracza = True
            if temp <= 0:
                StrzelanieGracza()
                TrafienieGracza(StrzalGracza_W_Kolumne, StrzalGracza_W_Wiersz)
                temp += 1
            os.system("cls")
            print(Style.BRIGHT + Fore.WHITE + "                         [" + Style.BRIGHT + Fore.BLUE + "+" +Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE + "[" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]" + Fore.RESET)
            print(Style.BRIGHT + Fore.GREEN + "                                                   Twój ruch" + Fore.RESET)
            print(Style.BRIGHT + Fore.WHITE + "                                                                                          O - puste pole" + Fore.RESET)
            print(Style.BRIGHT + Fore.BLACK + "                                                                                          S" + Fore.WHITE + " - pole ze statkiem" + Fore.RESET)
            print(Style.BRIGHT + Fore.WHITE + "                              Twoja Plansza:                   Plansza Komputera:         " + Fore.GREEN + "X" + Fore.WHITE + " - trafione pole" + Fore.RESET)
            print(Style.BRIGHT + Fore.BLUE + "                              ₁ ₂ ₃ ₄ ₅ ₆ ₇                      ₁ ₂ ₃ ₄ ₅ ₆ ₇            " + Fore.RED + "X" + Fore.WHITE + " - nietrafione pole" + Fore.RESET)
            Wyswietl_obie_plansze(Plansza_gracza, Plansza_komputera)
            print(Style.BRIGHT + Fore.WHITE + "                         [" + Style.BRIGHT + Fore.BLUE + "+" +Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE + "[" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]" + Fore.RESET)
            Ruch = 1 #Ruch komputera
            if WygranaGracza():
                print(Style.BRIGHT + Fore.GREEN + "Wygrałeś!\n")
                powrot = input(Style.BRIGHT + Fore.WHITE + Back.BLACK + "Powrót do Menu (" + Fore.GREEN + "T" + Fore.WHITE + "/" + Fore.RED + "N" + Fore.WHITE + "): " + Fore.RESET)
                if powrot.lower() == "t" or powrot.lower() == "ta" or powrot.lower() == "tak":
                    os.system("cls")
                    Menu()
                    opcja = int(input("Opcja: "))
                elif powrot.lower() == "n" or powrot.lower() == "ni" or powrot.lower() == "nie":
                    time.sleep(10000)
                Plansza_gracza = Stworz_plansze(7)
                Plansza_komputera = Stworz_plansze(7)
                Rozstawiono_statki_gracza = False
                Rozstawiono_statki_komputera = False
                Ruch = 0
            if WygranaKomputera():
                print(Style.BRIGHT + Fore.RED + "Przegrałeś!\n")
                powrot = input(Style.BRIGHT + Fore.WHITE + Back.BLACK + "Powrót do Menu (" + Fore.GREEN + "T" + Fore.WHITE + "/" + Fore.RED + "N" + Fore.WHITE + "): " + Fore.RESET)
                if powrot.lower() == "t" or powrot.lower() == "ta" or powrot.lower() == "tak":
                    os.system("cls")
                    Menu()
                    opcja = int(input("Opcja: "))
                elif powrot.lower() == "n" or powrot.lower() == "ni" or powrot.lower() == "nie":
                    time.sleep(10000) 
                else:
                    print(Style.BRIGHT + Fore.RED + "Nieprawidłowa opcja. " + Fore.WHITE + "Spróbuj ponownie.")
                Plansza_gracza = Stworz_plansze(7)
                Plansza_komputera = Stworz_plansze(7)
                Rozstawiono_statki_gracza = False
                Rozstawiono_statki_komputera = False
                Ruch = 0
            temp = 0
        elif Ruch == 1: #Ruch komputera
            print(Style.BRIGHT + Fore.WHITE + "\n                                                                                           O - puste pole" + Fore.RESET)
            print(Style.BRIGHT + Fore.BLACK + "                                                                                           S" + Fore.WHITE + " - pole ze statkiem" + Fore.RESET)
            print(Style.BRIGHT + Fore.WHITE + "                              Twoja Plansza:                   Plansza Komputera:          " + Fore.GREEN + "X" + Fore.WHITE + " - trafione pole" + Fore.RESET)
            print(Style.BRIGHT + Fore.WHITE + "                                                                                           " + Fore.RED + "X" + Fore.WHITE + " - nietrafione pole" + Fore.RESET)
            Wyswietl_obie_plansze(Plansza_gracza, Plansza_komputera)
            if Rozstawiono_statki_komputera == False:
                Rozstawianie_statkow_komputera(Plansza, Ilosc_statkow)
                Rozstawiono_statki_komputera = True
            if temp <= 0:
                StrzelanieKomputera()
                TrafienieKomputera(StrzalKomputera_W_Kolumne, StrzalKomputera_W_Wiersz)
                temp += 1
            print(Style.BRIGHT + Fore.WHITE +"\n                         [" + Style.BRIGHT + Fore.BLUE + "+" +Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE + "[" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]" + Fore.RESET)
            Ruch = 0 #Ruch gracza
            temp = 0
        print(Style.BRIGHT + Fore.WHITE +"\n                         [" + Style.BRIGHT + Fore.BLUE + "+" +Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE + "[" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]" + Fore.RESET)
        
    # Autorzy
    elif opcja == 2:
        os.system("cls") # Wyczyszczenie konsoli

        print(Style.BRIGHT + Fore.WHITE + "                         [" + Style.BRIGHT + Fore.BLUE + "+" +Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE + "[" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]" + Fore.RESET)
        print(Style.BRIGHT + Fore.WHITE + "                                               Statki - Autorzy" + Fore.WHITE + Fore.RESET)
        print(Style.BRIGHT + Fore.YELLOW + "\n                                       Szymon Stelmach, Szymon Przeklasa" + Fore.RESET)
        print(Style.BRIGHT + Fore.WHITE + "                         [" + Style.BRIGHT + Fore.BLUE + "+" +Style.BRIGHT + Fore.WHITE + "]" + Style.BRIGHT + Fore.BLUE + "-------------------------------------------------------" + Style.BRIGHT + Fore.WHITE + "[" + Style.BRIGHT + Fore.BLUE + "+" + Style.BRIGHT + Fore.WHITE + "]" + Fore.RESET)
        
        powrot = input(Style.BRIGHT + Fore.WHITE + Back.BLACK + "Powrót (" + Fore.GREEN + "T" + Fore.WHITE + "/" + Fore.RED + "N" + Fore.WHITE + "): " + Fore.RESET)
        if powrot.lower() == "t" or powrot.lower() == "ta" or powrot.lower() == "tak":
            os.system("cls")
            Menu()
            opcja = int(input("Opcja: "))
        elif powrot.lower() == "n" or powrot.lower() == "ni" or powrot.lower() == "nie":
            time.sleep(10000)
        else:
            pass