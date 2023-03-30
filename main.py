# William Zarzour
# 3/30/2023
# Simple financial model that creates data frame & csv of the model

import pandas as pd
from forecasting_functions import *

#time range
num_years = 5

# Revenue assumptions
initial_customers = 10
customers_per_year = 200
customer_churn_rate = 0.1
price_per_user = 100

# Expense assumptions
annual_fixed_costs = 1000000
total_fixed_costs = 5000000
variable_costs_per_user = 25
marketing_expense_revenue_ratio = 0.25

#sales team is expected to double after 3 years ->> Ie. Assumptions that would increase sales
initial_team_size = 2
team_growth_rate = 0.13
average_wages = 45000

#Tax rate
tax_rate = 0.15


customers= customer_growth_calculation(initial_customers,customers_per_year,num_years)
revenue = revenue_calculation(customers,customer_churn_rate,price_per_user)
annual_fixed_costs = calculate_annual_fc(annual_fixed_costs,num_years)
annual_variable_costs = calculate_vc(customers,variable_costs_per_user)
marketing_expenses = marketing_expenses_calculation(revenue,marketing_expense_revenue_ratio)
#sales team growth should be wages
sales_team_growth = team_growth_calc(initial_team_size,team_growth_rate,num_years)
wages = wages_expense_calc(sales_team_growth,average_wages)

#summarizing 
total_expenses = total_expenses_calc(annual_fixed_costs,annual_variable_costs,sales_team_growth,marketing_expenses)
ebitda = ebitda_calc(revenue, total_expenses)
net_income=net_income_calc(tax_rate,ebitda)


#printed info
print(f"""

Customers: {customers}
Revenue: {revenue}
Annual_fixed_costs: {annual_fixed_costs}
Annual_variable_costs: {annual_variable_costs}
Marketing: {marketing_expenses}
Team Size: {sales_team_growth}
total EXP: {total_expenses}
EBITDA: {ebitda}
Net income:{net_income}
""")


#convert to data frame
df = pd.DataFrame(list(zip(customers,sales_team_growth,revenue,annual_fixed_costs,annual_variable_costs,wages,marketing_expenses,total_expenses,ebitda,net_income)),
               columns=["Customers","Team Size","Revenue","Fixed Costs","Variable Costs","Wages","Marketing Expenses","Total Expenses","EBITDA", "Net Income"],
               index=range(1,num_years+1))
print(df)

