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

timeelapsed = 0
keyboard = Controller()

Items = {"ENCHANTED_IRON": (735.7,363.2),
         "ENCHANTED_REDSTONE": (699.75, 399.4609375),
         "ENCHANTED_LAPIS_LAZULI": (842.70703125, 366.6953125),
         "ENCHANTED_GOLD": (769.3046875, 367.12890625)}
bestmargin = 0
bestitem = None

def time_randomizer():
    time.sleep(uniform(0.3,6))

def time_randomizer2():
    time.sleep(uniform(2,15))
def Profit_Calc(b=False):
    global bestmargin
    global bestitem
    bestmargin = 0
    if b:
        if not bestitem:
            return False

    for key,val in Items.items():
        API_KEY = '13ec34b5-9040-4c29-bfd6-e3cc28f824aa'
        ITEM_ID = key

        url = f'https://api.hypixel.net/skyblock/bazaar?key={API_KEY}'

        try:
            response = requests.get(url)
            data = response.json()

            if not data['success']:
                print("API error:", data.get('cause', 'Unknown'))
                sys.exit(1)

            product = data['products'][ITEM_ID]
            buy_price = product['buy_summary'][0]['pricePerUnit'] if product['buy_summary'] else None
            sell_price = product['sell_summary'][0]['pricePerUnit'] if product['sell_summary'] else None
            print(f"TEST ----> Item: {ITEM_ID}, Buy: {buy_price:.2f}, Sell: {sell_price:.2f}, Margin: Not Calculated")
            if buy_price and sell_price:
                margin = ((sell_price - buy_price) / buy_price * 100)*-1
                print(f"Item: {ITEM_ID}, Buy: {buy_price:.2f}, Sell: {sell_price:.2f}, Margin: {margin:.2f}%")
                if margin > 1 and margin>bestmargin:
                    bestmargin = margin

                    if not b:
                        bestitem = ITEM_ID
                        pyperclip.copy(str(sell_price + 4))
                    else:
                        if ITEM_ID == bestitem:
                            pyperclip.copy(str(buy_price - 4))

            else:
                print("Price data not available.")

        except Exception as e:
            print("Error:", e)
            return False

    if bestitem:
        return True
    else:
        return False

def buy_item(item):
    x,y = Items[item]
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
    keyboard.type(str(pyperclip.paste()))
    pyautogui.moveTo(731.140625, 529.390625, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    pyautogui.moveTo(736.8515625, 398.4921875, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    keyboard.type("t")

def sell_item(item):
    x,y = Items[item]
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
    keyboard.type(str(pyperclip.paste()))
    pyautogui.moveTo(731.140625, 529.390625, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    pyautogui.moveTo(736.8515625, 398.4921875, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    keyboard.type("t")

def cancel_order(b = False):
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
        pyautogui.moveTo(626.30859375, 401.14453125, duration=0.2)
    elif b:
        pyautogui.moveTo(626.2578125, 432.421875, duration=0.2)
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

def flip_item():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    pyautogui.moveTo(770.109375, 505.3046875, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    pyautogui.moveTo(626.2578125, 432.421875, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    pyautogui.moveTo(622.61328125, 438.9375, duration=0.2)
    time_randomizer()
    pyautogui.click()
    keyboard.type("e")
    keyboard.release(Key.esc)
    time_randomizer()
    keyboard.type("t")

def claimcoin():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    pyautogui.moveTo(770.109375, 505.3046875, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    pyautogui.moveTo(626.30859375, 401.14453125, duration=0.2)
    time_randomizer()
    pyautogui.click()
    time_randomizer()
    keyboard.type("e")
    keyboard.release(Key.esc)
    time_randomizer()
    keyboard.type("t")

def CheckifFilled(b=False):
    if pyperclip.paste() == "BUY_TRIGGER" and b != False:
        pyperclip.copy("Done")
        return True
    elif pyperclip.paste() == "SELL_TRIGGER" and b==False:
        pyperclip.copy("Done")
        return True

class BreakAllLoops(Exception): pass
time.sleep(5)
while True:
    timeelapsed = 0
    thing2 = None
    thing1 = None
    item = Profit_Calc(b=False)
    buy_item(bestitem)
    try:
        while True:

            time.sleep(1)
            if CheckifFilled(b=True):
                time_randomizer2()
                flip_item()
                Profit_Calc(b=True)
                sell_item(bestitem)
                timeelapsed = 0
                while True:
                    if CheckifFilled():
                        break
                    time.sleep(1)
                    timeelapsed += 1
                    print(f"{timeelapsed}s")
                    if timeelapsed > 300:
                        cancel_order()
                        print("Breaking Loop....")
                        raise BreakAllLoops()
                    elif thing1 is not None and timeelapsed >= thing1 and timeelapsed%50==0 or thing1 is None:
                        thing1 = timeelapsed
                        time.sleep(uniform(0.5, 2))
                        keyboard.press(Key.enter)
                        keyboard.release(Key.enter)
                        time.sleep(uniform(0.5, 2))
                        pyautogui.click()
                        time.sleep(uniform(1, 1.2))
                        keyboard.type("e")
                        keyboard.release(Key.esc)
                        time.sleep(uniform(0.5, 2))
                        keyboard.type("t")
                timeelapsed = 0
                claimcoin()
                raise  BreakAllLoops
            time.sleep(1)
            timeelapsed +=1
            print(f"{timeelapsed}s")
            if timeelapsed>300:
                cancel_order(b=True)
                print("Breaking Loop....")
                raise BreakAllLoops()
            elif thing2 is not None and timeelapsed>=thing2 and timeelapsed%60==0 or thing2 is None:
                thing2=timeelapsed
                time.sleep(uniform(0.5, 2))
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                time.sleep(uniform(0.5, 2))
                pyautogui.click()
                time.sleep(uniform(1,1.2))
                keyboard.type("e")
                time.sleep(uniform(0.5, 2))
                keyboard.type("t")
    except BreakAllLoops:
        print("Exited all loops")
