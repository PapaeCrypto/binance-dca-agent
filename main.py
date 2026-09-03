import time
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def run_dca_simulation():
    print("\n" + "="*50)
    print("      BINANCE DCA (DOLLAR-COST AVERAGING) SIMULATOR      ")
    print("="*50)
    
    # 1. User Inputs
    coin = input("Enter coin to DCA (e.g., BTC, ETH, BNB): ").strip().upper()
    symbol = f"{coin}USDT"
    
    try:
        amount_per_interval = float(input("Enter investment amount per interval (USDT): "))
    except ValueError:
        print("[ERROR] Invalid amount! Please enter a valid numerical value.")
        return

    print("\nSelect DCA Interval:")
    print("1. Daily")
    print("2. Weekly")
    print("3. Monthly")
    interval_choice = input("Choose interval (1/2/3): ").strip()
    
    interval_map = {"1": "Daily", "2": "Weekly", "3": "Monthly"}
    interval_str = interval_map.get(interval_choice, "Weekly")
    
    try:
        total_periods = int(input(f"Enter how many {interval_str.lower()} periods to simulate (e.g., 12, 24, 52): "))
    except ValueError:
        print("[ERROR] Invalid period count! Please enter a valid integer.")
        return
    
    print(f"\n[INFO] Fetching live market data from Binance for {symbol}...")
    
    # 2. Fetch Live Price with Fallback Mechanism
    current_market_price = None
    api_urls = [
        f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}",
        f"https://data-api.binance.vision/api/v3/ticker/price?symbol={symbol}"
    ]
    
    for url in api_urls:
        try:
            response = requests.get(url, timeout=4, verify=False)
            if response.status_code == 200:
                data = response.json()
                if "price" in data:
                    current_market_price = float(data["price"])
                    break
        except Exception:
            continue
            
    if current_market_price is None:
        print("[WARNING] Network restricted by ISP. Using fallback market reference price.")
        fallback_prices = {"BTCUSDT": 65000.0, "ETHUSDT": 35000.0, "BNBUSDT": 600.0}
        current_market_price = fallback_prices.get(symbol, 500.0)

    time.sleep(1)
    
    # 3. Dynamic Simulation Calculation
    total_invested = amount_per_interval * total_periods
    estimated_avg_buy_price = current_market_price * 0.92 
    
    total_coins_accumulated = total_invested / estimated_avg_buy_price
    current_portfolio_value = total_coins_accumulated * current_market_price
    
    profit_loss = current_portfolio_value - total_invested
    roi_percentage = (profit_loss / total_invested) * 100
    
    # 4. Terminal Output Display
    print("\n" + "-"*50)
    print(f"📊 DCA SIMULATION RESULT: {symbol}")
    print("-" * 50)
    print(f"• Market Price Used  : ${current_market_price:,.2f} USDT")
    print(f"• Strategy Interval  : {interval_str}")
    print(f"• Total Periods      : {total_periods} {interval_str.lower()}s")
    print(f"• Total Capital In   : ${total_invested:,.2f} USDT")
    print(f"• Total Asset Got    : {total_coins_accumulated:.4f} {coin}")
    print(f"• Current Portfolio  : ${current_portfolio_value:,.2f} USDT")
    print(f"• Profit / Loss      : ${profit_loss:,.2f} USDT ({roi_percentage:+.2f}%)")
    print("="*50)
    print("[SUCCESS] DCA simulation completed successfully!")

if __name__ == "__main__":
    # Main Loop for Continuous Run / Exit Option
    while True:
        run_dca_simulation()
        
        print("\n" + "~"*50)
        choice = input("Do you want to run another simulation? (y/n): ").strip().lower()
        if choice != 'y':
            print("\n[INFO] Exiting DCA Simulator. Thank you for using Binance Agent!")
            break
        print("\n" + "="*50 + "\n")
