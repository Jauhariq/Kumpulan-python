merk = input("Merk baju P/A/S : ").lower()
if merk == 'p':
  print ('Merk Polo')
  ukuran = input('ukuran L/M/S : ' ).lower()
  if ukuran == 'l':
    print('Harga = 300000')
  elif ukuran == 'm':
    print('Harga = 225000')
  elif ukuran == 's':
    print('Harga = 175000')
  else:
    print('Maaf pilihan ukuran tidak tersedia!')
elif merk == 'a':
  print('Merk Alisan')
  ukuran = input('Ukuran L/M/S : ').lower()
  if ukuran == 'l':
    print('Harga = 275000')
  elif ukuran == 'm':
    print('Harga = 200000')
  elif ukuran == 's':
    print('Harga = 150000')
  else:
    print('Maaf ukuran tidak tersedia!')
elif merk == 's':
  print('Merk StYess')
  ukuran = input('Ukuran L/M/S : ').lower()
  if ukuran == 'l':
    print('Harga = 250000')
  elif ukuran == 'm':
    print('Harga = 175000')
  elif ukuran == 's':
    print('Harga = 125000')
  else:
    print('Maaf ukuran tidak tersedia!')
else:
    print('Maaf merk tidak tersedia!')
