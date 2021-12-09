import os
import getpass
from time import sleep
from datetime import date
import collections
import re
import enum

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
    user_query = ""

    screen_clear()
    while(user_query.lower() != "exit"):
        sy_stack = []
        sy_queue = []
        noNumUntilOp = False
        print("Enter a query ('exit' to leave)")
        user_query = input()

     #Thanks to brilliant.org for the pseudocode
            #1.  While there are tokens to be read:
        for i in range(0, len(user_query), 1):
            if(user_query.lower() == "exit"):
                break
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
        while(sy_stack):
            sy_queue.append(sy_stack.pop())

        print("Solution: ")
        print("=" + str(postfix_solver(sy_queue)))

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
        elif(c.isnumeric()):
            stack.append(int(c))

    return peek_stack(stack)



def operation_solver(val1, val2, op):
    if(op == '+'):
        return val2+val1
    elif(op=='-'):
        return val2-val1
    elif(op=='*'):
        return val2*val1
    elif(op=='/'):
        return val2/val1
    elif(op=='^'):
        return pow(val2, val1)






        

    


	








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
    print("Exit(-1):")
    print("Change files(0):")
    print("Write to "+filename1+"(1):")
    print("Write to "+filename2+"(2):")
    print("Graphing Calculator(3):")

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
                if(text_input != "-999"):
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
                if(text_input != "-999"):
                    fp.write(text_input + "\n")
    elif(choose==3):
        graphing_calculator()

print("Program end")
