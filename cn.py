import tkinter as tk
import time
import pyautogui
import os
pyautogui.alert(text="按下 Ctrl+s 开始连点",title="提示",button="好的")
print("作者：周示麟")
print("日志: ")

click_times = 15
click_frequency = 1/20
log_temp = "Wrong"
 
def log(text):
    print("[", time.asctime(), "]", text)

def start(event):
    log("user/key s")
    log("play function start")
    log_temp = "click_times: {} click_frequency: {}".format(str(click_times), str(click_frequency))
    log(log_temp)
    for i in range(click_times):
        pyautogui.click()
        time.sleep(click_frequency)

def submit():
    global click_frequency
    global click_times
    
    log("user/button buttonSubmit")
    click_frequency = 1 / int(entrySetFrequency.get())
    click_times = int(entrySetTimes.get())
    log_temp = "set var click_frequency to 1 / entrySetFrequency.get: " + str(click_frequency)
    log(log_temp)
    log_temp = "set var click_times to entrySetTimes.get: " + str(click_times)
    log(log_temp)

root = tk.Tk()
root.title("微连点 MicroAutoClicker   @周示麟")
root.geometry("400x150")

textSetFrequency = tk.Label(root, text="设置每秒单击次数：")
textSetFrequency.pack()

entrySetFrequency = tk.Entry(root)
entrySetFrequency.insert(0, "20")
entrySetFrequency.pack()

textSetTimes = tk.Label(root, text="设置总单击次数：")
textSetTimes.pack()

entrySetTimes = tk.Entry(root)
entrySetTimes.insert(0, "15")
entrySetTimes.pack()

buttonSubmit = tk.Button(root, text='提交', width=10, height=2, command=submit)
buttonSubmit.pack()

root.bind("<Control-s>", start)

root.mainloop()
