#-----------------------------------
#Írj három fügvényt, amik kapnak egy-egy listát és visszadja a páros számok számát, összegét és a legnagyobbat

#lista
numbers = [1,21,3,5,7,9,101,1,21,5]

#Páros számok száma
def count_even(numbers):
    darab =  0
    for i in numbers:
        if i%2==0:
            darab+=1
    return darab

#Páros számok összege
def sum_even(numbers):
    osszeg = 0
    for i in numbers:
        if i%2==0:
            osszeg= osszeg+i
    return osszeg

#Legnagyobb páros szám
def max_even(numbers):
    ElsoParosSzam=True
    for i in numbers:
        if ElsoParosSzam:
            if i%2==0:
                maximum=i  
                ElsoParosSzam = False
        elif i%2==0 and i>maximum:
            maximum=i
    if ElsoParosSzam:
         return None      
    else:
        return maximum

#Vizsgálat
darab = count_even(numbers)
osszeg = sum_even(numbers)

#Eredmény
print("A", numbers, "listában", darab, "db páros szám van.")
print("A", numbers, "listában", osszeg, "a páros számok összege.")
maximum = max_even(numbers)
if maximum is None:
    print("A", numbers, "listában nincs páros szám.")       
else:
    print("A", numbers, "listában", maximum, "a legnagyobb páros szám.")