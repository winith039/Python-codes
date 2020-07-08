list=[]
n=int(input("enter no. of terms in list\n"))
print("enter terms\n")
i=0
for i in range(0,n):
    l=int(input(""))
    list.append(l)
    i=i+1
    
    
    
tupple=(1,2,34,3,5,6)
n=int(input("enter the index number"))
print(tupple[n])



mydict={
        "c":"beginner",
        "c++":"medium",
        "java":"professional"
        
        }
print(mydict)
element=input("enter the element to be deleted")
del mydict[element]
print(mydict)
