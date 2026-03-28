#szám bekérés
number = int(input("Kérlek adj meg egy számot:"))

#intervallum vizsgálat
if number >= 10 and number <= 20:
    print("A megadott szám 10 és 20 között van.")
else:
    print("A megadott szám nincs a 10-20 közötti intervallumban.")

#szélső értékvizsgálat
if number <0 or number>100:
    print("A megadott szám szélső érték.")
else:
    print("A megadott szám nem szélsőérték.")

#ideális szám vizsgálat
if number >= 10 and number <= 20 and number%2 == 0:
    print("A megadott szám ideális szám.")
else:
    print("A megadott szám nem ideális szám.")

#különleges szám
if (number%3 == 0 or number%5==0) and number%15!=0:
    print("A megadott szám különleges szám.")
else:
    print("A megadott szám nem különleges szám.")