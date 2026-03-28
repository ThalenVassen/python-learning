#1-től 10-ig a számok
for i in range(10):
    print(i+1)

print("-----")

#1-20-ig a párosszámok
for i in range (20):
    if (i+1)%2==0:
        print(i+1)

print("-----")

#10-től 1-ig visszafelé a számok 1
for i in range(10):
    print(-1*(i-10))

print("-----")

#10-től 1-ig visszafelé a számok 2
n=10
for i in range(10):
    print(n-i)

print("-----")

#10-től 1-ig visszafelé a számok 3
for i in range(10,0,-1):
    print(i)

print("-----")
# 1-től 5-ig a számok és hogy páros vagy páratlan-e
for i in range(5):
    if (i+1)%2:
        print(i+1, "páratlan")
    else:
        print(i+1, "páros")

print("-----")

#1-10-ig aszámok összege
n=0
for i in range(10):
    n= n+i+1
print(n)

print("-----")

#1-10-ig aszámok összege2
n=0
for i in range(11):
    n= n+i
print(n)

print("-----")

# Hány páros szám van 1-20 között?
n=0
for i in range(1,21,1):
    if i%2==0:
        n+=1
print(n)

print("-----")

# 1-10 között van-e páros szám?
van = False
for i in range(1,1,1):
    if (i)%2==0:
        van = True
if van:
    print("van páros szám")
else:
    print("nincs páros szám)")

print("-----")

#1-20 közötti legnagyobb szám
max= 0
for i in range(1,21,1):
    if i>max:
        max=i
print(max)

print("-----")

#1-20 közötti legnagyobb páros szám
max= 0
for i in range(1,21,1):
    if i%2==0 and i>max:
        max=i
print(max)

