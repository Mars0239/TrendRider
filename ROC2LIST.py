import yfinance as yf

def calculate_roc(ticker, days=5):
    # Fetch historical data
    data = yf.download(ticker, period=f"{days+1}d")
    
    # Calculate ROC
    closing_prices = data['Close'].tolist()
    if len(closing_prices) < 2:
        return ticker, None
    return ticker, ((closing_prices[-1] - closing_prices[0]) / closing_prices[0]) * 100

def main():
    QQQ_list = ["CMCSA", "NFLX", "CSCO", "PEP", "COST", "ADBE", "AVGO", "GOOG", "GOOGL", "TSLA", "META", "NVDA", "AMZN", "MSFT", "AAPL"]
    SPY_list = ["JNJ", "V", "JPM", "UNH", "XOM", "LLY", "BRK-B", "META", "GOOG", "TSLA", "GOOGL", "NVDA", "AMZN", "MSFT", "AAPL"]

    print("ROC for QQQ list:")
    results_qqq = [calculate_roc(stock) for stock in QQQ_list]
    results_qqq.sort(key=lambda x: x[1] if x[1] is not None else float('-inf'))  # Sort by ROC value

    for stock, roc in results_qqq:
        if roc is not None:
            print(f"{stock}: {roc:.2f}%")
        else:
            print(f"{stock}: Data not available")

    print("\nROC for SPY list:")
    results_spy = [calculate_roc(stock) for stock in SPY_list]
    results_spy.sort(key=lambda x: x[1] if x[1] is not None else float('-inf'))  # Sort by ROC value

    for stock, roc in results_spy:
        if roc is not None:
            print(f"{stock}: {roc:.2f}%")
        else:
            print(f"{stock}: Data not available")

if __name__ == "__main__":
    main()

