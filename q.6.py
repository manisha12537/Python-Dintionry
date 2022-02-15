dic={"ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3,
}
a={}
for i in dic:
    a.update({i:dic[i]})
print(a)

# remove.duplicate