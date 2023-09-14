import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

def calculate_sharpe_ratio(ticker, days=63):  # 63 trading days for 3 months
    # Fetch historical data
    data = yf.download(ticker, period=f"{days}d")
    
    # Calculate daily returns
    daily_returns = data['Close'].pct_change().dropna()
    
    # Calculate Sharpe Ratio
    expected_return = daily_returns.mean() * days
    risk = daily_returns.std() * np.sqrt(days)
    sharpe_ratio = expected_return / risk
    
    return ticker, sharpe_ratio

def visualize_sharpe_ratios(stock_list, list_name):
    results = [calculate_sharpe_ratio(stock) for stock in stock_list]
    tickers, sharpe_ratios = zip(*results)
    
    plt.figure(figsize=(12, 6))
    plt.bar(tickers, sharpe_ratios, color='skyblue')
    plt.xlabel('Stocks')
    plt.ylabel('Sharpe Ratio')
    plt.title(f'Sharpe Ratios for {list_name} Stocks Over 3 Months')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

def main():
    QQQ_list = ["CMCSA", "NFLX", "CSCO", "PEP", "COST", "ADBE", "AVGO", "GOOG", "GOOGL", "TSLA", "META", "NVDA", "AMZN", "MSFT", "AAPL"]
    SPY_list = ["JNJ", "V", "JPM", "UNH", "XOM", "LLY", "BRK.B", "META", "GOOG", "TSLA", "GOOGL", "NVDA", "AMZN", "MSFT", "AAPL"]

    visualize_sharpe_ratios(QQQ_list, "QQQ")
    visualize_sharpe_ratios(SPY_list, "SPY")

if __name__ == "__main__":
    main()

