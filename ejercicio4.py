salario_base=int(input("Ingresar tu salario base: "))
horas_extra=int(input("ingresar las hora extra: "))
pago_hora_extra=50
bono=500
afp=15
salud=10
descuentos=(salario_base * afp/100) + (salario_base * salud/100)
salario_bruto = salario_base + (horas_extra * pago_hora_extra) + bono
salario_neto=salario_bruto-descuentos
print("El salario bruto es de: ",salario_bruto)
print("El descuento total es de: ",descuentos)
print("El salario neto es de: ",salario_neto)