from algeo2Dfix import main2
from algeo3dfix import main3
import os

print('TUGAS BESAR 2 ALJABAR GEOMETRI')
print('APLIKASI TRANSFORMASI MATRIKS MENGGUNAKAN OPENGL')
print('Anggota Kelompok : ')
print('T. Antra Oksidian Tafly / 13517020')
print('Andrian Cedric / 13517065')
print('Jan Meyer Saragih / 13517131')
print()
print('List peritah')
print('1. Operasi 2 dimensi')
print('2. Operasi 3 dimensi')
print('3. Exit program')
str = input('Masukkan input : ')

os.system('cls')

if (str == '1'):
    main2()
elif (str == '2'):
    main3()

while str != 'Exit' or 'exit' or '3':
   str = input('Masukkan input : ')

print('List peritah')
print('1. Operasi 2 dimensi')
print('2. Operasi 3 dimensi')
print('3. Exit program')

os.system('cls')
print('SEKIAN DAN TERIMA KASIH')
print('Anggota Kelompok : ')
print('T. Antra Oksidian Tafly / 13517020')
print('Andrian Cedric / 13517065')
print('Jan Meyer Saragih / 13517131')
