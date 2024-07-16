import sys
from PyQt6.QtWidgets import QApplication, QWidget 
                        # Clase Base para Widgets: QWidget es la clase base para todos los widgets en PyQt6. 
                        # Proporciona la funcionalidad básica necesaria para crear y gestionar widgets en una aplicación PyQt6.

class VentanaVacía(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100,100,250,250) #y,x,ancho,largo
        self.setWindowTitle("Mi primera ventana")
        self.show()





if __name__=='__main__':
    app = QApplication(sys.argv) # permite pasarle parámetros por consola
    ventana = VentanaVacía() # instancia de clase
    sys.exit(app.exec())