import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtWidgets import QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Creates a generic widget
        self.cw = QWidget()
        # Creates a grid layout
        self.grid = QGridLayout(self.cw)
        # QPushButton(content)-> Creates a button with content as its text
        self.btn = QPushButton("Texto do botão")
        # Widget.setStyleSheet(css-like-str): styles the button like in css
        self.btn.setStyleSheet("font-size:16px")
        # GridLayout.addWidget(widget,row,column,width_in_cols,height_in_rows)
        # -> Adds a widget to the layout at row and column with width and height
        # dimensions
        # widget.clicked: Event trigerred when button is clicked
        # widget.clicked.connect(callback): registers a callback function when clicked event is triggered
        self.btn.clicked.connect(self.acao)
        self.grid.addWidget(self.btn, 0, 0, 1, 1)
        # self.setCentralWidget(w) -> sets w as the central widget off MainWindow
        self.setCentralWidget(self.cw)

    def acao(self):
        # Dummy method
        print("Método de App")


if __name__ == "__main__":
    # QApplication(arguments): Entry point fo every QT program
    qt = QApplication(sys.argv)
    app = App()
    # Widget.show() -> Shows the widget on the screen
    app.show()
    # QApplication.exec_() -> Starts the program
    qt.exec_()
