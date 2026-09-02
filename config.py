# Configuration settings for Binance DCA Agent

API_KEY = "your_binance_api_key_here"
API_SECRET = "your_binance_api_secret_here"

# DCA Strategy Settings
SYMBOL = "BTCUSDT"          # Asset pair to accumulate
INVEST_AMOUNT = 50.0        # Amount in USDT per interval
INTERVAL_HOURS = 24         # Frequency of purchase (e.g., every 24 hours)
TESTNET = True              # Use Binance Testnet for safety during testing
