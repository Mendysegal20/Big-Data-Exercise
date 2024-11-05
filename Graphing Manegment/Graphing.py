import pandas as pd
import matplotlib.pyplot as plt

# Read the stocks data from the CSV file
def read_stock_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Use python change to complete the daily returns
def compute_daily_returns(df):
    daily_returns = df['PeakTime'].pct_change().dropna()
    return daily_returns

# Compute the average daily return, standard deviation of daily returns
def compute_statistics(daily_returns):
    avg_daily_return = daily_returns.mean()
    std_daily_return = daily_returns.std()
    cumulative_return = (daily_returns + 1).prod() - 1

    return avg_daily_return, std_daily_return, cumulative_return

# Plot daily closing prices
def plot_daily_closing_prices(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['PeakTime'], label='Daily Closing Price')
    plt.title('Daily Closing Prices')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

#Plot daily returns over time
def plot_daily_returns(daily_returns):
    plt.figure(figsize=(10, 6))
    plt.plot(daily_returns.index, daily_returns, label='Daily Returns', marker='o', linestyle='-')
    plt.title('Daily Returns')
    plt.xlabel('Time')
    plt.ylabel('Daily Return')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    # Read the CSV file as required
    file_path = 'myFile.csv'  # Replace with your file path
    df = read_stock_data(file_path)

    # Compute daily returns and statistics
    daily_returns = compute_daily_returns(df)
    avg_daily_return, std_daily_return, cumulative_return = compute_statistics(daily_returns)

    # Print computed statistics
    print(f"Average Daily Return: {avg_daily_return:.4f}")
    print(f"Standard Deviation of Daily Returns: {std_daily_return:.4f}")
    print(f"Cumulative Return: {cumulative_return:.4f}")

    # Plotting
    plot_daily_closing_prices(df)
    plot_daily_returns(daily_returns)

if __name__ == "__main__":
    main()
