import os
import getpass
from time import sleep
from datetime import date
import collections

#All of this code in the screen_clear function was written by tutorialspoint.com
print("OS: " + str(os.name))
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

#credit goes to them for this screen clearing code

def return_string_arr(text):
     string_container=""
     textarr = list()

     for c in text:
          string_container += c;
          if(c==' '):
              textarr.append(string_container)
              string_container = ""
     return textarr

def file_inputs():
    print("Choose the name of your file: ")
    filename1 = input() 
    file_path1 = r'C:\Users\\'+getpass.getuser() + '\Documents\\'+filename1+'.txt'
    if os.path.exists(file_path1):
        print('Opening File')
        screen_clear()
        with open(file_path1, 'r') as fp:
             print(fp.read())
    
    else:
        # create a file
        with open(file_path1, 'a') as fp:
            fp.write(str(date.today()))

    print("Choose the name of your definition file: ")
    filename2 = input()
    file_path2 = r'C:\Users\\'+getpass.getuser() + '\Documents\\'+filename2+'.txt'
    if os.path.exists(file_path2):
        print('Opening File')
        screen_clear()
        with open(file_path2, 'r') as fp:
             print(fp.read())
    
    else:
        # create a file
        with open(file_path2, 'a') as fp:
            fp.write(str(date.today()))
            fp.write("\nDefinitions")
    file_path3 = r'C:\Users\\'+getpass.getuser() + '\Documents\\'+filename3+'.txt'
    if os.path.exists(file_path3):
        print('Opening File')
        screen_clear()
        with open(file_path3, 'a') as fp:
            fp.write(filename1 + " ")
            fp.write(filename2 + " ")
    
    else:
        # create a file
        with open(file_path3, 'a') as fp:
            fp.write(filename1 + " ")
            fp.write(filename2 + " ")
    file_list = [file_path1, filename1, file_path2, filename2]
    return file_list

def display_f3():
    with open(file_path3, 'r') as fp:
         print(fp.read())

filename3 = 'filename_information'

file_path3 = r'C:\Users\\'+getpass.getuser() + '\Documents\\'+filename3+'.txt'

                
if os.path.exists(file_path3):
     with open(file_path3, 'r') as fp:
         filename_arr = return_string_arr(fp.read())
     print(filename_arr)    
     filename1 = filename_arr[0].strip(' ')
     file_path1 = r'C:\Users\\'+getpass.getuser() + '\Documents\\'+filename1+'.txt'
     filename2 = filename_arr[1].strip(' ')
     file_path2 = r'C:\Users\\'+getpass.getuser() + '\Documents\\'+filename2+'.txt'
else:
    print("First time user")
    file_info = file_inputs()
    file_path1 = file_info[0].strip(' ')
    filename1 = file_info[1].strip(' ')
    file_path2 = file_info[2].strip(' ')
    filename2 = file_info[3].strip(' ')

done = False
with open(file_path1, 'a') as fp:
     fp.write(str(date.today()) + "\n")
with open(file_path2, 'a') as fp:
     fp.write(str(date.today()) + "\n")
while(done == False):
    print("You are connected to " + filename1 + ".txt and " + filename2 + ".txt")
    print("Exit(-1):")
    print("Change files(0):")
    print("Write to "+filename1+"(1):")
    print("Write to "+filename2+"(2):")

    choose = int(input())
    if(choose==-1):
        print("Ciao")
        done=True
    elif(choose==0):
        file_info = file_inputs()
        file_path1 = file_info[0].strip(' ')
        filename1 = file_info[1].strip(' ')
        file_path2 = file_info[2].strip(' ')
        filename2 = file_info[3].strip(' ')
    elif(choose==1):
        text_content = ""
        screen_clear()
        with open(file_path1, 'r') as fp:
            print(fp.read())
        with open(file_path1, 'a') as fp:
            fp.write(text_content + "\n")
            text_input = ""
            print("-999 to exit")
            while(text_input != "-999"):
                text_input=input()
                fp.write(text_input + "\n")
    elif(choose==2):
        text_content = ""
        screen_clear()
        with open(file_path2, 'r') as fp:
            print(fp.read())
        with open(file_path2, 'a') as fp:
            fp.write(text_content + "\n")
            text_input = ""
            print("-999 to exit")
            while(text_input != "-999"):
                text_input=input()
                fp.write(text_input + "\n")

print("Program end")


        

    
    





