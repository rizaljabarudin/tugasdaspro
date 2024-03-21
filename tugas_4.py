x = int (input ("Masukkan Bilangan  : "))

Bil_okal = oct(x) [2:]
Bil_hexa =hex(x) [2:]
Bil_desimal = x
Bil_Bin = "{:08b}".format(x)

print("Bilangan biner:", Bil_Bin)
print("Bilangan oktal dari", x , "adalah", Bil_okal)
print("Bilangan Hexadesimal", x, "adalah", Bil_hexa)
print("Biallangan Desimal ", x , "adalah", Bil_desimal)