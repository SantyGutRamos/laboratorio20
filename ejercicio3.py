ingreso_mensual = float(input("Ingresar tus ingresos mensuales: "))

Aguinaldo = ingreso_mensual
ingreso_anual = ingreso_mensual * 12 + 2 * Aguinaldo 

tramo1_impuesto = 0
tramo2_impuesto = 0
tramo3_impuesto = 0
total_impuestos = 0

base_imponible_t3 = max(0, ingreso_anual - 100000)
tramo3_impuesto = base_imponible_t3 * 0.30

base_imponible_t2 = max(0, min(ingreso_anual, 100000) - 50000)
tramo2_impuesto = base_imponible_t2 * 0.20

base_imponible_t1 = max(0, min(ingreso_anual, 50000) -20000)
tramo1_impuesto = base_imponible_t1 * 0.10

total_impuestos = tramo3_impuesto + tramo2_impuesto + tramo1_impuesto

print("---")
print("El impuesto del tramo 3 (30%) es de: ", tramo3_impuesto)
print("El impuesto del tramo 2 (20%) es de: ", tramo2_impuesto)
print("El impuesto del tramo 1 (10%) es de: ", tramo1_impuesto)

print("el total de impuesto es de: ", total_impuestos)

tasa_efectiva = (total_impuestos / ingreso_anual) * 100
print("La tasa efectiva es de: ", tasa_efectiva,"%")