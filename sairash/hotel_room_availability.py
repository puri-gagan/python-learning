## -----------Assignment-------------- ##
"""
    Hotel Room availability
You have 5 story building hotel. Each floor has 5 rooms in it. True represents that the room is available, False represents occoupied

Total available rooms?
Total available rooms in each floor, the output should be in dict. for example, {"ground_floor": 2, "first_floor": 3, ...}
"""
room_info = {
    "ground_floor": [True, True, False, False, False],
    "first_floor": [False, True, False, True, True],
    "second_floor": [True, True, False, True, False],
    "third_floor": [False, True, False, True, False],
    "fourth_floor": [False, True, False, True, True],
}

available_room = 0
available_room_in_each_floor = {}

for floor in room_info.items():
    for is_available_room in floor[1]:
        if is_available_room:
            available_room = available_room + 1
    available_room_in_each_floor[floor[0]] = floor[1].count(True)
print(f"The available room is {available_room}")
print(f"{available_room_in_each_floor}")

