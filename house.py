total_cost = input("enter your cost of dream home? ") 
annual_salary = input ("enter your anual salary? ")
portion_saved = input("enter your portion to be saved? ")
monthly_income = int(annual_salary)/12
current_savings = 0
r = 0.04
growth = current_savings*r/12
portion_saved = int(annual_salary)*.10
portion_down_payment = int(total_cost)*.25
i = 0

while current_savings <= portion_down_payment:
    i = i+1
    growth = current_savings*r/12
    current_savings = current_savings + portion_saved/12+current_savings*r/12
    


print("number of months", i)









