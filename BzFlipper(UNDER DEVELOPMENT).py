#Copyright (c) 2025, notxnarayan
#All rights reserved.

#This source code is licensed under the GPL license found in the
#LICENSE file in the root directory of this source tree.


import time
import requests
import sys
import pyperclip
import pyautogui
from pynput.keyboard import Key, Controller
from random import uniform
import threading
import tkinter as tk
from tkinter import scrolledtext


pyperclip.set_clipboard("pbcopy")

keyboard = Controller()
buy_queue = []
sell_queue = []
action_queue = []

bestmargin = 0
bestitem = None

item_cords = {
    "ENCHANTED_IRON": (735.7, 363.2),
    "ENCHANTED_REDSTONE": (699.75, 399.4),
    #"ENCHANTED_LAPIS_LAZULI": (842.7, 366.6),
    #"ENCHANTED_GOLD": (769.3, 367.1)
}

item_names = {
    "ENCHANTED_IRON": "enchanted iron",
    "ENCHANTED_REDSTONE": "enchanted redstone",
    #"ENCHANTED_LAPIS_LAZULI": "enchanted lapis lazuli",
    #"ENCHANTED_GOLD": "enchanted gold"
}

latest_prices = {
    item: {"buy": None, "sell": None} for item in item_cords
}

action_map = {
    "cbuy": buy_queue,
    "csell": sell_queue,
}

def time_randomizer():
    time.sleep(uniform(0.3, 6))

def time_randomizer2():
    time.sleep(uniform(2, 15))

class TkConsole:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Live Console")
        self.root.attributes("-topmost", True)
        self.text_area = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, height=10, width=50, state='disabled'
        )
        self.text_area.pack(expand=True, fill='both')

    def write(self, message):
        self.text_area.config(state='normal')

        self.text_area.insert(tk.END, str(message) + "\n")

        lines = self.text_area.get("1.0", tk.END).split("\n")
        if len(lines) > 11:
            self.text_area.delete("1.0", "2.0")
        self.text_area.config(state='disabled')
        self.text_area.yview(tk.END)

    def start(self):
        self.root.mainloop()

console = TkConsole()


processed_orders = set()


class Node:
    def __init__(self, item, bors):
        self.name = item
        self.bors = bors
        self.time_elapsed = 0
        self.canceled = False
        self.queued = False
        self.active = True
        self.stopwatch_thread = threading.Thread(target=self.stopwatch)
        self.stopwatch_thread.start()
        self.re_innit()
        action_queue.append(f"{bors}-->{self.name}")

    def deactivate(self):
        self.active = False

    def re_innit(self):
        if self.bors == "buy":
            buy_queue.insert(0,self)
            threading.Thread(target=self.check_if_filledB).start()
        elif self.bors == "sell":
            sell_queue.insert(0,self)
            threading.Thread(target=self.check_if_filledA).start()

    def stopwatch(self):
        while self.active:
            time.sleep(1)
            self.time_elapsed += 1
            if self.time_elapsed >= 500 and not self.queued:
                self.canceled = True
                action_queue.append(f"c{self.bors}-->{self.name}")
                console.write(f"{self.bors} order for 160x {self.name} canceled...")
                self.deactivate()

    def check_if_filledB(self):
        while self.active:
            if CheckifFilled(self.name, b=True):
                action_queue.append(f"flip-->{self.name}")
                self.deactivate()

    def check_if_filledA(self):
        while self.active:
            if CheckifFilled(self.name, b=False):
                action_queue.append(f"claim-->{self.name}")
                self.deactivate()

    def __del__(self):
        self.deactivate()

    def __str__(self):
        return self.name


def CheckifFilled(item, b=False):
    key = (item, "buy" if b else "sell")
    if key in processed_orders:
        return False

    try:
        clipboard = pyperclip.paste()
        if clipboard is None:
            console.write(f"[WARN] Clipboard empty while checking {item}")
            return False
        clipboard = clipboard.lower()
    except Exception as e:
        console.write(f"[ERROR] Clipboard access failed: {e}")
        return False

    if item not in item_names:
        console.write(f"[ERROR] '{item}' not found in item_names.")
        return False

    formatted_name = item_names[item].lower()
    if b and "buy" in clipboard and formatted_name in clipboard:
        pyperclip.copy("Done")
        processed_orders.add(key)
        return True
    elif not b and "sell" in clipboard and formatted_name in clipboard:
        pyperclip.copy("Done")
        processed_orders.add(key)
        return True
    return False
import time
import os


def clear_console():
    os.system("clear")


def buy_item(item):
    time.sleep(1)
    console.write(f"Buying {item}")
    x,y = item_cords[item]
    time_randomizer2()
    pyautogui.moveTo(750, 500, duration=0.2)
    time_randomizer()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    pyautogui.moveTo(x,y, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    pyautogui.moveTo(733.6,399.1, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    pyautogui.moveTo(807.7,397, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    pyautogui.moveTo(699.6953125, 402.3515625, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    pyautogui.moveTo(843.6,402.7, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    buy_price = str(latest_prices[item]["buy"])
    keyboard.type(buy_price)
    pyautogui.moveTo(731.140625, 552.390625, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    pyautogui.moveTo(736.8515625, 398.4921875, duration=0.2)
    pyperclip.copy("Hello")
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    keyboard.type("t")
    console.write(f"Finishied Buying {item}")

def sell_item(item):
    time.sleep(1)
    console.write(f"Selling {item}")
    x,y = item_cords[item]
    pyautogui.moveTo(750, 500, duration=0.2)
    time_randomizer()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    pyautogui.moveTo(x,y, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    pyautogui.moveTo(733.6,399.1, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    pyautogui.moveTo(844.8,402.7, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    pyautogui.moveTo(843.6,402.7, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()

    buy_price = str(latest_prices[item]["sell"])
    keyboard.type(buy_price)

    pyautogui.moveTo(731.140625, 529.390625, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    pyautogui.moveTo(736.8515625, 398.4921875, duration=0.2)
    pyperclip.copy("Hello")
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    keyboard.type("t")
    console.write(f"Finishied Selling {item}")

def cancel_order(num,b = False):
    time.sleep(1)
    console.write(f"Cancelling order {num}")
    time_randomizer2()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    pyautogui.moveTo(770.109375, 505.3046875, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    if not b:
        console.write(f"Moving to{626.30859375 + (num * 35)}")
        pyautogui.moveTo(626.30859375+(num*35), 401.14453125, duration=0.2)
    elif b:
        console.write(f"Moving to{626.30859375 + (num * 35)}")
        pyautogui.moveTo(626.2578125+(num*35), 432.421875, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    pyautogui.click()
    time_randomizer()

    if not b:
        pyautogui.moveTo(734.33203125, 399.50390625, duration=0.2)
    elif b:
        pyautogui.moveTo(661.515625, 398.85546875, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    keyboard.type("e")
    keyboard.release(Key.esc)
    for i in range(0,5):
        time_randomizer()
        pyautogui.click()
        time_randomizer()
        pyautogui.moveTo(663.83203125, 507.84375, duration=0.2)
        time_randomizer()
        pyautogui.click()
        time_randomizer()
        pyautogui.moveTo(660.5234375, 417.4921875, duration=0.2)
        time_randomizer()
        pyautogui.click()
        time_randomizer()
        keyboard.type("e")
        keyboard.release(Key.esc)
        time_randomizer()
        keyboard.type("t")
        time_randomizer()
        keyboard.type("/pickupstash")
        time_randomizer()
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    console.write(f"Finishied Cancelling {num}")
def flip_item(num):
    time.sleep(1)
    console.write(f"Flipping item {num}")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    pyautogui.moveTo(770.109375, 505.3046875, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    console.write(f"Moving to{626.30859375 + (num * 35)}")
    pyautogui.moveTo(626.2578125+(num*35), 432.421875, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    keyboard.type("e")
    keyboard.release(Key.esc)
    time_randomizer()
    keyboard.type("t")
    console.write(f"Finishied Flipping {num}")

def claimcoin(num):
    time.sleep(1)
    console.write(f"Claiming coin {num}")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    pyautogui.moveTo(770.109375, 505.3046875, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    console.write(f"Moving to{626.30859375+(num*30)}")
    pyautogui.moveTo(626.30859375+(num*30), 401.14453125, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    keyboard.type("e")
    keyboard.release(Key.esc)
    time_randomizer()
    keyboard.type("t")
    console.write(f"Finishied Claimimg {num}")

def update_latest_prices():
    while True:
        try:
            API_KEY = '13ec34b5-9040-4c29-bfd6-e3cc28f824aa'
            url = f'https://api.hypixel.net/skyblock/bazaar?key={API_KEY}'
            response = requests.get(url)
            data = response.json()

            if not data['success']:
                console.write("API error:", data.get('cause', 'Unknown'))
            else:
                for item in latest_prices:
                    product = data['products'][item]
                    buy_price = product['buy_summary'][0]['pricePerUnit'] if product['buy_summary'] else None
                    sell_price = product['sell_summary'][0]['pricePerUnit'] if product['sell_summary'] else None
                    latest_prices[item]["buy"] = sell_price+5
                    latest_prices[item]["sell"] = buy_price-5

        except Exception as e:
            console.write(f"[ERROR] Price update failed: {e}")
        time.sleep(20)

def Profit_Calc():
    API_KEY = '13ec34b5-9040-4c29-bfd6-e3cc28f824aa'
    url = f'https://api.hypixel.net/skyblock/bazaar?key={API_KEY}'
    try:
        response = requests.get(url)
        data = response.json()
        if not data['success']:
            console.write("API error:", data.get('cause', 'Unknown'))
            return []

        good_items = []
        for key in item_cords:
            if any(node.name == key for node in buy_queue):
                continue
            product = data['products'][key]
            buy_price = product['buy_summary'][0]['pricePerUnit'] if product['buy_summary'] else None
            sell_price = product['sell_summary'][0]['pricePerUnit'] if product['sell_summary'] else None
            if buy_price and sell_price:
                margin = ((sell_price - buy_price) / buy_price * 100) * -1
                if margin > 1:
                    good_items.append((key, margin, buy_price, sell_price))
        return sorted(good_items, key=lambda x: x[1], reverse=True)
    except Exception as e:
        console.write("[ERROR] Profit_Calc failed:", e)
        return []

def create_orders():
    while True:
        time.sleep(1)
        current_buy_items = [node.name for node in buy_queue]
        remaining_slots = 10 - len(current_buy_items)
        if remaining_slots <= 0:
            continue
        profitable_items = Profit_Calc()
        added = 0
        for item, margin, buy_price, sell_price in profitable_items:
            if item in current_buy_items:
                continue

            Node(item, "buy")
            added += 1
            time.sleep(uniform(0.3, 2))
            if added >= remaining_slots:
                break

def actions():
    while True:
        try:
            bq = []
            sq = []
            for i in buy_queue:
                bq.append(i.name)
            for a in sell_queue:
                sq.append(a.name)
            bors, item = action_queue[0].split("-->")
            item_num = None
            console.write(f"Executing {bors} order for 160x {item}")
            console.write("Action Queue vvv")
            console.write(action_queue)
            console.write("Buy Queue vvv")
            console.write(bq)
            console.write("Sell Queue vvv")
            console.write(sq)

            if bors == "antikick":
                console.write("Performing anti-kick movement...")
                try:
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    time_randomizer()
                    pyautogui.click()
                    time_randomizer()
                    keyboard.type("e")
                    keyboard.release(Key.esc)
                    time_randomizer()
                    keyboard.type("t")
                except Exception as e:
                    console.write("Anti-kick failed:", e)

            elif "c" in bors and bors != "claim":
                console.write(f"Executing {bors} for 160x {item}")
                for idx, i in enumerate(action_map[bors]):
                    if i.name == item:
                        item_num = idx
                        if bors.strip("c") == "buy":
                            cancel_order(idx, b=True)
                        if bors.strip("c") == "sell":
                            cancel_order(idx, b=False)
                        action_map[bors].pop(idx)
                console.write(f"{item} at {item_num}")

            elif "flip" in bors:
                for idx, i in enumerate(buy_queue):
                    if i.name == item:

                        flip_item(idx)
                        console.write("Passing sell action")
                        action_queue.append(f"sell-->{i.name}")
                        buy_queue.pop(idx)
            elif "claim" in bors:
                for idx, i in enumerate(sell_queue):
                    if i.name == item:
                        claimcoin(idx)
                        sell_queue.pop(idx)
                        del i

            elif "sell" in bors and "c" not in bors:
                for idx, i in enumerate(buy_queue):
                    if i.name == item:
                        sell_item(item)
                        buy_queue.pop(idx)
                        i.bors = "sell"
                        i.time_elapsed = 0
                        i.queued = False
                        sell_queue.append(i)
                        threading.Thread(target=i.check_if_filledA).start()
                        break
            else:
                console.write(f"Executing {bors} order for 160x {item}")
                if bors == "buy":
                    buy_item(item)

            action_queue.pop(0)

        except IndexError:
            pass


if __name__ == "__main__":
    console.write("Start Test")
    threading.Thread(target=update_latest_prices, daemon=True).start()
    threading.Thread(target=create_orders, daemon=True).start()
    threading.Thread(target=actions, daemon=True).start()
    console.start()
    while True:
        time.sleep(1)





