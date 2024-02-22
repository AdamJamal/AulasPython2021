altura=float(input(""))
peso=float(input(""))

IMC= peso / altura**2

if   IMC < 18.5:
    print("{:.2f}".format(IMC),"\nMagreza")
elif IMC <= 24.9:
    print("{:.2f}".format(IMC),"\nNormal")
elif IMC <= 30.0:
    print("{:.2f}".format(IMC),"\nSobrepeso")
else:
    print("{:.2f}".format(IMC),"\nObesidade")        