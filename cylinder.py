# 21.09.2026 tunni jaoks Markoga.
import math

r = float(input("Sisesta silindri raadius: "))
h = float(input("Sisesta silindri kõrgus: "))

V = math.pi * r**2 * h
L = 2 * math.pi * r * h
A = 2 * math.pi * r * (h + r)

print("Silindri ruumala: ", V)
print("Silindri külgpindala:", L)
print("Silindri kogupindala:", A)