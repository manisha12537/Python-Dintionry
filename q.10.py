# sampleDict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }
# print(sampleDict["class"]["student"]["marks"]["history"])                                                                                



# sampleDict = { 
#   "name": "Kelly",
#   "age":25, 
#   "salary": 8000, 
#   "city": "New york" }
# list=[]
# for i in sampleDict:
#    list.append(i)
# print(list)


# sampleDict = {'a': 100, 'b': 200, 'c': 300}
# num=int(input("enter the charactor"))
# if  num in sampleDict.values():
#    print("true")
# else:
#    print("false")



# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# sampleDict["location"]=sampleDict.pop("city")
# print(sampleDict)


# sampleDict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# sum=0
# for i in sampleDict.values():
#     sum=sum+i
# print(sum)


# sampleDict = {
#      'emp1': {'name': 'Jhon', 'salary': 7500},
#      'emp2': {'name': 'Emma', 'salary': 8000},
#      'emp3': {'name': 'Brad', 'salary': 6500}
# }
# sampleDict['emp3']["salary"]=8500
# print(sampleDict)


dict1 =[{'Ten': 10, 'Twenty': 20, 'Thirty': 30},{"Ten":76,"Thirty":90}]
dict2={}
for i in dict1:
    for k,j in i.items():
        p=k
        for l in i.keys():
            if p==l:
                dict2[k]=(j)
print(dict2)

# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict1.update(dict2)
# print(dict1)



