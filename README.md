# Binance DCA Agent 🤖📈

> A lightweight, automated Dollar-Cost Averaging (DCA) agent built for the Binance Agent OS Mini Hackathon.

## 🔄 System Workflow
The agent operates on a continuous, interval-based loop:
1. Load Configuration: Reads settings (such as asset symbol, amount, and testnet flag) from config.py.
2. Execute DCA Cycle: Runs the trade execution logic (simulates orders securely if Testnet is active, or triggers live orders via Binance API).
3. Log & Sleep: Records the execution status and waits for the defined time interval before repeating the loop.


## ✨ Core Features
* Automated Periodic Accumulation: Runs continuously to execute recurring buy orders according to your preset intervals.
* Testnet/Sandbox Safety: Built-in toggle to simulate orders securely without risking real capital during testing phases.
* Modular Clean Code: Separates execution logic (main.py) from user configurations (config.py) for easy adjustments.

## 🛠️ Project Structure
* main.py: Core logic containing the main loop, timer, and logging mechanisms.
* config.py: Configuration file for setting market parameters and execution flags.
* LICENSE: MIT License governing open-source usage.

## 🚀 Getting Started & Installation
1. Clone the repository:
   git clone https://github.com/PapaeCrypto/binance-dca-agent.git
2. Adjust your setting inside :config.py
3. Run the agent script: python main.py
