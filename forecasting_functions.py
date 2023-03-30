# William Zarzour
# 3/30/2023

def customer_growth_calculation(initial_customers,customers_per_year,num_years):
    ''''''
    customer_assumptions = []
    for year in range(0,num_years+1):
        customer_assumptions.append(initial_customers+customers_per_year*(year-1))
    return customer_assumptions

def revenue_calculation(customers, customer_churn_rate,price_per_user):
    ''''''
    revenue = []
    for customer in customers:
        rev_per_customer=customer*(1-customer_churn_rate)*12*price_per_user
        revenue.append(rev_per_customer)
    return revenue

def calculate_annual_fc(fixed_costs,num_years,total=False):
    ''''''
    if total==True:
        return [fixed_costs/num_years for year in range(0,num_years)]
    
    return [fixed_costs for year in range(0,num_years)]

def calculate_vc(customers,variable_costs_per_user):
    ''''''
    return [customer*variable_costs_per_user for customer in customers]

def marketing_expenses_calculation(revenue,marketing_expense_revenue_ratio):
    ''''''
    return [value*marketing_expense_revenue_ratio for value in revenue]

def team_growth_calc(initial_team_size,growth_rate,num_years):
    ''''''
    team_growth = [initial_team_size]
    if growth_rate==0:
        return [initial_team_size]*num_years
    for value in team_growth:
        team_growth.append(value*(1+growth_rate))
        if len(team_growth)==num_years:
            return team_growth


def wages_expense_calc(sales_team_growth,average_annual_wages):
    ''''''
    return[value*average_annual_wages for value in sales_team_growth]


def total_expenses_calc(annual_fixed_costs,annual_variable_costs,sales_team_growth,marketing_expenses):
    ''''''
    return list(map(sum,zip(annual_fixed_costs,annual_variable_costs,sales_team_growth,marketing_expenses)))


def ebitda_calc(revenue, total_expenses):
    ''''''
    return list(map(sum,zip(revenue, total_expenses)))

def net_income_calc(tax_rate,ebitda):
    ''''''
    return [value*(1-tax_rate) for value in ebitda]
        



