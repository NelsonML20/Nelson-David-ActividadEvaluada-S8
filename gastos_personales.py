# Importamos las librerías necesarias de PyQt5
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,
    QLineEdit, QMessageBox, QListWidget
)
from PyQt5.QtGui import QIcon
import sys

# Creamos la aplicación principal de PyQt5
app = QApplication(sys.argv)

# Variable global para el total acumulado de gastos
total = 0

# Función que se ejecuta al presionar el botón "Agregar gasto"
def agregar_gastos():
    global total  # Permite modificar la variable global

    descr = entrada_descr.text().strip()
    monto_str = entrada_monto.text().strip()

    # Validación de campos vacíos
    if not descr or not monto_str:
        QMessageBox.warning(ventana, "Campos vacíos", "Por favor, completa ambos campos.")
        return

    try:
        monto = float(monto_str)
        total = total + monto  # Sumar al total

        # Mostrar información del gasto agregado
        QMessageBox.information(
            ventana,
            "Gasto agregado",
            f"Descripción: {descr}\nMonto: ${monto:.2f}\n\nTotal acumulado: ${total:.2f}"
        )

        # Agregar al historial
        historial.addItem(f"{descr} - ${monto:.2f}")

        # Limpiar entradas
        entrada_descr.clear()
        entrada_monto.clear()

    except ValueError:
        # Mostrar advertencia si el monto no es numérico
        QMessageBox.warning(
            ventana,
            "Error",
            "El monto debe ser un número válido."
        )

# Crear la ventana principal
ventana = QWidget()
ventana.setWindowTitle("Control de Gastos Personales")
ventana.setGeometry(300, 300, 400, 300)

# Icono de la ventana (opcional, asegúrate de tener el archivo)
try:
    icono = QIcon("icono.png")
    ventana.setWindowIcon(icono)
except:
    pass  # Si el ícono no existe, no da error

# Crear layout vertical
layout = QVBoxLayout()

# Etiqueta principal
txt = QLabel("Registro de gastos")

# Campo para la descripción del gasto
entrada_descr = QLineEdit()
entrada_descr.setPlaceholderText("Ingresar la descripción del gasto")

# Campo para el monto del gasto
entrada_monto = QLineEdit()
entrada_monto.setPlaceholderText("Ingresar el monto del gasto")

# Botón para agregar gasto
btn = QPushButton("Agregar gasto")
btn.clicked.connect(agregar_gastos)

# Lista para mostrar el historial de gastos
historial = QListWidget()

# Agregar widgets al layout
widgets = [txt, entrada_descr, entrada_monto, btn, historial]
for w in widgets:
    layout.addWidget(w)

# Asignar el layout a la ventana
ventana.setLayout(layout)

# Mostrar ventana
ventana.show()

# Ejecutar la aplicación
sys.exit(app.exec_())
