import os

incioArchivo = 'inicial_name.txt'
todir = 'final_name.txt'

arch1 = 'hallowen.bmp'
arch2 = 'navidad.bmp'

result = os.rename(incioArchivo,todir)
result = os.rename(arch1,arch2)

print("las rutas de origen a sido renombrada a las rutas de salida exitosamente")
print(f"A {todir} y {arch2}")