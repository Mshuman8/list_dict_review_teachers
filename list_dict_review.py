#List, Dictionary and Iteration Review

###################################################################################
LISTS
###################################################################################

##Create a list called group_names which includes the name of every person in our group.

group_names = ["Marisa", "Eliseo", "Aaron"]

##READ the List

#Print the second element of the list:
print(group_names[1])

#Identify the length of the list and print it in a sentence saying: Our group has _____ people.
print("Our group has " + str(len(group_names))

##Update the list:

#Add a "Ellie" to the group!
group_names.append("Ellie")
print(group_names)

#Reassign the fourth element to be "Jeff"
group_names[3] = "Jeff"
print(group_names)

##Iterate over the list

#Print out EACH name separately.
for person in group_names:
  print(person)

#For each person in the group, print "The #____ person to arrive was _______"
for x in range(len(group_names)):
  print("The #" + str(x + 1) + " person to arrive to our group was " + group_names[x] + ".")

###################################################################################
DICTIONARIES
###################################################################################

##Create a dictionary called group_ice_cream, of all the students in our group and their favorite ice cream.

group_ice_cream = {"Marisa": "Coffee", "Eliseo": "Rocky Road", "Aaron": "Cookie Dough"}

#What aspects of this dictionary are keys? What aspects are values?

##Read the Dictionary

#Print the second person in the dictionary.
print(group_ice_cream[1])

#Print the second person in the dictionary's favorite ice cream flavor
print(group_ice_cream["Eliseo"])

#Print the statement: "Our dictionary has _____ elements"
print("Our dictionary has " + str(len(group_ice_cream)) + " elements.")

##Update the Dictionary

#HOW DO I ADD SOMETHING TO A DICTIONARY? DO I APPEND?

#Replace Eliseo's favorite ice cream with "?"
group_ice_cream["Eliseo"] = "Coffee"

##Iterate over a dictionary

#For each person in the dictionary, print "______'s favorite ice cream is _______"
for name in group_ice_cream:
  print(name + "'s favorite ice cream is " + group_ice_cream[name])


###################################################################################
LISTS OF DICTIONARIES
###################################################################################

##Create a list called our_profiles that has a dictionary inside for each person in our group.  The dictionary should contain the person's name, age, birthday, and favorite ice cream.

our_profiles = [
  {"name": "Marisa", "age": 28, "birthday": "08/08/1990", "fav_ice_cream": "Coffee"}
  {"name": "Eliseo", "age": 29, "birthday": "06/08/1990", "fav_ice_cream": "Rocky Road"}
  {"name": "Aaron", "age": 17, "birthday": "08/08/2002", "fav_ice_cream": "Cookie Dough"}
]

##Read our list of DICTIONARIES

#Print the first element of the list. !!PLEASE NOTE THIS PRINTS A DICTIONARY BECAUSE EACH ELEMENT IS ITS OWN DICTIONARY!!
print(our_profiles[0])

#Print "_______ is ______ years old and loves _______ ice cream" for the second person in the group.
print(our_profiles[1]["name"] + " is " + our_profiles[1]["age"] + " years old and loves " + our_profiles[1][fav_ice_cream] + " ice cream.")


##Update our List

#Change the second person's age to 100.
our_profiles[1]["age"] = 100

#Add a new person to our group (Ellie, 22, 09/04/1996, Chocolate Fudge Brownie)
our_profiles.append({"name": "Ellie", "age": 22, "birthday": "09/04/1996", "fav_ice_cream": "Chocolate Fudge Brownie"})


##Iterate over the list of DICTIONARIES

#Create a list called our_birthdays of our birthdays.
our_birthdays = []

for person in our_profiles:
    our_birthdays.append(person["birthday"])

#Print a statment for each person that says: "_______'s birthday is _______ and they are currently ______ years old."
for person in our_profiles:
    print(person["name"] + "'s birthday is " + person["birthday"] + " and they are currently " + person["age"] + " years old.")
