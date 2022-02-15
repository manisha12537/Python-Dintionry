# a= [{"first":"1"}, 
# {"second": "2"}, 
# {"third": "1"}, 
# {"four": "5"}, 
# {"five":"5"}, 
# {"six":"9"},
# {"seven":"7"}

# ]
# b=[]
# for i in a:
#     for j in i.values():   
#         if j not in b:
#             b.append(j)
# print(b) 
# unick value


list=['2', '7',[3,4,6], '9', '5',[9,7,9],[6,9]] 
i=0
k=[]
while i<len(list):
    j=0
    while j<len(list[i]):
        k.append(list[i][j])
        # print(list[i][j])
        j=j+1
    i=i+1
print(k)






price=int(input("enter the charactor"))
list=[5000,2000,500,200,100,50,20,10,5,2,1]
dict={}
for i in list:
    j=price//i
    dict[i]=j
    price=price-i*j
print(dict)





