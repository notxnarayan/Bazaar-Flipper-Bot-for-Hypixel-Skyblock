# Bazaar-Flipper-Bot-for-Hypixel-Skyblock
This project is a fully automated Hypixel Skyblock Bazaar flipping bot designed to find the best profit margins and handle the entire flipping process for you.

It connects to the Hypixel Bazaar API to fetch real-time prices, identifies the most profitable items to flip, and then automates placing buy orders, waiting for them to fill, and creating sell orders. It also claims coins automatically once trades are completed.

The bot uses queues to manage buy and sell orders efficiently, ensuring that no orders are skipped or executed incorrectly. It includes built-in delays and randomization to make mouse and keyboard movements look human-like, reducing detection risk.

With its Tkinter-based interface, you can monitor logs, see actions being taken in real-time, making debugging easy. It’s optimized for smooth operation on Mac, using safe clipboard handling for item names.

Requirements:
- ChatTriggers module is required for this bot to function. This module handles in-game event detection and order completion tracking.
- The required index file is included in this repository. Place it inside your ChatTriggers modules folder before running the bot.

Disclaimer:
This project is for personal and educational purposes only. It automates in-game actions and violates Hypixel's Terms of Service. 
Using this bot on Hypixel can result in a permanent account ban. You are fully responsible for any consequences — use entirely at your own risk.

