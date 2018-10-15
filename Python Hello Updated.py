a = "HELLO world"
b = "12345"
c = 12345.44
d = True
e = False
h = b"Hello \xf0\x9f\x98\x8e"

ds1_list = [a,b,c,d,e,h,"hello world"]
ds2_dict = {"key1":a,"key2":b,"key3":c}
#lIST can be changed
l =['a', 1 , 18, 2]
#tuple cant be changed
t =('a', 1 , 18, 2)
#Dict
dict = {"code": 'a', "Count":1 , "Age":18, "Section":2}

from collections import OrderedDict
od = OrderedDict()
od["apples"] = 5
od["pears"] = 2
od["oranges"] = 9

print ("further statement will print the list:")
print (l)
print  (l[0])
print  (l[1])

print ("further statement will print the Tuple:")
print (t)
print (t[1])
print (t[2])

for i in range(5):
    print(i)

names = ["chris", "iftach", "jay"]
for Humanname in names:
    print (Humanname)




print ("further statement will print the dict:")
print (dict)
print (dict[code])
print (dict[2])


print ("further statement will print the ordered dict:")
print (od)
print (od[code])
print (od[2])

