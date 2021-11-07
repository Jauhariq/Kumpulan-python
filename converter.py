def convert():
	print("***WELCOME TO FREE UNIT CONVERTER***")
	print("==PYTHON 2021==".center(35))
	print("KONVERSI")
	unit_1 = input("Dari:").lower()
	unit_2 = input("Ke:").lower()
	
	if unit_1 == "m" and unit_2 == "cm":
		print("\n")
		print("METER KE CENTIMETER")
		while True:
			angka = input("Masukkan angka: ")
			if angka.isnumeric():
				hasil = int(angka) * 100
				print(str(angka), "m =", str(hasil), "cm\n")
			elif angka in ("b", "back"):
				print("\n")
				convert()
			elif angka == "q":
				print("Terimakasih telah menggunakan Unit Converter")
				break
				
	elif unit_1 == "cm" and unit_2 == "m":
		print("\n")
		print("CENTIMETER KE METER")
		while True:
			angka = input("Masukkan angka: ")
			if angka.isnumeric():
				hasil = int(angka) / 100
				print(str(angka), "cm =", str(hasil), "m\n")
			elif angka in ("b", "back"):
				print("\n")
				convert()
			elif angka == "q":
				print("Terimakasih telah menggunakan Unit Converter")
				break
	else:
				pass
				
				
convert()