import re
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.ensemble import IsolationForest
from prophet import Prophet

def parse_logs(log_file, log_pattern):
    with open(log_file, "r") as file:
        logs = [re.match(log_pattern, line).groupdict() for line in file if re.match(log_pattern, line)]
    return pd.DataFrame(logs)

def preprocess_data(df):
    df['datetime'] = pd.to_datetime(df['datetime'], format="%d/%b/%Y:%H:%M:%S %z", utc=True)
    df['status'] = df['status'].astype(int)
    df['size'] = df['size'].astype(int)
    return df

def analyze_traffic(df):
    return df.groupby(df['datetime'].dt.hour).size()

def detect_anomalies(df):
    model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
    df['traffic_score'] = df['size']
    df['anomaly'] = model.fit_predict(df[['traffic_score']])
    return df[df['anomaly'] == -1]

def forecast_traffic(df):
    traffic = df.resample('h', on='datetime')['size'].sum().reset_index().rename(columns={'datetime': 'ds', 'size': 'y'})
    traffic['ds'] = traffic['ds'].dt.tz_localize(None)
    model = Prophet()
    model.fit(traffic)
    future = model.make_future_dataframe(periods=24, freq='H')
    return model.predict(future), model


def visualize_results(traffic_by_hour, anomalies, forecast, model):
    traffic_by_hour.plot(kind='bar', title="Hourly Traffic Trend", xlabel="Hour", ylabel="Requests")
    plt.show()

    model.plot(forecast, xlabel="Time", ylabel="Forecast Traffic")
    plt.show()

    if not anomalies.empty:
        plt.scatter(anomalies['datetime'], anomalies['traffic_score'], color='red', label='Anomalies')
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
        plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=1))
        plt.gcf().autofmt_xdate()
        plt.legend()
        plt.show()

def main():
    log_file = "nginx_logs.log"
    log_pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<datetime>.+?)\] "(?P<method>\w+) (?P<url>.+?) HTTP/\d\.\d" (?P<status>\d+) (?P<size>\d+)'
    df = parse_logs(log_file, log_pattern)
    if df.empty:
        print("No logs parsed. Check the log file and pattern.")
        return
    df = preprocess_data(df)
    traffic_by_hour = analyze_traffic(df)
    print(f"Traffic by Hour:\n{traffic_by_hour}")
    anomalies = detect_anomalies(df)
    print(f"Anomalies:\n{anomalies}")
    forecast, model = forecast_traffic(df)
    visualize_results(traffic_by_hour, anomalies, forecast, model)

if __name__ == "__main__":
    main()
