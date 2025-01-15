from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QFont, QIcon, QFontDatabase
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SeaFox_OS")
        self.setWindowIcon(QIcon("imgs/SeaFox_Logo.png"))

        # Cargar la font
        self.load_fonts()

        # Crear el texto "SeaFox"
        self.label = QLabel("SeaFox")
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        # Crear los botones
        self.button1 = QPushButton("#1") 
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")

        # Inicializar la interfaz
        self.initUI()

    def load_fonts(self):
        # Cargar la fuente personalizada desde la carpeta 'fonts'
        font_id = QFontDatabase.addApplicationFont("fonts/PlaywriteIN-VariableFont_wght.ttf")

    def initUI(self):
        # Configurar el widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Crear un diseño vertical
        vbox = QVBoxLayout()

        # Añadir el texto y los botones al diseño
        vbox.addWidget(self.label)  # Añadir el texto 
        
        # Crear un diseño horizontal para los botones
        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        vbox.addStretch()  # Espaciador superior
        vbox.addLayout(hbox)
        vbox.addStretch()  # Espaciador inferior

        # Establecer el diseño en el widget central
        central_widget.setLayout(vbox)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    # Aplicar el archivo QSS
    with open("main/style.qss", "r") as file:
        app.setStyleSheet(file.read())

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
