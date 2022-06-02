list=[]
n=int(input("enter no. of terms in list\n"))
print("enter terms\n")
i=0
for i in range(0,n):
    l=int(input(""))
    list.append(l)
    i=i+1
j=0
print("\n")5
for j in range(0,n):
    if(list[j]>0):
        print(list[j])
    j=j+1
