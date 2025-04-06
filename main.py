from fetch_data import get_stock_data
from analysis import calculate_moving_average
from visualize import plot_stock_trend

stocks = ['AAPL', 'GOOGL']
data =  get_stock_data(stocks, '2019-01-01', '2024-01-01')
for stock in stocks:
    data = calculate_moving_average(data, stock)
plot_stock_trend(data, stocks)