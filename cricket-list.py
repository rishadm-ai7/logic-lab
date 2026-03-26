runs = [1,2,4,1,5,6,3,2,4,5,6,2,3,3,1,1,0,0,1,2,3,5,1]

b1=0
b2=0
lst=[b1,b2]
counter = 0


for i in range(0,len(runs)):
    lst[counter]+=runs[i]
    if (runs[i]%2==1) != ((i+1)%6==0):
        counter = 1-counter

b1,b2 = lst

print(b1,b2)