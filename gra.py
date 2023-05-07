import biblioteki

def stworz_plansze(wielkosc):
    plansza = []
    for i in range(wielkosc):
        plansza.append(["O"] * wielkosc)
    return plansza

def wyswietl_plansze(plansza):
    for rzad in plansza:
        print(" ".join(rzad))

wyswietl_plansze(plansza)