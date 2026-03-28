#Írj egy függvényt, ami kap két számot és vissza adja az összegüket (visszatérési értékkel)

def square_return(number1, number2):
    return number1+number2

number1=int(input("Adj meg egy számot: "))
number2=int(input("Adj meg egy másik számot: "))

numbers_sum=square_return(number1,number2)

print(numbers_sum)