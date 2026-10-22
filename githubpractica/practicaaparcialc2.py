import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget)
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
df=pd.read_csv('githubpractica/artistas.csv')
class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ventana de PyQT y Matplotlib')
        self.resize(700,500)
        df_agrupado=df.groupby('Artista')['Reproducciones_Millones'].sum()
        self.figura=Figure(figsize=(6,4))
        self.canvas=FigureCanvas(self.figura)
        ax=self.figura.add_subplot(111)
        ax.bar(df_agrupado.index,df_agrupado.values,color='blue')
        ax.set_title("Reproducciones de cada artista")
        ax.set_xlabel("Artistas")
        ax.set_ylabel("Reproducciones en millones")
        layout=QVBoxLayout()
        layout.addWidget(self.canvas)
        central=QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

app=QApplication(sys.argv)
ventana=Ventana()
ventana.show()
sys.exit(app.exec_())
