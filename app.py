import sys
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "AiurSentoriaKDss"

def amortizacionFrances(m, i, p):
    # print("{:.2f}".format(A))
    A = m*(i*(1+i)**(p)/((1+i)**(p)-1))
    tabla = []
    tabla.append([0, 0, 0, 0, m])

    for x in range(p):
        renta = round(A, 2)
        interes = round(tabla[x][4]*i, 2)
        amortiz = round(renta - interes, 2)
        nuevosaldo = round(tabla[x][4]-amortiz, 2)
        tabla.append([x+1, renta, interes, amortiz, nuevosaldo])
        # print(renta,interes,amortiz,nuevosaldo)
    
    return tabla

def amortizacionAleman(m,i,p):
    tabla = []
    tabla.append([0,0,0,0,m])
    AmoritzConst = m/p
    for x in range(p):
        amortiz = round(AmoritzConst,2)
        interes = round(tabla[x][4]*i, 2)
        renta = round(amortiz+interes, 2)
        nuevosaldo = round(tabla[x][4]-AmoritzConst, 2)
        tabla.append([x+1, renta, interes, amortiz, nuevosaldo])
    return tabla

def amortizacionIngles(m,i,p):
    tabla = []
    tabla.append([0,0,0,0,m])
    interesConst = round(m*i,2)
    for x in range(p):
        interes = interesConst
        mensualidad = interesConst
        amortizacion = 0
        saldo = m
        if x < 5:
            tabla.append([x+1,interes,mensualidad,amortizacion,saldo])
        if x == 5:
            tabla.append([x+1, interesConst, m+interesConst,m,0])

    return tabla

def amortizacionFlat(m,i,p):
    tabla = []
    tabla.append([0,0,0,0,m])
    interesConst = round(m*i,2)
    amortConst = round(m/p,2)
    for x in range(p):
        interes = interesConst
        amortizacion = amortConst
        servicio = interes+amortizacion
        nuevosaldo = tabla[x][4]-amortizacion
        tabla.append([x+1,interes, servicio,amortizacion,nuevosaldo])
    return tabla


@app.route("/", methods=['GET'])
def index():
    try:
        args = request.args
        m = int(args.get("monto"))
        i = float(args.get("interes"))
        p = int(args.get("periodo"))
        sysChoice = args.get("sistema")
        print(m, i, p, sysChoice)

        
        # validación de inputs
        if m < 1000 or m > 50000:
            print("Error de m")
            return render_template("./index.html", mensaje ="Valor del monto no valido")
        if i < 0.01 or i > 0.04: 
            print("Error de interes")
            return render_template("./index.html", mensaje ="Valor del interes no valido")
        if p < 6 or p > 24: 
            print("Error de periodo")
            return render_template("./index.html", mensaje ="Valor del periodo no valido")


        # calculo de amortización a una tabla
        if sysChoice == "Frances":
            tabla = amortizacionFrances(m, i, p)
        elif sysChoice == "Aleman":
            tabla = amortizacionAleman(m,i,p)
        elif sysChoice == "Ingles":
            tabla = amortizacionIngles(m,i,p)
        elif sysChoice == "Flat":
            tabla = amortizacionFlat(m,i,p)
        else:
            tabla = amortizacionFrances(m,i,p)

        
        return render_template("./index.html", data = tabla, sistemachoice = sysChoice)
    except:

        print("No hay parametros o uno es incorrecto")
        return render_template("./index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
