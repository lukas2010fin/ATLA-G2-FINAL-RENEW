import random
import pyautogui

chars = "abcdefghijklmnopqrstuvwxyz1234567890+´´¨¨åöä-.,_:;ÄÖ*^^``?=)(/&%¤#!½"
chars_list = list(chars)

password = pyautogui.password("Enter a password: ")
guess_password = ""

while(guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))
    print("<===========" + str(guess_password) + "===========>")
    if(guess_password == list(password)):
        print("Sinun salasanasi on:" + "".join(guess_password))
        input()
        break