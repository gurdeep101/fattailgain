# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 19:30:26 2021

@author: gurdeep.singh
"""

import mibian
import pandas as pd
import numpy as np

def put_iv(df):
    # lets write a function to calculate IV for put options
    try: 
        # iv - underlying, strike, interest rate, days to expiry
        return mibian.BS([df['futures'], df['Strike Price'], 0, df['days2expiry']], putPrice = df['close']).impliedVolatility
    except:
        return np.nan

def call_iv(df):
    # function to calculate IV of call option
    try:
        # underlying, strike, interest, days to expiry, volatility
        return mibian.BS([df['futures'], df['Strike Price'], 0, df['days2expiry']], callPrice = df['close']).impliedVolatility
    except:
        return np.nan
    
def iv_function(df):
    df['option_iv_parallel'] = np.where(df['Option Type'] == 'CE', df.apply(call_iv, axis = 1), df.apply(put_iv, axis = 1))
    return df