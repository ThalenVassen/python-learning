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