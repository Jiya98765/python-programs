tuple = ("j",1,2,3,3.2)
print(tuple)

dict = {
    "name":"radha",
    "fruit":"aam",
    "1":"3",
    "another dict":{"boy":"aman"}}
print(dict)
print(dict["1"])
print(dict["another dict"]["boy"])
dict["1"] = 10
print(dict)
print(dict.keys())
print(dict["1"])
del dict["name"]
print(dict)
#dict.pop(1)
print(dict)
dict["name"] = "radhe-radhe"
print(dict)
 
set = {}
print(set)
print(type(set))
