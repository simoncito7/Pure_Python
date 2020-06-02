# 1 -  Escribir una funcion que dado un vector al origen (definido por sus puntos x,y), devuelva la norma del vector, 
# dada por || (x, ~ y)|| = sqrt(x**2 + y**2)

# import math
# def norma(x1,y1):
# 	"""hola"""

# 	n = math.sqrt(x1**2+y1**2)
# 	return(n)

# print("Este programa calcula la normal de un vector \n")
# x1 = float(input("Ingrese la primer coordenada (x): "))
# y1 = float(input("Ingrese la segunda coordenada (y): "))

# print("La norma del vector ingresado es: ", norma(x1,y1))

#-----------------------------------------------------------------------------------------------------------------------
#2 - Escribir una función que dados dos puntos en el plano (x1,y1 y x2,y2), devuelva la resta de ambos (debe devolver un par de valores). 

# The following function returns the difference between the coordinates that are passed by argument
# def difference(x1,y1,x2,y2):

# 	resultado = (x2-x1,y2-y1)

# 	return(resultado)

# # Here, we print the result at the same time that we're calling the function
# print('La resta de los números ingresados es: ', difference(2,2,6,6))

#-----------------------------------------------------------------------------------------------

# 3 - Utilizando las funciones anteriores, escribir una función que dados dos puntos en el plano (x1,y1 y x2,y2), devuelva la distancia 
# entre ambos.

# Library math
# import math

# # This function returns the module of a vector passed by argument
# def norma(x1,y1):
# 	"""hola"""

# 	n = math.sqrt(x1**2+y1**2)
# 	return(n)

# # The following function returns the difference between the coordinates that are passed by argument
# def difference(x1,y1,x2,y2):

# 	resultado = (x2-x1,y2-y1)

# 	return(resultado)

# print("Este programa calcula la normal de un vector \n")
# x1 = float(input("Ingrese la primer coordenada en x: "))
# y1 = float(input("Ingrese la primer coordenada en y: "))
# x2 = float(input("Ingrese la segunda coordenada en x: "))
# y2 = float(input("Ingrese la segunda coordenada en y: "))

# (xr,yr) = difference(x1,y1,x2,y2)

# print("La norma del vector ingresado es: ", norma(xr,yr))

#----------------------------------------------------------------------------------------
# g) Escribir una función que calcule el área de un triángulo a partir de su base y su altura.

# def area_t(b,h):
# 	resultado = (b*h)/2
# 	return resultado

# print("El siguiente programa calcula el área de un triángulo a partir de su base y su altura.\n \n")
# b = float(input("Ingrese el valor de la base del triángulo por favor: "))
# h = float(input("Ingrese el valor de la altura del triángulo por favor: "))

# print ("El área del triángulo es: ", area_t(b,h))

#----------------------------------------------------------------------------------------
# Ejercicio 4.6.1. Escribir funciones que resuelvan los siguientes problemas: 
# a) Dado un número entero n, indicar si es o no par. 
# b) Dado un número entero n, indicar si es o no primo.

# Python program to check if  
# given number is even or prime or none of those 

# def es_par(n):
# 	if n%2==0:
# 		return True
# 	else:
# 		return False


# n = int(input("Enter a number to know if is an even or a prime number: "))

# f = es_par(n)
# if f==True:
# 	print("it's an even number")
# else:
# 	print("it isn't an even number")

# If given number is greater than 1 
# if n > 1: 
      
#    # Iterate from 2 to n / 2  
#    for i in range(2, n//2): 			#n//2 is for int division
         
#        # If num is divisible by any number between  
#        # 2 and n / 2, it is not prime  
#        if (n % i) == 0: 
#            print(n, "is not a prime number") 
#            break
#    else: 
#        print(n, "is a prime number") 
  
# else: 
#    print(n, "is not a prime number")

#----------------------------------------------------------------------------------------

# Ejercicio 4.6.2. Escribir una implementación propia de la función abs, que devuelva el valor absoluto de cualquier valor que reciba
# import math

# n = float(input("input any number to know its absolute value: "))

# n = (n)**2
# print("The absolute value of the input number is: ", math.sqrt(n))


#----------------------------------------------------------------------------------------

# Ejercicio 4.6.3. Escribir una función que reciba por parámetro una dimensión n, 
# e imprima la matriz identidad correspondiente a esa dimensión. 

# n = int(input("ingrese un número: "))

# numero_filas = n
# numero_columnas = n

# # se crea la matriz
# matriz = []
# for i in range(numero_filas):
#     matriz.append([])
#     for j in range(numero_columnas):
#         matriz[i].append(None)

# # se asignan valores
# for i in range(n):
# 	for j in range(n):
# 		if i==j:
# 			matriz[i][j]= 1
# 		else:
# 			matriz[i][j]= 0

# a = ""

# for j in range(n):
#     for i in range(n):		
       
#         a = a + str(matriz[i][j]) +'\t' 			# se va mostrando una fila a la vez
		
		
#     print (a)		# se imprime la fila
#     a=""			# se borra
    
#----------------------------------------------------------------------------------------
# Ejercicio: Sumar, restar, multiplicar y dividir dos polinomios ingresados por teclado.


#Importamos la libreria SympY para usar variables simbolicas (x, y)
# import sympy

# #Obtenes los dos polinomios introducidos por el usuario
# P1 = input("Primer Polinomio: ")
# P2 = input("Segundo Polinomio: ")
# print("\n")

# #Definimos los simbolos
# sympy.init_printing()
# x,y = sympy.symbols('x,y')

# #Luego almacenamos en varibles los dos polinomios procesados por la funcion Poly de sympy
# Poly1 = sympy.Poly(P1)
# Poly2 = sympy.Poly(P2)

# #Declaramos una funcion para cada operacion que querramos utilizar

# def mult(p1, p2):
# 	return p1 * p2

# def suma(p1, p2):
# 	return p1 + p2

# def res(p1, p2):
# 	return p1 - p2

# def div(p1, p2):
# 	return p1 / p2

# #Guardamos los valores retornados por las funciones y les pasamos los 2 polinomios como parametros,  Poly1 y Poly2
# resultMult = mult(Poly1, Poly2)
# resultSuma = suma(Poly1, Poly2)
# resultDiv = div(Poly1, Poly2)
# resultRes = res(Poly1, Poly2)

# #Mostramos el valor que deseemos
# print("Resultado: ", resultSuma)
# print("Resultado: ", resultRes)
# print("Resultado: ", resultMult)
# print("Resultado: ", resultDiv)

#-----------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 4.6.4. Escribir funciones que permitan encontrar:
# a) El máximo o mínimo de un polinomio de segundo grado (dados los coeﬁcientes a, b y c), indicando si es un máximo o un mínimo. 
# b) Las raíces (reales o complejas) de un polinomio de segundo grado. 
# Nota: validar que las operaciones puedan efectuarse antes de realizarlas (no dividir por cero, ni calcular la raíz de un número negativo). 
# c) La intersección de dos rectas (dadas las pendientes y ordenada al origen de cada recta). Nota: validar que no sean dos rectas con la misma
#  pendiente, antes de efectuar la operación. 

# firstly, we import all modules from the Sympy library
# from sympy import *

# # then, we create the 'x' and 'y' vars
# x=Symbol('x')
# y=Symbol('y')
# # allows to print something in a good way regarding the environment
# init_printing(use_unicode=True)
# # here, the enters the polynoms
# P1 = input("ingrese Polinomio 1: ")
# P2 = input("ingrese Polinomio 2: ")

# def maxminf(f):
#     """ Calcula los máximos y mínimos de una función f(x) """
#     df = diff(f, x) # First deriv
#     d2f = diff(f, x, 2) # Second deriv
#     pcs = solve(Eq(df,0)) # critical values
#     for p in pcs:
#         if d2f.subs(x,p)>0: 
#             tipo="Min"
#         elif d2f.subs(x,p)<0: 
#             tipo="Max"
#         else: 
#             tipo="Indefinido"
#         print("x = %f (%s)"%(p,tipo))

# # call to the function 
# maxminf(P1)
# # 
# resp=solve([P1,P2], dict=True)
# print(resp)


# Ejercicio 4.6.5. Escribir funciones que resuelvan los siguientes problemas: 
# a) Dado un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es
#  divisible por 100, excepto que también sea divisible por 400. 
# b) Dado un mes, devolver la cantidad de días correspondientes. 
#  c) Dada una fecha (día, mes, año), indicar si es válida o no.
#  d) Dada una fecha, indicar los días que faltan hasta ﬁn de mes. 
#  e) Dada una fecha, indicar los días que faltan hasta ﬁn de año. 
#  f) Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha. 
#  g) Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido entre ambas, en años, meses y días.

# from datetime import datetime, date, time, timedelta
# import calendar

# # that function allows to know if a year (enter by the user) is leap or not
# def bisiesto(diferencia):
#     if diferencia.days == 366:
#         print("Es año bisiesto")
#     else:
#         print("No es año bisiesto")

# y = int(input("Ingrese un año: "))

# fecha_inicial = datetime(y,1,1)

# fecha_final = datetime(y+1,1,1)

# diferencia = fecha_final - fecha_inicial

# bisiesto(diferencia)

# m = int(input("Ingrese un mes: "))
# print(calendar.month(y,m))

# function that indicates if a date is valid or not
# while True:
#    try:
#        fecha_str = input('\n Ingrese fecha ==> ejemplo "18/01/1952"...: ')
#        fecha = datetime.strptime(fecha_str, '%d/%m/%Y')
#        break
#    except:
#        print("\n No ha ingresado una fecha correcta...")
#        break

# print("\n ", fecha)

# -----------------------------------------------------------------------------------------------------------
# Ejercicio 5.7.1. Escribir un programa que reciba una a una las notas del usuario, preguntando a cada paso si desea
# ingresar más notas, e imprimiendo el promedio correspondiente

# print("Enter the qualifications for calculate the average score \n")
# count = 0
# acu = 0
# while True:
    
#     N = float(input("Enters the qualifications of the students: "))
#     if (N<0 or N>10):
#         print("invalid score")
#     else:
#         count+=1
#         acu+=N
#     opc = str(input("Do you want to enter another score? : Y or N: " ))
#     if (opc == 'N' or opc == 'n'):
#         print("The average score of the student is: ", acu/count)
#         break
#     else:
#         pass

#-----------------------------------------------------------------------------------------------------
# Ejercicio 5.7.3. Manejo de contraseñas 
# a) Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario la contraseña, y no le permita 
# continuar hasta que la haya ingresado correctamente. 
# b) Modiﬁcar el programa anterior para que solamente permita una cantidad ﬁja de intentos. 
# c) Modiﬁcar el programa anterior para que después de cada intento agregue una pausa cada vez mayor, utilizando la función 
# sleep del módulo time. 
# d) Modiﬁcar el programa anterior para que sea una función que devuelva si el usuario ingresó o no la contraseña correctamente, 
# mediante un valor booleano (True o False).

# import time 

# passw = "contrase"
# t=1
# count=5

# while True:
#     enterpass = input("Enter your password please:  ") 
#     if(enterpass != passw):
#         print("Wrong password. You can try another ", count-1, " times")
#         count = count - 1
#         if count != 0:
#             pass
#         else:
#             print("")
#             break
#         time.sleep(t)
#         t+=1
#     else:
#         print("Entering...")
#         time.sleep(5)
#         break

#---------------------------------------------------------------------------------------------------------

# Ejercicio 6.4. Escribir una función contar(l, x) que cuente cuántas veces aparece un carácter l dado en una cadena x. 

# x="1ndfghubwgh111njfdn1nsjdn1nj1"
# counter = 0

# def contar(x,counter):
#     "This function counts the amount of number '1' that contains"

#     for letter in x:
#         if(letter == '1'):
#             counter = counter + 1
#     return(counter)

# print(contar(x,counter))

#---------------------------------------------------------------------------------------------------------

# 6.8. Ejercicios
# Ejercicio 6.8.1. Escribir funciones que dada una cadena de caracteres:
# a) Imprima los dos primeros caracteres. 
# b) Imprima los tres últimos caracteres. 
# c) Imprima dicha cadena cada dos caracteres. Ej.: ’recta’ debería imprimir ’rca’ 
# d) Dicha cadena en sentido inverso. Ej.: ’hola mundo!’ debe imprimir ’!odnum aloh’ 
# e) Imprima la cadena en un sentido y en sentido inverso. Ej: ’reflejo’ imprime ’reflejoojelfer’. 

# cadena1 = "saglawrganwrig"
# cadena2= ""

# # a)
# print(cadena1[:2])
# # b)
# print(cadena1[-3:len(cadena1)])
# # c)
# for i in range(0,len(cadena1),2):
#     cadena2 = cadena2 + cadena1[i]

# print(cadena2)
# print(cadena1[::2])

# # d)
# print(cadena1[::-1])
# # e)
# print(cadena1 + cadena1[::-1])

#------------------------------------------------------------------------------------------------------

# Ejercicio 6.8.2. Escribir funciones que dada una cadena y un caracter: 
# a) Inserte el caracter entre cada letra de la cadena. Ej: ’separar’ y ’,’ deberíadevolver ’s,e,p,a,r,a,r’ 
# b) Reemplace todos los espacios por el caracter. Ej: ’mi archivo de texto.txt’ y ’_’ debería devolver ’mi_archivo_de_texto.txt’ 
# c) Reemplace todos los dígitos en la cadena por el caracter. Ej: ’su clave es: 1540’ y ’X’ debería devolver ’su clave es: XXXX’ 
# d) Inserte el caracter cada 3 dígitos en la cadena. Ej. ’2552552550’ y ’.’ debería devolver ’255.255.255.0’ 

# cadena = "separar"
# # a)
# cadena=cadena.replace("",',')
# print(cadena)
# # b)
# cadena2 = "mi archivo de texto.txt"
# cadena2 = cadena2.replace(" ","_")
# print(cadena2)

# # c) 
# cadena3="su clave es: 1540"
# cadena3=cadena3.replace('1540','XXXX')

# print(cadena3)

# # d)
# cadena4='2552552550'

# print('.'.join([str(cadena4)[i:i+3] for i in range(0, len(str(cadena4)), 3)]))

# ----------------------------------------------------------------------------------------------------------
# Ejercicio 7.3. Cartas como tuplas. 
# a) Proponer una representación con tuplas para las cartas de la baraja francesa. 
# b) Escribir una función poker que reciba cinco cartas de la baraja francesa e informe (devuelva el valor lógico correspondiente)
#  si esas cartas forman o no un poker (es decir que hay 4 cartas con el mismo número).

# t=(1,)
# c=2
# def agregar(t,c):
#     t=list(t)
#     while (c<14):
#         t.append(c)
#         c=c+1
        
#     t=tuple(t)
#     return t

# print(agregar(t,c))

# maso=(1,2,2,2,2)
# maso=list(maso)


# def poker(maso):

#     for i in range(len(maso)):
        
#         a=maso[i]
#         veces=maso.count(a)
#         if veces==4:
#             print("POKER!!!")
#             break

# poker(maso)

# -----------------------------------------------------------------------------------------------------------------

# Ejercicio 7.6.1. Escribir una función que reciba una tupla de elementos e indique si se encuentran ordenados de menor a mayor o no.

# def orden(t,band):

#     for i in range(0,len(t)-1):
#         if (t[i]>t[i+1]):
#             band=1

#     return band

# t=(1,2,3,1,5,9)
# band=0
# a=orden(t,band)

# if(a==1):
#     print("No está ordenada")
# else: print("Está ordenada")

# --------------------------------------------------------------------------------------------
# Ejercicio 7.4. El tiempo como tuplas. 
# a) Proponer una representación con tuplas para representar el tiempo. 
# b) Escribir una función sumaTiempo que reciba dos tiempos dados y devuelva su suma.

# print("Ingresar horario: \n ")

# def suma(t1,t2):
#     #t3=0,1,2
#     t3=[0,0,0]
#     t1=list(t1)
#     t2=list(t2)

#     t3[2]=t1[2]+t2[2]
#     if(t3[2]>=60):
#         t1[1]=t1[1]+1
#         t3[2]=t3[2]-60
    
#     t3[1]=t1[1]+t2[1]
#     if(t3[1]>=60):
#         t1[0]=t1[0]+1
#         t3[1]=t3[1]-60
    
#     t3[0]=t1[0]+t2[0]
    
#     t3=tuple(t3)
#     return t3

# while True:
#     hh1=int(input("Ingrese la hora: "))
#     if(hh1<0 or hh1>23):
#         print("Error. Ingrese un valor válido.")
#     else:
#         break

# while True:
#     mm1=int(input("Ingrese los minutos: "))
#     if(mm1<0 or mm1>59):
#         print("Error. Ingrese un valor válido.")
#     else:
#         break

# while True:
#     ss1=int(input("Ingrese los segundos: "))
#     if(ss1<0 or ss1>59):
#         print("Error. Ingrese un valor válido.")
#     else:
#         break

# while True:
#     hh2=int(input("Ingrese la hora: "))
#     if(hh2<0 or hh2>23):
#         print("Error. Ingrese un valor válido.")
#     else:
#         break

# while True:
#     mm2=int(input("Ingrese los minutos: "))
#     if(mm2<0 or mm2>59):
#         print("Error. Ingrese un valor válido.")
#     else:
#         break

# while True:
#     ss2=int(input("Ingrese los segundos: "))
#     if(ss2<0 or ss2>59):
#         print("Error. Ingrese un valor válido.")
#     else:
#         break

# t1=(hh1,mm1,ss1)
# t2=(hh2,mm2,ss2)
# t3=suma(t1,t2)

# print("La suma de los horarios ingresados da un total de ",t3[0]," horas, ",t3[1]," minutos y ",t3[2], "segundos")

# -----------------------------------------------------------------------------------------------------------------

# Ejercicio 7.6.2. Dominó. 
# a) Escribir una función que indique si dos ﬁchas de dominó encajan o no. Las ﬁchas son recibidas en dos tuplas,
# por ejemplo: (3,4) y (5,4) 
# b) Escribir una función que indique si dos ﬁchas de dominó encajan o no. Las ﬁchas son recibidas en una cadena, 
# por ejemplo: 3-4 2-5. Nota: utilizar la función split de las cadenas.

# this function indicates if two "domino" token or dominoes fit
# def encaje1(t1,t2):

#     if t1[0]==t2[0] or t1[0]==t2[1] or t1[1]==t2[0] or t1[1]==t2[1]:
#         print("Encajan")
#     else: 
#         print("No encajan")

# # Domino token 1
# t1=(0,1)
# # Domino token 2
# t2=(0,2)
# # Dominoes 
# c="3-2 2-5"

# # call to the function
# encaje1(t1,t2)
# # for the dominoes received in a string, first we use split() for replace the empty space in the middle by a comma
# def sacar_espacio(c):
#     c2=c.split(" ")
#     return c2
# # call to the function
# a = sacar_espacio(c)
# # here we create a empty list
# z=[]
# # print(a)
# # then, for each element of the resulting list (a), we replace the hyphen (-) by a comma
# for i in range(len(a)):
#     z.append(a[i].split("-"))

# # print(z)
# #Next, we store each element of the list z in differents lists (z1 and z2)
# z1=z[0]
# z2=z[1]

# # print(z1)
# # print(z2)
# # Finally, we use the same function that we have used for the first case
# encaje1(z1,z2)

# ---------------------------------------------------------------------------------

# Ejercicio 7.6.3. Campaña electoral 
# a) Escribir una función que reciba una tupla con nombres, y para cada nombre imprima el mensaje 
# Estimado <nombre>, vote por mí. 
# b) Escribir una función que reciba una tupla con nombres, una posición de origen p y una cantidad n,
# e imprima el mensaje anterior para los n nombres que se encuentran a partir de la posición p. 
# c) Modiﬁcar las funciones anteriores para que tengan en cuenta el género del destinatario, para ello, 
# deberán recibir una tupla de tuplas, conteniendo el nombre y el género.

# this function prints each name contained in the tuple
# def impresion1(nombres):
#     for i in nombres:
#         print("Estimado ", i, " vote por mí")
# # this function prints a specified range of names. It receives the names, the initial index and the final index.
# def impresion2(nombres,p,n):
#     for i in range(p,n):
#         print("Estimado ", nombres[i], " vote por mí")
# # this function prints each name contained in the tuple considering its gender.
# def impresion3(nombres):
#     for i in range(len(nombres)):
#         print("Estimado ", nombres[i], " vote por mí") if nombres[i][1]=='H' else print("Estimada ", nombres[i], " vote por mí")

# nombres=('Alberto','Bernardo','Carlos','María','Mónica','Yamila')
# p=2
# n=4
# nombres_genre=(('Alberto','H'),('Bernardo','H'),('Carlos','H'),('María','M'),('Mónica','M'),('Yamila','M'))
# # calling to the differents functions
# impresion1(nombres)             # a)
# impresion2(nombres,p,n)         # b)
# impresion3(nombres_genre)       # c)

# ------------------------------------------------------------------------------------------
# Ejercicio 7.6.4. Vectores 
# a) Escribir una función que reciba dos vectores y devuelva su producto escalar. 
# b) Escribir una función que reciba dos vectores y devuelva si son o no ortogonales. 
# c) Escribir una función que reciba dos vectores y devuelva si son paralelos o no. 
# d) Escribir una función que reciba un vector y devuelva su norma.

# el producto escalar de dos vectores v1 y v2 es v1*v2
# dos vectores serán ortogonales si su producto escalar es nulo
# dos vectores serán paralelos cuando haya un factor de proporcionalidad que los relacione: v1=k*v2
# la norma de un vector es la raíz cuadrada de la suma de los cuadrados de las componentes

# this function makes the dot product between two vectors passed by arg
# def prod_escalar(v1,v2):
#     acu=0
#     for i in range(len(v1)):
#         acu = acu + v1[i]*v2[i]
    
#     return acu
# # this function makes the dot product between two vectors and prints if they are or not orthogonal
# def prod_ortogonal(v1,v2):
#     acu=0
#     for i in range(len(v1)):
#         acu = acu + v1[i]*v2[i]
    
#     print("Son ortogonales ") if acu==0 else print("No son ortogonales")
# # this function test if two vectors are parallel
# def paralelos(v1,v2):
#     band=0
#     for i in range(len(v1)-1):
#         if (v1[i]/v2[i])!=(v1[i+1]/v2[i+1]):
#             band=1
    
#     if band == 0:
#         print("Son paralelos")
#     else:
#         print("No son paralelos")

# # vectors defined as tuples()
# v1=(2,3)
# v2=(1,2)
# v3=(-3,2)
# v4=(4,6)
# # call to the functions
# a = prod_escalar(v1,v2)
# print("El producto escalar de los vectores es: ", a)
# prod_ortogonal(v1,v2)
# paralelos(v1,v4)

# -----------------------------------------------------------------------------------------

# Ejercicio 7.6.5. Dada una lista de números enteros, escribir una función que: 
# a) Devuelva una lista con todos los que sean primos. 
# b) Devuelva la sumatoria y el promedio de los valores. 
# c) Devuelva una lista con el factorial de cada uno de esos números. 

# from math import factorial

# def prime_number(v):
#     z=[]
#     for j in range(len(v)):
#         n=v[j]
#         band=0
#         if n > 1:
#             # Iterate from 2 to n / 2  
#             for i in range(2, n//2): 			#n//2 is for int division
                    
#                 # If num is divisible by any number between  
#                 # 2 and n / 2, it is not prime  
#                 if (n % i) == 0: 
#                     band=1
                    
#             if band==0:
#                 z.append(n)
#             else:
#                 pass
#     return z      

# def sum_avg(v):
#     acu=0
#     avg=0

#     for i in range(len(v)):
#         acu = acu + v[i]
    
#     avg=acu/len(v)
#     print("La sumatoria es ", acu, " y el promedio es ",avg)

# def facto(v2):
#     z=[]
#     for i in range(len(v2)):
#         z.append(factorial(v2[i]))
    
#     return z

# v=[1,2,3,8,9,11,15,18,22,23,35,47,51,55,56]
# v2=[2,3,4]

# print(prime_number(v))
# sum_avg(v2)
# print(facto(v2))

#---------------------------------------------------------------------------------------------------------------
# Ejercicio 7.6.10. Matrices. 
# a) Escribir una función que reciba dos matrices y devuelva la suma. 
# b) Escribir una función que reciba dos matrices y devuelva el producto. 
# c) Escribir una función que indique si un grupo de vectores,recibidos mediante una lista, son linealmente 
# independientes o no.

# import numpy as np

# def suma(M1,M2):
#     M = []
#     for i in range(numero_filas):
#         M.append([])
#         for j in range(numero_columnas):
#             M[i].append(None)
                
#     for i in range(n):
#         for j in range(n):
#             M[i][j]=M1[i][j]+M2[i][j]
    
#     return M

# def producto(m,v):
#     print("El prodcuto de las matrices pasadas por argumento es: ", m * v)

# def independencia(x):

#     resultado = np.linalg.det(x)
#     if resultado == 0:
#         print("Son linealmente dependientes")
#     else:
#         print("Son linealmente independientes")

# n = int(input("ingrese un número: "))

# numero_filas = n
# numero_columnas = n

# # se crea la matriz 1
# M1 = []
# for i in range(numero_filas):
#     M1.append([])
#     for j in range(numero_columnas):
#         M1[i].append(None)

# # se crea la matriz 1
# M2 = []
# for i in range(numero_filas):
#     M2.append([])
#     for j in range(numero_columnas):
#         M2[i].append(None)

# # se asignan valores
# print("Ingrese los valores de la matriz 1: ")
# for i in range(n):
# 	for j in range(n):
# 		M1[i][j]=int(input())

# # se asignan valores
# print("Ingrese los valores de la matriz 2: ")
# for i in range(n):
# 	for j in range(n):
# 		M2[i][j]=int(input())
		
# print("Primer matriz ingresada: ", M1)
# print("Segunda matriz ingresada: ", M2)
# print("El resultado de la suma es: ", suma(M1,M2))

# m = np.array([[1,2,3],[4,5,6]])
# v = np.array([[1,2,3]])
# x = np.array([[1,1],[2,2]])    
# producto(m,v)
# independencia(x)

# -------------------------------------------------------------------------------------------

# Ejercicio 7.6.11. Plegado de un texto. 
# Escribir una función que reciba un texto y una longitud y devuelva una lista de cadenas de como máximo esa longitud.
# Las líneas deben ser cortadas correctamente en los espacios (sin cortar las palabras).

# def plegado(t,p):

#     t1=t.split(" ")
#     t1=t1[:p]
#     return t1

# t="Hola como estas que estabas por hacer con ese trabajo que nos habian dado hace unas semanas que estaba inconcluso"
# p=7
# t1=plegado(t,p)
# print(t1)

# --------------------------------------------------------------------------------------------------

# Ejercicio 7.6.12. Funciones que reciben funciones. 
# a) Escribir una funcion llamada map,que reciba una función y un número y devuelva el número que resulta de aplicar 
# la función recibida.
# b) Escribir una funcion llamada map,que reciba una función y una lista y devuelva la lista que resulta de aplicar 
# la función recibida a cada uno de los elementos de la lista recibida. 
# c) Escribir una función llamada ﬁlter, que reciba una función y una lista y devuelva una lista con los elementos de
# la lista recibida para los cuales la función recibida devuelve un valor verdadero. 

# this function receives another function and returns the result of the application of that function over the arguments
# def map(func, n):
#     print(func(n))
# this function will return a list containing all elements of the past vector that meets a certain condition
# In this case, the condition is that all the numbers must be positives.
# def filter(func,lista):
#     z=[]
#     for i in range(len(lista)):
#         if func(lista[i])==True:
#             z.append(lista[i])
#     return z

# #function 1
# def fun1(n):
#     return n**2
# # function 2
# def fun2(v):
#     for i in range(len(v)):
#         v[i]=2*v[i]
#     return(v)
# # function 3
# def fun3(n):
#     if n>0:
#         return True

# n=2
# v=[1,2,3,-6,2,-10]
# # call to the functions
# map(fun1,n)
# map(fun2,v)
# print(filter(fun3,v))

# ------------------------------------------------------------------------------------------------
# Ejercicio 8.7.1. Escribir una función que reciba una lista desordenada y un elemento, que: 
# a) Busque todos los elementos coincidan con el pasado por parámetro y devuelva la cantidad de coincidencias encontradas. 
# b) Busque la primera coincidencia del elemento en la lista y devuelva su posición. 
# c) Utilizando la función anterior busque todos los elementos coincidan con el pasado por parámetro y devuelva una lista 
# con las posiciones. 

# def busca1(lista,a):
#     count=0
#     for i in range(len(lista)):
#         b=str(lista[i])
#         if a==b:
#             count=count+1
    
#     if count==0:
#         print("Ese elemento no se encuentra en la lista")
#     else:
#         print("Ese elemento se encontró ",count, " veces en la lista")

# def busca2(lista,a):
#     band=0
#     for i in range(len(lista)):
#         b=str(lista[i])
#         if a==b:
#             return(i)           
    
#     if band==0:
#         print("No se encuentra ese elemento en la lista")
    
# def busca3(lista,a):
#     band=0
#     z=[]
#     for i in range(len(lista)):
#         b=str(lista[i])
#         if a==b:
#             band=1
#             z.append(i)           
    
#     if band==0:
#         print("No se encuentra ese elemento en la lista")
#     else:
#         return z

# lista=[1,5,8,6,8,7,5,3,'snb','hola','hello','willkomen',8,8,8]
# a=str(input("Ingrese un elemento cualquiera para buscar en la lista: "))

# busca1(lista,a)
# indice=busca2(lista,a)
# if indice != None:
#     print("El indice es: ", indice)
# print("El elemento ingresado se encuentra en las posiciones ",busca3(lista,a))

# 33 min    (14/04)
# ----------------------------------------------------------------------------------------------
# Ejercicio 8.7.2. Escribir una función que reciba una lista de números no ordenada, que: 
# a) Devuelva el valor máximo. 
# b) Devuelva una tupla que incluya el valor máximo y su posición. 

# def valorMax(lista):

#     for i in range(len(lista)):
#         if i==0:
#             max=lista[i]
#         elif i>0:
#             if(lista[i]>max):
#                 max=lista[i]
    
#     return max

# def valorMax2(lista):

#     for i in range(len(lista)):
#         if i==0:
#             max=lista[i]
#             imax=i
#         elif i>0:
#             if(lista[i]>max):
#                 max=lista[i]
#                 imax=i
    
#     return (max,imax)
        
# lista=[1,2,7,8,9,5566,2,55558,520,1148,65,6688888888,42,0,-58,78,-7777777777744444]

# maximo = valorMax(lista)
# print("Valor máximo encontrado: ", maximo)
# maximo2 = valorMax2(lista)
# print("Valor máximo encontrado y su posición: ", maximo2)

# 21 minutos - 14/04

# ----------------------------------------------------------------------------------------------

# Ejercicio 8.7.3. Agenda simpliﬁcada Escribir una función que reciba una cadena a buscar y una lista de tuplas 
# (nombre_completo, telefono), y busque dentro de la lista, todas las entradas que contengan en el nombre completo
#  la cadena recibida (puede ser el nombre, el apellido o sólo una parte de cualquiera de ellos). 
#  Debe devolver una lista con todas las tuplas encontradas. 

# def busca(agenda,cadena):
#     z1=""
#     z2=""
#     for i in agenda:
#         z1=i[0]
#         z11=z1.split(" ")
        
#         z2=i[1]
#         z22=z2.split(" ")
        
#         if (cadena in z11) or (cadena in z22):
#             return i


# cadena1='mariel'
# agenda=[('mariel monserrat','123456'),('simon valenzuela','123789'),('alfonzo valenzuela','456456'),('kiara monserrat','528456')]

# print(busca(agenda,cadena1))

# 33 min, 14/04
# ------------------------------------------------------------------------------------------------
# Ejercicio 9.5.1. Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario en 
# donde las claves sean los primeros elementos de las tuplas y los valores sean los segundos.

# def dicc(listaT):
#     d={}
#     for i in listaT:
#         d[i[0]]=i[1]

#     return d

# lista=[('simon','30'),('mariel','30'),('alfonzo','70'),('susana','56')]
# d=dicc(lista)   
# print("El diccionario creado es \n", d)

# 17 minutos,14/04

# ---------------------------------------------------------------------------------------
# Ejercicio 9.5.2. Diccionarios usados para contar. 
# a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de apariciones 
# de cada palabra en la cadena. Por ejemplo, si recibe "Qué lindo día que hace hoy"
# debe devolver: ’que’: 2, ’lindo’: 1, ’día’: 1, ’hace’: 1, ’hoy’: 1 
# b) Escribir una función que cuente la cantidad de apariciones de cada caracter en una cadena de texto, y 
# los devuelva en un diccionario. 

# here we define the function
# def cuenta(cadena):
#     L2=[]       # empty list
#     L3=[]       # empty list

#     # Here we replace the blank spaces by commas
#     L1=cadena.split(" ")
#     # In the following loop we go through L1 for make another list (L2) so that L2 only contains elements without repeating
#     for N in L1:
#         if N not in L2:
#             L2.append(N)
#     count=0
#     # in this loop we take each element of L2 and count the number of times this element appears in L1.
#     # then we make another list (L3) to store a tuple with the element and the number of times it appears
#     for element in L2:
#         for x in L1:
#             if element==x:
#                 count=count+1
#         L3.append((element,str(count)))
#         count=0
#     # finally, we define an empty dictionary for store the elements of list L3
#     d={}
#     for element in L3:
#         d[element[0]]=element[1]

#     # print(L3)
#     # print(d)
#     return d

# # definition of the function
# def cuenta2(cadena):
#     # first, we define three empty lists
#     L2=[]
#     L3=[]
#     L1=[]
#     # here, we make a list with each element of "cadena"
#     for i in cadena:
#         L1.append(i)
#     print(L1)
#     # here we make another list (L2) with all the elements that are differents in L1
#     for N in L1:
#         if N not in L2:
#             L2.append(N)
#     count=0
#     # in this cycle we count the number of times each element appears in "cadena". Then, we store the element
#     # and the number of times they appear respectively.
#     for element in L2:
#         for x in L1:
#             if element==x:
#                 count=count+1
#         L3.append((element,str(count)))
#         count=0

#     # finally, we store in an empty dictionary all the elements of L3
#     d={}
#     for element in L3:
#         d[element[0]]=element[1]

#     return d

# # strings declaration
# cadena="hola como estas como como estas estas hola rerendjg dnforgner hola hola holaaaa alalala lalala lalala"
# cadena1="sdgsdfw"
# # here we print the values returned by the respective functions
# print(cuenta(cadena))
# print(cuenta2(cadena1))

# 14/04
# ---------------------------------------------------------------------------------------------
# Ejercicio 9.5.3. Continuación de la agenda. Escribir un programa que vaya solicitando al usuario que ingrese nombres.
# a) Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar el teléfono y, opcionalmente, 
# permitir modiﬁcarlo si no es correcto. 
# b) Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente. El usuario puede utilizar la 
# cadena "*", para salir del programa. 

# def agenda():
#     d={}
#     while True:
    
#         opc=input("Desea ingresar un nombre? Y/N:  ")
#         if (opc == 'Y') or (opc == 'y'):

#             nombre=input("Ingrese un nombre: ")
#             if nombre in d.keys():
#                 print("Ese nombre ya existe")
#                 opc2=input("Desea modificarlo? Y/N  ")
#                 if (opc2 == 'Y') or (opc2 == 'y'):
#                     numero = int(input("Ingrese el numero de contacto: "))
#                     d[nombre]=numero
#                 elif (opc2 == 'N') or (opc2 == 'n'):
#                     print(d.get(nombre))
#                 else:
#                     print("opcion no valida")
#             else:
#                 numero = int(input("Ingrese el numero de contacto: "))
#                 d[nombre]=numero
#             print(d)

            
            
#         elif (opc == 'N') or (opc == 'n'):        
#             print("Ha elegido salir")
#             break

#         else:
#             print("Opción incorrecta")
#     return d

# d=agenda()
# if d!="":
#     print(d)

# 15/04
# ----------------------------------------------------------------------------------------
# Ejercicio 11.10.1. Escribir un programa, llamado head que reciba un archivo y un número N e imprima 
# las primeras N líneas del archivo.
#  
# using the libraries Numpy and Pandas
# import numpy as np
# import pandas as pd
# # a data frame is a table-like data structure
# # here we create a data frame using pandas
# df = pd.DataFrame({'animal':['snake', 'bat', 'tiger', 'lion','fox', 'eagle', 'shark', 'dog', 'deer']})
# # finally, we show the complete data frame and two "heads", one with five elements (default) and another with three.
# print(df)
# print("\n\n")
# print(df.head())
# print("\n\n")
# print(df.head(3))
# print("\n\n")

# -------------------------------------
# Facing the problem by another way...
# -------------------------------------

# this function printes N rows of the passed file
# def imprime(f,N):
#     #setting count in 0
#     count=0
#     # with the loop we can go through each row, so that we can print each row in a easy way
#     for row in f:
#         print(row)
#         count=count+1
#         if count>=N:
#             break    

# # Here we open "inputFile.txt" and configure it for reading. f is an object of type open()
# f = open('inputFile.txt','r')
# N = 5
# # call to the function
# imprime(f,N)
# #closing the file
# f.close()

# ------------------------------------------------------------------------------------
# Ejercicio 11.10.2. Escribir un programa, llamado cp.py, que copie todo el contenido de un archivo 
# (sea de texto o binario) a otro, de modo que quede exactamente igual. Nota: utilizar archivo.read(bytes) 
# para leer como máximo una cantidad de bytes.

# Firstly, we open two files with txt extension. The first one, is opened with 'r' permission only because we need read it and not change its content, 
# while the second is opened with 'w' permissions, because we need to write on it the same content of "inputFile.txt"
# archivoO = open('inputFile.txt','r')
# archivoD = open('archivito.txt','w')
# # here we use a for cycle for go through "archivoO" (inputFile.txt) and write each row on "archivoD" (archivito.txt)
# for row in archivoO:
#     archivoD.write(row)
# # finally, we close both files
# archivoO.close()
# archivoD.close()

# -----------------------------------------------------------------------------------------
# Ejercicio 11.10.3. Escribir un programa, llamado cut.py, que dado un archivo de texto, un delimitador y una lista de campos,imprima solamente esos campos,
# separados por ese delimitador. 

# open "input file.txt" with read permissions only. we work using f (open() objetc)
# f = open('inputFile.txt','r')

# going through f with a for loop
# for row in f:
#     print(row)
# we finally close f
# f.close()

# ------------------------------------------------------------------------------------------------
# Ejercicio 11.10.4. Escribir un programa, llamado wc.py que reciba un archivo, lo procese e imprima por pantalla cuántas líneas,
# cuantas palabras y cuántos caracteres contiene el archivo.

# firstly, we open the file we want to work with
# f = open('inputFile.txt','r')
# # here we define the counts for store the number of rows, words and letters contained in the file
# count_rows = 0
# count_words = 0
# count_letters = 0
# # this loop goes along the rows of the file and allows to count numbers of rows, words and letters.
# for row in f:
#     count_rows = count_rows + 1                     # counts each row
#     row_split=row.split()                           # create a list with each row 
#     count_words = count_words + len(row_split)      # here we count the number of word
#     for word in row_split:                          # here is a "little" for loop to each mini list to count the letters
#         count_letters = count_letters + len(word)   
# # by last we print the counters
# print(count_rows)
# print(count_words)
# print(count_letters)

# ----------------------------------------------------------------------------------------------
# Ejercicio11.10.5. Escribir un programa,llamado grep.py que reciba una expresión y un archivo e imprima las líneas del archivo que contienen la expresión recibida.

# first we ask an expression to the user
# expresion =str(input("Ingrese una expresión "))
# # here we open the file we are working with
# f = open('inputFile.txt','r')
# # then we go along the rows of the .txt looking for if there are one or more matches with the entered expression
# for row in f:
#     row_split=row.split()
#     # print(row_split)
#     for i in range(len(row_split)):
#         a=expresion.lower()             # this make lowercase the entered expression
#         b=(row_split[i]).lower()        # this line make lowercase each word of the row
#         if a == b:
#             print(row)
        
# f.close()

# -------------------------------------------------------------------------------------------------------------------
# example using "assert" 

# def factor(n):

#     assert n>=0, "n debe ser mayor o igual que 0"

#     fact=1
#     for i in range(2,n+1):
#         fact*=i
#     return fact

# n=-3

# print(factor(n))
# ------------------------------------------------------------------------------------------------------------------------------
# use of isinstance()
# i=2

# if not isinstance(i,(int,float,complex)):
#     raise TypeError(i,"No es numérico")

# ----------------------------------------------------------------------------------------------------------------------

# plot([x], y, [fmt], *, data=None, **kwargs)
# plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)

# x = (4,8,13,17,20)
# y = (54, 67, 98, 78, 45)
#
# import matplotlib.pyplot as plt
# plt.plot([4,8,13,17,20],[54, 67, 98, 78, 45])
# plt.show()

# ---------------------------------------------------------------------------------------
# se importa módulo random con alias r
import random as r

# método para la creación de grupos
def mezcla1(lista, num_integrantes):
    """Este método permite generar grupos de manera aleatoria"""

    cantGrupos = len(lista)/num_integrantes
    lista_2 = r.shuffle(lista)

    if (len(lista) % num_integrantes) == True:

        for i in range(cantGrupos):
            print


participantes = ["Simon Valenzuela", "Nicolas Sarubbi", "Cristian Ramirez", "Artur Sadovenko", "Emiliano Romero", "Gerardo Santa Cruz",
              "Manuel Quintana", "Fabian Fullone", "Ignacio Perozzi", "Feliz Molina", "Yesica Gallo", "Lucia Callejon",
              "Florencia Szulak", "Lucia Stefanuto", "Florencia Sidotti", "Daniela Araujo", "Alejandro Mercado", "Hernan Bevilacqua"]

cantXgrupo = 6

mezcla1(participantes,cantXgrupo)

# import random
#
# mylist = ["apple", "banana", "cherry","anana","brocoli","carne"]
#
# print(random.sample(mylist, k=2))


