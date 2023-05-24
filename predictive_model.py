from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np

# Fetch the data for a given stock
def get_stock_data(stock):
    collection = db[stock]
    data = collection.find_one()
    df = pd.DataFrame(data['timeseries']).T
    df.columns = ['open', 'high', 'low', 'close', 'volume']
    df = df.astype(float)
    return df

# Predict the closing price for the next day
def predict_next_day(stock):
    df = get_stock_data(stock)
    df['predict'] = df['close'].shift(-1)
    df.dropna(inplace=True)

    X = np.array(df.drop(['predict'], 1))
    y = np.array(df['predict'])
  
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(f"Prediction for next day's closing price for {stock}: {model.predict([X[-1]])}")

# Use the function for AAPL
predict_next_day('AAPL')
