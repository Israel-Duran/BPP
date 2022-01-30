import pandas as pd
import unittest


class unittest_app(unittest.TestCase):

    def setUp(self):
        try:
            self.df_excel= pd.read_excel('finanzas2020.xlsx')
            self.df = pd.DataFrame(self.df_excel)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')

    def test_gastos_mes(self):
        self.gastos_mes = []
        self.verificar_lista = [-17621, -24398, -29690, -34133, -17200, -24197, -18390, -29013, -29151, -22957, -24180, -25861]

        for columna, fila in self.df.items():
            gastosMes = 0
            for i in fila:
                if type(i) == str:
                    try:
                        i = float(i)
                    except:
                        i = 0
                if i < 0:
                    gastosMes = gastosMes + i

            self.gastos_mes.append(gastosMes)
        self.assertListEqual(self.gastos_mes, self.verificar_lista)

        try:
            self.df_gastos_mes = pd.DataFrame(self.gastos_mes)
            self.df_verificar_lista = pd.DataFrame(self.verificar_lista)
            pd.testing.assert_series_equal(self.df_gastos_mes.min(), self.df_verificar_lista.min())
            pd.testing.assert_series_equal(self.df_gastos_mes.mean(), self.df_verificar_lista.mean())
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')
        print(f'El mes que más ha gastado: {self.df_gastos_mes.min()}')
        print(f'La media de gastos es de: {self.df_gastos_mes.mean()}')


    def test_ingresos_mes(self):
        self.ingresos_mes = []
        self.verificar_lista = [29685, 24437, 21721, 15200, 27504, 22720, 26690, 20278, 18203, 26369, 25337, 22817]

        for columna, fila in self.df.items():
            ingresosMes = 0
            for i in fila:
                if type(i) == str:
                    try:
                        i = float(i)
                    except:
                        i = 0
                if i > 0:
                    ingresosMes = ingresosMes + i

            self.ingresos_mes.append(ingresosMes)
        self.assertListEqual(self.ingresos_mes, self.verificar_lista)

        try:
            self.df_ingresos_mes = pd.DataFrame(self.ingresos_mes)
            self.df_verificar_lista = pd.DataFrame(self.verificar_lista)
            pd.testing.assert_series_equal(self.df_ingresos_mes.max(),self.df_verificar_lista.max())
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')
        print(f'El mes que mas ha ahorrado mas: {self.df_ingresos_mes.max()} ')


    def test_gastosTotales(self):
        self.gastosTotales = 0
        self.verificar_gastos_totales = -296791

        for columna, fila in self.df.items():
            gastosMes = 0
            for i in fila:
                if type(i) == str:
                    try:
                        i = float(i)
                    except:
                        i = 0

                if i < 0:
                    gastosMes = gastosMes + i

            self.gastosTotales = self.gastosTotales + gastosMes
        self.assertEqual(self.gastosTotales, self.verificar_gastos_totales)
        print(f'Gastos totales a lo largo del año:{self.gastosTotales}')

    def test_IngresosTotales(self):
        self.ingresosTotales = 0
        self.verificar_ingresos_totales = 280961

        for columna, fila in self.df.items():
            ingresosMes = 0
            for i in fila:
                if type(i) == str:
                    try:
                        i = float(i)
                    except:
                        i = 0
                if i > 0:
                    ingresosMes = ingresosMes + i
            self.ingresosTotales = self.ingresosTotales + ingresosMes
        self.assertEqual(self.ingresosTotales, self.verificar_ingresos_totales)
        print(f'Ingresos totales a lo largo del año:{self.ingresosTotales}')


    def test_comlumnas(self):
        self.contador = 0
        self.columnas = 12
        try:
            for columna, fila  in self.df.items():
                self.contador += 1
            self.assertEqual(self.contador, self.columnas)
            if self.contador == 12:
                print(f'Las columnas son correctas, hay {self.contador} columnas')
            else:
                print('Las columnas son incorrectas')
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')

    # Comprobar el contenido de cada mes
    def test_contedino_mes(self):
        try:
            self.vacio = ' '
            self.assertNotIn(self.vacio, self.df)
            if self.vacio in self.df:
                print('Los meses no tienen contenido')
            else:
                print('Los meses tienen contenido')
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')

if __name__ == '__main__':
    unittest.main()
