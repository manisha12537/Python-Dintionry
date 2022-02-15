dict={"manisa":23,"nisha":78,"seema":15,"janvi":10,"shakshi":56}
d={}
for i,j in dict.items():
    k=j
    for a in dict.values():
        if k>a:
            k=a
        d.update({i:k})
print(d)




# dict={"manisa":23,"nisha":78,"seema":15,"janvi":10,"shakshi":56}
# for i,j in dict.items():
#     k=j
#     for a in dict.values():
#         if k>a:
#             k=a
# print(k)