# An aeroplane is boarding passengrs. The list is maintained on the basis of type of passenger type adult, child, senior. 
# Count total number of passengers of each type. 

passengers = ["adult", "child", "senior", "adult", "adult", "senior", "child", "senior", "adult", "child", "senior", "child", "adult", "adult", "senior", "adult", "adult"]
adult_count = 0
child_count = 0
senior_count = 0

for passenger in passengers:
  if passenger == "adult": 
    adult_count += 1
  elif passenger == "child":
    child_count += 1
  elif passenger == "senior":
    senior_count += 1 

print(f"Total adults: {adult_count}")
print(f"Total childs: {child_count}")
print(f"Total seniors: {senior_count}")