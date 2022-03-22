import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit
from PyQt5.QtWidgets import QWidget, QGridLayout, QSizePolicy


class Calculadora(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.cw = QWidget()
        # Determines that cw is a widget with a grid layout
        self.grid = QGridLayout(self.cw)
        # Defines the window title
        self.setWindowTitle("Calculadora do João")
        # self.setFixedSize(width,height) Fix the size of the aplication
        self.setFixedSize(400, 400)
        # QLineEdit: A editable line input widget
        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        # QWidget.setDisabled(bool): Disables input for a Widget
        self.display.setDisabled(True)
        self.display.setStyleSheet("* {background: #fff; color: #000; font-size:20px}")
        # QtWidget.setSizePolicy(width_pol,height_pol): Determines how the widget will resize
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.add_button(QPushButton(text="1"), 1, 0)
        self.add_button(QPushButton(text="2"), 1, 1)
        self.add_button(QPushButton(text="3"), 1, 2)
        self.add_button(QPushButton(text="+"), 1, 3)
        self.add_button(
            QPushButton(text="C"),
            1,
            4,
            callback=self.clear_display,
            style="background:rgb(240,60,60);font-weight: bold;",
        )

        self.add_button(QPushButton(text="4"), 2, 0)
        self.add_button(QPushButton(text="5"), 2, 1)
        self.add_button(QPushButton(text="6"), 2, 2)
        self.add_button(QPushButton(text="-"), 2, 3)
        self.add_button(
            QPushButton(text="<-"),
            2,
            4,
            callback=self.erase_text,
            style="background:rgb(240,100,40);font-weight: bold;",
        )

        self.add_button(QPushButton(text="7"), 3, 0)
        self.add_button(QPushButton(text="8"), 3, 1)
        self.add_button(QPushButton(text="9"), 3, 2)
        self.add_button(QPushButton(text="*"), 3, 3)
        self.add_button(QPushButton(text=" "), 3, 4)

        self.add_button(QPushButton(text="."), 4, 0)
        self.add_button(QPushButton(text="0"), 4, 1)
        self.add_button(QPushButton(text=" "), 4, 2)
        self.add_button(QPushButton(text="/"), 4, 3)
        self.add_button(
            QPushButton(text="="),
            4,
            4,
            callback=self.calculate_result,
            style="background:rgb(100,200,100);font-weight: bold;",
        )

        # Defines cw as central widget
        self.setCentralWidget(self.cw)

    def add_button(
        self,
        btn: QPushButton,
        row: int,
        col: int,
        row_span: int = 1,
        col_span: int = 1,
        callback=None,
        style=None,
    ):
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.grid.addWidget(btn, row, col, row_span, col_span)
        if style:
            btn.setStyleSheet(style)
        if not callback:
            btn.clicked.connect(
                # widget.setText(text:str): set text as the widget text
                # widget.text(): gets the widget text
                lambda: self.display.setText(self.display.text() + btn.text())
            )
            return
        btn.clicked.connect(callback)

    def clear_display(self):
        self.display.setText("")

    def erase_text(self):
        self.display.setText(self.display.text()[:-1])

    def calculate_result(self):
        try:
            text = self.display.text()
            result = eval(text)
            self.display.setText(str(result))
        except SyntaxError as e:
            self.display.setText("Conta inválida")
        except ZeroDivisionError:
            self.display.setText("Indefinido")


if __name__ == "__main__":
    runtime = QApplication(sys.argv)
    app = Calculadora()
    app.show()
    runtime.exec_()
