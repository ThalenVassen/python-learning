# Lista comprehension alapok
# páros számok kiszűrése

numbers=[1,2,3,4,5]

even =[i for i in numbers if i%2==0]

print(even)

#-------------------------------
# Lista comprehension alapok
# minden szám négyzete

numbers=[1,2,3,4,5]

even =[i*i for i in numbers]

print(even)

#-------------------------------
# Lista comprehension alapok
# Írj egy lista comprehensiont, ami csak a páros számok négyzetét adja vissza

numbers = [1,2,3,4,5]
even = [i*i for i in numbers if i%2==0]
print(even)

#-------------------------------
# Lista comprehension alapok
# Írj egy lista comprehensiont:
#   1) ami a számokat páros esetén megtartja,
#   2) páratlan esetén megszorozza 2-vel

numbers = [1,2,3,4,5]
result = [i if i%2==0 else i *2 for i in numbers]

print(result)

#-------------------------------
# Lista comprehension alapok
# Írj egy lista comprehensiont:
#   1) ami csak a pozitív számokat tartja meg, a negatívakat kihagyja 

numbers = [-2, -1, 0, 1, 2, 3]

result = [i for i in numbers if i>0]

print(result)

#-------------------------------
# Lista comprehension alapok
# Írj egy lista comprehensiont:
#   1) ami minden szám abszolút értékét adja vissza

numbers = [-3, -1, 0, 2, -5]

result = [i if i>=0 else i*(-1) for i in numbers]

print(result)