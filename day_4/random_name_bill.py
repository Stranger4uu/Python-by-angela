import random

friends = ["Yash","Tanishk","Nischay","Harsh","Jay","Abhi"]

print(random.choice(friends))
# Or
chosen_friend = random.choice(friends)
print(chosen_friend)
# Or
chosen_friend = random.randint(0,5)
print(friends[chosen_friend])
