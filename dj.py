import pyautogui
import keyboard
import time
from tkinter import *
import threading

count = 0
running = False

def click_mouse(interval):
    global count
    click_count = 0
    while not keyboard.is_pressed("esc"):
        if running:
            pyautogui.click()
            click_count += 1
            count = click_count  # 更新全局变量 count
            print("已点击次数：", click_count)
            time.sleep(1 / interval)

def update_label():
    global count, running
    label.config(text=f"点击次数：{count}\n状态：{'运行中' if running else '已停止'}")
    window.after(1000, update_label)

def on_press(event):
    global running
    if event.event_type == keyboard.KEY_DOWN and event.name == "f9":
        running = not running
        if running:
            print("开始点击")
            threading.Thread(target=click_mouse, args=(interval,), daemon=True).start()
        else:
            print("停止点击")

if __name__ == "__main__":
    interval = 10

    window = Tk()
    window.title("鼠标点击器")
    window.geometry("200x100")

    label = Label(window, text="", font=("Arial", 14))
    label.pack(pady=20)

    window.after(1000, update_label)

    keyboard.hook(on_press)

    window.mainloop()
