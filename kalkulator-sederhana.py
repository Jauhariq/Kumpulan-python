while True: #mengulang operasi kalo udah selesai
    print("\nKeterangan :\n+ = Pertamabahan\n- = Pengurangan\n* atau × = Perkalian\n/ atau : = Pembagian\n")
    operasi = input("Tentukan operasi yang ingin Anda lakukan,\nmisalnya +, -, *, / : ") 
    if operasi not in("+", "-", "*", "×", ":", "/"):
        print("Maaf operasi yang Anda masukan salah!") #kalo ngemasukin selain dari operasi yg diatas.
        break #buat berhentiin program atau ubah break menjadi continue buat ngulang program dari awal lagi jika operasi yang dimasukkan salah
        
    x = int(input("Masukkan angka pertama : ")) #masukin angka ke-1
    y = int(input("Masukkan angka kedua : ")) #masukin angka ke-2
    
    if operasi == "+": #jika ditambah
        print("Hasil dari", x, "+", y, "=", x+y)
    elif operasi == "-": #jika dikurang
        print("Hasil dari", x, "-", y, "=", x-y)
    elif operasi == "*" or operasi == "×": #jika dikali
        print("Hasil dari", x, "×", y, "=", x*y)
    elif operasi == "/" or operasi == ":": #jika dibagi
        print("Hasil dari", x, ":", y, "=", x/y)
