#Importamos las librerias necesarias de PyQt5
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox)
from PyQt5.QtGui import QIcon
import sys

# Creamos la aplicación principal de PyQt5
app = QApplication(sys.argv)

#creamos la variable global, que guardará el total acumulado de gastos
total = 0 

#creamos la función que se va a ejecutar cada ves que se preciona el botón.
def agregar_gastos():
    global total    # para poder modificar la variable "total"
    try:
        descr = entrada_descr.text()  # entrada de texto de la "descripción"
        monto = float(entrada_monto.text()) # entrada de texto del monto y convertirlo a número

        total = total + monto   # se suma el nuevo monto al total acumulado

        # cuadro de información con los datos del total y gastos actualizado
        QMessageBox.information(
            ventana,
            "Gasta agregado",
            f"Descripción: {descr}\nMonto: ${monto:.2f}\n\nTotal acumulado: ${total:.2f}"
        )
        
        # linea de codigo, limpiando las entrada para que el usuario pueda escribir un nuevo gasto
        entrada_descr.clear()
        entrada_monto.clear()

    #Linea de codigo por si el usuario escribe algo que no es número en el monto
    except ValueError:

        QMessageBox.warning(
            ventana,
            "Error", "El monto deber ser un número válido."
        )


# Ventana principal, donde se crea la ventana, se la asigna un titulo a la ventana tamaño de ventana, icono de ventana
ventana = QWidget()
ventana.setWindowTitle("Control de Gastos Personales")
ventana.setGeometry(300, 300, 400, 200)
icono = QIcon("icono.png")
ventana.setWindowIcon(icono)


# organizador de widgets en vertical
layout = QVBoxLayout()

# Widgets (elementos de la ventana)
#texto fijo
txt = QLabel("Registro de gastos")
# bloque de codigo para la descripción del gasto
entrada_descr = QLineEdit()
entrada_descr.setPlaceholderText("Ingresar la descripción del gasto")
# bloque de codigo para el monto del gasto
entrada_monto = QLineEdit()
entrada_monto.setPlaceholderText("Ingresar el monto del gasto")

#bloque de codigo del botón y manda a llamar a la función agregar_gastos
btn = QPushButton("Agregar gasto")
btn.clicked.connect(agregar_gastos)

#Agregar los widgets al layout con un ciclo
widgets = [txt,  entrada_descr, entrada_monto, btn]
for w in widgets:
    layout.addWidget(w)

#asignamos el layout a la ventana para que muestre los widgets en orden
ventana.setLayout(layout)

#linea para mostrar la ventana
ventana.show()

#Linea que mantiene la aplicación en ejecución hasta que el usuario la cierre
sys.exit(app.exec_())
