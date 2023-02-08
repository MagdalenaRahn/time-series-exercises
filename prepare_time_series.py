import os
import pandas as pd

from env import username, host, password





# datetime grocery sales function

def grocery_sales_datetime(df):
    
    '''this function takes in a dataframe, changes the 'sale_date' col
    to datetime and then sets it as the index, then creates day and month
    columns, along with total 'sale_amount' col, and returns the 
    modified dataframe
    '''
    
    # change 'sale_date' to datetime format
    df['sale_date'] = pd.to_datetime(df['sale_date'])

    # setting index to now-date-formated 'sale_date'
    df = df.set_index('sale_date')
    
    # sort dates ascending
    shop = shop.sort_index()

    # creating month col
    df['month'] = df.index.month

    # creating day col
    df['day'] = df.index.day

    # multiplying 'sale_amount' by 'item_price' to get 'sales_total'
    df['sales_total'] = df['sale_amount'] * df['item_price']
    
    return df








# datetime Germany energy function

def de_electric_time(df):
    
    '''
    this function takes in a dataframe, renames the columns, changes the 'date' 
    col to datetime and then sets it as the index, then creates day and month
    columns, fills nulls with 0 and returns the 
    modified dataframe
    '''
    
    # renaming cols
    df = df.rename(columns = {'Date' : 'date', 'Consumption' : 'consumption', 
                               'Wind' : 'wind', 'Solar' : 'solar', 
                               'Wind+Solar' : 'wind_solar'})

    # change 'Date' to datetime format
    df['date'] = pd.to_datetime(df['date'])

    # setting index to now-date-formated 'Date'
    df = df.set_index('date')

    # creating month & year cols
    df['month'] = df.index.month_name()
    df['year'] = df.index.year
    
    #filling NaNs with 0
    df.fillna(0, inplace = True)
    
    return df