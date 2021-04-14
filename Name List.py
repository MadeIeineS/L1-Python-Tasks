names = ["Evi", "Madeleine", "Dan", "Kelsey", "Cayden", "Hayley", "Darian"]

#Print the list but alphabetised
print(sorted(names))

#Task 2, checking if a name is in the list or not
name = input("What is your name? ").strip().title()

if name in names:
    print("Your name is already in the list")
else:
    print("Your name is not in the list")

#Task 3
replace_name = input("Would you like to replace a name? ")
if replace_name == "yes":
    new_name = input("What is your name? ")
    replace_names = input("What name would you like to replace? ")
    index = names.index(replace_names)
    index = new_name
    print(names.replace(index, new_name))

#Task 4,adding a name

add_name = input("Would you like to add a name? ")
if add_name == "yes":
    name_to_add = str(input("What name would you like to add? "))
    names.append(name_to_add)
    print(names)




