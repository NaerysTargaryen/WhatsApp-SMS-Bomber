import webbrowser
import pyautogui
import time
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"\033[38;2;{r};{g};{b}m"

def print_ascii_art():
    art = r'''
          /$$$$$$  /$$           /$$                                            
         /$$__  $$|__/          | $$                                            
        | $$  \__/ /$$  /$$$$$$| $$$$$$$    /$$$$$$  /$$   /$$ /$$   /$$  /$$$$$$ 
        | $$ /$$$$| $$ /$$__  $$| $$__  $$ /$$__  $$| $$  | $$| $$  | $$ /$$__  $$
        | $$|_  $$| $$| $$  \ $$| $$  \ $$| $$  \ $$| $$  | $$| $$  | $$| $$  \ $$
        | $$  \ $$| $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$
        |  $$$$$$/| $$|  $$$$$$$| $$$$$$$/|  $$$$$$$|  $$$$$$/|  $$$$$$/|  $$$$$$$
         \______/ |__/ \____  $$|_______/  \____  $$ \______/  \______/  \____  $$
                       /$$  \ $$           /$$  \ $$                     /$$  \ $$
                      |  $$$$$$/          |  $$$$$$/                    |  $$$$$$/
                       \______/            \______/                     \______/ 
'''
    print(random_color() + art + '\033[0m')

# Test
print_ascii_art()

message = input("What message would you like to send? ")
number = input("What number would you like to target? ")
amount = int(input("How many times would you like to send it? "))

webbrowser.open('https://web.whatsapp.com/send?phone=' + number + '&text=' + message)

time.sleep(7) #wait for whatsapp to load
for i in range(amount):
    pyautogui.typewrite(message)
    pyautogui.press('enter') #press enter key
    time.sleep(1) #wait before sending next message
    pyautogui.press('up') #move cursor to the previous message
    pyautogui.press('enter') #press enter key
    print(f"Message sent to {number}!")
    time.sleep(1) #wait before sending the next message

print("All messages sent!")
