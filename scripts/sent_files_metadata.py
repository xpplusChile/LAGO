import io
import os
from datetime import datetime


path_file="/home/sebastian/Documents/LAB_HEP/red_pitaya/"
file_name="prueba.txt"

#source="/home/src/datos"
files = sorted(os.listdir(path_file))
files_number=len(files)
files_size = sum(os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f))*1e-3 #para kilobyte *1e-3 para megabyte *1e-6
print(files_size)
print(files_number)

files_number=1
files_size=1

try:
	f = open("prueba.txt", "x")
	f.write("Lunes     :\n" + "0" + " archivos han sido enviados \n" + "0" + " kB de datos han sido enviados \n")
	f.write("Martes    :\n" + "0" + " archivos han sido enviados \n" + "0" + " kB de datos han sido enviados \n")
	f.write("Miercoles :\n" + "0" + " archivos han sido enviados \n" + "0" + " kB de datos han sido enviados \n")
	f.write("Jueves    :\n" + "0" + " archivos han sido enviados \n" + "0" + " kB de datos han sido enviados \n")
	f.write("Viernes   :\n" + "0" + " archivos han sido enviados \n" + "0" + " kB de datos han sido enviados \n")
	f.write("Sabado    :\n" + "0" + " archivos han sido enviados \n" + "0" + " kB de datos han sido enviados \n")
	f.write("Domingo   :\n" + "0" + " archivos han sido enviados \n" + "0" + " kB de datos han sido enviados \n")
	f.close()
except:
	print("")

f=open('prueba.txt', 'r')
# read a list of lines into data
data = f.readlines()

dt = datetime.now()
x = dt.weekday()

print(data[0+x*3])
print(data[1+x*3])
print(data[2+x*3])
	
data[1+x*3]=data[1+x*3].replace(" archivos han sido enviados", "")
data[2+x*3]=data[2+x*3].replace(" kB de datos han sido enviados", "")


data[1+x*3]=str(int(data[1+x*3])+files_number)
data[2+x*3]=str(float(data[2+x*3])+files_size)


# now change the 2nd line, note that you have to add a newline
data[1+x*3] = data[1+x*3]+" archivos han sido enviados\n"
data[2+x*3] = data[2+x*3]+" kB de datos han sido enviados\n"

# and write everything back
with open('prueba.txt', 'w') as file:
    file.writelines( data )
f.close()
    
