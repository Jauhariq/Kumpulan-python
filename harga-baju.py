merk = input("Merk baju P/A/S : ")
if merk == 'P'or merk == 'p':
  print ('Merk Polo')
  ukuran = input('ukuran L/M/S : ' )
  if ukuran == 'L' or ukuran == 'l':
    print('Harga = 300000')
  elif ukuran == 'M' or ukuran == 'm':
    print('Harga = 225000')
  else:
    print('Harga = 175000')
elif merk == 'A' or merk == 'a':
  print('Merk Alisan')
  ukuran = input('Ukuran L/M/S : ')
  if ukuran == 'L' or ukuran == 'l':
    print('Harga = 275000')
  elif ukuran == 'M' or ukuran == 'm':
    print('Harga = 200000')
  else:
    print('Harga = 150000')
else:
  print('Merk StYess')
  ukuran = input('Ukuran L/M/S : ')
  if ukuran == 'L' or ukuran == 'l':
    print('Harga = 250000')
  elif ukuran == 'M' or ukuran == 'm':
    print('Harga = 175000')
  else:
    print('Harga = 125000')
