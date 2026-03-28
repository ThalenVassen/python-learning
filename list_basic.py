numbers = [4,8,1,6,3]
numbers_sum = 0

#numbers kiiratása
for i in numbers:
    print(i)

#numbers-ben található  
for i in numbers:
    numbers_sum = numbers_sum + i
print("A számok összege:" , numbers_sum)

numbers_even =0
#hány páros szám van a numbers-ben
for i in numbers:
    if i %2 == 0:
        numbers_even+=1
print(numbers_even, "páros szám van")

numbers_max = numbers[0]
#legnagyobbszám
for i in numbers:
    if numbers_max < i:
        numbers_max = i
print("A legnagyobb szám:" , numbers_max)

#5-nél nagyobb számok mennyisége
numbers_more_than5 = 0
for i in numbers:
    if i > 5:
        numbers_more_than5+=1
print("A listában", numbers_more_than5,"db 5-nél nagyobb szám található.")

#legnagyobb páros szám
numbers_max_even = 0
even_number = False
for i in numbers:
    if i % 2 == 0:
        numbers_max_even = i
        even_number =True
        break
for i in numbers:
    if i %2 == 0 and i>numbers_max_even:
        numbers_max_even = i
if even_number:
    print("A legnagyobb páros szám:", numbers_max_even)
else:
    print("Nincs páros szám a listában.")    

