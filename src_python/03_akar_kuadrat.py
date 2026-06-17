# Program Mencari Akar Persamaan Kuadrat
a = float(input("Masukkan nilai a : "))
b = float(input("Masukkan nilai b : "))
c = float(input("Masukkan nilai c : "))

D = b**2 - 4*a*c

if D > 0:
    x1 = (-b + (D**0.5)) / (2*a)
    x2 = (-b - (D**0.5)) / (2*a)

    print("Akar real berbeda")
    print("x1 = %.3f" % x1)
    print("x2 = %.3f" % x2)

elif D == 0:
    x = -b / (2*a)

    print("Akar real kembar")
    print("x1 = x2 = %.3f" % x)

else:
    print("Persamaan memiliki akar-akar imajiner")
