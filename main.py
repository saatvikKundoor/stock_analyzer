import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import yfinance as yf 

def get_user_inputs():
    #user inputs for invested amount, hold duration, expected returns for bull/bear/base
    invested_amount = float(input("How much are you investing?"))
    hold_dur = int(input("How long will you be holding?"))
    bull_return = float(input("What is the expected return in a bullish market?"))
    bear_return = float(input("What is the expected return in a bearish market?"))
    base_return = float(input("What is the expected return in a bullish market?"))

def calculate_returns():
    #returns pre and post tax returns based on inputs
    pass

def fetch_sp500():
    pass

def display_result():
    #plot data comparisons
    pass

def main():
    get_user_inputs()
    calculate_returns()
    fetch_sp500()
    display_result()

main()

