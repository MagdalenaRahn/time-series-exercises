import os
import pandas as pd
import matplotlib.pyplot as plt

from env import username, host, password

from sklearn.metrics import mean_squared_error
from math import sqrt 


# function to get RMSE

def eval(val, yhat_df, target):
    
    '''
    This function takes in the target variable from validate
    and the predicted values in yhat_df and computes and returns
    the RMSE, rounded.
    '''
    
    RMSE = round(sqrt(mean_squared_error(val[target], yhat_df[target])), 0)
     
    print(f'The RMSE is {RMSE}')





# plotting and RMSE function

def plot_eval(train, val, yhat_df, target):
    
    '''
    This function takes in the target variable and returns a graph
    of the train, validate and predicted values from the yhat dataframe.
    It also labels the RMSE.
    '''
    
    plt.figure(figsize = (12, 6))
    
    plt.plot(train[target], label = 'Train', linewidth = 0.7, color = 'r')
    plt.plot(val[target], label = 'Validate', linewidth = 0.7, color = 'y')
    plt.plot(yhat_df[target], label = 'yhat', linewidth = 0.9, c = 'b')
    
    plt.legend()
    plt.title(target)
    
    RMSE = eval(val, yhat_df, 'amount')
    
    print(f'The RMSE is {RMSE}')
    
    plt.show()
    
    
    
    
# function to store the RMSE for comparing amongst models

def append_eval_df(model_type, target):
    
    '''
    This function takes in the type of model that was run
    and the name of the target variable.  It returns the eval_df 
    with the RMSE appended to it for that model and target. 
    '''
    
    RMSE = eval(val, yhat_df, 'amount')
    
    f = {'model_type': [model_type], 'target_var': [target],
        'rmse': [RMSE]}
    
    f = pd.DataFrame(f)
    
    return eval_df.append(f, ignore_index = True)
