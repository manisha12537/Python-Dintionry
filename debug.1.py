# a={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}

# b={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (a,b):
#     c.update(i)
# print(c)





# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3={}
# for i,j in d1.items():
#     for k,l in d2.items():
#         if i==k:
#             d3[i]=j+l
# d4={}
# for m in (d1,d2,d3):
#     d4.update(m)
# print(d4)


# char="MISSISSIPPI"

# dict={}
# for i in char:
#     if i not in dict:
#         dict[i]=1
#     else:
#         dict[i]=dict[i]+1
# print(dict)


# number=int(input("enter the number"))
# dict={}
# for i in range(1,number):
#     k=i*i
#     dict[i]=k
# print(dict)


# i=1
# j=15
# dict={}
# while i<=j:
#     k=i*i
#     dict[i]=k
#     i=i+1
# print(dict)   


# a={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# del a[1]
# print(a)



list=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI']]
dict={}
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        k=list[j][0]
        l=list[j][1]
        m=list[j][2]
        dict[k]=[l,m]
        j=j+1
    i=i+1
print(dict)




# a={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# b={}
# l=[]
# for i in a:
#     for j in a.values():
#         for k in j:
#             if k%2==0:
#                 l.append(k)

#                 # b[i]=k
# print(l)



# char="MANISHA"
# a=char[1:-1]+char[0]
# print(a)



