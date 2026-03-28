#1-10 a számok, de 7-nél álljon meg
for i in range(1,11):
    if i ==7:
        break
    print(i)

#1-10-ig a páratlan számok
for i in range(1,11):
    if i%2==0:
        continue
    print(i)

#Kérj be számokat addig, amíg:
    #negatív számot nem ad meg
    #a negatív szám állítsa le a programot
    #a többi számot add össze
    #a végén írd ki az összeget
user_number = int(input("adj megegy egész számot:"))
sum_number = 0
while True:
    if user_number < 0:
        break
    sum_number = sum_number + user_number
    user_number = int(input("adj megegy egész számot:"))
print("A megadott pozitív számok összege:" , sum_number)

#1-20 között a számokat írd ki, de hagyja ki a 3-maloszthatóakat és 17-nél álljon meg
for i in range(1,21):
    if i ==17:
        break
    if i %3==0:
        continue
    print(i)