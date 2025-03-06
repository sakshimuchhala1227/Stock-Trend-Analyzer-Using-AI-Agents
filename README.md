# Stock Trend Analyzer Using Agents

## Overview
This project is a **Stock Trend Analyzer** that leverages **LangGraph agents** to automate stock trend analysis. It fetches stock data using the **yfinance** API and determines whether a stock is in an **Uptrend (Buy)** or **Downtrend (Sell)** based on **moving averages**. The system provides users with a graphical representation of stock trends and insights into market movements. By using a modular approach with LangGraph, the project ensures scalability, flexibility, and improved data-driven decision-making.

## Built With
- **Python** - Core programming language
- **yfinance** - Fetching stock market data
- **LangGraph** - Agent-based workflow automation
- **Streamlit** - Interactive web UI for visualization
- **Matplotlib** - Data visualization

## Features
- Fetches **6 months** of stock data from Yahoo Finance using the yfinance API.
- Uses **Simple Moving Averages (SMA)** to analyze trends.
- Provides a **graphical representation** of stock trends.
- Built with **Streamlit** for an interactive UI.
- Implements **LangGraph agents** for modular and scalable workflow automation.

## Workflow
1. **User Input**: The user provides a stock symbol (e.g., `AAPL, MSFT`) via the Streamlit UI.
2. **Stock Data Fetching**: The system retrieves the last **6 months** of historical stock data using the **yfinance** API.
3. **Trend Analysis**: The moving average strategy is applied:
   - **Short-term SMA (20-day)** and **Long-term SMA (50-day)** are calculated.
   - If **SMA_20 > SMA_50**, the stock is in an **Uptrend (Buy)**.
   - Otherwise, it is in a **Downtrend (Sell)**.
4. **Visualization & Result**: A trend graph is generated and displayed along with the trend analysis.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/Stock-Trend-Analyzer.git
   cd Stock-Trend-Analyzer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run
1. Run the stock data tool script:
   ```bash
   python stock_data_tool.py
   ```
2. Run the stock agent script:
   ```bash
   python stock_agent.py
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

## Project Structure
```
Stock-Trend-Analyzer/
│── stock_agent.py          # Main logic for stock trend analysis using LangGraph
│── stock_data_tool.py      # Fetches stock data and plots trend graphs
│── streamlit_app.py        # Streamlit UI for stock analysis
│── requirements.txt        # Dependencies
│── README.md               # Project documentation
```

## Usage
- Enter a stock symbol (e.g., `AAPL, MSFT`) in the Streamlit UI.
- Click **Analyze Stocks** to fetch trend analysis.
- The system will display a **trend graph** and analysis result.

## Example Output
```
Fetching stock data for: AAPL
Analyzing stock trend...
Trend Analysis Result: Uptrend (Buy)
Graph saved at: AAPL_trend.png
```


