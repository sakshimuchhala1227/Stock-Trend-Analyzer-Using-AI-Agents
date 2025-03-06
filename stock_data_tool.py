import yfinance as yf
import matplotlib.pyplot as plt

def fetch_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        df = stock.history(period="6mo")  # Fetch 6 months of data

        if df.empty:
            print(f"Error: No data found for {symbol}. Check the stock symbol.")
            return None

        # Plot closing price
        plt.figure(figsize=(10, 5))
        plt.plot(df.index, df["Close"], label=f"{symbol} Closing Price", color="blue")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.title(f"{symbol} Stock Price Trend")
        plt.legend()
        plt.grid(True)

        # Save graph with stock symbol
        image_path = f"{symbol}_trend.png"
        plt.savefig(image_path)
        plt.close()

        return image_path

    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None
