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
import threading
import queue



pytesseract.pytesseract.tesseract_cmd = R"C:\Program Files\Tesseract-OCR\tesseract.exe"
#coords for profile

alliance1 = (480,250)
alliance2 = (740,280)
alliance_no_server1 = [730,270] # to use if server isnt visible 
alliance_no_server2 = [1165,320]
Server1 = [500,190]
Server2 = [670,215]   

#coords for the stats 

power1 = [300,517]
power2 = [461,540]

merit1 = [300,575]
merit2 = [461,600]

kills1 = [820,466]
kills2 = [980,485]

healed1 = [800,515]
healed2 = [980,535]

victories1 = [800,370]
victories2 = [980,390]

defeats1 = [800,395]
defeats2 = [980,415]

dead1 = [800,490]
dead2 = [980,510]

gathered1 = [800,560]
gathered2 = [980,586]








def click(x,y):
    
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.1)

def resizeWindow():
    try: 
        
        hwnd = win32gui.FindWindow(None, "Call of Dragons")
        win32gui.MoveWindow(hwnd, 0, 0, 1280, 720, True) 
        
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
    
    click(300,300) #click into the search bar 
    time.sleep(0.1) 
    pyautogui.write(str(player_id)) #write the player id into the search bar
    time.sleep(0.4)

    click(770,300) #click on search button
    time.sleep(0.5)
    click(770,300) #click on search button
    time.sleep(0.5)
    click(900,580) #click on view
    
    
    
def  save_alliance():
    # alliance = save_stats((alliance1), (alliance2))
    output_queue = queue.Queue()
    alliance = save_stats((alliance1), (alliance2),output_queue)

    try:
        alliance = alliance.split("]")[0]
        alliance = alliance.split("[")[1]
    except:
        pass
    
    return alliance

def save_server():
    output_queue = queue.Queue()
    server = save_stats(Server1, Server2, output_queue)
    return server


def save_stats(top_left, bottom_right,output_queue):



    height = bottom_right[1] - top_left[1]
    width = bottom_right[0] - top_left[0]

    img = pyautogui.screenshot(region=(top_left[0],top_left[1],width,height))
    
    


    #read the text from the image
    string = pytesseract.image_to_string(img)
    result = string.replace(",","")
    result = result.strip()
    output_queue.put(result)
    return result
    

def empty_search(): 

    
    for i in range(0,5):
        click(1180,650)
        time.sleep(0.2)


    click (477,640) #click on search lords (hidden at the bottom)
    time.sleep(0.5)



def main(id):
    resizeWindow()
    time.sleep(0.1)
    resizeWindow()
    find_player(id)
    time.sleep(0.5)
    alliance = save_alliance()
    server = save_server()
    click(600,530) #click on more info
    time.sleep(1)
    id = str(id)
    

    if id != 0:
        output_queue = queue.Queue() #not used, but saves me editing all the time lol
        # power_queue = queue.Queue()

        # powerThread = threading.Thread(target=save_stats, args=(power1,power2, power_queue))
        # powerThread.start()

        # merit_queue = queue.Queue()

        # meritThread = threading.Thread(target=save_stats, args=(merit1,merit2, merit_queue))
        # meritThread.start()

        # victories_queue = queue.Queue()
        # victoriesThread = threading.Thread(target=save_stats, args=(victories1,victories2, victories_queue))
        # victoriesThread.start()

        # defeats_queue = queue.Queue()
        # defeatsThread = threading.Thread(target=save_stats, args=(defeats1,defeats2, defeats_queue))
        # defeatsThread.start()
        
        # killed_queue = queue.Queue()
        # killsThread = threading.Thread(target=save_stats, args=(kills1,kills2, killed_queue))
        # killsThread.start()
        
        # healed_queue = queue.Queue()
        # healedThread = threading.Thread(target=save_stats, args=(healed1,healed2, healed_queue))
        # healedThread.start()
        
        # dead_queue = queue.Queue()
        # deadThread = threading.Thread(target=save_stats, args=(dead1,dead2, dead_queue))
        # deadThread.start()
        
        
        # gathered_queue = queue.Queue()
        # gatheredThread = threading.Thread(target=save_stats, args=(gathered1,gathered2, gathered_queue))
        # gatheredThread.start()
        
        # powerThread.join()
        # power = power_queue.get()
        # meritThread.join()
        # merits = merit_queue.get()
        # victoriesThread.join()
        # victories = victories_queue.get()
        # defeatsThread.join()
        # defeats = defeats_queue.get()
        # killsThread.join()
        # killed = killed_queue.get()
        # healedThread.join()
        # healed = healed_queue.get()
        # deadThread.join()
        # dead = dead_queue.get()
        # gatheredThread.join()
        # gathered = gathered_queue.get()
        
      
        power = save_stats(power1,power2,output_queue)
        merits = save_stats(merit1,merit2,output_queue)
        victories = save_stats(victories1,victories2,output_queue)
        defeats = save_stats(defeats1,defeats2,output_queue)
        killed = save_stats(kills1,kills2,output_queue)
        healed = save_stats(healed1,healed2,output_queue)
        dead = save_stats(dead1,dead2,output_queue)
        gathered = save_stats(gathered1,gathered2,output_queue)
        
        
        


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
        
        print (stats)


        # Specify the file path
    file_path = f'PlayerData/{id}.json'

    # Open the file in write mode
    with open(file_path, "w") as file:
        # Write the data to the file

        json.dump(stats, file)
        
    
    empty_search()
    return stats



# start_time = time.time()
# main(4999955)
# end_time = time.time()
# execution_time = end_time - start_time
# print(execution_time)




