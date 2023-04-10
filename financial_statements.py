
import yahooquery as yq
import pandas as pd


def initialize_ticker(ticker: str):
    '''Function that creates a Ticker object.'''
    company= yq.Ticker(ticker)
    return company

def get_income_statement(ticker):
    '''Function that uses yahoo query to collect the income statement and returns a dataframe.'''
    income_data = ticker.income_statement()
    return income_data

def get_cash_flow(ticker):
    '''Function that uses yahoo query to collect the cash flow statement and returns a dataframe.'''
    cash_data = ticker.cash_flow()
    return cash_data

def get_balance_sheet(ticker):
    '''Function that uses yahoo query to collect the balance sheet and returns a dataframe.'''
    balance_data = ticker.balance_sheet()
    return balance_data

def standardize_income_statement(data):
    '''Function that transposes the unsorted income statement financials into a sorted and simplified income statement into a dictionary where the columns are represented by the columns
    and the values represent the respective column's values.

    returns df

    Uses yahoo's standard format, incomplete financials on yahoo's end may result in not working??

    '''
    
    #check if other statements result in the same columns and info. If so POG if not, adapt the dataframe to be standardized. 
    data = data.transpose()
    accounts=["asOfDate",
                "periodType",
                "currencyCode",
                "TotalRevenue",
                "CostOfRevenue",
                "GrossProfit",
                "NormalizedEBITDA",
                "OperatingExpense",
                "EBIT",
                "TotalOperatingIncomeAsReported",
                "NetInterestIncome",
                "OtherIncomeExpense",
                "PretaxIncome",
                "TaxProvision",
                "NetIncomeCommonStockholders"]
    simplified_income_statement=data.loc[accounts]
    return simplified_income_statement


aapl=initialize_ticker("tsla")
data = get_income_statement(aapl)
income_statement = standardize_income_statement(data)
print(income_statement)




