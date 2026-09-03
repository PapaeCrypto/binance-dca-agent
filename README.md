# ⚡ Binance DCA Simulator

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
   git clone https://github.com/PapaeCrypto/binance-dca-agent.git
   cd binance-dca-agent
   ```
2. Install dependencies: makesure you have requests librry installed
   ```bash
   pip install requests
   ```
3. Run the agent
   ```bash
   python main.py
   ```

## Usage Example

==================================================
                          
   BINANCE DCA (DOLLAR-COST AVERAGING) SIMULATOR 
      
==================================================

Enter coin to DCA (e.g., BTC, ETH, BNB): bnb
Enter investment amount per interval (USDT): 10

Select DCA Interval:
1. Daily
2. Weekly
3. Monthly
Choose interval (1/2/3): 2

Enter how many weekly periods to simulate (e.g., 12, 24, 52): 12

[INFO] Fetching live market data from Binance for BNBUSDT...

--------------------------------------------------
📊 DCA SIMULATION RESULT: BNBUSDT
--------------------------------------------------
• Market Price Used  : $605.50 USDT

• Strategy Interval  : Weekly

• Total Periods      : 12 weeks

• Total Capital In   : $120.00 USDT

• Total Asset Got    : 0.2155 BNB

• Current Portfolio  : $130.49 USDT

• Profit / Loss      : +$10.49 USDT (+8.74%)
==================================================
[SUCCESS] DCA simulation completed successfully!
   
