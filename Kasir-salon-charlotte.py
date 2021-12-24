#Program Pembayaran Salon Charlotte
import questionary
from datetime import datetime
list = []
harga = []
total = []
jumlahpesan=[]
def login():
    print("+=============================+")
    print("|////|HALAMAN LOGIN KASIR|////|")
    print("+=============================+")
    username = questionary.text("Username :").ask()
    password = questionary.password("Password :").ask()
 
    if username == "admin" and password == "123":
        print("Login berhasil...\n")
        menu()
    else:
        print("Username atau Password salah, Silahkan coba kembali...\n")
        login()

def menu():
    print("""
+=======================================+
|///////////////////////////////////////|
|/////|Daftar Menu Salon Charlotte|/////|
|///////////////////////////////////////|
+=======================================+
|   Perawatan    |  Kode  |    Harga    |
+----------------+--------+-------------+
| Colouring      |  CLR   |  Rp.100000  |
| Rebounding     |  RBD   |  Rp.150000  |
| Hair Cut       |  HCT   |  Rp.30000   |
| Hair Mask      |  HMK   |  Rp.60000   |
| Manicure       |  MNC   |  Rp.35000   |
+=======================================+
 """)
    x1=0
    pertanyaan="Y"
    while pertanyaan !="N":
        pesan = str(input("Kode Perawatan [CLR/RBD/HCT/HMK/MNC] : ")).upper()
        if pesan == "CLR":
            list.append("Colouring ")
            harga.append(100000)
        elif pesan == "RBD":
            list.append("Rebounding")
            harga.append(150000)
        elif pesan == "HCT":
            list.append("Hair Cut  ")
            harga.append(30000 )
        elif pesan == "HMK":
            list.append("Hair Mask ")
            harga.append(60000 )
        elif pesan == "MNC":
            list.append("Manicure  ")
            harga.append(35000 )
        else:
            list.append("    -     ")
            harga.append(0)
        jumlahpesan.append(int(input("Jumlah Perawatan : ")))
        total.append(int(harga[x1]* jumlahpesan[x1]))
        
        pertanyaan=input("Ingin Menambahkan pesanan ? [Y/N]  : ").upper()
        x1=x1+1
    struk()
        
def struk():
    waktu = (f'Tanggal : {datetime.now():%d/%m/%Y        Jam : %H:%M:%S}')
    print("""
+==========================================+
|//////////////////////////////////////////|
|////////////|Struk Pembelian|/////////////|
|//////////////////////////////////////////|
+------------------------------------------+
 {}
+------------------------------------------+
|No.Perawatan         Jumlah       Total   |
|                     Pesan        Harga   |
+------------------------------------------+""".format(waktu))
    x=0
    while x<len(list):
        print(" {}  {}          {}       Rp. {}    ".format(x+1,list[x],jumlahpesan[x],total[x]))
        x=x+1
    print("+------------------------------------------+")
    harusbayar=sum(total)
    print(" Total Biaya                    Rp.",harusbayar)
    uang=int(input(" Masukan Uang Anda              Rp. "))
    kembalian= uang-harusbayar
    if kembalian < 0 :
        print("+==========================================+")
        print(" Maaf uang anda kurang          Rp.",abs(kembalian))
    else:
        print(" Kembali                        Rp.",kembalian,"")
    print("+==========================================+\n")
    kembali()
def kembali():
    tanya=input("Buat Pesanan Baru ? [Y/N]  : ").upper()
    if tanya == "Y":
        list.clear()
        harga.clear()
        total.clear()
        jumlahpesan.clear()
        menu()
    elif tanya == "N":
        print("Program Selesai...\n")
        exit()
    else:
        print("Kode tidak ditemukan, ulangi lagi...\n")
        kembali()
login()
