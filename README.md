# 🤖 Binance DCA Agent ( Dollar Cost Averaging)

An autonomous AI investment and DCA (Dollar Cost Averaging) simulation agent built for the Binance Agent OS ecosystem. This repository provides a robust, interactive workflow to simulate and project automated asset accumulation strategies using real-time market data.

---

## 🌟 Key Features

* Live Market Data Integration: Fetches real-time cryptocurrency ticker prices directly from Binance Public APIs with an automatic fallback mechanism (binance.vision) for high availability.
* Interactive DCA Configuration: Allows users to dynamically input custom coin symbols, DCA amount per session, and total frequency cycles.
* Smart Portfolio Projection: Automatically calculates simulated average entry prices, total invested capital, estimated coin accumulation, and projected ROI percentages.
* Continuous Monitoring Loop: Features an active session loop so the agent stays online, allowing multi-session simulations and a clean exit command (exit).
* Agent OS Compliance: Fully integrated with standard agent manifests (agent-manifest.json) tailored for Track A submission.

---

## 📂 Repository Structure

```text
binance-dca-agent/
├── agent-manifest.json    # Agent OS registration and metadata
├── main.py                # Core agent logic, DCA simulation math, and live API fetcher
└── README.md              # Project documentation
```
## 🚀 Quick Start Guide

### Prerequisites
* Python 3.x installed on your system.
* No external libraries required (uses Python standard libraries: urllib, json, time, sys).

### Running the Agent
1. Clone the repository or download the source code.
   ```bash
   git clone https://github.com/PapaeCrypto/binance-dca-agent.git
   ```
3. Open your terminal in the project directory.
4. Run the main agent script:
   ```bash
   python main.py
   ```
5. Enter your desired coin symbol (e.g., btc, eth), enter the DCA amount per session, and specify the number of intervals.
6. Type exit whenever you want to safely terminate the agent session.
   
## 🛡️ License
This project is developed for the Binance Agent OS Hackathon .
