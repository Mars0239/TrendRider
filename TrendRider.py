import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import time
import logging
from datetime import datetime

logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)

def get_data(tickers):
    try:
        return yf.download(tickers, period="1d", interval="5m")['Close']
    except Exception as e:
        logging.error(f"Error fetching data: {e}")
        return None

def calculate_change(data):
    if len(data) < 2: 
        return 0
    return (data.iloc[-1] - data.iloc[0]) / data.iloc[0]

def display_changes(changes):
    # Display the change in each stock's value
    print(changes)

def plot_probabilities(up_prob, down_prob, flat_prob):
    plt.bar(['Up', 'Down', 'Flat'], [up_prob, down_prob, flat_prob])
    plt.ylim(0, 1)
    plt.ylabel('Probability')
    plt.title('Estimated SPY Movement Probability')
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    plt.text(1, 0.9, f"Time: {current_time}", horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
    plt.show()

def calculate_probabilities(changes, total_stocks):
    up_count = (changes > 0.005).sum()
    down_count = (changes < -0.005).sum()
    flat_count = len(changes) - up_count - down_count
    up_prob = up_count / total_stocks
    down_prob = down_count / total_stocks
    flat_prob = flat_count / total_stocks
    return up_prob, down_prob, flat_prob

def main(tickers):
    while True:
        data = get_data(tickers)
        if data is None:
            time.sleep(60)
            continue
        
        # Apply the function along axis=0 (i.e., on each ticker's time series)
        changes = data.apply(calculate_change, axis=0)
        display_changes(changes)

        up_prob, down_prob, flat_prob = calculate_probabilities(changes, len(tickers))
        plot_probabilities(up_prob, down_prob, flat_prob)
        
        time.sleep(300)

if __name__ == "__main__":
    tickers = ['AAPL', 'MSFT', 'AMZN', 'NVDA', 'NFLX', 'GOOGL', 'TSLA', 'META', 'JPM', 'BRK-B', 'SPY']
    main(tickers)

