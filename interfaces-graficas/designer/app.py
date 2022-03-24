import sys
from os import path
from design import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QErrorMessage
from PyQt5.QtGui import QPixmap

USER_HOME = path.abspath(path.expandvars("$HOME"))

# The app should inherit from QMainWindow and the Ui_class created by QtDesigner
class App(QMainWindow, Ui_MainWindow):
    accepted_file_tipes = (".jpg", ".jpeg", ".png")

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)

        self.BtnFindFile.clicked.connect(self.open_image)
        self.BtnResize.clicked.connect(self.resize_image)
        self.BtnSaveFile.clicked.connect(self.save_image)

    def show_error(self, prompt):
        QErrorMessage(self.centralwidget).showMessage(prompt)

    def open_image(self):
        # QFileDialog.getOpenFileName() -> Opens a file picker window
        # returns a tuple in this form: (filename,filter)
        img_path, filter = QFileDialog.getOpenFileName(
            self.centralwidget,
            directory=USER_HOME,
            caption="Choose an image file",
            filter="Images (*.png *.jpg *.jpeg);; All files (*)",
        )
        if not img_path:
            return
        if filter != "Images (*.png *.jpg *.jpeg)":
            _, extension = path.splitext(img_path)
            if extension not in App.accepted_file_tipes:
                self.show_error("Invalid file type")

        self.InputImgPath.setText(img_path)
        self.original_img = QPixmap(img_path)
        self.ImgPlaceholder.setPixmap(self.original_img)
        self.HeightPropValue.setText(str(self.original_img.height()))
        self.WidthPropValue.setText(str(self.original_img.width()))

    def resize_image(self):
        try:
            width = int(self.WidthPropValue.text())
            self.new_img = self.original_img.scaledToWidth(width)
        except (ValueError, AttributeError):
            self.show_error("Please choose an image")
            return
        self.ImgPlaceholder.setPixmap(self.new_img)
        self.HeightPropValue.setText(str(self.new_img.height()))

    def save_image(self):
        new_file, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            caption="Save file",
            directory=USER_HOME,
            filter="Images (*.png *.jpeg *.jpg)",
        )

        if not self.new_img:
            self.new_img = self.original_img

        status = self.new_img.save(new_file, "PNG")
        if status == False:
            self.show_error("Could not save file")


if __name__ == "__main__":
    runtime = QApplication(sys.argv)
    app = App()
    app.show()
    runtime.exec_()
