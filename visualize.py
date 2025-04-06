import matplotlib.pyplot as plt

def plot_stock_trend(data, stocks):
    plt.figure(figsize = (12,6))
    for stock in stocks:
        plt.plot(data[stock], label = stock)
    plt.title('Stock Price Trend')
    plt.xlabel('Date')
    plt.ylabel('Adjusted Closing Price')
    plt.legend()
    plt.show()