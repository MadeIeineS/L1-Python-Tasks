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
new_name = input("What is your name?")
replace = input("What name would you like to replace?")

if new_name in names:
    print("That name is already in the list")
else:
    replace


