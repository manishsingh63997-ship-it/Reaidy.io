
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load data
df = pd.read_csv("energy_usage.csv")
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date').reset_index(drop=True)

# Feature Engineering
df['lag_1'] = df['Energy_Usage'].shift(1)
df['lag_2'] = df['Energy_Usage'].shift(2)
df['lag_3'] = df['Energy_Usage'].shift(3)
df['roll_3'] = df['Energy_Usage'].rolling(3).mean()
df['roll_7'] = df['Energy_Usage'].rolling(7).mean()
df = df.dropna().reset_index(drop=True)

X = df[['lag_1','lag_2','lag_3','roll_3','roll_7']]
y = df['Energy_Usage']

split_index = int(len(df)*0.8)
X_train, X_test = X[:split_index], X[split_index:]
y_train, y_test = y[:split_index], y[split_index:]

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print("Model MAE:", mae)

# Forecast next 7 days
forecast_days = 7
last_data = df.copy()
future_predictions = []

for i in range(forecast_days):
    last_row = last_data.iloc[-1]

    new_row = {}
    new_row['lag_1'] = last_row['Energy_Usage']
    new_row['lag_2'] = last_row['lag_1']
    new_row['lag_3'] = last_row['lag_2']

    last_3 = list(last_data['Energy_Usage'].tail(3))
    last_7 = list(last_data['Energy_Usage'].tail(7))

    new_row['roll_3'] = np.mean(last_3)
    new_row['roll_7'] = np.mean(last_7)

    X_new = pd.DataFrame([new_row])
    pred = model.predict(X_new)[0]
    future_predictions.append(pred)

    next_date = last_row['Date'] + pd.Timedelta(days=1)

    append_row = {
        'Date': next_date,
        'Energy_Usage': pred,
        'lag_1': new_row['lag_1'],
        'lag_2': new_row['lag_2'],
        'lag_3': new_row['lag_3'],
        'roll_3': new_row['roll_3'],
        'roll_7': new_row['roll_7']
    }

    last_data = pd.concat([last_data, pd.DataFrame([append_row])], ignore_index=True)

future_dates = pd.date_range(start=df['Date'].iloc[-1] + pd.Timedelta(days=1), periods=7)
forecast_df = pd.DataFrame({
    "Date": future_dates,
    "Forecasted_Energy_Usage": future_predictions
})

forecast_df.to_csv("Output.csv", index=False)
print("Forecast saved as Output.csv")
print(forecast_df)
