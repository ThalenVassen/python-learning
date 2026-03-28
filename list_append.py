#Kérj be 5 számot a felhasználótól, és tedd bele egy listába. A végén írd ki a listát.

user_list=[]
for i in range(5):
    user_number = int(input("Kérlek adjmegegyszámot:"))
    user_list.append(user_number)
print("A felhasználó általmegadott számok:" , user_list)

#Add meg az előző listában található számok összegét
user_list_sum = 0
for i in user_list:
    user_list_sum = user_list_sum + i
print("A felhasználó által megadott számok összege:", user_list_sum)

#A lista legnagyobb számának a megtalálása
user_list_max = user_list[0]
for i in user_list:
    if i > user_list_max:
        user_list_max =i
print("A listában található legnagyobbszám:", user_list_max)

#Addig kérj be számokat afelhasználótól, amíg 0-t nem ad meg
user_new_list = []
while True:
    user_new_number = int(input("Kérlek adjmegegyszámot:"))
    if user_new_number == 0:
        break
    user_new_list.append(user_new_number)
print("A felhasználó által megadott számok:", user_new_list)

#Az előző bővítve azzal, hogya párosszámokat külön is kiiratjuk
user_new_list = []
user_new_list_even =[]
while True:
    user_new_number = int(input("Kérlek adjmegegyszámot:"))
    if user_new_number == 0:
        break
    user_new_list.append(user_new_number)
    if user_new_number %2==0:
        user_new_list_even.append(user_new_number)

print("A felhasználó által megadott számok:", user_new_list)
print("Ebből a párosszámok:", user_new_list_even)

#első páros szám megtalálása és kiírása
numbers=[1,2,3,4,5]
found_even =  True
for i in numbers:
    if i%2==0:
        print(i)
        found_even =  False
        break
if found_even:
    print("Nincs páros szám.")


#első páros szám megtalálása és kiírása
numbers=[1,3,4,6,8]
found_even_MoreThan5 = True
for i in numbers:
    if i>5 and i%2==0:
        print("Az első 5-nél nagyobb páros szám:", i)
        found_even_MoreThan5 =False
        break
if found_even_MoreThan5:
    print("Nincs 5-nélnagyobbpáros szám a listában.")


# Egy lista összes páros számát kiírja
all_numbers=[1,2,3,4,5,6,7,8,9,10,11,12]
even_numbers=[]
for i in all_numbers:
    if i %2==0:
        even_numbers.append(i)

if not even_numbers:
    print("Egy páros számot sem tartalmaza lista.")
else:
    print("A páros számoka az eredeti listában:",even_numbers)

#Eredeti lista elemeinek négyzetét írd ki
all_numbers=[1,2,3,4,5,6,7,8,9,10,11,12]
all_numbers_square=[]
for i in all_numbers:
    all_numbers_square.append(i*i)
if not all_numbers:
    print("Nem volt szám a listában amit négyzetre kellett volna emelni.")
else:
    print("Az eredeti lista:", all_numbers, "és ezek négyzete:", all_numbers_square)


#Vizsgálj megegy listát, addmeg hány páros szám vanésmennyi azok összege
all_numbers=[1,2,3,4,5,6,7,8,9,10,11,12]
even_numbers=0
even_numbers_sum=0

for i in all_numbers:
    if i%2==0:
        even_numbers+=1
        even_numbers_sum=even_numbers_sum+i

if not all_numbers:
    print("Nem volt párosszám a listában.")
else:
    print(even_numbers, "db páros számot találtam, amelyeknek az összege:", even_numbers_sum)