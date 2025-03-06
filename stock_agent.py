import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import linregress
from langgraph.graph import StateGraph
from typing import TypedDict
from stock_data_tool import fetch_stock_data
import os

# Define State Schema
class StockState(TypedDict):
    stock_symbol: str
    image_path: str
    trend: str

# Define Stock Data Agent
def stock_data_agent(state: StockState):
    symbol = state["stock_symbol"]
    print(f"\nFetching stock data for: {symbol}")
    
    image_path = fetch_stock_data(symbol)

    if image_path is None:
        return {"image_path": None, "trend": "Invalid Stock Symbol"}

    return {"image_path": image_path}

# Define Trend Analysis Function
def analyze_trend(symbol):
    """Fetch stock data and analyze its trend using moving averages ."""
    stock = yf.Ticker(symbol)
    df = stock.history(period="6mo")  # Get 6 months of stock data

    if df.empty:
        return "Invalid Stock Symbol"

    # Calculate Moving Averages
    df["SMA_20"] = df["Close"].rolling(window=20).mean()  # 20-day moving average
    df["SMA_50"] = df["Close"].rolling(window=50).mean()  # 50-day moving average

    # Determine Trend using Moving Averages
    if df["SMA_20"].iloc[-1] > df["SMA_50"].iloc[-1]:  
        trend = "Uptrend (Buy)"
    else:
        trend = "Downtrend (Sell)"

    # Linear Regression for Trend Analysis
    # y = df["Close"].dropna().values
    # x = np.arange(len(y))
    # slope, _, _, _, _ = linregress(x, y)  

    # If slope is positive, trend is up, otherwise down
    # if slope > 0:
    #     trend = "Uptrend (Buy)"
    # else:
    #     trend = "Downtrend (Sell)"

    return trend

# Define Decision Agent (Analyzes Trend)
def decision_agent(state: StockState):
    if state["image_path"] is None:
        return {"trend": "Invalid Stock Symbol"}
    
    print("Analyzing stock trend...")

    trend = analyze_trend(state["stock_symbol"])

    return {"trend": trend}

# Build LangGraph Workflow
graph = StateGraph(StockState)

graph.add_node("StockData", stock_data_agent)
graph.add_node("Decision", decision_agent)

graph.set_entry_point("StockData")
graph.add_edge("StockData", "Decision")

graph.set_finish_point("Decision")

stock_agent = graph.compile()

def analyze_stock(symbol):
    """Function to process a stock symbol and return the analysis result."""
    symbol = symbol.strip().upper()  # Clean input
    
    result = stock_agent.invoke({"stock_symbol": symbol})
    
    analysis_output = {
        "stock": symbol,
        "image_path": result["image_path"],
        "trend": result["trend"],
        "description": ""
    }
    
    # Add Analysis Explanation
    if result["trend"] == "Uptrend (Buy)":
        analysis_output["description"] = (
            "- The stock shows an upward movement, suggesting positive growth potential.\n"
            "- It may be a good time to buy, but consider other market factors as well."
        )
    elif result["trend"] == "Downtrend (Sell)":
        analysis_output["description"] = (
            "- The stock is showing a downward trend based on recent price patterns.\n"
            "- It may not be the best time to invest; further analysis is recommended."
        )
    else:
        analysis_output["description"] = (
            "- The stock symbol provided is invalid. Please check and try again."
        )
    
    return analysis_output
