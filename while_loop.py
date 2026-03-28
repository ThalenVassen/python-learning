#1-10-ig aszámok
i=1
while i <=10:
    print(i)
    i+=1

#10-től 1-iga számok
i=10
while i>=1:
    print(i)
    i-=1

#1-től 10-ig a számok összege
i=1
i_sum=0
while i<=10:
    i_sum = i_sum+i
    i+=1
print(i_sum)

# hány db páros szám van 1-20 között
i=1
i_even=0
while i<=20:
    if i%2==0:
        i_even+=1
    i+=1
print(i_even)

#szám bekérése amíg 0-t nem ad meg, majd kiírja,hogy hány számot adott meg
think_number = 0
user_number = think_number+1
tip_number = 0
while user_number != think_number:
    user_number = int(input("Kérlek adj meg egy egész számot:"))
    if user_number == think_number:
        print(tip_number,"db tippet adtál meg")
    else:
        tip_number+=1

#Egyszerűsített számbekérés
user_number = int(input("Kérlek adj meg egy egész számot:"))
tip_number = 0
while 0 != user_number:
    tip_number+=1
    user_number = int(input("Kérlek adj meg egy egész számot:"))
print(tip_number,"db tippet adtál meg")