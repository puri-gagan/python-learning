# Hotel room availability, 5 story building hotel, each floor has 5 rooms, true means available, false means booked. 
# finding total available rooms, and total available rooms in each floor. 

room_info = {"ground_floor": [True, False, True, True, True], "first_floor": [True, False, True, False, True], 
             "second floor": [True, True, False, True, True], "third floor": [True, False, True, True, True], 
             "fourth floor": [True, False, True, False, True]}

total_rooms = 0
available_rooms = 0
available_rooms_per_floor = {}

for floor, rooms in room_info.items():
    available_rooms_floorwise_count = 0
    print(f"{floor}: {rooms}")
    for room in rooms: 
        if room == True: 
            available_rooms += 1   
            available_rooms_floorwise_count += 1
    available_rooms_per_floor[floor] = available_rooms_floorwise_count        
print(f"Available rooms: {available_rooms}")
print(f"Available rooms per floor: {available_rooms_per_floor}")
