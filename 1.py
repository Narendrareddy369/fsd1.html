#Tuples
# squares=[]
# for i in range(10):
#     squares
for i in range(10):
    print(i)

squares=[1,2,3,4,5]
for i in squares:
    print(i**2)

x=("A")
print(type(x))

#type casting (converting a tuple into a list)
Tuple1=(1,2,3,4,5)
print(type(Tuple1))

Tuple2=list(Tuple1)
print(type(Tuple2))

x=(1,2,3,print,str,True)
print(x.count(1))
print(x.index(1))

#Dictionary
#create and print a dictionary:
this_dict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print(this_dict)

var=dict(name="Ram",address="Tirupati",no=9874563210)
print(var)
print(type(var))

print(var.get("name"))

this_dict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
if "Name" in this_dict:
    print("Yes,'model' is one of the keys in the thisdict dictionary")
else:
    print("NO, 'model' is not present in the dictionary")
#change values
this_dict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
this_dict["year"]=2018
print(this_dict)

#update dictionary
this_dict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
this_dict.update({"year":2020})

#add dictionary items
this_dict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
this_dict["color"]="red"
print(this_dict)

this_dict.pop("model")
print(this_dict)

this_dict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
del this_dict["model"]
print(this_dict)

this_dict.clear()
print(this_dict)

my_dict=this_dict.copy()
print(my_dict)

x={1,2.5,'three',print,int}
print(x,len(x),type(x),sep='\n')

a='kannada'
print(a,len(a),type(a),sep='')
x=set(a)
print(x,len(x),type(x),sep='')
x={}
print(x,len(x),type(x),sep='\n')
x=set()
print(x,len(x),type(x),sep='\n')
x={1}
print(x,len(x),type(x),sep='\n')

# x_ls=[1,1221,55,41,'shjd',False]
# x_ls[0]

# x_set={1,1221,55,41,'shjd',False}
# x_set[0]

#sets
this_set={"apple","banana","cherry"}
this_set.add("orange")
print(this_set)

this_set={"apple","banana","cherry"}
tropical={"pineapple","mango","papaya"}
this_set.update(tropical)
print(this_set)

this_set={"apple","banana","cherry"}
mylist=["kiwi","orange"]
this_set.update(mylist)
print(this_set)
print(type(this_set))


this_set={"apple","banana","cherry"}
this_set.remove("banana")
print(this_set)


this_set={"apple","banana","cherry"}
this_set.discard("banana")
print(this_set)

a=set([1,2,3,4,5])
b=set([4,5,6,7,8])
c=a.union(b)
d=b.union(a)
print(a,b,c,d,sep='\n')


a=set([1,2,3,4,5])
b=set([4,5,6,7,8])
c=a.intersection(b)
d=b.intersection(a)
print(a,b,c,d,sep='\n')


a=set([1,2,3,4,5])
b=set([4,5,6,7,8])
c=a.difference(b)
d=b.difference(a)
print(a,b,c,d,sep='\n')

x=(1,2,3)
y=list(x)
y.append(4)
print(tuple(y))
