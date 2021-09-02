import os
import time
import pyautogui
a = 1
b = "1"
c = "2"
print("Otomatize bilgi toplama")
print("------------------------")
target = pyautogui.prompt(text="      hedef giriniz", title="OBT İÇİN İP SEÇİMİ", default="")
nmap = input("nmap için\nevet = 1\nhayır = 2\n>_ ")
if nmap == b:
    os.system("clear")
    time.sleep(2)
    os.system("whois "+ target)
    time.sleep(1)
    print("-----------------------")
    os.system("nmap -sS -sV "+ target)
    print("-----------------------")
    os.system("dnsenum "+ target)
    pyautogui.alert(text="OBT SONUÇLARI GÖSTERİLMİŞTİR")
if nmap == c:
    os.system("clear")
    time.sleep(2)
    os.system("whois "+ target)
    time.sleep(1)
    print("-----------------------")
    os.system("dnsenum "+ target)
    pyautogui.alert(text="OBT SONUÇLARI GÖSTERİLMİŞTİR")
'''
pyautogui.keyDown("ctrl")
pyautogui.press("c")
pyautogui.alert(text=os.system("clear"))
'''