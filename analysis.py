def calculate_moving_average(data, stock, window = 50):
    ma_column = f'{stock}_{window}_MA'
    data[ma_column] = data[stock].rolling(window = window).mean()
    return data
