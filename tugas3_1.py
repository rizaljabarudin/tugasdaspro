data_mahasiswa = {'rizal': '1011','salwan': '3456','arridho': '1234','gatshu': '7897','agil': '3456',
                  'irvan': '5678','agung': '6789','destito': '1456','ilham': '2579','amir': '5893',}

welcome = '''
============================================================
============ Selamat Datang Di Simak Unkhair================
 ================== Silahkan Login =========================
============================================================
'''

print (welcome)

username = input ("Masukan Username Anda : ")
password = input ("Masukan Password Anda : ")

if username in data_mahasiswa and data_mahasiswa[username] == password :
    print ("Anda Berhasil Login Ke SIMAK")

else :
    print ("Login Gagal, Username Atau password Anda Salah")