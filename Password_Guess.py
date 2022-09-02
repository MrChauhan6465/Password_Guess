import random
import pyautogui

chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_-=+,<>/|';[]{}"
chars_list = list(chars)

password = pyautogui.password("Enter A Password: ")
guess_password = ""

while(guess_password != password):
	guess_password = random.choices(chars_list, k=len(password))
	print("<==========="+ str(guess_password) + "===========>")

	if(guess_password == list(password)):
		print("Your Password Is: " + "".join(guess_password))
		input()
		break
