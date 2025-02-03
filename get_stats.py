import pyautogui
import time
import win32api, win32con
import win32gui
import os
import mouse
import pytesseract
import cv2
import random
import json
import time
import sys



pytesseract.pytesseract.tesseract_cmd = R"C:\Program Files\Tesseract-OCR\tesseract.exe"
#coords for profile

alliance1 = (730,255)
alliance2 = (1065,285)
alliance_no_server1 = [730,270] # to use if server isnt visible 
alliance_no_server2 = [1165,320]
Server1 = [1320,425]
Server2 = [1400,460]   

#coords for the stats 

power1 = [430,770]
power2 = [630,810]

merit1 = [430,861]
merit2 = [630,898]

kills1 = [1350,693]
kills2 = [1500,723]

healed1 = [1350,766]
healed2 = [1500,796]

victories1 = [1350,540]
victories2 = [1500,585]

defeats1 = [1350,575]
defeats2 = [1500,615]

dead1 = [1350,730]
dead2 = [1500,760]

gathered1 = [1250,845]
gathered2 = [1500,880]








def click(x,y):
    
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.1)

def resizeWindow():
    try: 
        
        hwnd = win32gui.FindWindow(None, "Call of Dragons")
        win32gui.MoveWindow(hwnd, 0, 0, 1920, 1080, True) 
        
    except:
        print("Game isnt open - resizeWindow")
        pass

def foreground():
    try: 
        hwnd = win32gui.FindWindow(None, "Call of Dragons")
        win32gui.SetForegroundWindow(hwnd)
    except:
        print("Game isnt open - foreground")
        pass



def find_player(player_id):
    # This function will find a player in the game and return their stats
    # First, we need to get the player's id from the spreadsheet
    resizeWindow()
    foreground()


    #prerequisite for this is having the search lords window open 
    
    click(455,452) #click into the search bar 
    time.sleep(0.1) 
    pyautogui.write(str(player_id)) #write the player id into the search bar
    time.sleep(0.4)

    click(1154,447) #click on search button
    time.sleep(0.5)
    click(1154,447) #click on search button
    time.sleep(0.5)
    click(1363,866) #click on view
    
    
    
def  save_alliance():

    # alliance = save_stats((alliance1), (alliance2))
    alliance = save_stats((alliance_no_server1), (alliance_no_server2))

    try:
        alliance = alliance.split("]")[0]
        alliance = alliance.split("[")[1]
    except:
        pass
    
    return alliance

def save_server():
    server = save_stats(Server1, Server2)
    return server


def save_stats(top_left, bottom_right):



    height = bottom_right[1] - top_left[1]
    width = bottom_right[0] - top_left[0]

    img = pyautogui.screenshot(region=(top_left[0],top_left[1],width,height))
    
    


    #read the text from the image
    string = pytesseract.image_to_string(img)
    result = string.replace(",","")
    result = result.strip()
    
    return result
    

def empty_search(): 

    
    for i in range(0,5):
        click(1794,932)
        time.sleep(0.4)


    click (688,961) #click on search lords (hidden at the bottom)
    time.sleep(0.5)



def main(id):
    
    resizeWindow()
    find_player(id)
    time.sleep(0.5)
    alliance = save_alliance()
    server = save_server()
    click(909,763) #click on more info
    time.sleep(1)
    id = str(id)
    

    if id != 0:
        power = save_stats(power1,power2)
        merits = save_stats(merit1,merit2)
        victories = save_stats(victories1,victories2)
        defeats = save_stats(defeats1,defeats2)
        killed = save_stats(kills1,kills2)
        healed = save_stats(healed1,healed2)
        dead = save_stats(dead1,dead2)
        gathered = save_stats(gathered1,gathered2)
        


        stats = {
            'id': id,
            'alliance': alliance,
            'server': server,
            'power': power,
            'merits': merits,
            'victories': victories,
            'defeats': defeats,#
            'killed': killed,
            'healed': healed,
            'dead': dead,
            'gathered': gathered

        }


        # Specify the file path
    file_path = f'PlayerData/{id}.json'

    # Open the file in write mode
    with open(file_path, "w") as file:
        # Write the data to the file

        json.dump(stats, file)
        
    
    empty_search()
    return stats







