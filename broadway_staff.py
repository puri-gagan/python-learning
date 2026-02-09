class Staff:
    def __init__(self, name, staff_id, base_salary):
        self.name = name
        self.staff_id = staff_id
        self.base_salary = base_salary
 
    def calculate_salary(self):
        return self.base_salary
 
    def display_info(self):
        print(f"Staff: {self.name} with ID: {self.staff_id} has Base salary: RS. {self.base_salary}")
 
