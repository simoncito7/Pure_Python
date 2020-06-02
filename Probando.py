# import math

# def norma(x1,y1):
# 	"""Esta función devuelve la norma del vector ingresado"""
# 	n=sqrt(x1**2+y1**2)
# 	return(n)

# print("Programa que calcula la norma de un vector")
# x1=float(input("Ingrese la coordenada en x"))
# y1=float(input("Ingrese la coordenada en y"))

# print("La norma del vector es: ", norma(x1,y1))

#------------------------------------------------------------------------------------------------------------------------
# datetime to string using strftime()
# from datetime import datetime

# now = datetime.now() # current date and time

# meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
# dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

# year = now.strftime("%Y")
# print("year:", year)

# month = now.strftime("%m")
# month = int(month)
# mes = meses[month-1]
# print("mes:", mes)

# day = now.strftime("%d")
# print("day:", day)

# time = now.strftime("%H:%M:%S")
# print("time:", time)

# date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
# print("date and time:",date_time)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)
