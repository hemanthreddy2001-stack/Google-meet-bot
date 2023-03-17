import pyautogui as pg
from datetime import datetime as dt
import webbrowser
import time
import pywhatkit as pw
import cv2
import csv

def delay(sec):
    print('waiting for '+str(sec)+' seconds')
    for i in range(sec, 0, -1):
        print(i)
        time.sleep(1)

def wait(h,m):
    now=dt.now()
    ch= now.hour
    cm= now.minute
    if h<=ch and m<=cm:
        return
    print('waiting for '+str((h-ch)*3600+(m-cm)*60)+' seconds from '+str(ch)+":"+str(cm))
    delay((h-ch)*3600+(m-cm)*60)

def find_phNo(name):
    with open("contacts.csv", 'r') as file:
            csvfile=csv.DictReader(file)
            for r in csvfile:
                    if name==dict(r)['Names']:
                            return dict(r)['Phone_numbers']

def joinMeet(link, leave=False,durationInMins=5/60,h=dt.now().hour, m=dt.now().minute):
    # waiting until join time
    wait(h, m)
    
    # open browser
    with pg.hold('win'):
        pg.press('2')
    delay(5)
    
    #open link in new tab
    webbrowser.open(link)
    delay(10)
    
    # turn off camera
    print("turning off camera")
    with pg.hold('ctrl'):
        pg.press('e')
    delay(3)
    
    # turn off audio
    print("turning off audio")
    with pg.hold('ctrl'):
        pg.press('d')
    delay(4)
    
    # join btn
    print("clicking join button")
    joinBtn = None
    
    # while joinBtn is None:
    try:
        print('connecting...')
        joinBtn = pg.locateCenterOnScreen("joinnowbtn.png")
        if joinBtn is None:
            raise pg.ImageNotFoundException
            
    except pg.ImageNotFoundException:
        print("'join now' button not found. clicking 'ask to join' button")
        joinBtn = pg.locateCenterOnScreen("asktojoinbtn.png")
        if joinBtn is None:
            raise pg.ImageNotFoundException
            
    except pg.ImageNotFoundException:
        print("ask to join button not found")

    pg.click(joinBtn[0], joinBtn[1])
    print('meet joined at ',dt.now().strftime('%I:%M %p'))
    pw.sendwhatmsg_instantly('<your phone_num with country code>', link+' meet joined at '+dt.now().strftime('%I:%M %p'), tab_close=True, close_time=5)
    
    # leave meet
    if leave:
        delay(durationInMins*60) # duration is in mins
        with pg.hold('ctrl'):
            pg.press('w')
        print(link+' meet left at ',dt.now().strftime('%I:%M %p'))
        pw.sendwhatmsg_instantly('<your phone_num with country code>', 'meet left at'+dt.now().strftime('%I:%M %p'), tab_close=True, close_time=5)

if __name__=='__main__':
    joinMeet('link',h="Joining hour", m="Joining minute")