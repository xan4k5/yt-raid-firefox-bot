import pyautogui
import time

print("Waiting for 3 seconds.")
time.sleep(3)

x, y = pyautogui.position()
print(f"{x}, {y}")
