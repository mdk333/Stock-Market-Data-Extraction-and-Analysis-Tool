from alpha_vantage.timeseries import TimeSeries
from pymongo import MongoClient

# Initialize Alpha Vantage API with your API key
ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')

# Initialize MongoDB client
client = MongoClient('mongodb://localhost:27017/')
db = client['stock_db']

# Define the list of stocks we are interested in
stocks = ['AAPL', 'GOOGL', 'AMZN']

# Fetch data and store in MongoDB
for stock in stocks:
    data, meta_data = ts.get_intraday(stock, interval='1min', outputsize='full')
    db[stock].insert_one({'metadata': meta_data, 'timeseries': data.to_dict()})
