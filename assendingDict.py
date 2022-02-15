dict={"a":5,"b":7,"c":2,"d":1,"e":9,"f":4}
list=[]
for i in dict:
    list.append(dict[i])
for j in range(len(list)):
    for k in range(len(list)):
        if list[j]>list[k]:
            var1=list[j]
            list[j]=list[k]
            list[k]=var1
d={}
for a in range(len(list)):
    for i in dict:
        if list[a]==dict[i]:
            d[i]=list[a]
print(d)