import os
import getpass
from time import sleep
from datetime import date
import numpy as np
import pandas  as pd
import collections
import re
import enum
import math 
import seaborn as sns
import sys
sys.path.insert(0, 'c:\pyzo2015a\lib\site-packages\plotly')
import chart_studio.plotly as py
import plotly.express as px
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)


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


def graphing_calculator():
    text = ""
    while(text.lower() != "exit"):
        print("Loop")
        text = arithmetic()
        if(text.lower() == "functions"):
            functions()
    



def functions():
    help_options = ["Exit", "Summate", "Integrate", "Derivate", "Graph"]
    inp = ""
    while(inp != "exit"):
        print("'Help' for list")
        inp = input()
        if(inp.lower() == 'help'):
            for s in help_options:
                print(s)
        elif(inp.lower() == 'summate'):
            print("Sum")
        elif(inp.lower() == 'integrate'):
            print("Integrate")
        elif(inp.lower() == 'derivate'):
            print("Derivate")
        elif(inp.lower() == 'graph'):
            graph()

def graph():
    print("Graph lol")
    arr_1 = np.random.randn(50,4)
    df_1 = pd.DataFrame(arr_1, columns=['A','B','C','D'])
    df_1.head()
    df_1.plot()
    sleep(2)
    sleep(2)



def shunting_yard(user_query):
        PI = 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160943305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912983367336244065664308602139494639522473719070217986094370277053921717629317675238467481846766940513200056812714526356082778577134275778960917363717872146844090122495343014654958537105079227968925892354201995611212902196086403441815981362977477130996051870721134999999837297804995105973173281609631859502445945534690830264252230825334468503526193118817101000313783875288658753320838142061717766914730359825349042875546873115956286388235378759375195778185778053217122680661300192787661119590921642019893809525720106548586327886593615338182796823030195203530185296899577362259941389124972177528347913151557485724245415069595082953311686172785588907509838175463746493931925506040092770167113900984882401285836160356370766010471018194295559619894676783744944825537977472684710404753464620804668425906949129331367702898915210475216205696602405803815019351125338243003558764024749647326391419927260426992279678235478163600934172164121992458631503028618297455570674983850549458858692699569092721079750930295532116534498720275596023648066549911988183479775356636980742654252786255181841757467289097777279380008164706001614524919217321721477235014144197356854816136115735255213347574184946843852332390739414333454776241686251898356948556209921922218427255025425688 
        sy_stack = []
        sy_queue = []
        noNumUntilOp = False
           #Thanks to brilliant.org for the pseudocode
            #1.  While there are tokens to be read:
        for i in range(0, len(user_query), 1):
            #2.  Read a token
            c = user_query[i]
            #3.  If it's a number add it to queue
            if(c.isnumeric() and not noNumUntilOp):
                str_int = ""
                if(i+1 < len(user_query) and user_query[i+1].isnumeric()):
                    str_int += c
                    while(i+1 < len(user_query) and user_query[i+1].isnumeric()):
                        i += 1
                        c = user_query[i]
                        str_int += c
                        noNumUntilOp = True
                else:
                    str_int += c
                sy_queue.append(str_int)
                str_int = ""
            #4.  If it's an operator
            elif(c == '+' or c == '-' or c == '/' or c == '*' or c=='^'):
                noNumUntilOp = False
         #5.      While there's an operator on the top of the stack with greater precedence:
                while(sy_stack and get_prec(peek_stack(sy_stack)) >= get_prec(c)):
         #6.   Pop operators from the stack onto the output queue
                    sy_queue.append(sy_stack.pop())
         #7.               Push the current operator onto the stack
                sy_stack.append(c)
	     #8.        If it's a left bracket push it onto the stack  
            elif(c=='('):
                sy_stack.append(c)
         #9.        If it's a right bracket
            elif(c==')'):
         #10.            While there's not a left bracket at the top of the stack:
                while(peek_stack(sy_stack) != '('):
         #11.                     Pop operators from the stack onto the output queue.
                    sy_queue.append(sy_stack.pop())
         #12.             Pop the left bracket from the stack and discard it
                sy_stack.pop()
	     #13. While there are operators on the stack, pop them to the queue
            elif(c=='p' or c=='P'):
                sy_queue.append(PI)
        while(sy_stack):
            sy_queue.append(sy_stack.pop())
        return sy_queue

def arithmetic():
    
    user_query = ""
    exit_while = False
    screen_clear()
    while(not exit_while):
        print("Enter a query (Keywords: 'Exit'/'Functions')")
        user_query = input()
        if(user_query.lower() == "exit" or user_query.lower() == "functions"):
            exit_while = True
            break
        sy_queue = shunting_yard(user_query)
 
        if(not exit_while):
            print("Solution: ")
            print("=" + str(postfix_solver(sy_queue)))
        
    return user_query


def peek_stack(stack):
    if stack:
        return stack[-1]


def postfix_solver(sy_queue):
    hold1 = ""
    hold2 = ""
    stack = []
    for i in range(len(sy_queue)):
        print(stack)
        c = sy_queue[i]
        if(stack and (c == '+' or c=='-' or c=='/' or c=='*'or c=='^')):
            hold1 = stack.pop()
            hold2 = stack.pop()
            stack.append(operation_solver(hold1, hold2, c))
        else:
            stack.append(is_float(c))

    return peek_stack(stack)

def is_float(fl):
    try:
        float(fl)
        return fl
    except ValueError:
        return 0.0

def operation_solver(val1, val2, op):
    if(op == '+'):
        return float(val2)+float(val1)
    elif(op=='-'):
        return float(val2)-float(val1)
    elif(op=='*'):
        return float(val2)*float(val1)
    elif(op=='/'):
        return float(val2)/float(val1)
    elif(op=='^'):
        return pow(float(val2), float(val1))

def get_prec(c):
    if(c=='+' or c=='-'):
        return 1
    elif(c=='/' or c=='*'):
        return 2
    elif(c=='^'):
        return 3
    else:
        return 0
        
def enqueue(li):
    li.append()
    return li

def dequeue(li):
    li.pop(0)
    return li




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
    screen_clear()
    print("You are connected to " + filename1 + ".txt and " + filename2 + ".txt")
    print("'Exit':")
    print("Change files(0):")
    print("Write to "+filename1+"(1):")
    print("Write to "+filename2+"(2):")
    print("Graphing Calculator(3):")

    choose = input()
    if(choose.lower()=="exit"):
        print("Ciao")
        done=True
    elif(choose=="0"):
        file_info = file_inputs()
        file_path1 = file_info[0].strip(' ')
        filename1 = file_info[1].strip(' ')
        file_path2 = file_info[2].strip(' ')
        filename2 = file_info[3].strip(' ')
    elif(choose=="1"):
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
                if(text_input != "-999"):
                    fp.write(text_input + "\n")
    elif(choose=="2"):
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
                if(text_input != "-999"):
                    fp.write(text_input + "\n")
    elif(choose=="3"):
        graphing_calculator()



        

    
    





