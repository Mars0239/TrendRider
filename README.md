# TrendRider
Real-time S&amp;P500 Movement Prediction
TrendRider
TrendRider is a Python-based stock market analysis tool that provides insights into stock trends and potential movements. 
By leveraging the power of the yfinance library, TrendRider fetches real-time stock data and calculates key financial metrics like Rate of Change (ROC) and Sharpe Ratio. Additionally, 
it estimates the movement probability of the SPY index based on the performance of a selected list of stocks.

Features
Rate of Change (ROC): Calculates the ROC for a list of stocks over a specified period, providing insights into their recent performance.
Sharpe Ratio: Evaluates the risk-adjusted performance of stocks over a given period.
SPY Movement Probability: Estimates the probability of the SPY index moving up, down, or remaining flat based on the performance of a predefined list of stocks.

Installation
1. git clone https://github.com/Mars0239/TrendRider.git

2. Navigate to the project directory and install the required libraries:
cd TrendRider
pip install -r requirements.txt

Usage
Run the main script to start the analysis:
python main.py

The script will fetch real-time stock data every 5 minutes and display the estimated SPY movement probability.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
