import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import time
from datetime import datetime

# getting data
def get_data(tickers):
    data = yf.download(tickers, period="1d", interval="5m")
    return data['Close']

# calculate change ratio
def calculate_change(data):
    return (data.iloc[-1] - data.iloc[0]) / data.iloc[0]

# main function 
def main():
    # stock list
    tickers = ['AAPL', 'MSFT', 'AMZN', 'NVDA', 'NFLX', 'GOOGL', 'TSLA', 'META', 'JPM', 'QQQ', 'SPY']
    
    while True:
        data = get_data(tickers)
        changes = data.apply(calculate_change)
        
        # calcuate stocks up count, down count and flat count
        up_count = (changes > 0.005).sum()
        down_count = (changes < -0.005).sum()
        flat_count = len(changes) - up_count - down_count
        
        # calculate SPY probability of up, down or flat
        total_stocks = len(tickers) - 1  # 排除SPY本身
        up_prob = up_count / total_stocks
        down_prob = down_count / total_stocks
        flat_prob = flat_count / total_stocks
        
        # visualizing
        plt.bar(['Up', 'Down', 'Flat'], [up_prob, down_prob, flat_prob])
        plt.ylim(0, 1)
        plt.ylabel('Probability')
        plt.title('Estimated SPY Movement Probability')
        
        # add current time
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        plt.text(1, 0.9, f"Time: {current_time}", horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
        
        plt.show()
        
        # update in every 5 min
        time.sleep(300)

if __name__ == "__main__":
    main()
