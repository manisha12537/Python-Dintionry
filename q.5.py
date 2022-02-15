list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,] 
m={}
i=0
while i<len(list1):
        m.update({list1[i]:list2[i]})
        i=i+1
print(m)
