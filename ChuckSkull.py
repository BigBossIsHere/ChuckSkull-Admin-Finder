#CHUCK SKULL ADMIN FINDER
#THIS TOOL IS A BRUTE-FORCER TO FIND WEBSITES LOGIN PANELS
#THIS TOOL IS CODED BY B1G BO55
#THIS SCRIPT MUST BE USED WITH PYTHON 3.x : TO SET IT UP ON LINUX : apt-get install python3
#FOR EXECUTION IN LINUX : python3 ChSk.py
import urllib.request
import urllib.error
import os
from time import sleep
import sys
def print_slowly(text):
    sys.stdout.flush()
    sleep(3.5)
    print (text)
os.system ('clear')
print ('')
print ('')
print (''' 
\033[91m   
   +_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-__-_-_-_+
   +_-_-_-_-_-THIS IS A TOOL FOR ADMIN PANEL FINDING_-_-_-_-_-+
   +-_-I DONT HAVE ANY RESPONSIBILTY OF YOUR USE OF THE TOOL_-+
   +_-_-_-_-_-_JUST ENTER THE WEBSITE(S) AND WAIT XD_-_-_-_-_-+
   +_-_-_-_-_-_-_-_-_-_-CODED BY #BIG BOSS_-_-_-_-_-_-_-_-_-_-+
   +_-_-_-_-_-_-_-_-ChuckSkull Admin Panel Finder_-_-_-_-_-_-_+
   +_-_-_-_-_-_-_-_-_-_-Coded At 37/11/1851-_-_-_-_-_-_-_-_-_-+
   +_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-__-_-_-_+
   ''')
print ('\n')
print_slowly (' \033[92m[\033[91m+\033[92m] CHUCK SKULL IS STARTING ...')
print ('')
print ('')
print ('[1] Use A List Of Websites\n[2] Use A Link Of A Website\n')
choice = input ('Choose : ')
if choice == '1' or choice == '[1]' :
    print_slowly ('Write URL With protocol \033[91mhttp://\033[92m or \033[91mhttps://\033[92m don\'t use \033[91m/\033[92m after writing url in your list')
    websites_list = input ('Enter your website list : ')
    logins_list = input ('Enter your Login list : ')
    websites_list_opening = open (websites_list , 'r').read().splitlines()
    logins_list_opening = open (logins_list , 'r').read().splitlines()
    os.system ('clear')
    for website in websites_list_opening :
        for login in logins_list_opening :
            try :
                correctpanel = (website + '/' + login)
                the_panel_opening = urllib.request.urlopen (correctpanel)
                print (' \033[96m---------------------------------------------------')
                print (correctpanel)
                print (' \033[96m---------------Admin login Is Found----------------')
            except :
                print (' \033[91m---------------------------------------------------')
                print (correctpanel)
                print (' \033[91m---------------Admin login Not Found---------------')
    print ('To contact Me : bigbosswashere@gmail.com ')
elif choice == '2' or choice == '[2]' :
    print_slowly ('Write URL With protocol \033[91mhttp://\033[92m or \033[91mhttps://\033[92m don\'t use \033[91m/\033[92m after writing url in your list')
    website = input("Enter Website URL : ")
    logins_list = input('Enter your Login list : ')
    logins_list_opening = open(logins_list, 'r').read().splitlines()
    os.system('clear')
    for login in logins_list_opening:
        try:
            correctpanel = (website + '/' + login)
            the_panel_opening = urllib.request.urlopen(correctpanel)
            print(' \033[96m---------------------------------------------------')
            print(correctpanel)
            print(' \033[96m---------------Admin login Is Found----------------')
        except:
            print(' \033[91m---------------------------------------------------')
            print(correctpanel)
            print(' \033[91m---------------Admin login Not Found---------------')
    print('To contact Me : bigbosswashere@gmail.com ')
else :
    os.system('exit')
