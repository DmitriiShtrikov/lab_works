class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_info(self):
        return f"Сотрудник: {self.name}, ID: {self.emp_id}"

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def manage_project(self):
        return f"Менеджер {self.name} управляет проектом в отделе {self.department}."

    def get_info(self):
        return f"Менеджер: {self.name}, ID: {self.emp_id}, Отдел: {self.department}"

class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        super().__init__(name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"Технический специалист {self.name} выполняет техническое обслуживание по специальности: {self.specialization}."

    def get_info(self):
        return f"Технический специалист: {self.name}, ID: {self.emp_id}, Специализация: {self.specialization}"


class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Manager.__init__(self, name, emp_id, department)
        Technician.__init__(self, name, emp_id, specialization)
        self.subordinates = []

    def add_employee(self, employee):
        self.subordinates.append(employee)

    def manage_project(self):
        return f"TechManager {self.name} управляет проектом и выполняет техническое обслуживание."

    def get_team_info(self):
        team_info = [member.get_info() for member in self.subordinates]
        return f"Команда под управлением {self.name}:\n" + "\n".join(team_info)