#-----------------------------------
#Írj egy függvényt, ami kap egy listát és dict segítségével megmondja melyik szám szerepel a legtöbbször
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