# William Zarzour
# 3/30/2023
# Simple financial model that creates data frame & csv of the model

from forecasting_functions import *

aapl=initialize_ticker("aapl")
data = get_income_statement(aapl)
income_statement = standardize_income_statement(data)
print(income_statement)
x = average_account_calculation(income_statement)
print(x)
y = growth_rate_calculation(income_statement)
print(y)




'''
df = pd.DataFrame(list(zip(customers,sales_team_growth,revenue,annual_fixed_costs,annual_variable_costs,wages,marketing_expenses,total_expenses,ebitda,net_income)),
               columns=["Customers","Team Size","Revenue","Fixed Costs","Variable Costs","Wages","Marketing Expenses","Total Expenses","EBITDA", "Net Income"],
               index=range(1,num_years+1))
print(df)

'''