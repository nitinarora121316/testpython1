import unittest

class SalaryCalculator:

    def calculate_yearly_salary(self, hourly_rate, hours_per_week):
        weekly_salary = hourly_rate * hours_per_week
        yearly_salary = weekly_salary * 52
        return yearly_salary

class TestSalaryCalculator(unittest.TestCase):

    def test_calculate_yearly_salary(self):
        calculator = SalaryCalculator()

        # Example scenario: hourly rate of $20 and 40 hours per week
        yearly_salary = calculator.calculate_yearly_salary(20, 40)
        print(yearly_salary)

        # Ensure that the calculated salary is greater than $30,000
        self.assertGreater(yearly_salary, 30000)

if __name__ == '__main__':
    unittest.main()
