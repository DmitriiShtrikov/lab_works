from package_for7 import Company_Employers


employee1 = Company_Employers.Employee("Алексей Петров", 1)
manager1 = Company_Employers.Manager("Мария Иванова", 2, "Маркетинг")
technician1 = Company_Employers.Technician("Иван Смирнов", 3, "Электронные системы")
tech_manager = Company_Employers.TechManager("Сергей Васильев", 4, "IT", "Программирование")

tech_manager.add_employee(employee1)
tech_manager.add_employee(manager1)
tech_manager.add_employee(technician1)

print(employee1.get_info())
print(manager1.get_info())
print(technician1.get_info())
print(tech_manager.get_team_info())