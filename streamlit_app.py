import streamlit as st
from stock_agent import analyze_stock

# Streamlit UI Configuration
st.set_page_config(page_title="Stock Trend Analyzer", layout="wide")

# Title and Description
st.title("Stock Trend Analyzer")
st.write(
    "Enter stock symbols to fetch their latest trend analysis. "
    "The system will determine whether the stock is in an Uptrend (Buy) or Downtrend (Sell)."
)

# User Input for Stock Symbols
stock_input = st.text_input("Enter stock symbols (comma-separated, e.g., AAPL,MSFT,TSLA):")

if st.button("Analyze Stocks"):
    if not stock_input:
        st.warning("Please enter at least one stock symbol.")
    else:
        stock_symbols = [symbol.strip().upper() for symbol in stock_input.split(",")]

        for symbol in stock_symbols:
            st.subheader(f"Analysis for {symbol}")

            with st.spinner(f"Fetching stock data for {symbol}..."):
                result = analyze_stock(symbol)

            # Display Trend Analysis
            if result["image_path"]:
                st.image(result["image_path"], caption=f"Stock Trend: {symbol}", use_column_width=True)

            # Show trend result
            if result["trend"] == "Invalid Stock Symbol":
                st.error("Invalid Stock Symbol. Please check and try again.")
            else:
                st.write(f"Trend Analysis Result: **{result['trend']}**")
                st.info(result["description"])

            # Separator for multiple stocks
            st.markdown("---")
