"""
Count Passenger Types
An aeroplane is boarding passengers. The list is maintained on the basis of type of passenger type adult, child, senior

count total number of passenger on each type.
"""

passengers = [
    "adult",
    "child",
    "adult",
    "senior",
    "child",
    "adult",
    "adult",
    "child",
    "adult",
    "senior",
    "child",
    "adult",
]
adults = 0
children = 0
seniors = 0

for passenger_type in passengers:
    if passenger_type == "adult":
        adults = adults + 1
    elif passenger_type == "child":
        children = children + 1
    elif passenger_type == "senior":
        seniors = seniors + 1
    else:
        print("invalid passender type.")

print("Adults:", adults)
print("Children:", children)
print("Seniors:", seniors)
