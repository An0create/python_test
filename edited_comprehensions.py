employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]

def mod(employee_list):
   temp = employee_list['name'] + "_" + employee_list["department"]
   return temp

def to_mod_list(employee_list):
    map_employee = map(mod, employee_list)
    mod_employee_list = list(map_employee)
    return mod_employee_list

    raise NotImplementedError()

def generate_usernames(mod_list):
    usernames = [x.replace(" ", "_") for x in mod_list]
    return usernames

    raise NotImplementedError()

def map_id_to_initial(employee_list):
    id_to_initial = {employee["id"]: employee["name"][0] for employee in employee_list}
    return id_to_initial

    raise NotImplementedError()

def main():
   mod_emp_list = to_mod_list(employee_list)
   print("Modified employee list: " + str(mod_emp_list) + "\n")

   print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")

   print(f"Initials and ids: {map_id_to_initial(employee_list)}")

if __name__ == "__main__":
   main()