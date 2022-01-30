import pandas as pd
import matplotlib.pyplot as plt


#APARTADO 1
try:
    df_excel= pd.read_excel('finanzas2020.xlsx')
    df = pd.DataFrame(df_excel)
except Exception as e:
    print(f'Ha ocurrido un error: {e}')

gastos_mes = []
ingresos_mes = []
gastosTotales = 0
ingresosTotales = 0


try:
    for columna, fila in df.items():
        gastosMes = 0
        ingresosMes = 0
        for i in fila:
            if type(i) == str:
                try:
                    i = float(i)
                except:
                    i = 0
            if i > 0:
                ingresosMes = ingresosMes + i
            elif i < 0:
                gastosMes = gastosMes + i

        gastos_mes.append(gastosMes)
        ingresos_mes.append(ingresosMes)

        ingresosTotales = ingresosTotales + ingresosMes
        gastosTotales = gastosTotales + gastosMes
except Exception as e:
    print(f'Ha ocurrido un error: {e}')
finally:
    print('Fin del bucle')

df_gastos_mes = pd.DataFrame(gastos_mes)
df_ahorro_mes = pd.DataFrame(ingresos_mes)

print(f'El mes que ha gastado mas: {df_gastos_mes.min()}')
print(f'El mes que mas ha ahorrado mas: {df_ahorro_mes.max()} ')
print(f'La media de gastos al año es: {df_gastos_mes.mean()}')
print(f'Gastos total a lo largo del año:{gastosTotales}')
print(f'Ingresos totales a lo largo del año:{ingresosTotales}')



try:
    x= ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    y = ingresos_mes

    plt.plot(x, y, marker='o', linestyle = '--', color='b')
    plt.xlabel('Meses')
    plt.ylabel('Ingresos')
    plt.title('Ingresos a lo largo del año')
    plt.show()

except Exception as e:
    print(f'Ha ocurrido un error: {e}')

#APARTADO 2

#Comprobar que tiene 12 columnas
try:
    contador = 0
    for columna, fila  in df.items():
        contador += 1
    if contador == 12:
        print(f'Las columnas son correctas, hay {contador} columnas')
    else:
        print('Las columnas son incorrectas')
except Exception as e:
    print(f'Error: {e}')

#Comprobar el contenido de cada mes
try:
    if ' ' in df:
        print('Los meses no tienen contenido')
    else:
        print('Los meses tienen contenido')
except Exception as e:
    print(f'Ha ocurrido un error: {e}')