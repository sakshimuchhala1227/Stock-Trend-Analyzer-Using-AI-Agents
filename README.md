<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stock Trend Analyzer Using Agents</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            line-height: 1.6;
        }
        h1, h2 {
            color: #333;
        }
        code {
            background: #f4f4f4;
            padding: 5px;
            border-radius: 5px;
        }
        pre {
            background: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <h1>Stock Trend Analyzer Using Agents</h1>
    
    <h2>Overview</h2>
    <p>This project is a <strong>Stock Trend Analyzer</strong> that leverages <strong>LangGraph agents</strong> to automate stock trend analysis. It fetches stock data using the <strong>yfinance</strong> API and determines whether a stock is in an <strong>Uptrend (Buy)</strong> or <strong>Downtrend (Sell)</strong> based on <strong>moving averages</strong>. The system provides users with a graphical representation of stock trends and insights into market movements. By using a modular approach with LangGraph, the project ensures scalability, flexibility, and improved data-driven decision-making.</p>
    
    <h2>Built With</h2>
    <ul>
        <li><strong>Python</strong> - Core programming language</li>
        <li><strong>yfinance</strong> - Fetching stock market data</li>
        <li><strong>LangGraph</strong> - Agent-based workflow automation</li>
        <li><strong>Streamlit</strong> - Interactive web UI for visualization</li>
        <li><strong>Matplotlib</strong> - Data visualization</li>
    </ul>
    
    <h2>Features</h2>
    <ul>
        <li>Fetches <strong>6 months</strong> of stock data from Yahoo Finance using the yfinance API.</li>
        <li>Uses <strong>Simple Moving Averages (SMA)</strong> to analyze trends.</li>
        <li>Provides a <strong>graphical representation</strong> of stock trends.</li>
        <li>Built with <strong>Streamlit</strong> for an interactive UI.</li>
        <li>Implements <strong>LangGraph agents</strong> for modular and scalable workflow automation.</li>
    </ul>
    
    <h2>Workflow</h2>
    <ol>
        <li><strong>User Input</strong>: The user provides a stock symbol (e.g., <code>AAPL, MSFT</code>) via the Streamlit UI.</li>
        <li><strong>Stock Data Fetching</strong>: The system retrieves the last <strong>6 months</strong> of historical stock data using the <strong>yfinance</strong> API.</li>
        <li><strong>Trend Analysis</strong>: The moving average strategy is applied:
            <ul>
                <li><strong>Short-term SMA (20-day)</strong> and <strong>Long-term SMA (50-day)</strong> are calculated.</li>
                <li>If <code>SMA_20 &gt; SMA_50</code>, the stock is in an <strong>Uptrend (Buy)</strong>.</li>
                <li>Otherwise, it is in a <strong>Downtrend (Sell)</strong>.</li>
            </ul>
        </li>
        <li><strong>Visualization & Result</strong>: A trend graph is generated and displayed along with the trend analysis.</li>
    </ol>
    
    <h2>Installation</h2>
    <p>1. Clone the repository:</p>
    <pre><code>git clone https://github.com/your-repo/Stock-Trend-Analyzer.git
cd Stock-Trend-Analyzer</code></pre>
    
    <p>2. Install dependencies:</p>
    <pre><code>pip install -r requirements.txt</code></pre>
    
    <h2>How to Run</h2>
    <p>1. Run the stock data tool script:</p>
    <pre><code>python stock_data_tool.py</code></pre>
    
    <p>2. Run the stock agent script:</p>
    <pre><code>python stock_agent.py</code></pre>
    
    <p>3. Run the Streamlit app:</p>
    <pre><code>streamlit run streamlit_app.py</code></pre>
    
    <h2>Project Structure</h2>
    <pre><code>Stock-Trend-Analyzer/
│── stock_agent.py          # Main logic for stock trend analysis using LangGraph
│── stock_data_tool.py      # Fetches stock data and plots trend graphs
│── streamlit_app.py        # Streamlit UI for stock analysis
│── requirements.txt        # Dependencies
│── README.md               # Project documentation</code></pre>
    
    <h2>Usage</h2>
    <ul>
        <li>Enter a stock symbol (e.g., <code>AAPL, MSFT</code>) in the Streamlit UI.</li>
        <li>Click <strong>Analyze Stocks</strong> to fetch trend analysis.</li>
        <li>The system will display a <strong>trend graph</strong> and analysis result.</li>
    </ul>
    
    <h2>Example Output</h2>
    <pre><code>Fetching stock data for: AAPL
Analyzing stock trend...
Trend Analysis Result: Uptrend (Buy)
Graph saved at: AAPL_trend.png</code></pre>
</body>
</html>
