import random
import csv


trabajadores = ['Juan Pérez','María García','Carlos López','Ana Martínez','Pedro Rodríguez','Laura Hernández','Miguel Sánchez','Isabel Gómez','Francisco Díaz','Elena Fernández']

def sueldos_aleatorios(trabajadores):
    trabajador= {(trabajadores[0]):random.randint(350000,2500000),(trabajadores[1]):random.randint(350000,2500000),(trabajadores[2]):random.randint(350000,2500000),(trabajadores[3]):random.randint(350000,2500000),(trabajadores[4]):random.randint(350000,2500000),(trabajadores[5]):random.randint(350000,2500000),(trabajadores[6]):random.randint(350000,2500000),(trabajadores[7]):random.randint(350000,2500000),(trabajadores[8]):random.randint(350000,2500000),(trabajadores[9]):random.randint(350000,2500000)}
    
    
    return trabajador

trabajador=sueldos_aleatorios(trabajadores)

def llamar_nombressueldo(trabajador):
    print (trabajadores[0],("$"),trabajador['Juan Pérez'])
    print (trabajadores[1],("$"),trabajador['María García'])
    print (trabajadores[2],("$"),trabajador['Carlos López'])
    print (trabajadores[3],("$"),trabajador['Ana Martínez'])
    print (trabajadores[4],("$"),trabajador['Pedro Rodríguez'])
    print (trabajadores[5],("$"),trabajador['Laura Hernández'])
    print (trabajadores[6],("$"),trabajador['Miguel Sánchez'])
    print (trabajadores[7],("$"),trabajador['Isabel Gómez'])
    print (trabajadores[8],("$"),trabajador['Francisco Díaz'])
    print (trabajadores[9],("$"),trabajador['Elena Fernández'])

"""sueldo=trabajador['Juan Pérez'],trabajador['María García'],trabajador['Carlos López'],trabajador['Ana Martínez'],trabajador['Pedro Rodríguez'],trabajador['Laura Hernández'],trabajador['Miguel Sánchez'],trabajador['Isabel Gómez'],trabajador['Francisco Díaz'],trabajador['Elena Fernández']"""
def clasificar_sueldo(trabajador,trabajadores):
    sueldosMenores=[]
    sueldosMedianos=[]
    sueldosGrandes=[]
    i=-1
    for trabajadorNombre,sueldo in trabajador.items():
        i=i+1
        if sueldo<=800000:
            sueldosMenores.append(trabajadores[i])
            sueldosMenores.append(sueldo)
        if sueldo>800000 and sueldo<2000000:
            sueldosMedianos.append(trabajadores[i])
            sueldosMedianos.append(sueldo)
        if sueldo>=2000000:
            sueldosGrandes.append(trabajadores[i])
            sueldosGrandes.append(sueldo)   
    print ("")
    print (f"Sueldos Menores a $800.000 Total:{(int(len(sueldosMenores)/2))}")
    print ("")
    print (sueldosMenores)
    print("")
    print (f"Sueldos entre $800.000 y $2.000.000 Total:{(int(len(sueldosMedianos)/2))}")
    print("")
    print (sueldosMedianos)
    print("")
    print (f"Sueldos Mayores a $2.000.000 Total:{(int(len(sueldosGrandes)/2))}")
    print("")
    print (sueldosGrandes)
    return sueldosMenores


            
def mangosaur():
    with open ('trabajadores.csv', 'w', newline="") as archivo:
        archivo.write("Nombre | Sueldo | Descuento Salud | Descuento AFP | Sueldo Liquido")
    





while True:
    try:
        print("")
        print ("----------MENU----------")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print ("3. guardar csv")
        print("4. Salir del programa")
        opcMen=int(input("->"))
    except ValueError:
        print("valor ingresado en el menu es incorrecto. reintenta")
        
    else: 
        match opcMen:
            case 1:
                
                print ("\n")
                trabajador=sueldos_aleatorios(trabajadores)
                llamar_nombressueldo(trabajador)
                print ("")
                print ("Sueldos aleatorios listos.")
                print ("\n")
            case 2:
                clasificar_sueldo(trabajador,trabajadores)
            case 3:
                mangosaur()
                print ("guardado")
                print ("")
                
            case 4:
                print ("gracias por usar el programa")
                break
                
            
            
                    