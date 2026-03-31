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

#-----------------------------------
#Írj egy függvényt, ami kap egy listát és dict segítségével megmondja melyik szám szerepel a legtöbbször,d9ntetlenesetén None
numbers=[1,2,2,2]

def most_frequent(numbers):
    max_value = 0
    max_key=None
    count={}
    dontetlen =False
    for i in numbers:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for key,value in count.items():
        if value == max_value:
            dontetlen =True
        elif value > max_value:
            max_value=value
            max_key = key
            dontetlen =False
    if dontetlen:
        return None
    else:
        return max_key

max_key=most_frequent(numbers)

print(max_key)

#-----------------------------------
#Írj egy függvényt, ami kap egy listát és dict segítségével megmondja melyik szám szerepel a legtöbbször - gGET használata
numbers=[1,2,1,3,2,1]

def most_frequent(numbers):
    max_value = 0
    max_key=None
    count={}
    dontetlen =False
    for i in numbers:
        count[i]=count.get(i,0)+1
    for key,value in count.items():
        if value == max_value:
            dontetlen =True
        elif value > max_value:
            max_value=value
            max_key = key
            dontetlen =False
    if dontetlen:
        return None
    else:
        return max_key

max_key=most_frequent(numbers)

print(max_key)

#-----------------------------------
#Írj egy függvényt, ami kap egy listát és megmondja melyik fordul elő egyszer
numbers=[1,2,1,3,2,4]
target=1

def target_mark(numbers,target):
    target_key=[]
    count={}
    for i in numbers:
        count[i]=count.get(i,0)+1
    for key,value in count.items():
        if value == target:
            target_key.append(key)

    return target_key

target_key=target_mark(numbers,target)

print(target_key)

#-----------------------------------
#Írj egy függvényt, ami kap egy listát és megmondja van-e benne ismétlés
numbers=[1,2,1,4]

def recurrence_mark(numbers):
    count={}
    for i in numbers:
        count[i]=count.get(i,0)+1
        if count[i]>1:
            return True
    return False

recurrence=recurrence_mark(numbers)

print(recurrence)

#-----------------------------------
#Írj egy függvényt, ami kap egy listát és megmondja van-e benne ismétlés SET
numbers=[1,2,3,4]

def recurrence_mark(numbers):
    return len(numbers)!=len(set(numbers))

recurrence=recurrence_mark(numbers)

print(recurrence)