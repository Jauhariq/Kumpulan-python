def start(): #pake fungsi buat dipanggil nantinya
	while True: #mengulang program
		judul = "Kalkulator Sederhana".center(58) #bikin teks ditengah
		print(judul) #cetak judul
		print('='*58) #biar rapih dikit aja wkwkwk cetak '=' 58 kali
		print("\nKeterangan :\n+ = Pertamabahan\n- = Pengurangan\n* atau × = Perkalian\n/ atau : = Pembagian\n") #keterangan operasi yg bisa di pake
		operasi = input("Tentukan operasi yang ingin Anda lakukan,\nmisalnya +, -, *, / : ") #masukin operasi
		if operasi not in("+", "-", "*", "×", ":", "/"):
			print("\nMaaf operasi yang Anda masukan salah!, silahkan coba lagi!\n") #kalo ngemasukin selain dari operasi yg diatas.
			
			break #buat berhentiin program atau ubah break menjadi continue atau juga bisa pakai start() buat skip code yg dibawah dan ngulang program dari awal lagi jika operasi yang dimasukkan salah
		
		try: #jika user input selain dari angka pasti eror tuh, nah pake try buat lanjut ke except
				x = int(input("\nMasukkan angka pertama : ")) #masukin angka ke-1
				y = int(input("Masukkan angka kedua : ")) #masukin angka ke-2
		except: #akan dieksekusi jika try eror, kalo ga eror ya except bakalan di skip
			    print("\nMaaf yang Anda masukkan bukan angka, silahkan coba lagi!\n") #cetak except
			    break #fungsinya sama kek di line 11
		if operasi == "+": #jika ditambah
		    print("Hasil dari", x, "+", y, "=", x+y) #cetak hasil +
		elif operasi == "-": #jika dikurang
		    print("Hasil dari", x, "-", y, "=", x-y) #cetak hasil -
		elif operasi == "*" or operasi == "×": #jika dikali
		    print("Hasil dari", x, "×", y, "=", x*y) #cetak hasil ×
		elif operasi == "/" or operasi == ":": #jika dibagi
		    print("Hasil dari", x, ":", y, "=", x/y) #cetak hasil /
	
start() #manggil isi fungsi start
