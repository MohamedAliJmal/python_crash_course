def test(unsorted,sorted_list):
        for i in range(len(unsorted)-1):
            bl=True
            while bl:
                for j in range(len(unsorted)-1):
                    if unsorted[j]<unsorted[j+1]:
                        unsorted[j],unsorted[j+1]=unsorted[j+1],unsorted[j]
                    else :
                        bl=False
        for i in unsorted:
            sorted_list.append(i)
    

a=[1,2,3,4,5]
b=[]
test(a,b)
print(b)
