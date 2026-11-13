
# OUTPUT

"""

Enter the Number : 5
*        *  
  *    *    
    *      
  *    *    
*        *  

"""

a = int(input("Enter the Number : "))
for i in range(1,a+1):
    for j in range(1,a+1):
        if i == j :
            print("*" ,end="  ")
        elif  i+j==(a+1):
            print("*" ,end="  ")
        else:
            print(" ",end=" ")
    print()
