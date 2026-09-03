# ⚡ Binance DCA Agent Simulator

A lightweight, interactive command-line interface (CLI) tool built in Python to simulate Dollar-Cost Averaging (DCA) strategies and analyze real-time market data directly from the Binance API.

---

## 🚀 Key Features

* Live Market Pricing: Fetches real-time asset prices directly from Binance public endpoints with built-in network fallback protection.
* Customizable DCA Strategy: Input your preferred coin symbol (e.g., BTC, ETH, BNB), investment amount per interval, and frequency (Daily, Weekly, or Monthly).
* Flexible Period Simulation: Define custom historical periods to instantly calculate total capital invested, accumulated asset amounts, current portfolio value, and overall ROI (Profit/Loss).
* Continuous Interactive Loop: Run multiple simulations seamlessly without needing to restart the script, complete with an easy exit option.
* Professional Terminal Interface: Clean layout optimized for screen recordings, demonstrations, and *Build in Public* showcases.

---

## 🛠️ Tech Stack

* Language: Python 3.x
* Libraries: requests, urllib3
* API: Binance Public Ticker API (/api/v3/ticker/price)

---

## 📦 Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/binance-dca-agent.git
   cd binance-dca-agent
