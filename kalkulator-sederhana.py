def start():
	while True: #mengulang program
		judul = "Kalkulator Sederhana".center(50) #bikin teks ditengah
		print(judul) #cetak judul
		print('='*50) #biar rapih dikit aja wkwkwk cetak '=' 50 kali
		print("\nKeterangan :\n+ = Pertamabahan\n- = Pengurangan\n* atau × = Perkalian\n/ atau : = Pembagian\n") #keterangan operasi yg bisa di pake
		operasi = input("Tentukan operasi yang ingin Anda lakukan,\nmisalnya +, -, *, / : ") #masukin operasi
		if operasi not in("+", "-", "*", "×", ":", "/"):
			print("\nMaaf operasi yang Anda masukan salah!, silahkan coba lagi!\n") #kalo ngemasukin selain dari operasi yg diatas.
			
			break #buat berhentiin program atau ubah break menjadi continue atau juga bisa pakai start() buat skip code yg dibawah dan ngulang program dari awal lagi jika operasi yang dimasukkan salah
		
		try: #jika user input selain dari angka pasti eror tuh, nah pake try buat lanjut ke except
				x = int(input("\nMasukkan angka pertama : ")) #masukin angka ke-
				y = int(input("Masukkan angka kedua : ")) #masukin angka ke-2
		except: #akan dieksekusi jika try eror, kalo ga eror ya except bakalan di skip
			    print("\nMaaf yang Anda masukkan bukan angka, silahkan coba lagi!\n")
			    break #fungsinya sama kek di line 11
		if operasi == "+": #jika ditambah
			print("Hasil dari", x, "+", y, "=", x+y)
		elif operasi == "-": #jika dikurang
		    print("Hasil dari", x, "-", y, "=", x-y)
		elif operasi == "*" or operasi == "×": #jika dikali
		    print("Hasil dari", x, "×", y, "=", x*y)
		elif operasi == "/" or operasi == ":": #jika dibagi
		    print("Hasil dari", x, ":", y, "=", x/y)
	
start()
