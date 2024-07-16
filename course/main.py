from PyQt6.QtWidgets import (QApplication,QLabel,QWidget,QLineEdit,QPushButton,
QMessageBox,QCheckBox)
from PyQt6.QtGui import QPixmap
from PyQt6.QtGui import QFont, QPixmap



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100,100,1500,1500)
        self.setWindowTitle("Ventana Principal")

        self.generar_contenido()

    def generar_contenido(self):
        image_path = 'casa.jpeg'

        try:
            with open(image_path):
                image_label = QLabel(self)
                image_label.setPixmap(QPixmap(image_path))

        except FileNotFoundError as e:
            QMessageBox.warning(self,"Error Message",
            "Imagen no encontrada: {e}",
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close)

        except Exception as e:
            QMessageBox.warning(self,"Error Message",
            "Error en el main view: {e}",
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close)