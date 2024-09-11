employee_list = [
   {"id": 2835, "name": "Janice", "department": "UX"},
   {"id": 3546, "name": "Eduardo", "department": "QC"},
   {"id": 8932, "name": "Megan", "department": "Management"}
]
def mod(employee_list):
   temp = employee_list['name'] + " " + employee_list["department"]
   return temp

def to_mod_list(employee_list):
   map_employee = map(mod, employee_list)
   mod_employee_list = list(map_employee)
   return mod_employee_list

   raise NotImplementedError()

def generate_users(mod_list):
   usernames = [x.replace(" ", "_") for x in mod_list]
   return usernames

   raise NotImplementedError()

def main():
   mod_emp_list = to_mod_list(employee_list)
   print("Modified employee list: " + str(mod_emp_list) + "\n")
   print(f"Usernames: {generate_users(mod_emp_list)}\n")

if __name__ == "__main__":
   main()