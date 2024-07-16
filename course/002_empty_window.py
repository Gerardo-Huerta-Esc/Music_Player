import sys
from PyQt6.QtWidgets import (QApplication,QLabel,QWidget,QLineEdit,QPushButton,
QMessageBox,QCheckBox)

from PyQt6.QtGui import QFont, QPixmap

from registro import RegistrarUsuarioView

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()
    
    def inicializar_ui(self):
        self.setGeometry(100,100,350,250)
        self.setWindowTitle("Login") # generate the tittle
        self.generar_formulario() # initialize method .generar_formulario()
        self.show()
    
    def generar_formulario(self):
        self.is_logged = False

        user_label = QLabel(self)
        user_label.setText("Usuario")
        user_label.setFont(QFont('Arial',10))
        user_label.move(20,54)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250,24)
        self.user_input.move(90,50)


        password_label = QLabel(self)
        password_label .setText("Password:")
        password_label .setFont(QFont('Arial',10))
        password_label .move(20,86)

        self.password_input = QLineEdit(self)
        self.password_input.resize(250,24)
        self.password_input.move(90,82) 
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password) # la contraseña no está vista 
        
        # window to see the password
        self.check_view_password = QCheckBox(self)
        self.check_view_password.setText("Ver Contraseña")
        self.check_view_password.move(90,107)
        self.check_view_password.toggled.connect(self.mostrar_contrasena) 
        
        # login button 
        login_button = QPushButton(self)
        login_button.setText('Login')
        login_button.resize(320,34)
        login_button.move(20,140)
        login_button.clicked.connect(self.iniciar_mainview) 
        
        # registry button
        login_button = QPushButton(self)
        login_button.setText('Registrarte')
        login_button.resize(320,34)
        login_button.move(20,180)
        login_button.clicked.connect(self.registrar_usuario) 
    
    def mostrar_contrasena(self,clicked):
        if clicked:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal) # la contraseña sí está a la vista
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

    def iniciar_mainview(self):
        pass

    def registrar_usuario(self):
        self.new_user_form = RegistrarUsuarioView() 
        self.new_user_form.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec())













# para qué sirve la clase QLabel  y QApplication y QLineEdit, QPushButton, QMessageBox,QCheckBox?