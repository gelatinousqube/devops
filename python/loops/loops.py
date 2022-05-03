
#WHILE
count = 10
while(count > 0):
    print("*" * count)
    count -= 1

#FOR RANGE
for i in range(1,11):
    print ("*" * i)

#FOR STRING
myStr = "test"
for c in myStr:
    print(c)

#FOR WITH LIST
dcList = ["Batman","Superman","Wonder Woman","Aquaman", "Flash", "Cyborg"]
for hero in dcList:
    print(hero)

#FOR WITH IF
for i in range(1,11):
    if i == 8:
        break
        print ("Inside IF:",i)                
    print (i)

for i in range(1,11):
    if i == 8:
        print ("Inside IF:",i)
        break        
    print (i)

for i in range(1,11):
    if i == 8:
        continue
        print ("Inside IF:",i)                
    print (i)

for i in range(1,11):
    if i < 8:
        pass
        print ("Inside IF:",i)                
    print (i)