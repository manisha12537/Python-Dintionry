a= dic1={1:10, 2:20}
b=dic2={3:30,2:40}
c=dic3={5:50,6:60}
d={}
d.update(a)
d.update(b)
d.update(c)
print(d)
# make one dictionary



# {1: 10, 2: 60, 3: 30,  5: 50, 6: 60}