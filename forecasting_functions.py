# William Zarzour
# 3/30/2023
from financial_statements import *
import random as rand



def average_account_calculation(data):
    '''Calculates average of 4yrs '''
    average_data = data
    #data.iloc[startr:stopr:stepr,startc:stopc:stepc] looking for the index range 3-15
    accounts = average_data.iloc[3:15:,0:5]
    account_averages = accounts.mean(axis=1)
    average_data["mean"] = account_averages
    return average_data

def growth_rate_calculation(data):
    '''Determines the average growth rate across the 4 year period based on the % change excluding TTM. Returns dictionary with account name as key and value as growth rate with type float.'''
    accounts = data.iloc[3:15:,0:3]
    percent_change_data = accounts.pct_change(axis="columns")
    account_averages = percent_change_data.mean(axis=1)
    growth_averages=account_averages.to_dict()
    return growth_averages

def rate_of_change(average_growth_rates, rate_of_change):
    '''modifies the growth rates from the growth rate calculations positively.
    '''
    projected_rates_of_change=average_growth_rates.copy()
    projected_rates_of_change.update((key, value+rate_of_change) for key, value in projected_rates_of_change.items())
    return projected_rates_of_change


def spiked_growth(average_growth_rates):
    '''modifies the growth rates from the growth rate calculations positively.
    '''
    #low growth that spikes to +15-25% 

    pass

def spiked_loss(average_growth_rates):
    '''modifies the growth rates from the growth rate calculations positively.
    '''
    #low growth that spikes to -15-25% 
    
    pass

def loss_with_spiked_growth(average_growth_rates):
    '''modifies the growth rates from the growth rate calculations positively.
    '''
    #negative 1-5% loss with nearly a 25-50% positives pike
    
    pass

def gain_with_spiked_loss(average_growth_rates):
    '''modifies the growth rates from the growth rate calculations positively.
    '''
    #negative 1-5% loss with nearly a 25-50% spike
    
    pass
