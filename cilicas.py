"""
#1
num_vendedores = int(input("Ingrese la cantidad de vendedores: "))
vendedores= []
ven = []

for i in range(num_vendedores):
    sueldo_base = float(input(f"Ingrese el salario base del vendedor {i+1}: "))
    ven.append(sueldo_base)
    ventas_v = []
    for j in range(3):
        venta_s = float(input(f"Ingrese la venta {j+1} del vendedor {i+1}: "))
        ventas_v.append(venta_s)
    ven.append(ventas_v)

comisiones = []
salario_total = []

for i in range(len(vendedores)):
    comision = sum(ven[i]) * 0.1
    salario_total = vendedores[i] + comision
    comisiones.append(comision)
    salario_total.append(salario_total)

for i in range(len(vendedores)):
    print(f"Vendedor {i+1}:")
    print(f"La comision que recibio el vendedor fue de: ${comisiones[i]:.2f}")
    print(f"ek salario total del vendedor fue: ${salario_total[i]:.2f}\n")

"""
"""
#2
import random


d_rojo = 0.4
d_amarillo = 0.25
d_blanco = 0

total_venta = 0

num_clientes = int(input("Ingrese la cantidad de clientes a atender: "))


for i in range(num_clientes):
  
    color_bolita = random.randint(1, 3)
    
   
    if color_bolita == 1:
        descuento = d_rojo
    elif color_bolita == 2:
        descuento = d_amarillo
    else:
        descuento = d_blanco
    
    total_compra = float(input(f"Ingrese el total de la compra del cliente {i+1}: "))
    
    total_pagar = total_compra * (1 - descuento)
    
    total_venta += total_pagar
      
    print(f"El cliente {i+1} pagará ${total_pagar:.2f}")
print(f"\nEl total durante el dia fue de: ${total_venta:.2f}")

"""
"""
#3
alumnos = 40  
materias = 5  
no_minima = 60 
no_nivelar = 0  


for i in range(alumnos):
    promedio = 0
    for j in range(materias):
        nota = float(input(f"Ingrese la nota de la materia {j+1} del alumno {i+1}: "))
        promedio += nota
    promedio /= materias
    if promedio < no_minima:
        no_nivelar += 1


print(f"La cantidad de alumnos sin derecho a nivelación es: {no_nivelar}")

"""
"""
#4
votaciones = [0, 0, 0]


for i in range(2500000):
    voto = int(input("Ingrese el número del candidato votado (1, 2 o 3): "))
    votaciones[voto - 1] += 1


ganador = votaciones.index(max(votaciones)) + 1
cantidad_votos = max(votaciones)


print("El candidato ganador fue", ganador, "con", cantidad_votos, "votos.")

"""
"""
#5
men_50 = 0
entre_50_y_70 = 0
entre_70_y_80 = 0
ma_80 = 0

for i in range(100):
    calificacion = int(input(f"Ingrese la calificación  que obtuvo estudiante {i+1}: "))
    
    if calificacion < 50:
        men_50 += 1
    elif calificacion < 70:
        entre_50_y_70 += 1
    elif calificacion < 80:
    
        entre_70_y_80 += 1
    else:
        ma_80 += 1

print(f"Cantidad de estudiantes con calificación menor a 50: {men_50}, la cantidad de estudiantes con calificación entre 50 y 70: {entre_50_y_70}")
print(f"Cantidad de estudiantes con calificación entre 70 y 80: {entre_70_y_80}, la cantidad de estudiantes con calificación mayor a 80: {ma_80}")

"""