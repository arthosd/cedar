"""
This file aggregate all the function to write in the log file
"""
import datetime
import os

def lprint(text,level):
    "text = Log message to be written in file"
    "Level = The importance of the log message going from 1 to 3"
    date = datetime.datetime.now() # Getting the exact date
    level_word = None

    # Checking if log directory exists
    if os.path.isdir("log") is not None:
        # Create directory
        try :
            os.mkdir("log")
        except FileExistsError:
            pass
    
    if level == 1 :
        level_word = "PROCEDURE "
    elif level == 2:
        level_word = "WARNING "
    else :
        level_word = "FATAL ERROR "
    
    log_to_write = level_word+"["+str(date)+"]"+" : "+text+"\n"

    # Opening log file
    log_file = open ("log/cedar.log", "a")
    # Writting in file
    log_file.write(log_to_write)
    # Closing file
    log_file.close()
