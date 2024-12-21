import math
from get_stats import *
import win32clipboard
from mouse import release, press, move, is_pressed


amount_of_IDs = 0
copy_id_x = (592)
copy_id_y = (484)

pixels_to_scroll = 10


top_account_x = (820)
top_account_y = (580)
mid_account_x = (820)
mid_account_y = (655)
bot_account_x = (820)
bot_account_y = (725)



# create a collection of all the IDs that I can fill later
ids = []



def get_clipboard():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data


def drag(start_x, start_y, end_x, end_y, absolute=True, duration=0):
    """
    Holds the left mouse button, moving from start to end position, then
    releases. `absolute` and `duration` are parameters regarding the mouse
    movement.
    """
    if is_pressed():
        release()
    move(start_x, start_y, absolute, 0)
    press()
    move(end_x, end_y, absolute, duration)
    time.sleep(0.5)
    release()


def scroll_down():
    print("scrolling down")
    drag(825, 810, top_account_x, top_account_y, absolute=True, duration=1)


def get_id(top_coords,bot_coords):
        old_id = ""
        
        account_x = top_coords
        account_y = bot_coords
        click(account_x, account_y)
        time.sleep(0.5)
        click(copy_id_x, copy_id_y)
        time.sleep(0.2)
        
        
        id = get_clipboard()
        print(id)

        if id == old_id or id == "":
            time.sleep(1)
            print("trying again")
            click(copy_id_x, copy_id_y)
            time.sleep(0.1)
            id = get_clipboard()
        else:
            old_id = id

        ids.append(id)
        click(1000,1000) #cancel out 
        time.sleep(1)
    

def id_scan(amount_of_IDs_to_scan, server):

    

    # divide amount_of_IDs by 3 and round up to get the amount of scrolls needed
    amount_of_IDs = math.ceil(amount_of_IDs_to_scan / 3)
    resizeWindow()
    
    for i in range(amount_of_IDs):

        get_id(top_account_x, top_account_y)
        get_id(mid_account_x, mid_account_y)
        get_id(bot_account_x, bot_account_y)

        scroll_down()
        time.sleep(0.4)


    print(ids)

    file_path = rf'IDs/{server}.json'

    # Open the file in write mode
    with open(file_path, "w") as file:
        # Write the data to the file
        for id in ids:
            file.write(f"{id}\n")


        
        





    


