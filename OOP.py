# ---------------------------------------------------------------------------------
# OOP with Python
# probando ámbitos y espacios de nombres
# def prueba_ambitos():
#
#     def hacer_local():
#         algo = "algo local"
#
#     def hacer_nonlocal():
#         nonlocal algo
#         algo = "algo no local"
#
#     def hacer_global():
#         global algo
#         algo = "algo global"
#     algo = "algo de prueba"
#     hacer_local()
#     print("Luego de la asignación local:", algo)
#     hacer_nonlocal()
#     print("Luego de la asignación no local:", algo)
#     hacer_global()
#     print("Luego de la asignación global:", algo)
#
# prueba_ambitos()
# print("In global scope:", algo)
#
# la asignación local (que es el comportamiento normal) no cambió la vinculación de algo de prueba_ambitos.
# La asignación nonlocal cambió la vinculación de algo de prueba_ambitos, y la asignación global cambió la
# vinculación a nivel de módulo.
# -------------------------------------------------------------------------------------------------------------



# # importing library
# import math
#
# # here we define the class "Punto"
# class Punto():
#     """Representation of a point on the plane"""
#
#     def __init__(self, x = 0, y = 0):
#         "Class constructor"
#         # here we do the validation of the input data. Input data must be numeric
#         if self.es_numero(x) and self.es_numero(y):
#
#             self.x = x
#             self.y = y
#         else:
#             raise(TypeError("X y Y deben ser valores numéricos"))
#     # method for validation of input data
#     def es_numero(self, valor):
#         "Comprueba que los valores ingresados sean numéricos"
#         return isinstance(valor, (int, float, complex))
#     # method to calculate the distance between two coordinates
#     def distancia(self, otro):
#         "Calcula la distancia entre dos puntos del plano"
#         dx = self.x - otro.x
#         dy = self.y - otro.y
#         dist = math.sqrt(dx**2 + dy**2)
#         return dist
#
#
# p = Punto(5,7)
# q = Punto(2,3)
#
# print(p.x)
# print(p.y)
# print(q.x)
# print(q.y)
# print("distancia: ", p.distancia(q))

