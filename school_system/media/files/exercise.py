fruits=("apple","mangoes","grapes","banana")
print(fruits)
x=()
print(x)
tuplex=tuple()
print(tuplex)
numbers=(1,2,3,4,5)
print(numbers[1])
n=(4,)
print(n)
y={0:10,1:20}
print(y[1])
a={0:10,1:20,}
a[2]=30
print(a)
students={"age":"sharon","status":"grace","name":"loyce"}
students["class"]="jane"
print(students)
country_codes={"kenya":254,"uganda":253,"rwanda":255}
country_codes["Tanzania"]=256
print(country_codes)
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic1.update(dic2)
print(dic1)
dic1.update(dic3)
print(dic1)
print(3 in dic1)
print(7 in dic1)
print(dic1)
for key in country_codes:
    print(key) 
d=dict()
# for x in range(1,16):
#     d[x]=x**2
#     print(d)
    d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
# d = d1.copy()
d.update(d2)
print(d)






