my_dict = {"Artem" : 2003, "Slava" : 1999, "Ignat" : 2005}
print(my_dict)
print(my_dict["Slava"])
print(my_dict.get("Afonya", "Такой не найден"))
my_dict.update({"Grisha" : 2001, "Timur" : 2000})
deleted = my_dict.pop("Grisha")
print(deleted)
print(my_dict)

print()

my_set = {1,2,3,4,2,5,3,1, True, "Galka", "Galka"}
print(my_set)
my_set.add("Morj")
my_set.add(8)
my_set.discard(1)
print(my_set)

