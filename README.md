# Binance DCA Agent 🤖📈

> A lightweight, automated Dollar-Cost Averaging (DCA) agent built for the Binance Agent OS Mini Hackathon.

## 🔄 System Workflow & Architecture

The agent operates on a continuous, interval-based loop designed to execute disciplined asset accumulation with safety checks.


+-------------------------------------------------------+
|                   Start Agent (main.py)               |
+-------------------------------------------------------+
                            │
                            ▼
+-------------------------------------------------------+
|              Load Config (config.py)                  |
|  - Asset Symbol (e.g., BTCUSDT)                       |
|  - Investment Amount & Interval                       |
|  - Testnet Mode Flag                                  |
+-------------------------------------------------------+
                            │
                            ▼
+-------------------------------------------------------+
|             Execute DCA Cycle Function                |
+-------------------------------------------------------+
                            │
              Is TESTNET Mode Enabled? (True/False)
                           / \
                          /   \
               [YES]     /     \     [NO]
                        ▼       ▼
       +─────────────────────────+     +─────────────────────────+
       |   Simulate Order Exec.  |     |   Live Order Execution  |
       |   (Safe sandbox logging)|     |   (Binance API integration)|
       +─────────────────────────+     +─────────────────────────+
                        │                       │
                        └───────────┬───────────┘
                                    │
                                    ▼
+-------------------------------------------------------+
|             Log Results & Status Update               |
+-------------------------------------------------------+
                            │
                            ▼
+-------------------------------------------------------+
|        Sleep Timer (Interval Hours converted to sec)  |
+-------------------------------------------------------+
                            │
                            └────── (Repeat Loop) ───┘
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
