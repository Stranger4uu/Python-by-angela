# nested list in dictionary

travel_log = {
    "Rajasthan":["alwar","jaipur","ramgarh"],
    "States":["rajasthan","goa"]
}
print(travel_log["Rajasthan"][1])

nested_list = ["A","B",["C","D"]]

print(nested_list[2][1])

travel_log = {
    "Rajasthan":{
    "cities_visited": ["alwar","jaipur","ramgarh"],
    "total_visited": 26
    },
    "States":{
    "states_visited": ["rajasthan","goa","punjab"],
    "total_visited": 12
    },
}

print(travel_log["States"]["states_visited"][2])


