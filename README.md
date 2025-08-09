# Bazaar-Flipper-Bot-for-Hypixel-Skyblock
This is a personal project built to automate Bazaar trading in Hypixel Skyblock. It monitors item prices in real time, detects profitable flipping opportunities, and executes buy/sell orders automatically.

Key Features
Live Price Tracking – Continuously retrieves item prices using the Hypixel API.

Profit Margin Calculation – Identifies items with profitable spreads between buy and sell prices.

Automated Order Execution – Places buy orders, flips them to sell orders when filled, and manages the full trade cycle.

Order Management – Cancels stale orders after a set timeout, prevents duplicate trades, and claims coins from completed sales.

Real-Time Console – Tkinter-based interface displaying current queues, executed actions, and trade status.

AFK Prevention – Periodic in-game interactions to avoid disconnection from inactivity.

Requirements
ChatTriggers Module – Required for detecting order completions and triggering certain in-game actions.

Index File – Included in this repository and must be installed in your ChatTriggers modules folder.

How It Works
Fetches up-to-date Bazaar prices for tracked items.

Selects items meeting profitability criteria.

Places buy orders and monitors their status.

Converts completed buy orders to sell orders.

Cancels orders exceeding the set timeout and claims coins automatically.

Disclaimer
This project is for personal and educational purposes only.
It automates in-game actions and violates Hypixel’s Terms of Service. Running this bot on Hypixel can result in a permanent account ban.
Use entirely at your own risk.
