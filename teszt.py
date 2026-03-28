#Írd ki a lokális maximumokat
all_numbers= [1,3,2,5,4]
for i in range(1,len(all_numbers)-1):
    if all_numbers[i-1]<all_numbers[i]>all_numbers[i+1]:
        print(all_numbers[i])
