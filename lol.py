import webbrowser
import time
import win32com.client
import sys
#recieving user input
responde = input("y/n")
cantidad = int(input('cantidad'))
#loop
if responde == "y":
    for x in range(cantidad):
        #coneting to the terminal
        shell = win32com.client.Dispatch("WScript.Shell")
        #The tweets (you can add/delete/change it)
        tweet = "Fuck Elon Musk"
        tweet2 = "Fuck Donald trump"
        tweet3 = "fuck twitter"
        tweet4 = "Elon musk is extremely fat"
        #opening the browser and going to twiter
        webbrowser.open("https://x.com/home")
        #delay so the browser can procces  the input
        time.sleep(4)
        #opening the new tweet window
        shell.SendKeys("n" , 0)
        #more delay
        time.sleep(1)
        #cycling trought the tweets
        shell.SendKeys(tweet, 0)
        shell.SendKeys("^{ENTER}" , 0)
        shell.SendKeys(tweet2, 0)
        shell.SendKeys("^{ENTER}" , 0)
        time.sleep(1)
        shell.SendKeys(tweet3 , 0)
        shell.SendKeys("^{ENTER}" , 0)
        time.sleep(1)
        shell.SendKeys(tweet4 , 0)
        shell.SendKeys("^{ENTER}" , 0)
        time.sleep(1)
#ending the script        
else:
    sys.exit()