import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import yfinance as yf 


def get_user_inputs():
    #user inputs for invested amount, hold duration, expected returns for bull/bear/base
    invested_amount = float(input("How much are you investing? "))
    hold_dur = int(input("How long will you be holding (years)? "))
    bull_return = float(input("What is the expected return in a bullish market? (percent change) "))/100
    base_return = float(input("What is the expected return in a base market? (percent change) "))/100
    bear_return = float(input("What is the expected return in a bearish market? (percent change) "))/100
    return(invested_amount,hold_dur,bull_return,bear_return,base_return)
invested_amount,hold_dur,bull_return,bear_return,base_return = get_user_inputs()
def calculate_returns():
    #returns pre and post tax returns based on inputs

    #pre tax section
    bull_return_pre = invested_amount * ((1+bull_return)**hold_dur)
    bear_return_pre = invested_amount * ((1+bear_return)**hold_dur)
    base_return_pre = invested_amount * ((1+base_return)**hold_dur)

    #post tax section
    capital_gains_tax = float(input("How much is your capital gains tax? (percent ex. 8) "))/100
    if invested_amount < bull_return_pre:
        bull_return_post = bull_return_pre - ((bull_return_pre -invested_amount) * capital_gains_tax)
    else:
        bull_return_post = bull_return_pre

    if invested_amount < bear_return_pre:
        bear_return_post = bear_return_pre - ((bear_return_pre - invested_amount) * capital_gains_tax)
    else:
        bear_return_post = bear_return_pre

    if invested_amount < base_return_pre:
        base_return_post = base_return_pre - ((base_return_pre - invested_amount) * capital_gains_tax)
    else:
        base_return_post = base_return_pre
    print("In a bullish market, before tax, your {} would become {:.2f}. After tax, your {} would become {:.2f}".format(invested_amount,bull_return_pre,invested_amount, bull_return_post))
    print("In a base market, before tax, your {} would become {:.2f}. After tax, your {} would become {:.2f}".format(invested_amount,base_return_pre,invested_amount, base_return_post))
    print("In a bearish market, before tax, your {} would become {:.2f}. After tax, your {} would become {:.2f}".format(invested_amount,bear_return_pre,invested_amount, bear_return_post))
    return(capital_gains_tax, bull_return_post,base_return_post,bear_return_post)
capital_gains_tax,bull_return_post,base_return_post,bear_return_post= calculate_returns()

def fetch_sp500():
    #fetch data from sp500, return results from investing in SP500 with same invested_amount + hold_dur.
    sp500_data = yf.Ticker("^GSPC").history((str(hold_dur)+"y"))
    sp500_start = sp500_data.iloc[0,3]
    sp500_end = sp500_data.iloc[-1,3]
    sp500_annual_growth = ((sp500_end/sp500_start)**(1/hold_dur))-1
    sp500_results = (invested_amount * (1+sp500_annual_growth)**hold_dur)
    if invested_amount < sp500_results:
        #capital gains tax only applies to profit.
        sp500_post = sp500_results - ((sp500_results - invested_amount)*capital_gains_tax)
    else:
        sp500_post = sp500_results
    print(sp500_data)
    print("If you had invested in the S&P500, after taxes, your {} would've turned into {:.2f}".format(invested_amount,sp500_post))
def display_result():
    #plot data comparisons
    pass

def main():
    #get_user_inputs()
    #calculate_returns()
    fetch_sp500()
    display_result()

main()
