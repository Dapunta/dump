#!/usr/bin/python3
#-*-coding:utf-8-*-

import requests,sys,os,time,json
from concurrent.futures import ThreadPoolExecutor as ThreadPool

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def mlaku(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.04)

def banner():
    print("""   ___                \n  / _ \__ ____ _  ___ ® ┌──────────────────────────────┐\n / // / // /  ' \/ _ \  │  Script By Dapunta Khurayra  │\n/____/\_,_/_/_/_/ .__/  │   •• Github.com/Dapunta ••   │\n   ID Facebook /_/      └──────────────────────────────┘""")
  
def login():
    os.system('clear')
    banner()
    toket = input("\n[•] Token : ")
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print('\n[•] Login Successful')
        menu()
    except KeyError:
        print ("\n[!] Token Invalid")
        os.system('clear')
        login()

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
	print("[4] Get Data Target")
	print("[0] Log Out")
	r=input("\n[•] Choose : ")
	if r=="":
	    print("\n[!] Fill In The Correct")
	    menu()
	elif r=="1":
	    friend()
	elif r=="2":
	    public()
	elif r=="3":
	    followers()
	elif r=="4":
	    target()
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
		limit = input("\n[•] Limit (Max 1000) : ")
		try:
			jok = requests.get("https://graph.facebook.com/me?access_token="+toket)
			op = json.loads(jok.text)
			print("[•] Name Account     : "+op["name"])
		except KeyError:
			print("\n[!] ID NOT found")
			print("\n[ Back ]")
			friend()
		r=requests.get("https://graph.facebook.com/me?fields=friends.limit("+limit+")&access_token="+toket)
		id = []
		z=json.loads(r.text)
		jalan("\n[•] Getting ID ...\n")
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print(a['id']+" • "+a['name'])
		ys.close()
		print ('\n[•] Sukses Dump ID From %s'%op['name'])
		print ("[•] Total ID : %s"%(len(id)))
		print ("[•] Output   : %s"%qq)
		input("\n[ Back ]")
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
		idt = input("\n[•] ID Target        : ")
		limit = input("[•] Limit (Max 1000) : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("[•] Name Account     : "+op["name"])
		except KeyError:
			print("\n[!] ID NOT found")
			print("\n[ Back ]")
			public()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit("+limit+")&access_token="+toket)
		id = []
		z=json.loads(r.text)
		jalan("\n[•] Getting ID ...\n")
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print(a['id']+" • "+a['name'])
		ys.close()
		print ('\n[•] Sukses Dump ID From %s'%op['name'])
		print ("[•] Total ID : %s"%(len(id)))
		print ("[•] Output   : %s"%qq)
		input("\n[ Back ]")
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
		idt = input("\n[•] ID Target        : ")
		limit = input("[•] Limit (Max 1000) : ")
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
		for a in z['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print(a['id']+" • "+a['name'])
		ys.close()
		print ('\n[•] Sukses Dump ID From %s'%op['name'])
		print ("[•] Total ID : %s"%(len(id)))
		print ("[•] Output   : %s"%qq)
		input("\n[ Back ]")
		menu()
		
	except Exception as e:
		exit("[•] Error : %s"%e)

def target():
    try:
        toket=open('login.txt','r').read()
    except KeyError:
        print("\n[!] Token Invalid")
        os.system('rm -rf login.txt')
        login()
    idt = input("\n[•] ID Target : ")
    try:
        zx = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
        zy = json.loads(zx.text)
    except KeyError:
        print("\n[!] ID NOT found")
        print("\n[ Back ]")
        menu()
    try:
        nm = zy["name"]
    except KeyError:
        nm = ("-")
    try:
        nd = zy["first_name"]
    except KeyError:
        nd = ("-")
    try:
        nt = zy["middle_name"]
    except KeyError:
        nt = ("-")
    try:
        nb = zy["last_name"]
    except KeyError:
        nb = ("-")
    try:
        ut = zy["birthday"]
    except KeyError:
        ut = ("-")
    try:
        gd = zy["gender"]
    except KeyError:
        gd = ("-")
    try:
        em = zy["email"]
    except KeyError:
        em = ("-")
    try:
        lk = zy["link"]
    except KeyError:
        lk = ("-")
    try:
        us = zy["username"]
    except KeyError:
        us = ("-")
    try:
        rg = zy["religion"]
    except KeyError:
        rg = ("-")
    try:
        rl = zy["relationship_status"]
    except KeyError:
        rl = ("-")
    try:
        rls = zy["significant_other"]["name"]
    except KeyError:
        rls = ("-")
    try:
        lc = zy["location"]["name"]
    except KeyError:
        lc = ("-")
    try:
        ht = zy["hometown"]["name"]
    except KeyError:
        ht = ("-")
    try:
        ab = zy["about"]
    except KeyError:
        ab = ("-")
    try:
        lo = zy["locale"]
    except KeyError:
        lo = ("-")
    mlaku("[•] Name : " + nm)
    mlaku("[•] First Name : " + nd)
    mlaku("[•] Middle Name : " + nt)
    mlaku("[•] Last Name : " + nb)
    mlaku("[•] Birthday : " + ut)
    mlaku("[•] Gender : " + gd)
    mlaku("[•] Email : " + em)
    mlaku("[•] Link : " + lk)
    mlaku("[•] Username : " + us)
    mlaku("[•] Religion : " + rg)
    mlaku("[•] Relationship Status : " + rl)
    mlaku("[•] Relationship With : " + rls)
    mlaku("[•] Location : " + lc)
    mlaku("[•] Hometown : " + ht)
    mlaku("[•] About : " + ab)
    mlaku("[•] Locale : " + lo)
    input("\n[ Back ]")
    menu()

if __name__=='__main__':
	os.system("git pull")
	menu()
