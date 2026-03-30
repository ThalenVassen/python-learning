#-----------------------------------
#Írj egy függvényt, ami kap egy listát és visszaadja, hogy a számok hányszor szerepelnek benne
numbers=[1,2,1,3,2,1]

def number_count(numbers):
    count={}
    for i in numbers:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count

count=number_count(numbers)
print(count)

#-----------------------------------
#Írj egy függvényt, ami kap egy listát és egy számot és visszaadja, hogy hányszor szerepel benne
numbers=[1,2,1,3,2,1]
number = 2

def number_count(numbers,number):
    count=0
    for i in numbers:
        if i ==number:
            count+=1
    return count

count=number_count(numbers,number)
print(count)

#-----------------------------------
#Írj egy függvényt, ami kap egy listát és dict segítségével megmondja melyik szám szerepel a legtöbbször
numbers=[1,2,1,3,2,1]
count={}

def number_count(numbers):
    for i in numbers:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count

count=number_count(numbers)

max_value = 0
max_key=None

for key,value in count.items():
    if value > max_value:
        max_value=value
        max_key = key
print(max_value)

#-----------------------------------
#Írj egy függvényt, ami kap egy listát és dict segítségével megmondja melyik szám szerepel a legtöbbször MÁSKÉPPEN
numbers=[1,2,1,3,2,1]

def most_frequent(numbers):
    max_value = 0
    max_key=None
    count={}
    for i in numbers:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for key,value in count.items():
        if value > max_value:
            max_value=value
            max_key = key
    return max_key

max_key=most_frequent(numbers)

print(max_key)