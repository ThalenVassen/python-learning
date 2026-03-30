#írj egy köszönő fügvényt majd hívd meg
def hello():
    print("Hello Python")
hello()

#-----------------------------------
#írj egyyfügvényt ami kap egyszámot és kiírjaa négyzetét
def square(number):
    print(number*number)
number=int(input("Adj meg egy számot és megmondom a négyzetét! "))
square(number)

#-----------------------------------
#Írj egy függvényt, ami kap két számot és vissza adja az összegüket (visszatérési értékkel)
def square_return(number1, number2):
    return number1+number2

number1=int(input("Adj meg egy számot: "))
number2=int(input("Adj meg egy másik számot: "))

numbers_sum=square_return(number1,number2)
print(numbers_sum)

#-----------------------------------
#Írj egy fügvényt, ami kap egy listát és visszadja a legnagyobb értéket
def max_number(numbers):
    for i, value in enumerate(numbers):
        if i==0:
            high_number=numbers[0]
        elif high_number<numbers[i]:
            high_number=numbers[i]
    return(high_number)

numbers = [1,2,3,5,7,9,10,1,2,5]
high_number=max_number(numbers)

print("A", numbers, "listában a legnagyobbszám a:", high_number)

#-----------------------------------
#Írj egy fügvényt, ami kap egy listát és visszadja a legnagyobb értéket ----- MÁSIK MEGOLDÁS
def max_number(numbers):
    high_number=numbers[0]
    for i in numbers:
        if high_number<i:
            high_number=i
    return(high_number)

numbers = [1,2,3,5,7,9,10,1,2,5]
high_number=max_number(numbers)

print("A", numbers, "listában a legnagyobbszám a:", high_number)

#-----------------------------------
#Írj egy fügvényt, ami kap egy listát és visszadja hány páros szám van benne
def even_number(numbers):
    even_number_count=0
    for i in numbers:
        if i%2==0:
            even_number_count+=1
    return(even_number_count)

numbers = [1,2,3,5,7,9,10,1,2,5]
even_number_count=even_number(numbers)

print("A", numbers, "listában", even_number_count,"db páros számtalálható")

#-----------------------------------
#Írj egy fügvényt, ami kap egy listát és visszadja a páros számok összegét
def even_number(numbers):
    even_number_sum=0
    for i in numbers:
        if i%2==0:
            even_number_sum+=i
    return(even_number_sum)

numbers = [1,2,3,5,7,9,10,1,2,5]
even_number_sum=even_number(numbers)

print("A", numbers, "listában", even_number_sum,"a párosos számok összege")

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

#-----------------------------------
#Írj egy fügvényt, ami kap egy listát és visszadja a páros számok számát, összegét
numbers = [1,2,3,5,7,9,10,1,2,5]

def list_analysis(numbers):
    darab = 0
    osszeg =0
    for i in numbers:
        if i %2==0:
            darab+=1
            osszeg=osszeg+i
    return (darab,osszeg)

darab, osszeg =list_analysis(numbers)

print(numbers, "listában", darab, "darab páros szám található, melyeknek összege:", osszeg)

#-----------------------------------
#Írj egy fügvényt, ami kap egy listát és visszadja a második legnagyobb számot

numbers = [5,5,5]

def second_max(numbers):
    second_max_number = None
    max_number=numbers[0]
    for i in numbers:
        if i>max_number:
            second_max_number = max_number
            max_number = i
        elif max_number !=i and (second_max_number is None or i>second_max_number):
            second_max_number=i
            
        return second_max_number

second_max_number =second_max(numbers)
if second_max_number is None:
    print("Minden szám ugyanaz!")
else:
    print(numbers, "listában a második legnagyobb szám a", second_max_number)

#-----------------------------------
#Írj egy fügvényt, ami kap egy listát és visszadja a legnagyobb páros és legkisebb páratlan számot

numbers = [1,2,3,4,5,6]
numbers_even= [2,8,6]
numbers_odd = [1,5,3]

def second_max(numbers):
    list_max_even_number = None
    list_max_odd_number = None
    for i in numbers:
        if i %2==0:
            if list_max_even_number is None or i> list_max_even_number:
                list_max_even_number = i
        elif list_max_odd_number is None or i<list_max_odd_number:
            list_max_odd_number = i
        
    return list_max_even_number, list_max_odd_number

def kiiras(numbers):
    list_max_even_number, list_max_odd_number =second_max(numbers)
    if list_max_even_number is None:
        print("Nincs páros szám!")
    else:
        print(numbers, "listában a legnagyobb páros szám:", list_max_even_number)
    if list_max_odd_number is None:
        print("Nincs páratlan szám!")
    else:
        print(numbers, "listában a legnagyobb páratlan szám a", list_max_odd_number)
    return

#vegyes lista
kiiras(numbers)

#csak páros
numbers=numbers_even
kiiras(numbers)

#csak páratlan
numbers=numbers_odd
kiiras(numbers)


#-----------------------------------
#Írj egy fügvényt, ami kap egy listát és visszadja, hogyszigoróan növekvő-e
numbers = [1,2,3,4,5,6]
numbers_random1= [1,2,2,4]
numbers_random2 = [5,3,1]

def szigoruan_novekvo(numbers):
    for i in range(0, len(numbers)-1):
        if numbers[i] >= numbers[i+1]:
            return False
    return True

def kiiratas(szigoruan_novekvoek_a_szamok,numbers):
    if szigoruan_novekvoek_a_szamok:
        print("A", numbers, "számokból álló lista szigorúan növekvő.")
    else:
        print("A", numbers, "számokból álló lista nem szigorúan növekvő.")
    return

#Alap eset
szigoruan_novekvoek_a_szamok=szigoruan_novekvo(numbers)
kiiratas(szigoruan_novekvoek_a_szamok,numbers)

#ismétlődő, de növekszik
numbers=numbers_random1
szigoruan_novekvoek_a_szamok=szigoruan_novekvo(numbers)
kiiratas(szigoruan_novekvoek_a_szamok,numbers)

#csökken
numbers=numbers_random2
szigoruan_novekvoek_a_szamok=szigoruan_novekvo(numbers)
kiiratas(szigoruan_novekvoek_a_szamok,numbers)

#-----------------------------------
#Írj egy fügvényt, ami kap egy listát és visszadja, hogy hullámzó-e (fel-le-fel)
numbers = [1,3,2,4,3,6]
numbers_random1= [5,3,4,2,3]
numbers_random2 = [1,2,3,4]
numbers_random3 = [3,2,4]
numbers_random4 = [1,3,2,1]

def hullamzo(numbers):
    if len(numbers)<3:
        return False
    for i in range(1, len(numbers)-1):
        if not(numbers[i-1] < numbers[i] > numbers[i+1] or numbers[i-1] > numbers[i] < numbers[i+1]):
            return False
    return True

def kiiratas(hullamzo_lista,numbers):
    if hullamzo_lista:
        print("A", numbers, "lista hullámzó számokat tartalmaz.")
    else:
        print("A", numbers, "lista nem hullámzó számokat tartalmaz")
    return

#True
hullamzo_lista=hullamzo(numbers)
kiiratas(hullamzo_lista,numbers)

#True
numbers=numbers_random1
hullamzo_lista=hullamzo(numbers)
kiiratas(hullamzo_lista,numbers)

#False
numbers=numbers_random2
hullamzo_lista=hullamzo(numbers)
kiiratas(hullamzo_lista,numbers)

#False
numbers=numbers_random3
hullamzo_lista=hullamzo(numbers)
kiiratas(hullamzo_lista,numbers)

#False
numbers=numbers_random4
hullamzo_lista=hullamzo(numbers)
kiiratas(hullamzo_lista,numbers)


#-----------------------------------
#Írj egy fügvényt, ami kap egy listát és visszadja, hogy hullámzó-e (fel-le-fel), úgy, hogy nézzük az irányokat
numbers = [1,3,2,4,3,6]
numbers_random1= [5,3,4,2,3]
numbers_random2 = [1,2,3,4]
numbers_random3 = [3,2,4]
numbers_random4 = [1,3,3,4]

def hullamzo(numbers):
    if len(numbers)<3:
        return False
    direction = None
    previous_direction=None
    for i in range(0, len(numbers)-1):
        if numbers[i]==numbers[i+1]:
            return False
        elif numbers[i]<numbers[i+1]:
            direction = 1
        else:
            direction = -1
        if direction == previous_direction:
            return False
        else:
            previous_direction =direction
    return True

def kiiratas(hullamzo_lista,numbers):
    if hullamzo_lista:
        print("A", numbers, "lista hullámzó számokat tartalmaz.")
    else:
        print("A", numbers, "lista nem hullámzó számokat tartalmaz")
    return

#True
hullamzo_lista=hullamzo(numbers)
kiiratas(hullamzo_lista,numbers)

#True
numbers=numbers_random1
hullamzo_lista=hullamzo(numbers)
kiiratas(hullamzo_lista,numbers)

#False
numbers=numbers_random2
hullamzo_lista=hullamzo(numbers)
kiiratas(hullamzo_lista,numbers)

#False
numbers=numbers_random3
hullamzo_lista=hullamzo(numbers)
kiiratas(hullamzo_lista,numbers)

#False
numbers=numbers_random4
hullamzo_lista=hullamzo(numbers)
kiiratas(hullamzo_lista,numbers)

#-----------------------------------
#Írj egy fügvényt, ami kap egy listát és törli a páros számokat
numbers = [2,3,2,4,3,6]
numbers_random1= [5,3,4,2,3]
numbers_random2 = [1,2,3,4]
numbers_random3 = [3,2,4]
numbers_random4 = [1,3,3,4]

def even_new_list(numbers):
    new_event_list=[]
    for i in numbers:
        if i%2!=0:
            new_event_list.append(i)
    return new_event_list

def kiiratas(new_event_list):
    print(new_event_list)
    return

#True
new_event_list=even_new_list(numbers)
kiiratas(new_event_list)

#True
numbers=numbers_random1
new_event_list=even_new_list(numbers)
kiiratas(new_event_list)

#False
numbers=numbers_random2
new_event_list=even_new_list(numbers)
kiiratas(new_event_list)

#False
numbers=numbers_random3
new_event_list=even_new_list(numbers)
kiiratas(new_event_list)

#False
numbers=numbers_random4
new_event_list=even_new_list(numbers)
kiiratas(new_event_list)

#-----------------------------------
#Írj egy fügvényt, ami megfordítja a benne lévőszámok sorrendját
numbers = [2,3,2,4,3,6]
numbers_random1= [5,3,4,2,3]
numbers_random2 = [1,2,3,4]
numbers_random3 = [3,2,4]
numbers_random4 = [1,3,3,4]

def new_list(numbers):
    reverse_list=[]
    for i in range(len(numbers)-1,-1,-1):
        reverse_list.append(numbers[i])
    return reverse_list

def kiiratas(reverse_list):
    print(reverse_list)
    return

#True
reverse_list=new_list(numbers)
kiiratas(reverse_list)

#True
numbers=numbers_random1
reverse_list=new_list(numbers)
kiiratas(reverse_list)

#False
numbers=numbers_random2
reverse_list=new_list(numbers)
kiiratas(reverse_list)

#False
numbers=numbers_random3
reverse_list=new_list(numbers)
kiiratas(reverse_list)

#False
numbers=numbers_random4
reverse_list=new_list(numbers)
kiiratas(reverse_list)

#-----------------------------------
#Írj egy fügvényt, ami megmondja a listáról,  hogy palindrom-e (ugyan azelőlről mint hátulról)
numbers = [1,2,3,3,2,1]
numbers_random1= [5,3,4,2,3]
numbers_random2 = [1,2,3,4]
numbers_random3 = [1,2,1]
numbers_random4 = [1,3,4]

def new_list(numbers):
    for i in range(len(numbers)//2):
        if numbers[i] !=numbers[len(numbers)-1-i]:
            return False
    return True

def kiiratas(palindrom_list,numbers):
    if palindrom_list:
        print("Palindrom:", numbers)
    else:
        print("Nem palindrom:", numbers)
    return

#True
palindrom_list=new_list(numbers)
kiiratas(palindrom_list,numbers)

#True
numbers=numbers_random1
palindrom_list=new_list(numbers)
kiiratas(palindrom_list,numbers)

#False
numbers=numbers_random2
palindrom_list=new_list(numbers)
kiiratas(palindrom_list,numbers)

#False
numbers=numbers_random3
palindrom_list=new_list(numbers)
kiiratas(palindrom_list,numbers)

#False
numbers=numbers_random4
palindrom_list=new_list(numbers)
kiiratas(palindrom_list,numbers)

#-----------------------------------
#Írj egy fügvényt, ami megmondja a listáról,  hogy melyik számfordulelő a legtöbbször
numbers = [1,2,1,3,2,1]
numbers_random1= [1,2,1,2,3,3,3]
numbers_random2 = []

def new_list(numbers):
    if not numbers:
        return None,None
    leggyakoribb_szam=numbers[0]
    gyakorisag = 0
    dontetlen=False
    for i in range(0,len(numbers)):
        aktualis_gyakorisag = 0
        for n in range(i,len(numbers)):
            if numbers[n] == numbers[i]:
                aktualis_gyakorisag+=1
        if gyakorisag<aktualis_gyakorisag:
            gyakorisag=aktualis_gyakorisag
            leggyakoribb_szam = numbers[i]
            dontetlen = False
        elif aktualis_gyakorisag == gyakorisag:
            dontetlen = True   
    if dontetlen:
        return None,None
    else:
        return leggyakoribb_szam,gyakorisag

def kiiratas(leggyakoribb_szam,gyakorisag,numbers):
    if leggyakoribb_szam is None:
        print("Nincs olyan szám ami többször fordul elő, mint más szám.")
    else:
        print("A",numbers,"listában a legygyakoribb szám a", leggyakoribb_szam,"ami", gyakorisag,"fordul elő.")
    return

#0
leggyakoribb_szam,gyakorisag=new_list(numbers)
kiiratas(leggyakoribb_szam,gyakorisag,numbers)

#1
numbers=numbers_random1
leggyakoribb_szam,gyakorisag=new_list(numbers)
kiiratas(leggyakoribb_szam,gyakorisag,numbers)

#2
numbers=numbers_random2
leggyakoribb_szam,gyakorisag=new_list(numbers)
kiiratas(leggyakoribb_szam,gyakorisag,numbers)

#-----------------------------------
#Írj egy fügvényt, ami megmondja két listáról, hogy anagramma-e.

numbers1 = [1,2,3]
numbers2 = [3,2,2]

def anagramma(numbers1, numbers2):
    if len(numbers1)!=len(numbers2):
        return False
    for i in numbers1:
        numbers1_i_count = 0
        for n in numbers1:
            if i ==n:
                numbers1_i_count+=1
        numbers2_m_count = 0
        for m in numbers2:
            if i ==m:
                numbers2_m_count+=1
        if numbers1_i_count!=numbers2_m_count:
            return False
    return True

numbers_anagramma=anagramma(numbers1,numbers2)

print(numbers_anagramma)