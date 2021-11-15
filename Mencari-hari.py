import calendar,sys,os
from time import sleep
from deep_translator import GoogleTranslator
#warna
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def berjalan(s):
        for c in s + "\n":
                sys.stdout.write(c)
                sys.stdout.flush()
                sleep(0.05)
def berjalan2(x):
	for n in x + "\n":
		sys.stdout.write(n)
		sys.stdout.flush()
		sleep(0.005)
def banner():
	sleep(0.0005)
	berjalan2("""\n\x1b[1;91m
████████╗███████╗██████╗░░█████╗░██╗░░██╗
╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██║░██╔╝
░░░██║░░░█████╗░░██████╦╝███████║█████═╝░
░░░██║░░░██╔══╝░░██╔══██╗██╔══██║██╔═██╗░
░░░██║░░░███████╗██████╦╝██║░░██║██║░╚██╗
░░░╚═╝░░░╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝

	██╗░░██╗░█████╗░██████╗░██╗
	██║░░██║██╔══██╗██╔══██╗██║
	███████║███████║██████╔╝██║
	██╔══██║██╔══██║██╔══██╗██║
	██║░░██║██║░░██║██║░░██║██║
	╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝
	  
	        
\x1b[1;92m •\x1b[1;93m•\x1b[1;91m•
                       \x1b[1;94m────────────────────────────────────────────────────
                       \x1b[1;97m [\x1b[1;94m•\x1b[1;92m•\x1b[1;97m] Author   : Animoneesan
                       \x1b[1;97m [\x1b[1;92m•\x1b[1;94m•\x1b[1;97m] Github   : ~
                       \x1b[1;97m [\x1b[1;94m•\x1b[1;92m•\x1b[1;97m] Facebook : ~
                       \x1b[1;94m────────────────────────────────────────────────────
""")
                       


def bersih():
	os.system("clear")

def mulai():
	sleep(0.3)
	bersih()
	banner()
	print()
	berjalan(OKBLUE+"ini Adalah Tool Pencari Nama Hari Dari Keterangan Lahir")
	print()
	berjalan("Mau Melanjutkan ?? y/N ")
	a = input(WARNING+">>>> : ")
	if a == "y" or a == "Y":
		try:
			mulaiLagi()
		except KeyboardInterrupt:
			print("Interrupt !!")
	else:
		berjalan("Exit ~~~~")
def mulaiLagi():
	bersih()
	sleep(0.5)
	berjalan(OKGREEN+"Silahkan Isi Data Berikut !! ")
	date = int(input("Masukkan Tanggal Lahir Anda : "))
	month = int(input("Masukkan Bulan Lahir Anda  (contoh : 03) : "))
	year = int(input("Masukkan Tahun Lahir Anda : "))
	sleep(0.5)
	bersih()
	berjalan("Sedang Mencari . . . .")
	print()
	berjalan("Sukses !!")
	day = calendar.weekday(year,month,date)
	dayName = calendar.day_name[day]
	dayNameIndo = GoogleTranslator(target = "id").translate(dayName)
	print("Anda Lahir Di Hari {}".format(dayNameIndo))

if __name__ == "__main__":
	mulai()
