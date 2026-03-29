#-----------------------------------
#Írj egy fügvényt, ami megmondja két listáról, hogy anagramma-e.

numbers1 = [1,2,3]
numbers2 = [3,2,2]

def anagramma(numbers1, numbers2):
    if not numbers1 or not numbers2 or len(numbers1)!=len(numbers2):
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