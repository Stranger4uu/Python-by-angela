States_names_of_INDIA = [
    "andhra pradesh",
    "arunachal pradesh",
    "assam",
    "bihar",
    "chhattisgarh",
    "goa",
    "gujarat",
    "haryana",
    "himachal pradesh",
    "jharkhand",
    "karnataka",
    "kerala",
    "madhya pradesh",
    "maharashtra",
    "manipur",
    "meghalaya",
    "mizoram",
    "nagaland",
    "odisha",
    "punjab",
    "rajasthan",
    "sikkim",
    "tamil nadu",
    "telangana",
    "tripura",
    "uttar pradesh",
    "uttarakhand",
    "west bengal"
]
print(States_names_of_INDIA[20])
print(States_names_of_INDIA[-5])


# we can alter any item in the list easily, example is below...

States_names_of_INDIA[20] = "where pink city is"
print(States_names_of_INDIA)

# appemd function can add any single item at the end of the list , example is below 

States_names_of_INDIA.append("any future state")

print(States_names_of_INDIA)


# other functions 

States_names_of_INDIA = ["rajasthan", "gujarat", "delhi", "punjab"]


# append() function can add a single item at the end of the list
States_names_of_INDIA.append("haryana")
print(States_names_of_INDIA)


# insert() function can insert a single item at a specific index
States_names_of_INDIA.insert(1, "maharashtra")
print(States_names_of_INDIA)


# extend() function can add multiple items at the end of the list
States_names_of_INDIA.extend(["goa", "assam"])
print(States_names_of_INDIA)


# remove() function can remove the first matching item from the list
States_names_of_INDIA.remove("delhi")
print(States_names_of_INDIA)


# pop() function can remove item at a specific index (default last)
States_names_of_INDIA.pop(2)   # removes item at index 2
print(States_names_of_INDIA)

States_names_of_INDIA.pop()    # removes last item
print(States_names_of_INDIA)


# clear() function can remove all items from the list
copy_for_clear = States_names_of_INDIA.copy()  # to restore later
copy_for_clear.clear()
print(copy_for_clear)


# index() function can return index number of a given item
print(States_names_of_INDIA.index("punjab"))


# count() function can return how many times an item is present
print(States_names_of_INDIA.count("punjab"))


# sort() function can arrange the list in ascending order
States_names_of_INDIA.sort()
print(States_names_of_INDIA)


# reverse() function can reverse the order of the list
States_names_of_INDIA.reverse()
print(States_names_of_INDIA)


# copy() function can create a duplicate list
new_list = States_names_of_INDIA.copy()
print(new_list)


# len() function can return the total number of items in the list
print(len(States_names_of_INDIA))


# max() function returns the max value (alphabetically in strings)
print(max(States_names_of_INDIA))


# min() function returns the min value
print(min(States_names_of_INDIA))


# sum() function returns sum of list items (works only for numbers)
numbers = [10, 20, 30]
print(sum(numbers))
