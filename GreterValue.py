dict={"a":81,"b":21,"c":90,"d":98,"e":6}
list=[]
for i in dict.values():
    list.append(i)
for j in list:
    for k in list:
        if j<k:
            j=k
print(j)































       
# dict={"a":81,"b":21,"c":90,"d":98,"e":6}
# b={}
# for i,j in dict.items():
#     k=j
#     for a in dict.values():
#         if k<a:
#             k=a
#         b.update({i:k})
# print(b)




