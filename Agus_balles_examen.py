import random
import csv

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
trabajadoresSueldos={}
def asignar_sueldos(trabajadores):
 
    for trabajador in trabajadores:
        trabajadoresSueldos[trabajador] = random.randint(300000, 2500000)
        print ("---------------")
        print("Sueldos asignados.")
        print ("---------------")
        
def clasificar_sueldos(trabajadores):
    menores_800k = []
    entre_800k_2m = []
    mayores_2m = []
    
    for trabajador in (trabajadores):
        sueldo = trabajador ["sueldo"]
        if sueldo < 800000:
            menores_800k.append(trabajador)
        elif 800000 <= sueldo <= 2000000:
            entre_800k_2m.append(trabajador)
        else:
            mayores_2m.append(trabajador)
            
    print("---------------")
    print("Sueldos menores a $800.000: TOTAL:", len(menores_800k))
    for t in menores_800k:
        print(t["nombre"],t["sueldo"])
        
    print("\nSueldos entre $800.000 y $2.000.000: TOTAL:", len(entre_800k_2m))
    for t in entre_800k_2m:
        print(t["nombre"],t["sueldo"])
              
    print("Sueldos superiores a $2.000.000: TOTAL:", len(mayores_2m))
    for t in mayores_2m:
        print(t["nombre"],t["sueldo"])
    print("---------------")
    
    
def ver_estadisticas(trabajadores):
    sueldos = [trabajador["sueldo"] for trabajador in trabajadores]
    total_sueldos = sum(sueldos)
    promedio_sueldos = total_sueldos / len(sueldos)
    max_sueldo =max (sueldos)
    min_sueldo =min (sueldos)
    print("---------------")
    print("Estadísticas:")
    print(f"Sueldo total: ${total_sueldos}")
    print(f"Sueldo promedio: ${promedio_sueldos}")
    print(f"Sueldo máximo: ${max_sueldo}")
    print(f"Sueldo minimo: ${min_sueldo}")
    print("---------------")
    
def generar_reporte(trabajadores):
    with open("reporte_sueldos.csv", mode="w", newline="") as file:
        writer= csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo base",  "Descuento salud",  "Descuento AFP" , "Sueldo líquido"])
        
        for trabajador in trabajadores:
            sueldo_base = trabajador["sueldo"]
            descuento_salud = sueldo_base  * 0.07
            descuento_afp = sueldo_base  * 0.12
            sueldo_liquido = sueldo_base - descuento_salud - descuento_afp
            writer.writerow ([trabajador["nombre"], trabajador["cargo"], sueldo_base, descuento_salud, descuento_afp, sueldo_liquido])
            
    print ("Reporte generado y guardado como 'reporte_sueldos.csv'.")
    
    
def salir():
    print("Finalizando programa...")
    print("Desarrollado por Agustina Ballesteros")
    print("RUT: 21.720.579-4")
    
    
def menu():
    while True:
        print("\nMenu:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas.")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        opcion= int(input("Selecicione una opción: "))
        
        if opcion == 1:
            asignar_sueldos(trabajadores)
        elif opcion == 2:
            clasificar_sueldos(trabajadores)
        elif opcion == 3:
            ver_estadisticas(trabajadores)
        elif opcion == 4: 
            generar_reporte(trabajadores)
        elif opcion == 5:
            salir()
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            
menu()
            
    
    
    
    
        
    
        
    
    
        
        
        
    
        
        
    
  
