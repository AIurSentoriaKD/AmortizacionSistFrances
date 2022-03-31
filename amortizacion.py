# Funcion amortizacion, calcula el valor de la amortización.
def amortizacion(monto, interes, periodos):
    # print("{:.2f}".format(A))
    return monto*(interes*(1+interes)**(periodos)/((1+interes)**(periodos)-1))


# Valores iniciales
m = 15000  # monto
i = 0.04  # interes
p = 12  # periodos

# valor de amortizacion
A = amortizacion(m, i, p)

tabla = []
tabla.append([0,0,0,0,m])

for x in range(p):
    renta = round(A,2)
    interes = round(tabla[x][4]*i,2)
    amortiz = round(renta - interes,2)
    nuevosaldo = round(tabla[x][4]-amortiz,2)
    tabla.append([x+1,renta,interes,amortiz,nuevosaldo])
    #print(renta,interes,amortiz,nuevosaldo)

print(tabla)