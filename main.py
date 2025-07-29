import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import yfinance as yf 

invested_amount = 0
hold_dur = 0
bull_return = 0
bear_return = 0
base_return = 0
def get_user_inputs():
    #user inputs for invested amount, hold duration, expected returns for bull/bear/base
    invested_amount = float(input("How much are you investing?"))
    hold_dur = int(input("How long will you be holding (years)?"))
    bull_return = float(input("What is the expected return in a bullish market? (percent change)"))
    bear_return = float(input("What is the expected return in a bearish market? (percent change)"))
    base_return = float(input("What is the expected return in a bullish market? (percent change)"))
    return(invested_amount,hold_dur,bull_return,bear_return,base_return)
invested_amount,hold_dur,bull_return,bear_return,base_return = get_user_inputs()
def calculate_returns():
    #returns pre and post tax returns based on inputs
    print(invested_amount)
    pass

def fetch_sp500():
    pass

def display_result():
    #plot data comparisons
    pass

def main():
    #get_user_inputs()
    calculate_returns()
    fetch_sp500()
    display_result()

main()

