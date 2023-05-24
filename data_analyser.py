from alpha_vantage.techindicators import TechIndicators

# Initialize TechIndicators with your API key
ti = TechIndicators(key='YOUR_API_KEY', output_format='pandas')

# Fetch and print SMA, EMA and RSI for a given stock
def print_indicators(stock):
    data_sma, meta_data_sma = ti.get_sma(stock)
    data_ema, meta_data_ema = ti.get_ema(stock)
    data_rsi, meta_data_rsi = ti.get_rsi(stock)

    print(f"SMA for {stock}: {data_sma['SMA'][-1]}")
    print(f"EMA for {stock}: {data_ema['EMA'][-1]}")
    print(f"RSI for {stock}: {data_rsi['RSI'][-1]}")

# Use the function for AAPL
print_indicators('AAPL')
