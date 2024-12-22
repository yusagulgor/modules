
from modules import *
# import numpy as np

# print(dif)

"""

Test aşaması . Çalışıyor mu diye deneniyor.

"""

# !Graphplotter is okey

# def f(x: int) -> float:
#     return x**2

# def g(x: int) -> float:
#     return x**2 + 2

# def h(x: int) -> float:
#     return x + 1

# def f_3D(u: float, v: float) -> float:
#     return np.sin(u)

# def g_3D(u: float, v: float) -> float:
#     return np.cos(v)

# def h_3D(u: float, v: float) -> float:
#     return u + v


# plotter = GraphPlotter()
# dimension = int(input("Lütfen grafik boyutunu seçin (2D için 2, 3D için 3): "))
# # * Ex usage
# if dimension == 2:
#     plotter.plot_2D([f])
# elif dimension == 3:
#     plotter.plot_3D([f_3D, g_3D, h_3D])
# else:
#     print("Geçersiz boyut seçimi.")

# point1 = Point(2, 3)
# point2 = Point(4, 1)

# x1,y1 = point1()
# print(f"x1 :{x1} , y1 :{y1}")

# Vektör ekleme
# graph_plotter = GraphPlotter()
# graph_plotter.vector_addition(point1, point2)

# Skaler çarpma
# graph_plotter.scalar_multiplication(point1, 3)

# İç çarpım
# graph_plotter.dot_product(point1, point2)
# print()

# !ÇALIŞIYOR Const

# class Constant(Const):
#     NAME = "Yusa"


# Constant().NAME = "Hayır" # ?Error

# name = Constant().NAME # ?have TypeError 
# print(name)

# ! --------------------------------------------


# GEHUB.fcodef("pytestfgh") #* Çalışıyor:D

# * Ok
# class IAT(Module):
#     def __init__(self, name:str):
#         super().__init__(name)

#     def pi(self):
#         return self.name

# a = IAT("hite")
# print(a.pi())