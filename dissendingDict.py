dict={"a":5,"b":7,"c":2,"d":1,"e":9,"f":4,}
list=[]
for i in dict:
    list.append(dict[i])
for a in range(len(list)):
    for b in range(len(list)):
        if list[a]<list[b]:
            m=list[a]
            list[a]=list[b]
            list[b]=m
d={}
for p in range(len(list)):
    for i in dict:
        if list[p]==dict[i]:
            d[i]=list[p]
print(d)








