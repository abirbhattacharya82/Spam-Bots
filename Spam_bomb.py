#GUI Spam Bot
from tkinter import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def spammer():
    target1=e1.get()
    message=e2.get()
    target="'"+target1+"'"
    d=webdriver.Chrome("files/driver_1.exe")
    d.get("https://web.whatsapp.com/")
    wait=WebDriverWait(d,600)
    x_arg="//span[contains(@title, "+target+")]"
    target=wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    target.click()
    message_box=d.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
    for i in range(0,5):
        message_box.send_keys(message+Keys.ENTER)


window=Tk()
window.title("Spam Bomber")
window.resizable(0,0)

l1=Label(window,text="Enter your Whom to Send")
l1.grid(row=0,column=0)

e1_val=StringVar()
e1=Entry(window,textvariable=e1_val)
e1.grid(row=0,column=1)

l2=Label(window,text="Enter What to Send")
l2.grid(row=1,column=0)

e2_val=StringVar()
e2=Entry(window,textvariable=e2_val)
e2.grid(row=1,column=1)

b1=Button(window,text="Start Spamming",width=40,command=spammer)
b1.grid(row=2,column=0,columnspan=2)

window.mainloop()