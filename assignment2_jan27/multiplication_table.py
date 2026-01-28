# Print the multiplication table for 1 to 3. 

for i in range(1, 4):
  print(f"Multiplication table for {i}: ")
  for j in range(1, 11):
    each_result = i * j
    print(f"{i} * {j} = {each_result} ")
  print("") # print() always adds a newline automatically in the end so "\n" not required. 