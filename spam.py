import pyautogui,time
text = input()
time.sleep(5)
for i in range(5):
    pyautogui.typewrite(text)#your text that would be a spam message
    pyautogui.press('enter')
