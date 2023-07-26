import random
import os,time,sys
from termcolor import colored
from hElp import Adduser, Cat, Cd, Chmod, Cp, Find, Grep, Help, Ln, Ls, Man, Mkdir, Rm, Sudo, Touch
from man import _adduser,_cat,_chmod,_clear,_cp,_grep,_ln,_ls,_man,_mkdir,_rm,_sudo,_touch


os.system('cls') and os.system('clear')


# Group of Different functions for different styles
class style():
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'
    underline = '\033[4m'
    reset = '\033[0m'

# 'home' directory (~/home)
files = ["$", "Lesson_1", "Lesson_2", "Lesson_3", "Lesson_4"]

#the lesson's directories :)
file_1 = ["one.txt", "fun_quiz"]
file_2 = ["two", "test", "fun_quiz"]
file_3 = ["three", "fun_quiz"]
file_4 = ["four", "fun_quiz"]



# yeh, the commands
commands = ["help", "man", "ls", "cat", "clear", "touch", "chmod", "rm", "cp", "cd", "mkdir", "ln",
            "find", "grep", "sudo", "adduser", "exit"]


npc_XX = ["Uh oh! Looks like you've done something wrong, try again\n", "bruh, check your spelling and try again\n", "maybe check your spelling?\n", "try again\n", "nope\n", "niope", "Failure is the mother of success\n"]
def clearer():
    if welcome == commands[4]:
        os.system('cls') and os.system('clear')

def theHelp():
    if welcome == "help":
        print(commands)
#exit
def Exit():
    if welcome == commands[-1]:
        getOut = input("this commands let's you exit this program. Once you exit, you have to redo the lessons.(just blame the developer, yeh me: for not adding a save option) \nAre you sure you wanna quit?\n(type 'yeh' or 'nah')  ")
        if getOut == "yeh":
            print("Thanks for learning, cya! :D")
            time.sleep(3)
            os.system('cls') and os.system('clear')
            exit()

def print_slow(str):
    for variable in str:
        sys.stdout.write(variable)
        sys.stdout.flush()
        time.sleep(0.03) 

#creating how the help command would function
def helpio_():
    if welcome == (commands[0] + " " + " --help"):
        print(Help)
    elif welcome == (commands[1] + " " + " --help"):
        print(Man)
    elif welcome == (commands[2] + " " + " --help"):
        print(Ls)
    elif welcome == (commands[3] + " " + " --help"):
        print(Cat)    
    elif welcome == (commands[5] + " " + " --help"):
        print(Touch)    
    elif welcome == (commands[6] + " "  + " --help"):
        print(Chmod)
    elif welcome == (commands[7] + "  " + " --help"):
        print(Rm)
    elif welcome == (commands[8] + " "  + " --help"):
        print(Cp)
    elif welcome == (commands[9] + " " + " --help"):
        print(Cd)
    elif welcome == (commands[10] + " " + " --help"):
        print(Mkdir)
    elif welcome == (commands[11] + " " + " --help"):
        print(Ln)
    elif welcome == (commands[12] + " " + " --help"):
        print(Find)
    elif welcome == (commands[13] + " " + " --help"):
        print(Grep)
    elif welcome == (commands[14] + " " + " --help"):
        print(Sudo)
    elif welcome == (commands[15] + " " + " --help"):
        print(Adduser)

#"help", "man", "ls", "cat", "clear", "touch", "chmod", "rm", "cp", "cd", "mkdir", "ln", "find", "grep", "sudo", "adduser", "exit"
#0        1       2     3      4         5        6       7     8     9      10      11     12      13      14       15        16
def longAsHeck():
    if welcome == (commands[1] + " " + commands[1]):
        print(_man)
    if welcome == (commands[1] + " " + commands[2]):
        print(_ls)
    if welcome == (commands[1] + " " + commands[3]):
        print(_cat)
    if welcome == (commands[1] + " " + commands[4]):
        print(_clear)
    if welcome == (commands[1] + " " + commands[5]):
        print(_touch)
    if welcome == (commands[1] + " " + commands[6]):
        print(_chmod)
    if welcome == (commands[1] + " " + commands[7]):
        print(_rm)
    if welcome == (commands[1] + " " + commands[8]):
        print(_cp)
    if welcome == (commands[1] + " " + commands[10]):
        print(_mkdir)
    if welcome == (commands[1] + " " + commands[11]):
        print(_ln)
    if welcome == (commands[1] + " " + commands[13]):
        print(_grep)
    if welcome == (commands[1] + " " + commands[14]):
        print(_sudo)
    if welcome == (commands[1] + " " + commands[15]):
        print(_adduser)







#==========================================================================================
# :O
print_slow(style.cyan + "wake up...\n")
time.sleep(3)
print_slow(style.cyan + "c'mon, c'mon please work...\n")
time.sleep(3)
print(style.cyan + "!!! :D")
time.sleep(3)
os.system('cls') and os.system('clear')


#==========================================================================================
#lessgooo
print_slow(style.cyan + "hey ya noob™, welcome to Learn-Linux. you are currently locked here because you forgot to pluck the weeds from your backyard. In order to get out, you'll need to find keys from the directories using bash commands. I'll walk you through basic bash commands, so theres no need to panic :) (note: if you would like to exit this program, type in the command 'exit' in the terminal)\n")
print_slow("whatever commands you learn, try it on a real terminal ;)\n")
input(style.reset + "press enter to continue ")
os.system('cls') and os.system('clear')

#creating variable for user
new_user = input("Enter new UNIX user:")
os.system('cls') and os.system('clear')

#==========================================================================================

print_slow(style.cyan + "to start of let's type the 'help' command to list all the commands\n")
while True:
    welcome = input(style.green + new_user + "@Learn-Linux" + style.reset + ":" + style.blue + "~" + style.reset + files[0] + " ")
    Exit()
    if welcome == commands[0]:
        print(*commands, sep=" ")
        print("\n")
        time.sleep(2)
        print_slow(style.cyan + "Good job! And remember, if you forget a command don't forget to type help to list all the commands.\n")
        print_slow("now, please wait for 5 seconds, 'cause why not? XD ...")
        time.sleep(5)
        os.system('cls') and os.system('clear')
        break

    else:
        print_slow(random.choice(npc_XX))
        
#==========================================================================================

print_slow(style.cyan + "just wanted to clear the console. Yup, I have OCD, I bet you have it too")
for i in range(3):
    print_slow(" ")
    time.sleep(0.6)
    print_slow(".")
    time.sleep(2)
print_slow(".")
time.sleep(2)
print_slow("\n")
print_slow("ls is a command that lists information about every file/directory in the directory. Just running the ls command outputs the name of every file in the directory.\n")
while True:
    welcome = input(style.green + new_user + "@Learn-Linux" + style.reset + ":" + style.blue + "~" + style.reset + files[0] + " ")  
    theHelp()
    clearer()
    Exit()
    if welcome == commands[2]:
        print(*files[1:5], sep=" ")
        print("\n")
        print_slow(style.cyan + "Oooo~ Lesson_1 looks interesting\n")
        break
    else:
        print_slow(style.cyan + "bruh, check your spelling and try again :D\n")
        
#==========================================================================================

print_slow("let's navigate into 'Lesson_1', shall we?\n")
time.sleep(1)
print_slow("in order to navigate into directories, we use the 'cd' command\n")
time.sleep(1)
print_slow("now, type in 'cd Lesson_1' in order to move 'Lesson_1'\n")  
while True:    
    welcome = input(style.green + new_user + "@Learn-Linux" + style.reset + ":" + style.blue + "~" + style.reset + files[0] + " ")
    Exit()
    clearer()
    theHelp()
    if welcome == (commands[9] + " " + files[1]):
        print_slow(style.cyan + "not that difficult aye? you've just move to the directory called 'Lesson_1'. Check around! :D\n")
        break

    elif welcome == (commands[9] + " " + files[2]): 
        print_slow(style.red + "I am the directory keeper for Lesson_2\n")
        print_slow("please don't try and break into other directories without a key\n")
        input("what's the key? " + style.reset)
        
        if input == "-n":
            print_slow(style.red + "welcome, you may enter")                
            break   
        else:
            print("error, key undefined\n")
            print_slow(style.red + "now, find the key to enter\n")

    elif welcome == (commands[9] + " " + files[3]):
        print_slow("please don't try and break into other directories without a key\n")
        

    elif welcome == (commands[9] + " " + files[4]):
        print_slow("please don't try and break into other directories without a key\n")
        print_slow("oh! i see you picking your nose! :)\n")
        print_slow("now move to 'Lesson_3'!\n")
   
#==========================================================================================  

#                                            ───────────────────────────────────────
#                                            ───▐▀▄───────▄▀▌───▄▄▄▄▄▄▄─────────────
#                                            ───▌▒▒▀▄▄▄▄▄▀▒▒▐▄▀▀▒██▒██▒▀▀▄──────────
#                                            ──▐▒▒▒▒▀▒▀▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄────────
#                                            ──▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▒▒▒▒▒▒▒▒▀▄──────
#                                            ▀█▒▒▒█▌▒▒█▒▒▐█▒▒▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌─────
#                                            ▀▌▒▒▒▒▒▒▀▒▀▒▒▒▒▒▒▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐───▄▄
#                                             ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌▄█▒█
#                                             ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒█▀─
#                                            ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌────
#                                            ─▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐─────        
#                                            ─▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌─────
#                                            ──▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐──────
#                                            ──▐▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▌──────
#                                            ────▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀────────

#==========================================================================================
# Lesson_1

#"help", "man", "ls", "cat", "clear", "touch", "chmod", "rm", "cp", "cd", "mkdir", "ln", "find", "grep", "sudo", "adduser", "exit"
#0        1       2     3      4         5        6       7     8     9      10      11     12      13      14       15        16
while True:
    welcome = input(style.green + new_user + "@Learn-Linux" + style.reset + ":" + style.blue + "~/" + files[1] + style.reset + files[0])
    Exit()
    clearer()
    helpio_()
    theHelp()
    
    if welcome == (commands[2]):       
        print(*file_1,sep=" ")
        time.sleep(2)
        print("\n")
        print_slow(style.cyan + "well done!\n")
        time.sleep(2)
        print_slow("one.txt? that's new.\n")
        print_slow("a '.txt' file is a text file which we can read using the 'cat' command\n")
        time.sleep(2)
        print_slow("Go on! type 'cat one.txt'\n" + style.reset)
    
    if welcome == commands[3] + " " + file_1[0]:        
        print("looking for the key? the key is the answer to this question: What option numbers all output lines for the command 'cat'?\n")
        print("\n")
        print_slow(style.cyan + "oh wow! now, in order to look at the options for the command 'cat', we can use their help function '--help'\n" + style.reset)
        print_slow("type 'cat --help'\n" + style.reset)


    if welcome == (commands[3] + " " + "--help"):
        print(Cat)
        print("\n")
        print("\n")
        input(style.cyan + "what's the option for 'cat' that numbers all output lines?" + style.reset + " ")
    if input == "-n":
        print_slow(style.cyan + "H00ray! You have found the key to Lesson_2!\n")
        print_slow("Hurry, type cd to go back the home directory and hop straight into Lesson_2!!!\n")    
    
    
    if welcome == commands[9]:
        break


#==========================================================================================

while True:
    welcome = input(style.green + new_user + "@Learn-Linux" + style.reset + ":" + style.blue + "~" + style.reset + files[0] + " ")
    if welcome == (commands[9] + " " + files[2]): 
        print_slow(style.red + "I am the directory keeper for Lesson_2\n")
        print_slow("please don't try and break into other directories without a key\n")
        input("what's the key for Lesson_2? " + style.reset)
        
        if input == "-n":
            print_slow(style.red + "welcome, you may enter\n")                
            break   
        else:
            print("error, key undefined\n")
            print_slow(style.red + "now, find the key to enter\n")

#==========================================================================================

# Lesson_2 begin...

#"help", "man", "ls", "cat", "clear", "touch", "chmod", "rm", "cp", "cd", "mkdir", "ln", "find", "grep", "sudo", "adduser", "exit"
#0        1       2     3      4         5        6       7     8     9      10      11     12      13      14       15        16
print_slow(style.cyan + "we're in Lesson_2, wanna look around?\n")
while True:
    welcome = input("{style.green}{new_user}@Learn-Linux{style.reset}:{style.blue}~/{files[2]}{style.reset}{files[0]}")
    if welcome == commands[2]:
        print(*file_2, sep=" ")
        print("\n")
        print("\n")
        print_slow("")
 













#==========================================================================================



