# William Zarzour
# 3/30/2023
from financial_statements import *



def average_account_calculation(data):
    '''Calculates average of 4yrs + TTM. yes adding TTM probably skews data as it is duplicating 9 months of data. '''
    average_data = data
    #data.iloc[startr:stopr:stepr,startc:stopc:stepc] looking for the index range 3-15
    accounts = average_data.iloc[3:15:,0:6]
    account_averages = accounts.mean(axis=1)
    average_data["mean"] = account_averages
    return average_data

def growth_rate_calculation(data):
    '''Determines the average growth rate across the 4 year period based on the % change excluding TTM. Returns dictionary with account name as key and value as growth rate with type float.'''
    accounts = data.iloc[3:15:,0:4]
    percent_change_data = accounts.pct_change(axis="columns")
    account_averages = percent_change_data.mean(axis=1)
    growth_averages=account_averages.to_dict()
    return growth_averages


def customer_growth_calculation(initial_customers,customers_per_year,num_years):
    '''Creates a list of annual customers using initial customers and an increase or decrease of customers per year.
    
   Parameters -> [float]
    returns -> [float]'''

    customer_assumptions = []
    for year in range(0,num_years+1):
        customer_assumptions.append(initial_customers+customers_per_year*(year-1))
    return customer_assumptions


def calculate_annual_fc(fixed_costs,num_years,total=False):
    '''Creates a list of annual fixed costs.
    If total is false then the fixed_cost variable are treated as annual

    if total is True then the fixed_cost variable are treated as total over the projection period
    
    Parameters -> [float]
    returns -> [float]'''

    if total==True:
        return [fixed_costs/num_years for year in range(0,num_years)]
    
    return [fixed_costs for year in range(0,num_years)]

def calculate_vc(customers,variable_costs_per_user):
    '''Creates a list of annual variable costs by multiplying cost per user by total users.

    
    Parameters -> [float]
    returns -> [float]'''

    return [customer*variable_costs_per_user for customer in customers]

def marketing_expenses_calculation(revenue,marketing_expense_revenue_ratio):
    '''Creates a list of marketing expenses calculated as a percentage of revenue.
    
    Parameters -> [float]
    returns -> [float]'''

    return [value*marketing_expense_revenue_ratio for value in revenue]

def team_growth_calc(initial_team_size,growth_rate,num_years):
    '''Creates a list of floats that represent the total number of paid employees.
    
    Parameters -> [float]
    returns -> [float]'''

    team_growth = [initial_team_size]
    if growth_rate==0:
        return [initial_team_size]*num_years
    for value in team_growth:
        team_growth.append(value*(1+growth_rate))
        if len(team_growth)==num_years:
            return team_growth


def wages_expense_calc(sales_team_growth,average_annual_wages):
    '''Creates a list of the annual wage expense using average annual wage per paid employee.
    
    Parameters -> [float]
    returns -> [float]'''

    return[value*average_annual_wages for value in sales_team_growth]


def total_expenses_calc(annual_fixed_costs,annual_variable_costs,sales_team_growth,marketing_expenses):
    '''Creates a list of annual total expenses.
    
    Parameters -> [float]
    returns -> [float]'''

    return list(map(sum,zip(annual_fixed_costs,annual_variable_costs,sales_team_growth,marketing_expenses)))


def ebitda_calc(revenue, total_expenses):
    '''Calculates the Earnings Before Income Tax Depreciation and Amortization(EBITDA).
    
    Parameters -> [float]
    returns -> [float]'''

    return list(map(sum,zip(revenue, total_expenses)))

def net_income_calc(tax_rate,ebitda):
    '''Creates a list of the annual net_income or loss. ebitda*(1-tax rate)
    
    Parameters ebitda -> [float]
    tax rate -> float
    returns -> [float]'''

    return [value*(1-tax_rate) for value in ebitda]
        



