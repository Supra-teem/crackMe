import random
#import pyautogui
import string
attempts=0

chars = "abcdefghijklmnopqrstuvwxyz0123456789"

# chars = string.printable
chars_list = list(chars)

password=input("Enter a Password: ")
#password = pyautogui.password("Enter a password : ")

guess_password = ""

while(guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))

    print("<=================="+ str(guess_password)+ "==================>")
    attempts= attempts+1
    if(guess_password == list(password)):
        print("Your password is : "+ "".join(guess_password))
        print(f"It is found after {attempts} attempts")
        break