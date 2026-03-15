number = int(input("Please write a number:"))
evenORodd =""
number_type = ""
if number % 2 == 0:
    evenORodd = "páros"
else:
    evenORodd = "páraltan"
if number > 10:
    number_type = "nagy"
elif number == 10:
    number_type = "tíz"
else:
    number_type = "kis"

print("A beírt szám", evenORodd, "és", number_type)