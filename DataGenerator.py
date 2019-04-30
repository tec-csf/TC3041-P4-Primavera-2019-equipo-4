import random
print (random.randint(0, 5))

f = open("practica4_data.txt", "w")
#f.write("Now the file has more content!")

f.write("# DDL\n\nCREATE DATABASE practica4\n\n# DML\n\n# CONTEXT-DATABASE: practica4\n\n")



measurements=["energia_utilizada", "energia_generada", "temperatura"]
tag1nom="medida"
tag1val="KW"
tag2val="centrigrados"
generador=["generador1", "generador2", "generador3"]
habitacion=["habitacion1", "habitacion2", "habitacion3"]

#energia
for i in range(14000000):
    f.write(measurements[random.randint(0,1)]+","+tag1nom+"="+tag1val+",generador="+generador[random.randint(0,2)]+" valor="+str(random.randint(0, 10000))+" "+str(1556496000+i)+"\n")
    if (i % 1000000 == 0):
        print("Ya pasaron: "+str(i)+"\n")


#temperatura
for i in range(6000000):
    f.write(measurements[2] + ",habitacion=" + habitacion[
        random.randint(0, 2)] +",medida=C" +" valor=" + str(random.randint(0, 30)) + " "+str(1556496000+i) + "\n")
    if (i % 1000000 == 0):
        print("Ya pasaron: "+str(i)+"\n")
f.close()