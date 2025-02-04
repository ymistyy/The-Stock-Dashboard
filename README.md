# The-Stock-Dashboard
A dashboard for stocks!

The Stock Dashboard is a web application that allows users to view stock prices, read the latest news related to the stock market, and browse trending Reddit posts from various stock-related subreddits. The app uses Flask for the backend, Yahoo Finance for stock prices, the NewsAPI for the latest market news, and PRAW for Reddit integration.

## Features

- **Real-time stock prices**: Get the latest stock prices for popular stocks like VOO, AAPL, TSLA, and more.
- **Stock charts**: View stock charts for each stock by clicking on the "View Chart" link.
- **Latest market news**: Stay updated with the latest news articles related to the stock market.
- **Trending Reddit posts**: Browse popular posts from Reddit stock communities like r/wallstreetbets and r/stocks.

## Requirements

index.html needs to be in a folder called: "templates"
Before you can run the application, you'll need the following dependencies:

- Python 3.7+
- Flask
- yfinance
- praw
- requests
- dotenv

<h2 id="environment-variables">Environment Variables</h2>
    <p>Add your Reddit credentials to the <code>.env</code> file:</p>
    <pre><code>REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_user_agent</code></pre>

![image](https://github.com/user-attachments/assets/822d58b3-6982-42e1-bc17-5823cdc56ff2)

![image](https://github.com/user-attachments/assets/4ee7b7f7-bad7-4c01-b8a4-55f7b139b418)

