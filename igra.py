import math
import random
ime = input("Upisi svoje ime ")
broj_pobjeda = int(input("Na koliko pobjeda zeliš igrati? "))
print("Upute su slijedeće: upiši svoj odabir(kamen/skare/papir), a računalo će istovremeno odabrati te će biti prikazan njegov odabir i pobjednik")
print("Upisi samo neku od opcija i sve malim slovima")

igrac_pobjeda = 0
aipobjeda = 0
reset = 0
while igrac_pobjeda<broj_pobjeda and aipobjeda<broj_pobjeda:
    if(reset == 1):
        ime = input("Upisi svoje ime ")
        broj_pobjeda = int(input("Na koliko pobjeda zeliš igrati? "))
    odabir_igrac = (input("Upiši 1 od opcija: ")).lower()
    if(odabir_igrac[0] == 'š'):
        odabir_igrac = "s" + odabir_igrac[1:]
    if(odabir_igrac == 'kamen'):
        int_odabir_igrac = 1
    if(odabir_igrac == 'skare'):
        int_odabir_igrac = 2
    if(odabir_igrac == 'papir'):
        int_odabir_igrac = 3
    y = int_odabir_igrac
    x = random.randint(1,3)
    if(x == 1):
        odabir_ai = "kamen"
        print("Računalo bira kamen")
    if(x == 2):
        odabir_ai = "skare"
        print("Računalo bira skare")
    if(x == 3):
        odabir_ai = "papir"
        print("Računalo bira papir")

    if(x == 1 and y == 1):
        print("Nema pobjednika")
        print(ime + " " + str(igrac_pobjeda) +':' + str(aipobjeda) + " racunalo")
    if(x == 1 and y == 2):
        print("Računalo pobjeđuje")
        aipobjeda += 1
        print(ime + " " +str(igrac_pobjeda) +' : ' + str(aipobjeda) + " racunalo")

    if(x == 1 and y == 3):
        print("Igrac pobjeđuje")
        igrac_pobjeda += 1
        print(ime + " " + str(igrac_pobjeda) + ' : ' + str(aipobjeda) + " racunalo")
    if(x == 2 and y == 1):
        print("Igrac pobjeduje")
        igrac_pobjeda += 1
        print(ime + " " + str(igrac_pobjeda) +' : ' + str(aipobjeda) + " racunalo")
    if(x == 2 and y == 2):
        print("Nema pobjednika")
        print(ime + " " + str(igrac_pobjeda) +' : ' + str(aipobjeda) + " racunalo")
    if(x == 2 and y == 3):
        print("Računalo pobjeđuje")
        aipobjeda += 1
        print(ime + " " +str(igrac_pobjeda) + ' : ' + str(aipobjeda) + " racunalo")

    if(x == 3 and y == 1):
        print("Računalo pobjeduje")
        aipobjeda += 1
        print(ime + " " +str(igrac_pobjeda) + ' : ' + str(aipobjeda) + " racunalo")

    if(x == 3 and y == 2):
        print("Igrac pobjeduje")
        igrac_pobjeda += 1
        print(ime + " " +str(igrac_pobjeda) + ' : ' + str(aipobjeda) + " racunalo")

    if(x == 3 and y == 3):
        print("Nema pobjednika")
        print(ime + " " +str(igrac_pobjeda) + ' : ' + str(aipobjeda) + "racunalo")
    reset = 0
    if(igrac_pobjeda == broj_pobjeda   ):
        print(ime+ " je pobjednik")
        kraj = input("Pritisni enter za zatvaranje ili o za novu igru ")
        if (kraj == "o" or kraj == "O"):
            aipobjeda = 0
            igrac_pobjeda = 0
            ime = ""
            reset = 1
    if(aipobjeda == broj_pobjeda):
        print("Računalo je pobjednik")
        kraj = input("Pritisni enter za zatvaranje ili o za novu igru ")
        if(kraj == "o" or kraj == "O"):
            aipobjeda=0
            igrac_pobjeda=0
            ime = ""
            reset  = 1
