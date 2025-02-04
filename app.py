import os
import yfinance as yf
import requests
import praw
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv

load_dotenv()

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

STOCKS = list(set([
    "VOO", "MGNI", "SPY", "NVDA", "AMD", "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", 
    "META", "NFLX", "BABA", "V", "MA", "PYPL", "DIS", "GS", "JPM", "WMT", "BA", 
    "INTC", "UBER", "LYFT", "TWTR", "CRM", "NVDA", "SNAP", "AMD", "QCOM", "TSM", 
    "INTU", "BIDU", "LULU", "SHOP", "ROKU", "SE", "PFE", "JNJ", "MRNA", "INTC"
]))

SUBREDDITS = ["wallstreetbets", "smallstreetbets", "stocks", "investing"]

app = Flask(__name__)

def fetch_stock_prices():
    stock_data = {}
    for stock in STOCKS:
        ticker = yf.Ticker(stock)
        data = ticker.history(period="1d")
        if not data.empty:
            stock_data[stock] = {
                "price": round(data["Close"].iloc[-1], 2),
                "change": round(data["Close"].iloc[-1] - data["Open"].iloc[-1], 2),
                "percent_change": round(((data["Close"].iloc[-1] - data["Open"].iloc[-1]) / data["Open"].iloc[-1]) * 100, 2),
                "chart_url": f"https://finance.yahoo.com/quote/{stock}/chart"
            }
    return stock_data

# API needed for news
def fetch_news():
    url = f"https://newsapi.org/v2/everything?q=stock%20market&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    articles = response.json().get("articles", [])[:5]
    return [{"title": a["title"], "url": a["url"]} for a in articles]

def fetch_reddit_posts():
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )

    posts = []
    for subreddit_name in SUBREDDITS:
        subreddit = reddit.subreddit(subreddit_name)
        for submission in subreddit.hot(limit=5):
            posts.append({"title": submission.title, "url": submission.url, "created_utc": submission.created_utc})

    return posts[:20]

@app.route("/api/stocks")
def api_stocks():
    stock_prices = fetch_stock_prices()
    return jsonify(stock_prices)

@app.route("/api/reddit")
def api_reddit():
    reddit_posts = fetch_reddit_posts()
    return jsonify(reddit_posts)

@app.route("/")
def index():
    stock_prices = fetch_stock_prices()
    news = fetch_news()
    reddit_posts = fetch_reddit_posts()

    return render_template("index.html", stocks=stock_prices, news=news, reddit_posts=reddit_posts)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)  # Disable for prod
