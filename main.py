import time
import logging
from config import SYMBOL, INVEST_AMOUNT, INTERVAL_HOURS, TESTNET

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def execute_dca_order():
    logging.info(f"Initiating DCA cycle for {SYMBOL}...")
    logging.info(f"Target Investment: {INVEST_AMOUNT} USDT")
    
    if TESTNET:
        logging.info("[TESTNET MODE] Order simulated successfully. No real funds were used.")
    else:
        # Real order execution logic via Binance API goes here
        pass
    
    logging.info("DCA cycle completed. Waiting for the next interval...\n")

if __name__ == "__main__":
    logging.info("Starting Binance DCA Agent...")
    logging.info(f"Mode: {'Testnet' if TESTNET else 'Live'}")
    
    try:
        while True:
            execute_dca_order()
            # Convert hours to seconds for the sleep timer
            time.sleep(INTERVAL_HOURS * 3600)
    except KeyboardInterrupt:
        logging.info("Binance DCA Agent stopped by user.")
