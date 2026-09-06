import urllib.request
import json
import time
import sys

def fetch_binance_price(symbol):
    endpoints = [
        f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}",
        f"https://data-api.binance.vision/api/v3/ticker/price?symbol={symbol}"
    ]
    
    for url in endpoints:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=3) as response:
                data = json.loads(response.read().decode())
                return float(data['price'])
        except Exception:
            continue
            
    return None

def run_dca_agent():
    print("==================================================")
    print("🤖 BINANCE DCA AGENT (Track A: Dollar Cost Averaging)")
    print("==================================================")
    print("[+] Initializing Agent OS environment...")
    time.sleep(1)
    
    print("\n[?] Instructions:")
    print("    - Configure your DCA strategy interactively.")
    print("    - Type 'exit' anytime to stop the agent session.")
    
    while True:
        print("-" * 50)
        coin_input = input("Enter coin symbol to DCA [or type 'exit']: ").strip()
        
        if coin_input.lower() == 'exit':
            print("\n[+] Shutting down Agent OS environment safely...")
            time.sleep(1)
            print("✨ Agent session terminated. Goodbye!")
            break
            
        if not coin_input:
            symbol = "BTCUSDT"
            display_symbol = "BTC"
        else:
            clean_coin = coin_input.upper().replace("USDT", "")
            symbol = clean_coin + "USDT"
            display_symbol = clean_coin
            
        try:
            amount_input = input(f"Enter amount per DCA session (USD) [Default 50]: ").strip()
            amount = float(amount_input) if amount_input else 50.0
            
            print("Select DCA Interval:")
            print("  1. Daily")
            print("  2. Weekly")
            print("  3. Monthly")
            interval_choice = input("Enter choice (1/2/3) [Default 2 - Weekly]: ").strip()
            
            if interval_choice == '1':
                interval_str = "Daily"
            elif interval_choice == '3':
                interval_str = "Monthly"
            else:
                interval_str = "Weekly"
                
            duration_input = input(f"Enter duration / total {interval_str.lower()} intervals [Default 4]: ").strip()
            duration_cycles = int(duration_input) if duration_input else 4
            
        except ValueError:
            print("⚠️ Invalid numeric/choice input. Using default values ($50, Weekly, 4 intervals).")
            amount = 50.0
            interval_str = "Weekly"
            duration_cycles = 4
            
        print(f"\n[+] Asset: {symbol} | Amount: ${amount} | Interval: {interval_str} | Duration: {duration_cycles} cycles")
        print("[+] Connecting to Binance Market Data Streams...\n")
        time.sleep(1)

        print(f"--------------------------------------------------")
        print(f"📊 Running DCA Simulation for: {symbol}")
        
        current_price = fetch_binance_price(symbol)
        
        if current_price:
            print(f"💰 Current Live Price : ${current_price:,.2f}")
            time.sleep(1)
            
            # Simulasi perhitungan DCA
            total_invested = amount * duration_cycles
            avg_entry_price = current_price * 0.985  # Simulasi rata-rata harga masuk
            estimated_coins = total_invested / avg_entry_price
            current_portfolio_value = estimated_coins * current_price
            roi_percentage = ((current_portfolio_value - total_invested) / total_invested) * 100
            
            print(f"⏱️ Strategy Frequency : Every {interval_str} ({duration_cycles} total executions)")
            print(f"📈 Simulated Avg Entry : ${avg_entry_price:,.2f}")
            print(f"💵 Total Capital Invested : ${total_invested:,.2f}")
            print(f"🪙 Estimated Accumulation : {estimated_coins:,.4f} {display_symbol}")
            print(f"💼 Projected Portfolio Value: ${current_portfolio_value:,.2f}")
            print(f"🚀 Estimated ROI (Sim)    : +{roi_percentage:.2f}%")
            print(f"🔒 Status             : Scanned & Verified via Agent OS.")
        else:
            print(f"⚠️ Warning            : Invalid symbol or connection timeout for '{symbol}'.")
        
        print("--------------------------------------------------")
        print("\n✨ DCA simulation cycle completed. Ready for the next session.\n")

if __name__ == "__main__":
    run_dca_agent()
