portion_down_payment = 0.25
current_savings = 0
r_rate = 0.04


annual_salary= float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))


monthly_salary = annual_salary / 12

total_dreamed_savings = total_cost * portion_down_payment

months = 0 # inicializando contador de meses

while current_savings < total_dreamed_savings:
    current_savings += monthly_salary * portion_saved + current_savings*r_rate / 12
    months += 1
    
print("Number of months: ", months)