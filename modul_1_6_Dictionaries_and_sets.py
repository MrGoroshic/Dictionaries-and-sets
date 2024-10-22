my_dict = {"Artem" : 2003, "Slava" : 1999, "Ignat" : 2005}
print(my_dict)
print(my_dict["Slava"])
print(my_dict.get("Afonya"))
my_dict.update({"Grisha" : 2001, "Timur" : 2000})
a = my_dict["Grisha"]
del my_dict["Grisha"]
print(a)
print(my_dict)

my_set = {1,2,3,4,2,5,3,1, True, "Galka", "Galka"}
print(my_set)
my_set.add((8,"Morj"))
my_set.discard(1)
print(my_set)

