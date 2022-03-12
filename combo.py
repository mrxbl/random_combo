""" 
-------------------------------------------------------------------------
- Cod BY : @KaosMrx
- Github : https://github.com/mrxbl
- Telegram: https://t.me/@KaosMrx
-  TOOL TAMAMI BANA AİT DEĞİL BOŞ YAPMAYIN
-------------------------------------------------------------------------
      
""" 

try:
	import os, sys, requests, string, time,random
	from time import sleep
except ImportError:
	os.system("pip install requests")
	
	
	
	
A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"

def baner():
	banera =f"""{E}
	
                                            
 \033[1;93m < \033[1;92mBU TOOL ÜCRETSİZDİR PARA İLE SATILAMAZ\033[1;93m >  \033[1;91m 
 ---------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mAUTHOR     : SAYİNBYMAN
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram     : @KaosMrx
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mYOUTUBE    : AÇILMADI
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/mrxbl\033[1;91m
  ---------------------------
"""     

	for sidra in banera.splitlines():
		time.sleep(0.05)
		print(sidra)
		
def clear():
	if os.name == 'nt':
		os.system('cls')
		os.system('title Cod BY mrxblack')
	else:
		os.system('clear')


def COMBO():
	clear();baner()
	token = input(E+"("+C+"⌯"+E+") "+C+"TOKEN ALIP GİRİNİZ :"+B)
	ID = input(E+"("+C+"⌯"+E+") "+C+"TELEGRAM KENDİ İD NİZİ GİRİNİZ BİLMİYORSANIZ ROSE YE İD YAZMANIZ YETERLİDİR :"+B)
	clear();baner()
	sn = int(input(E+"("+C+"⌯"+E+") "+C+"KAÇ COMBO İSTİYORSUN (10 dan fazla giriniz): "))
	
	os.system('rm -rf combo.txt')
	i=1
	for i in range (0,sn):
		i = 1+1
		USER = ''.join(random.choices( string.digits + string.ascii_letters, k = 4))
		PASA = USER+"12345",USER+"123","12345567890","1234512345","1122334455","1234554321","1234554321","1q2w3e4r5t","Aa123123","1111aaaa","20012001","19981998","1234qwer","10001000","19901990"
		PASS = random.choice(PASA)
		LISTA = USER+":"+PASS
		print (E+"["+C+"COMBO PRO "+E+"] "+str(LISTA))
		with open("pro.txt","a") as pro:
			pro.write(str(LISTA)+"\n")
			
	
	try:
		massage = ("➥ • Denenen Combolar ✓\n\n➥• USER : PASS \n\n➥• Number : "+str(sn)+"\n\n. — — — — —  — — — — — . \n➥• Beta Aşamasındadır Hataları istisna geçiniz")
		requests.post(f'https://api.telegram.org/bot{token}/sendDocument?chat_id={ID}&caption={massage}', files={'document':open('combo.txt', 'rb')})
		print(E+" \n\nOnaylanan Combolar✓"+H+"kaydedildi> combo.txt")
	except:pass
	sleep (10)
		


while True:
	COMBO()  
