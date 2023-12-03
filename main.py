class Employee:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def calculate_salary(self, position, experience):
        # Задаємо базовий оклад для кожної посади
        position_salary = {
            'manager': 50000,
            'developer': 60000,
            'designer': 55000
        }

        # Коефіцієнт для додаткового винагородження за стаж
        experience_bonus = 1000 * experience

        # Розраховуємо оклад
        base_salary = position_salary.get(position, 0)
        total_salary = base_salary + experience_bonus

        # Розраховуємо податковий збір (припустимо ставку податку 15%)
        tax = 0.15 * total_salary

        return total_salary, tax

    def display_info(self, position, experience):
        salary, tax = self.calculate_salary(position, experience)
        print(f"Інформація про співробітника:\n"
              f"Прізвище: {self.last_name}\n"
              f"Ім'я: {self.first_name}\n"
              f"Посада: {position}\n"
              f"Оклад: {salary} грн\n"
              f"Податковий збір: {tax} грн")


# Приклад використання класу Employee
employee1 = Employee("Петров", "Іван")
employee1.display_info("developer", 3)

