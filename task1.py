# def wag():
#     p_hour = float(input("Введите выработку сотрудника в часах: "))
#     in_hour = float(input("Введите ставку в час: "))
#     prem = float(input("Введите размер премии: "))
#     return p_hour * in_hour + prem
#
# print(f"Размер з/п = {wag()}")

from sys import argv
wag = argv
argv = float(wag[1]) *  float(wag[2]) + float(wag[3])
print(f"Размер з/п = {argv}")
