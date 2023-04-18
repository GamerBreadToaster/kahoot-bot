import webbrowser, time, keyboard as kb, mouse, os
os.system('cls')

if os.path.isfile('options.txt') == False:
    with open("options.txt", "w") as file:
        file.write("kahoot code:\n000000\n\nname:\ndefault\n\namount of bots:\n5\nduplicate delay by:\n1\n")
elif os.path.isfile('options.txt'):
    with open("options.txt", "r") as file:
        readlines_2 = file.readlines()
    new_readlines = [x[:-1] for x in readlines_2]
    code = int(new_readlines[1])
    name = new_readlines[4]
    bots = int(new_readlines[7])

#
url = f"https://kahoot.it/?pin={code}&refer_method=link"

#
webbrowser.get().open(url)
time.sleep(1.5)
kb.send("tab, tab")
kb.write(name)
kb.send("enter")
time.sleep(2)

if bots > 1:
    for i in range(bots - 1):
        webbrowser.get().open(url)
        time.sleep(0.2)
        mouse.click('left')
        time.sleep(1.1)
        kb.send("tab, tab")
        kb.write((name + str(i+2)))
        kb.send("enter")
