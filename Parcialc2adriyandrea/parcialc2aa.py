import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget)
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
df=pd.read_csv('Parcialc2adriyandrea/inventario.csv')
print("**************************")
print("Inspección del inventario")
print("**************************")
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())

class Inventario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Inventario de sucursales')
        self.resize(700,500)
        df_agrupado=df.groupby('Sucursal')['Cantidad'].sum()
        self.figura=Figure(figsize=(6,4))
        self.canvas=FigureCanvas(self.figura)
        ax=self.figura.add_subplot(111)
        colores=['#F5CEE4', '#CEEFF5', '#CEF5D5','#F5F4CE','#E2CEF5']
        ax.bar(df_agrupado.index,df_agrupado.values,color=colores)
        ax.set_title("Inventario de sucursales")
        ax.set_xlabel("Sucursales")
        ax.set_ylabel("Cantidad de producto")
        layout=QVBoxLayout()
        layout.addWidget(self.canvas)
        central=QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

app=QApplication(sys.argv)
ventana=Inventario()
ventana.show()
sys.exit(app.exec_())        
        
