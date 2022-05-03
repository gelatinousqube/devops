number_of_elements = 8




for i in range(number_of_elements):
    if(i == 0):
        first = 0
        print(i)
    elif(i == 1):
        last = i
        print(i)
    else:  
        x = first + last
        print(x)      
        first = last
        last = x
        
    


# 0 1 1 2 3 5 

