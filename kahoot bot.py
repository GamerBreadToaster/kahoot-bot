import webbrowser,time, keyboard as kb, mouse

code = input("what is the kahoot code: ")
bots = int(input("How many bots do you want to send: "))
name = input("what name will the bot have: ")

url = f"https://kahoot.it/?pin={code}&refer_method=link"
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
webbrowser.get().open(url)
time.sleep(1.5)
kb.send("tab, tab")
kb.write(name)
kb.send("enter")
time.sleep(2)

for i in range(bots - 1):
    webbrowser.get().open(url)
    time.sleep(0.2)
    mouse.click('left')
    time.sleep(1.1)
    kb.send("tab, tab")
    kb.write((name + str(i+2)))
    kb.send("enter")