# Import modules
import time

# Welcome Message
print("""



 _____                           _         _____       _     
/  __ \                         ( )       |  _  |     (_)    
| /  \/ ___  ___ _ __ ___   ___ |/ ___    | | | |_   _ _ ____
| |    / _ \/ __| '_ ` _ \ / _ \  / __|   | | | | | | | |_  /
| \__/\ (_) \__ \ | | | | | (_) | \__ \   \ \/' / |_| | |/ / 
 \____/\___/|___/_| |_| |_|\___/  |___/    \_/\_\\__,_|_/___|
                                                             
                                                            
\n

Welome to my Quiz Game!
""")
time.sleep(2)

# Verify user wants to play game, if not then quit
playing = input('Would you like to play? ')
if playing.lower() != 'yes':
    quit() 
if playing.lower() == 'yes':
    print("Okay, let's begin...\n")
time.sleep(1)

score = 0

# Question 1
answer = input("What does CPU stand for? ")
if answer.lower() == 'central processing unit':
    print("That is correct.\n")
    score = score + 1
else:
    print('Sorry, that is incorrect.\n')
time.sleep(1)

# Question 2
answer = input("What does RAM stand for? ")
if answer.lower() == 'random access memory':
    print("That is correct.\n")
    score = score + 1
else:
    print('Sorry, that is incorrect.\n')
time.sleep(1)

# Question 3
answer = input("What is the abbreviation for Hyper Text Markup Language?  ")
if answer.lower() == 'html':
    print("That is correct.\n")
    score = score + 1
else:
    print('Sorry, that is incorrect.\n')
time.sleep(1)

# Question 4
answer = input("What is the latest version of Windows? ")
if answer.lower() == 'windows 11':
    print("That is correct.\n")
    score = score + 1
else:
    print('Sorry, that is incorrect.\n')
time.sleep(1)

# Question 5
answer = input("What is the distribution that Kali Linux is built upon? ")
if answer.lower() == 'debian':
    print("That is correct.\n")
    score = score + 1
else:
    print('Sorry, that is incorrect.\n')
time.sleep(1)

print("Quiz completed. You answered " + str(score) + " out of 5 correctly.")
print('You scored %' + str(score/5 * 100) + '.')
print('Thank you for playing. Goodbye.')
