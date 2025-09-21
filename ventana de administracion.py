# extras_gastos.py

from PyQt5.QtWidgets import QMessageBox, QListWidget

# Crear el historial visual (QListWidget)
historial = QListWidget()

def inicializar_icono(ventana):
    """Intenta asignar un ícono a la ventana, sin generar error si no existe."""
    from PyQt5.QtGui import QIcon
    try:
        icono = QIcon("icono.png")
        ventana.setWindowIcon(icono)
    except:
        pass

def agregar_gastos(entrada_descr, entrada_monto, historial_widget, ventana, total):
    """
    Función mejorada para agregar gastos:
    - Valida campos vacíos.
    - Valida monto numérico.
    - Actualiza el historial visual.
    - Muestra mensajes de éxito o error.
    
    Retorna el nuevo total actualizado.
    """

    descr = entrada_descr.text().strip()
    monto_str = entrada_monto.text().strip()

    # Validación de campos vacíos
    if not descr or not monto_str:
        QMessageBox.warning(ventana, "Campos vacíos", "Por favor, completa ambos campos.")
        return total

    try:
        monto = float(monto_str)
        total += monto

        # Mostrar información del gasto agregado
        QMessageBox.information(
            ventana,
            "Gasto agregado",
            f"Descripción: {descr}\nMonto: ${monto:.2f}\n\nTotal acumulado: ${total:.2f}"
        )

        # Agregar gasto al historial visual
        historial_widget.addItem(f"{descr} - ${monto:.2f}")

        # Limpiar los campos de entrada
        entrada_descr.clear()
        entrada_monto.clear()

        return total

    except ValueError:
        QMessageBox.warning(ventana, "Error", "El monto debe ser un número válido.")
        return total
